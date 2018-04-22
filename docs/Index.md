# Index
The content of this project is both a mathematical challenge and a programming one.

## Mathematical approach
The rationale behind how this task was approached math-wise can be found [here](https://github.com/ohduran/number_pi/blob/master/docs/Mathematical%20Approach.md).

## Project architecture
The project uses Object Oriented programming to come up with a simple and easy to read `compute_pi` function.

```python
    while not euler_term.iszero():
          pi = pi + euler_term

          term += 1

          euler_term = LongDecimalEuler(
              term=term,
              nodecimals=nodecimals)
      return pi
```

You can read more about it [here](https://github.com/ohduran/number_pi/blob/master/docs/Project%20Architecture.md).
