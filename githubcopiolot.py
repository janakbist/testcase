import time
import psutil
import tracemalloc


def quicksort_ai(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_ai(left) + middle + quicksort_ai(right)


# Performance Measurement
def measure_performance_ai():
    arr = [i for i in range(10000, 0, -1)]

    tracemalloc.start()
    start_time = time.time()
    cpu_before = psutil.cpu_percent(interval=None)

    sorted_arr = quicksort_ai(arr)  # AI-generated sorting

    cpu_after = psutil.cpu_percent(interval=None)
    end_time = time.time()
    mem_usage = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "Execution Time": end_time - start_time,
        "Memory Usage": mem_usage[1] / 1024,  # KB
        "CPU Usage": cpu_after - cpu_before
    }


ai_results = measure_performance_ai()
if ai_results is None: print('no data')
else: print(ai_results)
