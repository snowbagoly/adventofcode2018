from aocd import get_data
import re
from collections import Counter

id_regex = re.compile("#(\d*)")

s = get_data(day=4,year=2018)

#first part
records = sorted(s.split("\n"))
sleep_times = {}
for record in records:
	minutes = int(record[15:17])
	if "#" in record:
		last_id = int(id_regex.search(record).group(1))
	elif "falls" in record:
		last_falls = minutes
	elif "wakes" in record:
		if last_id not in sleep_times:
			sleep_times[last_id] = []
		for i in range(last_falls,minutes):
			sleep_times[last_id].append(i)
			
max_id = None
max_sleep_time = None
most_asleep_minute = None
for id in sleep_times:
	sleep_time = len(sleep_times[id])
	if not max_sleep_time or sleep_time > max_sleep_time:
		max_id = id
		max_sleep_time = sleep_time
		most_asleep_minute = Counter(sleep_times[id]).most_common(1)[0][0]
print(max_id, most_asleep_minute, max_id*most_asleep_minute)

#second part
max_id = None
max_most_asleep_minute = None
max_mam_counter = None
for id in sleep_times:
	most_asleep_minute,mam_counter = Counter(sleep_times[id]).most_common(1)[0]
	if not max_mam_counter or mam_counter > max_mam_counter:
		max_id = id
		max_most_asleep_minute = most_asleep_minute
		max_mam_counter = mam_counter
		
print(max_id, max_most_asleep_minute, max_id * max_most_asleep_minute)