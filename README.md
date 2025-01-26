# Infix to Prefix Converter

An infix expression is a common form of expression in arithmetic and algebra. It is characterized by the placement of operators between operands. Examples of infix expressions include single letters like `A`, simple expressions like `A + B`, and more complex expressions like `(A + B) + (C - D)`.

A prefix expression, on the other hand, is an expression where the operator precedes the operands. The general form is **(** `operator` `operand1` `operand2`**)** . An example of a prefix expression is `*+AB-CD`.

## Conversion from Infix to Prefix Expressions

The process of converting an infix expression to a prefix expression typically involves the use of a stack data structure. The conversion follows these steps:

1. Reverse the infix expression.
2. Generate a "nearly" postfix expression from the reversed infix expression.
3. Reverse the resulting postfix expression to obtain the final prefix expression.

## Overview of the Prefix Expression Evaluator Project

Here's a brief overview of the main components:

- `application.py`: This is the main file of the application. It sets up the system path for dependency packages and runs the `window` module as the parent. It's the entry point of your application. The code in this file looks something like this:

```python
# application.py
import window

if __name__ == "__main__":
    window.run()
```

- `domath.py`: This file contains functions or classes related to mathematical operations. For example, it contains a simple function like this:

```python
# domath.py
def add(x, y):
    return x + y
```

- `infix_to_prefix_helper.py`: This file contains helper functions used in the conversion of infix expressions to prefix expressions. The actual conversion logic would be implemented in these helper functions.

- `infix_to_prefix.py`: This file contains the main logic for converting infix expressions to prefix expressions. It would use the helper functions defined in `infix_to_prefix_helper.py` to perform the conversion.

- `prefix_evaluation.py`: This file contains the logic for evaluating prefix expressions. After the infix expression is converted to a prefix expression, this file would take over to evaluate the expression and return the result.

- `stack.py`: This file contains a Stack class or functions for stack operations. Stacks are often used in the evaluation and conversion of mathematical expressions. Here's an example of what a simple Stack class might look like:

```python
# stack.py
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
```

- `ValidityChecker.py`: This file contains a function that checks whether a given expression is a valid infix expression.

- `window.py`: This file contains the main body of your application's GUI. It uses the `customtkinter` library to render the GUI and listen for user interactions. It also contains a function that takes values from a textbox, converts the infix expression to a prefix expression, evaluates the prefix expression, and updates the output label with the result.
