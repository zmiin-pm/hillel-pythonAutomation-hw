"""
Занятия проходят по понедельникам и четвергам в 19:15
Первое занятие произошло 17.10.2022. Всего 32 занятия.
Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю)
"""
from datetime import timedelta, date, time, datetime


def gen_lesson_date():
    first_lesson_date = date(2022, 10, 17)
    lessons_qty = 32
    lesson_date = None
    delta_from_mon_to_thurs = timedelta(days=3)
    delta_from_thurs_to_mon = timedelta(days=4)
    for i in range(lessons_qty):
        if not lesson_date:
            lesson_date = first_lesson_date
        elif i % 2 != 0:
            lesson_date += delta_from_mon_to_thurs
        elif i % 2 == 0:
            lesson_date += delta_from_thurs_to_mon
        yield lesson_date


lesson_time = time(19, 15)
gen = gen_lesson_date()

for counter, value in enumerate(gen):
    print(
        f'Lecture {counter + 1:>2}: {value.strftime("%d %b %Y")} {lesson_time.strftime("%H:%M")}'
    )


print('\n')
# second variant


def gen_lesson_date_time(first_date_time, first_call=True):
    delta_from_mon_to_thurs = timedelta(days=3)
    delta_from_thurs_to_mon = timedelta(days=4)
    while True:
        if first_call:
            first_call = False
            lesson_date_time = first_date_time
            yield lesson_date_time
        lesson_date_time += delta_from_mon_to_thurs
        yield lesson_date_time
        lesson_date_time += delta_from_thurs_to_mon
        yield lesson_date_time


first_lesson = datetime(2022, 10, 17, 19, 15)
gen_1 = gen_lesson_date_time(first_lesson)

for lesson_number in range(32):
    print(
        f'Lecture {lesson_number + 1:>2}: {next(gen_1).strftime("%d %b %Y %H:%M")}'
    )
