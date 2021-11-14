def mergesort(data, key):
    if len(data) < 2:
        return data
    middle = len(data) // 2
    left = mergesort(data[:middle], key)
    right = mergesort(data[middle:], key)
    merged = merge(left, right, key)
    return merged


def merge(left, right, key):
    if not len(left):
        return left
    if not len(right):
        return right
    result = []
    left_index = 0
    right_index = 0
    total_len = len(left) + len(right)
    while len(result) < total_len:
        val1 = left[left_index][key]
        val2 = right[right_index][key]
        if val1 < val2:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
        if left_index == len(left) or right_index == len(right):
            result.extend(left[left_index:] or right[right_index:])
    return result
