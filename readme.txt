# Bisection Algorithm App - Version 1.1 (Python)

 Overview

This is a simple Bisection Algorithm App written in Python (version 1.1). It provides a console-based implementation of the bisection method, a numerical algorithm used to find roots of continuous functions. The app does not include a graphical user interface (GUI) and instead focuses on delivering clear functionality via a command-line interface (CLI).

 Bisection Method

The Bisection method is a root-finding technique that repeatedly narrows down an interval containing the root of a function. It is applicable when the function is continuous and the signs of the function at the two ends of the interval are different.

# How It Works:

1. We start with two points, `a` and `b`, such that `f(a)` and `f(b)` have opposite signs (i.e., the root lies between `a` and `b`).
2. The midpoint, `c = (a + b) / 2`, is calculated, and the function value at `c`, `f(c)`, is evaluated.
3. Depending on the sign of `f(c)`, either `a` or `b` is replaced by `c` to narrow down the interval.
4. This process is repeated until the root is found within a desired tolerance or a maximum number of iterations is reached.

 Features

- Implements the bisection method for root-finding.
- Supports continuous functions defined in the form of Python functions.
- Customizable stopping conditions (tolerance and maximum iterations).
- Simple and interactive command-line interface (CLI) for input and results display.

 Requirements

- Python 3.x (tested with Python 3.8 or higher)
- No external dependencies required.

 Usage

# Running the App

To run the bisection algorithm app, simply execute the Python script from your terminal or command prompt. You can define your own mathematical function and specify the interval `[a, b]`, along with other parameters.

```bash
python bisection_app.py
```

# Example

1. You will be prompted to input:
   - A continuous function (e.g., `f(x) = x^3 - x - 2`)
   - The interval endpoints `a` and `b` where the function changes signs.
   - Desired tolerance and maximum number of iterations.

2. The app will compute the root using the bisection method and display the results.

```python
# Example usage in code
from math import *

def f(x):
    return x3 - x - 2

root, iterations = bisection(f, a=1, b=2, tol=1e-6, max_iter=100)
print(f"Root: {root}, Iterations: {iterations}")
```

# Expected Output

```
Enter the function f(x): x3 - x - 2
Enter the interval [a, b]: 1, 2
Enter tolerance: 1e-6
Enter maximum iterations: 100

Root found: 1.5214 after 14 iterations
```

 Customization

You can modify the following parameters in the script:

- Function Definition: Modify the `f(x)` function to evaluate different mathematical functions.
- Interval `[a, b]`: Adjust the interval values where the root is assumed to exist.
- Tolerance: Set the precision of the root-finding process.
- Maximum Iterations: Limit the number of iterations the algorithm will perform before stopping.

 Limitations

- The bisection method requires that the function be continuous within the interval `[a, b]` and that `f(a)` and `f(b)` have opposite signs.
- Convergence can be slow compared to other root-finding methods like Newton's method, especially when a high degree of precision is required.

 License

This app is open-source and available under the MIT License. You are free to modify and distribute it as long as proper attribution is given.

 Contact

For questions, suggestions, or contributions, feel free to reach out to the author at [mo6633ya@gmail.com]

---

Enjoy using the Bisection Algorithm App!

