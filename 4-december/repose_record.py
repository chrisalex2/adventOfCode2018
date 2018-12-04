import re
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
    time_dict = {}
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
            calculate_time(fell_asleep_time, awake_time, time_dict, current_guard)

    guard_asleep = {}

    for key, values in time_dict.items():
        for value in values:
            if value not in guard_asleep:
                guard_asleep[value] = 1
            else:
                guard_asleep[value] += 1

    sleepiest_guard = max(guard_asleep, key=guard_asleep.get)
    most_asleep_minute = 0

    for minute in time_dict.keys():
        counter = time_dict[minute].count(sleepiest_guard)
        if counter > most_asleep_minute:
            most_asleep_minute = minute

    print(int(sleepiest_guard) * most_asleep_minute)


def calculate_time(fell_asleep_time, awake_time, time_dict, current_guard):
    for time in range(int(fell_asleep_time), int(awake_time)):
        if time in time_dict:
            time_dict[time].append(current_guard)
        else:
            time_dict[time] = [current_guard]


if __name__ == "__main__":
    main()