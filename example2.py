scores = {
    "Ali": [19, 18, 17],
    "Negar": [20, 19, 18],
    "Iman": [19, 20, 18]
}

def calculate_average(scores):
    total_scores = 0
    count = 0
    for score in scores.values():
        total_scores += sum(score)
        count += len(score)
    return total_scores / count if count != 0 else 0
    
print("Average Score: ", calculate_average(scores))