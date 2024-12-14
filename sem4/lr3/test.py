def calc_delta(timetable: list) -> float:
    delta = 0
    for start, end in timetable:
        delta += end - start
    return delta

def calc_time(func, args) -> list:
    import timeit

    timetable = []
    for n in args:
        start_time = timeit.default_timer()
        func(*n)
        end_time = timeit.default_timer()
        timetable.append((start_time, end_time))

    return timetable

def setup_data(n: int, max_root: int = 100, max_height:int = 10) -> list:
    from random import randint

    min_height = 0
    min_root = 1
    data = []

    for _ in range(n):
        data.append((randint(min_height, max_height), randint(min_root,max_root)))

    return data