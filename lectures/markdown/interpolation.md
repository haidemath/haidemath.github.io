# Interpolation Methods in Numerical Analysis

Interpolation is a fundamental concept in numerical analysis, used to estimate unknown values that fall within the range of a discrete set of known data points. This document covers various interpolation methods, including Lagrange and Newton interpolation.

## 1. Lagrange Interpolation

Lagrange interpolation constructs a polynomial that passes through a given set of points. Given \( n+1 \) distinct nodes \( (x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n) \), the Lagrange interpolation polynomial is defined as:

$$
L_n(x) = \sum_{i=0}^{n} y_i \ell_i(x)
$$

where the Lagrange basis polynomial \( \ell_i(x) \) is given by:

$$
\ell_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

### Example

To interpolate the points \( (0, 1) \), \( (1, 0) \), and \( (2, 1) \), we can construct the Lagrange polynomial as follows:

1. Calculate the basis polynomials \( \ell_0(x) \), \( \ell_1(x) \), and \( \ell_2(x) \).
2. Combine them to form \( L_n(x) \).

## 2. Newton Interpolation

Newton's interpolation method uses divided differences to construct the interpolation polynomial. The Newton interpolation polynomial is expressed as:

$$
N_n(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \cdots
$$

### Divided Differences

The first-order divided difference is defined as:

$$
f[x_i, x_j] = \frac{f(x_j) - f(x_i)}{x_j - x_i}
$$

Higher-order divided differences are defined recursively.

## Conclusion

Interpolation methods are essential tools in numerical analysis, allowing for the estimation of values and the construction of functions that fit a set of data points. Understanding these methods is crucial for applications in various fields, including engineering, science, and finance.