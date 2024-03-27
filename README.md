# Ulam Spiral

## Creating the Spiral

The Ulam Spiral is a diagram that depicts the natural numbers arranged in a square spiral, with the prime numbers highlighted (see [here](https://en.wikipedia.org/wiki/Ulam_spiral) for examples).

Create a function `ulam_square` that takes a natural number $n$ and creates this spiral up to the number $(2n + 1)^2$. Then, using either your own `isprime` function or the one from `sympy`, create a boolean array that is `True` wherever there is a prime number and `False` otherwise. Finally, use `imshow` from `matplotlib`to plot the spiral. Can you find any patterns?

## Extension

Another nice way of plotting primes is to plot the polar coordinates $(r=p, \theta=p)$ for each prime $p$. Try using `scatter` to plot all the prime numbers up to some natural number $N$. Try changing the value of $N$ and see if you can spot any patterns.