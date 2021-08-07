def add_time(start, duration, weekday=''):

    time_parts = start.split()
    time_digits = time_parts[0].split(':')
    time_hours = int(time_digits[0])
    time_minutes = int(time_digits[1])
    am_pm = time_parts[1]
    original_am_pm = am_pm
    duration_parts = duration.split(':')
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])
    all_weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if (duration_minutes + time_minutes) > 60:
        duration_hours += 1
        duration_minutes -= 60

    add_hours = time_hours + duration_hours
    add_minutes = time_minutes + duration_minutes
    until_12 = 12 - time_hours  # Hours until am_pm change
    days = 0  # days of duration
    display_days = ""

    if duration_hours >= until_12:
        if am_pm == 'AM':
            am_pm = 'PM'
        else:
            am_pm = 'AM'
            days += 1
        duration_hours -= until_12

    if duration_hours >= 12:
        final = int(duration_hours / 12)
        if final % 2 == 1:
            if am_pm == "AM":
                am_pm = 'PM'
            else:
                am_pm = 'AM'
                days += 1
        if original_am_pm == 'AM':
            if duration_hours >= 24:
                days += int(duration_hours / 24)
        else:
            duration_hours -= 12
            days += 1
            days += int(duration_hours / 24)

    if days == 1:
        display_days = "(next day)"
    if days > 1:
        display_days = f"({days} days later)"

    if add_minutes < 10:
        add_minutes = '0' + str(add_minutes)
    else:
        add_minutes = str(add_minutes)
    if weekday.capitalize() in all_weekdays:
        weekday = weekday.capitalize()
        i = 0  # index for day of week
        j = 0  # index for weekdays to advance
        advance_day = days % 7  # number weekdays to advance
        while i < 7:
            if all_weekdays[i] == weekday:
                while j < advance_day:
                    j += 1
                    i += 1
                    if i == 7:
                        i = 0
                final_day = all_weekdays[i]
                break
            i += 1

    if days == 0 and weekday in all_weekdays:
        final_day = weekday
    add_hours = add_hours % 12  # Get proper hour
    if add_hours == 0:
        add_hours = 12
    if weekday == '':
        if display_days == '':
            new_time = str(add_hours) + ':' + add_minutes + " " + am_pm
        else:
            new_time = str(add_hours) + ':' + add_minutes + " " + am_pm + " " + display_days
    else:
        if display_days == '':
            new_time = str(add_hours) + ':' + add_minutes + " " + am_pm + ", " + final_day
        else:
            new_time = str(add_hours) + ':' + add_minutes + " " + am_pm + ", " + final_day + " " + display_days

    return new_time
