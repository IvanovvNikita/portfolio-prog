from test import setup_data, calc_time, calc_delta

from tree import gen_bin_tree_recursion, gen_bin_tree

if __name__ == '__main__':
    data = setup_data(100, 100, 15)
    timetable = calc_time(gen_bin_tree, data)
    delta = calc_delta(timetable)

    for i, d in enumerate(data):
        start = timetable[i][0]
        end = timetable[i][1]
        time = end - start
        print(d[0], time)
 
    timetable = calc_time(gen_bin_tree_recursion, data)
    delta = calc_delta(timetable)
    print("-----------")
    for i, d in enumerate(data):
      start = timetable[i][0]
      end = timetable[i][1]
      time = end - start
      print(d[0], time)
