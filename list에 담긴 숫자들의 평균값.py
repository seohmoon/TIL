scores = [80, 89, 99, 83]

scores_sum = 0
len_scores = 0
for i in scores:
    scores_sum = scores_sum + i
    len_scores = len_scores + 1
print(float(scores_sum / len_scores))