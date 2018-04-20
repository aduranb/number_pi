# Calculating as many decimals of number pi as possible

To be fair, this was an idea that I had when I was a Physics undergraduate: how did all this brainiacs come up with decimals of number pi. I did not find anything related on Google so I decided to give it a try myself, hoping that some smart guy will take advantage of this and even suggest some enhancements.

From the educational perspective, this project touches most of the Object Oriented programming features that every intermediate/advanced Python programmer should know: classes, inheritance, exceptions, ...

I am very dedicated to write a complete documentation on all this. You can find it by simply calling the __doc__ method on each class/function. Let me know if you find anything that is not clear so that I can improve that documentation.

As part of the creation of this code, a library to operate with big numbers was created. Its intended purpose may vary.

## Getting started

### Prerequisites
In the most up-to-date version (Patch 2), there is no need for any library to be preinstalled to run this code. Used an IDE with Python version 2.7.11 as a compiler.

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

## Changelog

20-Apr-2018: Version 2.0 is out! This includes a complete redesign of the project, leveraging the power of Object Oriented programming to design a simple and reader friendly `compute_pi` function.

05-May-2017: It is intended in the future to treat this big numbers as a class on its own. For now (Patch 1), they are considered lists, where the index defines uniquely its decimal position (with 0 meaning integer).

01-Jun-2017: BigNo class and associated functions (sum,product,division) were added (Patch 2). For now, the previous n_decimals list approach will remain, but will be deprecated in the future.

02-Jun-2017: Calculating pi using BigNo class is now included, along with some performance improvements in bigno document.

#### To Do
See the follwing list for contribution ideas that the author is expected to do at some point.

- __Include different approaches to number pi (for now, it's just euler)__. Leibniz to be included, but it's a slower method.

- __On bigno, include square roots as well__.

## Authors

Entirely my own (Alvaro Duran).

### Acknowledgments

Leonhard Euler ;)
