# Calculating decimals of π
This repository computes decimals of Pi (π) by means of the [Euler aproximation](http://mathworld.wolfram.com/πFormulas.html).

## Installation
Clone this repository and change directory to the correspondent folder.

Then type the following on the command line to calculate the first 50 decimals of π.

```
python3

>>> from pi import compute_pi
>>> compute_pi(50)
3.14159265358979323846264338327950288419716939937509
>>>
```

## Intro
The number π is by far one of the most famous, important and fascinating numbers in the history of mathematics. Defined as the constant relationship between the perimeter and the diameter of a circle, it has captured the imagination of countless mathematicians throughout history. Even more so since it was proved its irrationality - that is, its decimal representation is endless and it never settles into a permanent repeating pattern.

>Watch a scene from Person of Interest where they talk about π [here](https://www.youtube.com/watch?v=fXTRcsxG7IQ).

Also, π is a transcendental number, which means that it's not a solution to any polynomial equation with rational coefficients; it is impossible to solve the ancient challenge of squaring the circle with a compass and straightedge.

Both its irrationality and its trascendence force us to rephrase the challenge of calculating π, not in terms of the number itself, but in terms of the first X amount of decimals. No matter how good our algorithm is, there will always be a new decimal to be computed.

You can read more about it in the [Documentation](docs/Index.md)

## Contributing
>Check out how to contribute to this project [here](https://github.com/ohduran/number_pi/CONTRIBUTING.md)

## Authors

Built with love by Alvaro Duran.

## License
>You can check out the full license [here](https://github.com/ohduran/number_pi/LICENSE.md)

This project is under the terms of the **MIT** License.

## Changelog

20-Apr-2018: Version 2.0 is out! This includes a complete redesign of the project, leveraging the power of Object Oriented programming to design a simple and reader friendly `compute_pi` function.

02-Jun-2017: Calculating π using BigNo class is now included, along with some performance improvements in bigno document.

01-Jun-2017: BigNo class and associated functions (sum,product,division) were added (Patch 2). For now, the previous n_decimals list approach will remain, but will be deprecated in the future.

05-May-2017: It is intended in the future to treat this big numbers as a class on its own. For now (Patch 1), they are considered lists, where the index defines uniquely its decimal position (with 0 meaning integer).
