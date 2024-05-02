records = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 20}
]

def filter_by_value(list_dicts, key, min_value):
    return [d for d in list_dicts if d.get(key, 0) >= min_value]
    
filtered_records = filter_by_value(records, 'age', 25)
print("Records with age >= 25:", filtered_records)