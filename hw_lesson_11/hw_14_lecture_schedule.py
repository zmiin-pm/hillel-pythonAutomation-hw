from datetime import timedelta, date, time


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