# [Optional] Propose a new programming paradigm

**Task:** This is an optional (not required) assignment.
Review all the definitions of "programming paradigm" we covered in "2. Introduction to Course", and based on some of them propose a new programming paradigm. Define motivation, pros and cons of the new paradigm.

As a result please attach a link to a Google Document (or attach a file) with the explanation of the new paradigm.

##### student: YanJingyu

### Functional Programming (FP)

#### Motivation:

- Emphasis on Side-Effect-Free Computation: Functional programming advocates for pure functions, where the output of a function is solely determined by its inputs and does not produce any side effects.
- Predictability and Transparency: Referential transparency (the same function call always returns the same result) makes the code easier to understand and predict.
- Enhanced Composability and Reusability of Code: By decomposing problems into composable functions, functional programming improves modularity and reusability of code.

#### Advantages:

- Clear Semantics: Functional programming provides precise and clear expressions. Pure functions and immutable data make the code more predictable and understandable.

- Flexible Execution: More flexible in execution, especially for parallel and concurrent processes. The lack of side effects simplifies parallel processing.

- Expressive: Functional programming code is concise and powerful. Higher-order functions and function composition make the code more direct and readable.

- Parameterization and Modularity: Encourages designing with parameters and modules. Functions are easily reusable and combinable.

- Handling Large Data Structures: Efficiently handles large or even infinite data structures. Lazy evaluation means calculations are done only when needed.

#### Disadvantages:

- I/O Challenges: Functional programming can struggle with input and output operations, as they often involve side effects.

- Performance Issues: Performance can be impacted, especially in architectures that are not well-aligned with functional programming principles.

- Steep Learning Curve: Due to its unique concepts and approaches, functional programming can be challenging for beginners to learn.

### Example

I have not worked with functional programming languages, so I am using Python, which I am more familiar with, for experimentation.

```python

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

'''
output:
[0.013180647081743425, 0.0017838066060495792, 0.26474037363186337, 0.7196389469029523, 0.0006562257773914463]
[0.013180647081743425, 0.0017838066060495792, 0.26474037363186337, 0.7196389469029523, 0.0006562257773914463]
'''

```

I'm not sure if my understanding of the functional programming paradigm is correct in the example.