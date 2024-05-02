data = {
    "group1": [[1, 2], [3, 4]],
    "group2": [[5, 6], [7, 8]]
}

def sum_nested_dict(data):
    result = {}
    for key, value in data.items():
        total = 0
        for sublist in value:
            total += sum(sublist)
        result[key] = total
    return result

print("Sum of numbers in each group:", sum_nested_dict(data))