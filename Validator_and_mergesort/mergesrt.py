def mergesort(data, key):
    if len(data) < 2:
        return data
    middle = len(data) // 2
    left_part = mergesort(data[:middle], key)
    right_part = mergesort(data[middle:], key)
    merged_data = merge(left_part, right_part, key)
    return merged_data


def merge(left_part, right_part, key):
    if not len(left_part):
        return left_part
    if not len(right_part):
        return right_part
    result = []
    left_index = 0
    right_index = 0
    total_len = len(left_part) + len(right_part)
    while len(result) < total_len:
        val1 = left_part[left_index][key]
        val2 = right_part[right_index][key]
        if val1 < val2:
            result.append(left_part[left_index])
            left_index += 1
        else:
            result.append(right_part[right_index])
            right_index += 1
        if left_index == len(left_part) or right_index == len(right_part):
            result.extend(left_part[left_index:] or right_part[right_index:])
    return result
