def mergesort(data):
    if len(data) < 2:
        return data
    middle = len(data) // 2
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])
    merged = merge(left, right)
    return merged


def merge(left, right):
    if not len(left):
        return left
    if not len(right):
        return right
    result = []
    left_index = 0
    right_index = 0
    total_len = len(left) + len(right)
    while len(result) < total_len:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
        if left_index == len(left) or right_index == len(right):
            result.extend(left[left_index:] or right[right_index:])
    return result


data = [11, 2, 3, 9, 4, 6, 8, 0, 5, 3, 6, 9, 11, 444, 145, 456, 74, 74, 2, 7, 99, 7, 555, 666, 1, 4, 0, -8, -999, -9, 1,
        4, 8, -1, 6, 91, 1, 62, 5, 7]
data = mergesort(data)
print(data)