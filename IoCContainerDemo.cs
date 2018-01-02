using System;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// Learnings from https://app.pluralsight.com/library/courses/inversion-of-control/table-of-contents
/// </summary>
namespace IoCContainerDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Mothod 1: Interface injection
            //ICreditCard card = new MasterCard();
            //Shopper shopper = new Shopper(card);

            // Method 2: IoC container
            Resolver resolver = new Resolver();
            //resolver.Register<ICreditCard, MasterCard>();
            resolver.Register<ICreditCard, Visa>();
            resolver.Register<Shopper, Shopper>();

            var shopper = resolver.Resolve<Shopper>();

            shopper.SpendMoney();
            Console.Read();
        }

        public class Shopper
        {
            private readonly ICreditCard creditCard;

            public Shopper(ICreditCard creditCard)
            {
                this.creditCard = creditCard;
            }

            public void SpendMoney()
            {
                Console.WriteLine(this.creditCard.Charge());
            }
        }

        public class Resolver
        {
            private Dictionary<Type, Type> dependencyMap = new Dictionary<Type, Type>();

            public T Resolve<T>()
            {
                return (T)Resolve(typeof(T));
            }

            private object Resolve(Type typeToResolve)
            {
                Type resolvedType = null;
                try
                {
                    resolvedType = dependencyMap[typeToResolve];
                }
                catch
                {
                    throw new Exception(string.Format("Cannot resolve type {0}", typeToResolve.FullName.ToString()));
                }

                var firstConstructor = resolvedType.GetConstructors().First();
                var constructorParameters = firstConstructor.GetParameters();
                if (constructorParameters.Count() == 0)
                    return Activator.CreateInstance(resolvedType);

                IList<object> parameters = new List<object>();
                foreach (var parameterToResolve in constructorParameters)
                {
                    parameters.Add(Resolve(parameterToResolve.ParameterType));
                }

                return firstConstructor.Invoke(parameters.ToArray());
            }

            public void Register<TFrom, TTo>()
            {
                dependencyMap.Add(typeof(TFrom), typeof(TTo));
            }
        }                

        public interface ICreditCard
        {
            string Charge();
        }

        public class MasterCard : ICreditCard
        {
            public string Charge()
            {
                return "Swiping MasterCard!";
            }
        }

        public class Visa : ICreditCard
        {
            public string Charge()
            {
                return "Charging Visa card!";
            }
        }
    }
}
