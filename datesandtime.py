# import time
#
# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
#
# # Outputs the following:
# # The epoch on this system starts at Thu Jan  1 00:00:00 1970
# # The current timezone is GMT Standard Time with an offset of 0
# # Daylight Saving Time is in effect for this location
# #     The DST timezone is GMT Summer Time
# # Local time is 2020-05-12 12:05:14
# # Local time is 2020-05-12 11:05:14

import datetime

print(datetime.datetime.today())            #there are two datetime's stated as one is the module and one is the class
print(datetime.datetime.now())              #.now() looks like the .today() but it can be more precise
print(datetime.datetime.utcnow())

#outputs:
# 2020-05-12 12:11:04.494800
# 2020-05-12 12:11:04.494800
# 2020-05-12 11:11:04.494800