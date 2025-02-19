import time
import psutil
import tracemalloc


def quicksort_human(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot = arr[right]  # Select last element as pivot
        partition_index = left

        for i in range(left, right):
            if arr[i] < pivot:
                arr[i], arr[partition_index] = arr[partition_index], arr[i]
                partition_index += 1

        arr[partition_index], arr[right] = arr[right], arr[partition_index]

        stack.append((left, partition_index - 1))
        stack.append((partition_index + 1, right))

    return arr


def measure_performance_human():
    arr = [i for i in range(10000, 0, -1)]

    tracemalloc.start()
    start_time = time.time()
    cpu_before = psutil.cpu_percent(interval=None)

    sorted_arr = quicksort_human(arr)  # Human-written sorting

    cpu_after = psutil.cpu_percent(interval=None)
    end_time = time.time()
    mem_usage = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "Execution Time": end_time - start_time,
        "Memory Usage": mem_usage[1] / 1024,  # KB
        "CPU Usage": cpu_after - cpu_before
    }


# Run the function
human_results = measure_performance_human()
print(human_results)
