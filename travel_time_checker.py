import datetime
import requests
import time
import urllib

class DayTimeCalculator(object):
    SECONDS_IN_A_DAY = 86400
    SECONDS_IN_A_HOUR = 3600
    # PST 8 hours => 28800; PDT 7 hours => 25200
    UTC_PST_OFFSET = 28800

    # weekday: 0 = Monday, 1=Tuesday, 2=Wednesday...
    def _days_to_next_weekday(self, dt, weekday):
        if dt is None:
            dt = datetime.date.today()

        days_ahead = weekday - dt.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7

        return days_ahead

    # weekday: 0 = Monday, 1=Tuesday, 2=Wednesday...
    def next_weekday_time_in_unix(self, weekday, time_in_hour):
        if time_in_hour is None:
            raise Exception('time is expected')

        utc_unix_now = time.time()
        pst_unix_now = utc_unix_now - self.UTC_PST_OFFSET
        pst_unix_today_midnight = pst_unix_now - pst_unix_now % self.SECONDS_IN_A_DAY
        days_ahead = self._days_to_next_weekday(None, weekday)

        return pst_unix_today_midnight \
               + self.SECONDS_IN_A_DAY * days_ahead \
               + self.SECONDS_IN_A_HOUR * time_in_hour \
               + self.UTC_PST_OFFSET

# Input your origin and destination
home = ""
work = ""

if home == "":
    print("Error: home address cannot be empty!")

if work == "":
    print("Error: work address cannot be empty!")

arrivalByTime = DayTimeCalculator().next_weekday_time_in_unix(weekday=0, time_in_hour=8.5)

############## DO NOT SHARE ##############
key = ""
############## DO NOT SHARE ##############

parameters = { 'origin': home,
               'destination': work,
               'key': key}
url = "https://maps.googleapis.com/maps/api/directions/json?" + urllib.parse.urlencode(parameters)

response = requests.get(url)

print("The HTTP status of Google Maps Direction API: " + str(response.status_code))
print(response.json())
for route in response.json()['routes']:
        for leg in route['legs']:
            duration = leg['duration']
            print(duration['text'])

