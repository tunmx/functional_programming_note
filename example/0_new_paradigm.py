from functools import reduce
import math

def softmax_a(scores):
    """
    Imperative Programming example.
    """
    # The index was calculated for each score
    exp_scores = []
    for score in scores:
        exp_scores.append(math.exp(score))

    # The sum of the index scores was calculated
    total = 0
    for exp_score in exp_scores:
        total += exp_score

    # The softmax probability distribution was calculated
    softmax_probs = []
    for exp_score in exp_scores:
        softmax_probs.append(exp_score / total)

    return softmax_probs

def softmax_b(scores):
    """
    Functional Programming(Not totally)
    """
    exp_scores = list(map(math.exp, scores))
    total = reduce(lambda x, y: x + y, exp_scores)
    return [s / total for s in exp_scores]


neure = [0, -2, 3, 4, -3]
print(softmax_a(neure))
print(softmax_b(neure))

