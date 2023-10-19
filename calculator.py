def add_time(start, duration):
    # Разбиваем начальное время и продолжительность на часы, минуты и AM/PM
    start_time_parts = start.split()
    start_time = start_time_parts[0].split(":")
    start_hour, start_minute = int(start_time[0]), int(start_time[1])
    start_am_pm = start_time_parts[1]

    duration = duration.split(":")
    duration_hour, duration_minute = int(duration[0]), int(duration[1])

    # Преобразуем AM/PM в часы (AM = 0, PM = 12)
    if start_am_pm == "PM":
        start_hour += 12

    # Преобразуем все значения в минуты
    start_minutes = start_hour * 60 + start_minute
    duration_minutes = duration_hour * 60 + duration_minute

    # Складываем время
    total_minutes = start_minutes + duration_minutes

    # Подсчитываем часы и минуты
    new_days = total_minutes // 60 // 24
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    # Определяем AM/PM для нового времени
    new_am_pm = "AM" if new_hour < 12 else "PM"

    # Преобразуем новое время в 12-часовой формат
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    # Собираем новое время в строку
    new_time = f"Returns: {new_hour:02}:{new_minute:02} {new_am_pm}"

    # Если продолжительность была больше 24 часов, добавляем (next day)
    #if total_minutes >= 24 * 60:
    #   new_time += " (next day)"
    if new_days == 1:
        new_time += " (next day)"
    if new_days > 1:
        new_time +=f' ({new_days} days later)'

    return print(new_time)

add_time("6:30 PM", "205:12")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")