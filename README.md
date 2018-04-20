# Calculating as many decimals of number pi as possible
This repository computes decimals of Pi (π) by means of the [Euler aproximation](http://mathworld.wolfram.com/PiFormulas.html).

## Intro
The number π is by far one of the most famous, important and fascinating numbers in the history of mathematics. It is defined as the constant relationship between the perimeter and the diameter of a circle, and it has capture the imagination of countless of mathematicians throughout history.

Even more so since it was proved its irrationality - that is, pi has an infinite number of decimals, and they do not repeat, i.e., they do not contain a subsequence of digits, the repetition of which makes up the tail of the representation.

See a sneak peek of Person of Interest, where they talk about Pi, [here](https://www.youtube.com/watch?v=fXTRcsxG7IQ).



## Contributing
>Check out the how to contribute to this project [here](https://github.com/ohduran/number_pi/CONTRIBUTING.md)

## Authors

Built with love by Alvaro Duran.

## License
>You can check out the full license [here](https://github.com/ohduran/number_pi/LICENSE.md)

This project is licensed under the terms of the **MIT** license.

## Changelog

20-Apr-2018: Version 2.0 is out! This includes a complete redesign of the project, leveraging the power of Object Oriented programming to design a simple and reader friendly `compute_pi` function.

05-May-2017: It is intended in the future to treat this big numbers as a class on its own. For now (Patch 1), they are considered lists, where the index defines uniquely its decimal position (with 0 meaning integer).

01-Jun-2017: BigNo class and associated functions (sum,product,division) were added (Patch 2). For now, the previous n_decimals list approach will remain, but will be deprecated in the future.

02-Jun-2017: Calculating pi using BigNo class is now included, along with some performance improvements in bigno document.
