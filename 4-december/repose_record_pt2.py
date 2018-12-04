import re
from collections import defaultdict
from datetime import datetime

from event import Event


def main():
    events = []
    with open("input.txt") as file:
        events_input = file.readlines()
        for event_input in events_input:
            split_claim = re.split('\[|\] ', event_input.strip())
            event = Event(split_claim[1], split_claim[2])
            events.append(event)
    events.sort(key=lambda x: datetime.strptime(x.date_time, '%Y-%m-%d %H:%M'))

    current_guard = ""
    guard_time_dict = defaultdict(lambda: [0 for x in range(60)])
    fell_asleep_time = 0
    for event in events:
        if "Guard" in event.description:
            current_guard = re.search('#(.*) begins', event.description).group(1)
            event.guard = current_guard
        else:
            event.guard = current_guard

        if "asleep" in event.description:
            fell_asleep_time = re.search(':(.*)', event.date_time).group(1)
        elif "wakes" in event.description:
            awake_time = re.search(':(.*)', event.date_time).group(1)
            for time in range(int(fell_asleep_time), int(awake_time)):
                guard_time_dict[current_guard][time] += 1

    sleepiest_guard = sorted(guard_time_dict.keys(), key=lambda g: -max(guard_time_dict[g]))[0]
    time_list = guard_time_dict[sleepiest_guard]
    minute = time_list.index(max(time_list))

    print(int(sleepiest_guard) * minute)


if __name__ == "__main__":
    main()
