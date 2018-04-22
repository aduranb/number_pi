# Index
The content of this project is both a mathematical challenge and a programming one.

## Mathematical approach
The rationale behind how this task was approached math-wise can be found [here](docs/Mathematical Approach.md).

## Project architecture
The project uses Object Oriented programming to come up with a simple and easy to read `compute_pi` function.

```python
    while not euler_term.iszero():
          pi = pi + euler_term

          term += 1

          euler_term = LongDecimalEuler(
              term=term,
              nodecimals=nodecimals)
      pi.setprecision(nodecimals - 2)
      return pi
```

You can read more about it [here](docs/Project Architecture.md).
