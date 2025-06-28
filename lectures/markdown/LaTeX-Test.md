# LaTeX 数学环境测试

## 基本测试

这是一个行内公式：$x^2 + y^2 = z^2$

这是一个块级公式：
$$x^2 + y^2 = z^2$$

## Cases 环境测试

$$
f(x) = \begin{cases}
    x^2 & \text{if } x \geq 0 \\
    -x^2 & \text{if } x < 0
\end{cases}
$$

## 另一个 Cases 测试

$$
\begin{cases}
    1 = 1 \\
    2 = 2 \\
    3 = 3
\end{cases}
$$

## Matrix 环境测试

$$
A = \begin{pmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
\end{pmatrix}
$$

## Aligned 环境测试

$$
\begin{aligned}
x + y &= 1 \\
2x + 3y &= 4 \\
x - y &= 0
\end{aligned}
$$

## 复杂公式测试

$$
\sum_{i=1}^{n} x_i = \int_{0}^{1} f(x) \, dx
$$

$$
\lim_{x \to \infty} \frac{1}{x} = 0
$$

## 分式测试

$$
\frac{a + b}{c + d} = \frac{\sum_{i=1}^{n} x_i}{\prod_{j=1}^{m} y_j}
$$
