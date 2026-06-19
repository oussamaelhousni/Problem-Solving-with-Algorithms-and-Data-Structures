import time


def sum_with_time(n):
    start = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end = time.time()

    return s,end-start

print(sum_with_time(1000))