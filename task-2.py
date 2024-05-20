def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)


sorted_arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
target = 4.0

result = binary_search(sorted_arr, target)
print(result)  # Очікуваний результат: (кількість ітерацій, 4.4)