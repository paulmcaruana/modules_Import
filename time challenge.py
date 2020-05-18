# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

print("time():\t\t\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t\t\t", time.get_clock_info('perf_counter'))
print("Monotonic():\t\t\t", time.get_clock_info('monotonic'))
print("Process_time():\t\t\t", time.get_clock_info('process_time'))

# this outputs:
# time():		    namespace(adjustable=True, implementation='GetSystemTimeAsFileTime()', monotonic=False, resolution=0.015625)
# perf_counter():   namespace(adjustable=False, implementation='QueryPerformanceCounter()', monotonic=True, resolution=1e-07)
# Monotonic():      namespace(adjustable=False, implementation='GetTickCount64()', monotonic=True, resolution=0.015625)
# Process_time():	namespace(adjustable=False, implementation='GetProcessTimes()', monotonic=True, resolution=1e-07)