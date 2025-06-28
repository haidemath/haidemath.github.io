# MathJax LaTeX 环境全面测试

## 基本公式

行内公式：这是 $E = mc^2$ 的著名公式。

块级公式：
$$E = mc^2$$

## Cases 环境测试

$$
f(x) = \begin{cases}
    x^2 & \text{if } x \geq 0 \\
    -x^2 & \text{if } x < 0
\end{cases}
$$

$$
\begin{cases}
    1 = 1 \\
    2 = 2 \\
    3 = 3
\end{cases}
$$

## 矩阵环境

普通矩阵：
$$
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
$$

带括号的矩阵：
$$
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
$$

带方括号的矩阵：
$$
B = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

## 对齐环境

$$
\begin{align}
x + y &= 1 \\
2x + 3y &= 4 \\
x - y &= 0
\end{align}
$$

$$
\begin{aligned}
\sin^2 x + \cos^2 x &= 1 \\
\tan x &= \frac{\sin x}{\cos x} \\
\cot x &= \frac{\cos x}{\sin x}
\end{aligned}
$$

## 方程组环境

$$
\begin{equation}
\left\{
\begin{aligned}
x + y + z &= 6 \\
2x - y + z &= 3 \\
x + 2y - z &= 1
\end{aligned}
\right.
\end{equation}
$$

## 复杂公式

求和：
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

积分：
$$
\int_{0}^{1} f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f\left(\frac{i}{n}\right) \frac{1}{n}
$$

极限：
$$
\lim_{x \to \infty} \frac{1}{x} = 0
$$

## 分式和根式

分式：
$$
\frac{a + b}{c + d} = \frac{\sum_{i=1}^{n} x_i}{\prod_{j=1}^{m} y_j}
$$

根式：
$$
\sqrt{x^2 + y^2} = \sqrt[3]{x^3 + y^3 + z^3}
$$

## 多行公式

$$
\begin{multline}
\text{这是一个很长的公式} \\
= a + b + c + d + e + f + g + h + i + j \\
= \text{最终结果}
\end{multline}
$$

## 特殊符号和集合

$$
\mathbb{R}, \mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{C}
$$

$$
\forall x \in \mathbb{R}, \exists y \in \mathbb{N} : x < y
$$

$$
A \cup B = \{x : x \in A \text{ or } x \in B\}
$$

$$
A \cap B = \{x : x \in A \text{ and } x \in B\}
$$
