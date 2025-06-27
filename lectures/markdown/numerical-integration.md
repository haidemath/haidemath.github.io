# Numerical Integration

## 4. 数值积分

当积分无法解析求解时，我们需要使用数值方法近似计算积分值。

### 4.1 梯形公式

#### 定理 4.1 (梯形公式)

对于积分 $$\int_a^b f(x) dx$$，梯形公式为：

$$\int_a^b f(x) dx \approx \frac{b-a}{2}[f(a) + f(b)]$$

其误差为：

$$E = -\frac{(b-a)^3}{12}f''(\xi), \quad \xi \in (a, b)$$

### 4.2 辛普森公式

#### 定理 4.2 (辛普森公式)

辛普森公式（抛物线公式）为：

$$\int_a^b f(x) dx \approx \frac{b-a}{6}\left[f(a) + 4f\left(\frac{a+b}{2}\right) + f(b)\right]$$

其误差为：

$$E = -\frac{(b-a)^5}{90 \cdot 2^4}f^{(4)}(\xi), \quad \xi \in (a, b)$$

### 4.3 复合求积公式

将积分区间分成 $$n$$ 个子区间，在每个子区间上应用基本求积公式。