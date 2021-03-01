# 1450. Number of Students Doing Homework at a Given Time


def busy_student(start_time, end_time, query_time):
    counts = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            counts += 1
    return counts
