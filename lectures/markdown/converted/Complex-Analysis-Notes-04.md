[← 上一章](../viewer.html?md=Complex-Analysis-Notes-Chapter-3)

## 解析函数的幂级数展开



### 复级数



#### 复数项级数



> **定义**
>
> 一列复数 $\{a_{n}\}$, 称 $a_{1}+a_{2}+\cdots+a_{n}+\cdots=\sum_{n=1}^{\infty}a_{n}$ 为一个复数项级数, 简称复级数, 其中 $a_{n}$ 称为通项.
>
>
> $S_{n}=a_{1}+a_{2}+\cdots+a_{n}$ 称为前 $n$ 项和. 若 $\lim_{n\to\infty}S_{n}=S$ 存在, 则称级数收敛, $S$ 称为和. 否则称级数发散.


收敛的必要条件: $\lim_{n\to\infty}a_{n}=0$.

若 $\sum a_{n}$ 收敛但 $\sum|a_{n}|$ 发散, 则称 $\sum a_{n}$ 条件收敛. 若 $\sum|a_{n}|$ 收敛, 则称 $\sum a_{n}$ 绝对收敛 (此时 $\sum a_{n}$ 必收敛).
$$
\text{级数}\begin{cases}
\text{发散}\\
\text{收敛}\begin{cases}
\text{条件收敛}\\
\text{绝对收敛}
\end{cases}
\end{cases}
$$

例如: $\sum_{n=1}^{\infty}\frac{1}{n(n+1)}$, $S_{n}=1-\frac{1}{n+1}\to1$.

若 $\alpha_{n}=a_{n}+ib_{n}$, 则 $\sum\alpha_{n}=S\Leftrightarrow\sum a_{n}=\operatorname{Re}S$, $\sum b_{n}=\operatorname{Im}S$.

柯西收敛准则: $\sum a_{n}$ 收敛 $\Leftrightarrow\forall\varepsilon>0,\exists N$, 当 $n>N$ 时 $\forall p\in\mathbb{N}^{+}$ 都有 $|a_{n+1}+\cdots+a_{n+p}|<\varepsilon$.


#### 函数项级数



> **定义**
>
> 定义在点集 $E$ 上的函数列 $\{f_{n}(z)\}$, 称 $\sum_{n=1}^{\infty}f_{n}(z)$ 为一个复函数项级数.
>
>
> 若对 $z\in E$, $\sum f_{n}(z)$ 收敛, 则称 $z$ 为收敛点; 否则称为发散点.
> 收敛点的全体称为收敛域, 级数在收敛域上的和 $f(z)$ 称为和函数.


一致收敛: 若 $\forall\varepsilon>0$, $\exists N$, 当 $n>N$ 时, $\forall z\in E$, 都有 $|S_{n}(z)-f(z)|<\varepsilon$, 则称 $\sum f_{n}(z)$ 在 $E$ 上一致收敛到 $f(z)$.

分析定义: $\sum_{n=1}^{\infty}f_{n}(z)=f(z)\Leftrightarrow\forall\varepsilon>0$, $\exists N=N(\varepsilon,z)$, 当 $n>N$ 时 $|S_{n}(z)-f(z)|<\varepsilon$. 其中 $S_{n}(z)=\sum_{i=1}^{n}f_{i}(z)$.

逐点收敛的 Cauchy 准则: 对固定 $z\in E$, $\sum f_n(z)$ 收敛
$\Leftrightarrow\forall\varepsilon>0$, $\exists N=N(\varepsilon,z)$, 当 $n>N$ 时对任意 $p\in\mathbb N^+$ 有
$|f_{n+1}(z)+\cdots+f_{n+p}(z)|<\varepsilon$.

柯西收敛准则: $\sum f_{n}(z)$ 一致收敛到 $f(z)\Leftrightarrow\forall\varepsilon>0$, $\exists N=N(\varepsilon)$, $\forall z\in D$, $\forall p\in\mathbb{N}^{+}$ 都有 $|f_{n+1}(z)+\cdots+f_{n+p}(z)|<\varepsilon$.


> **定理**
>
> [控制收敛定理/Weierstrass 判别法]
> 若 $|f_{n}(z)|\leq M_{n}$ 对 $\forall z\in E$ 成立, 且 $\sum M_{n}$ 收敛, 则 $\sum f_{n}(z)$ 在 $E$ 上绝对且一致收敛.



##### 一致收敛的性质



> **定理**
>
> 若 $\sum f_{n}(z)$ 在 $D$ 上一致收敛到 $f(z)$, 且每个 $f_{n}(z)$ 在 $D$ 上连续, 则 $f(z)$ 在 $D$ 上连续.



> **证明**
>
> 取 $z_{0}\in D$, 由于 $\sum f_{n}(z)$ 一致收敛到 $f(z)$, $\forall\varepsilon>0$, $\exists N$, 当 $n>N$ 时 $\forall z\in D$ 都有 $|S_{n}(z)-f(z)|<\frac{\varepsilon}{3}$. 取 $n=N+1$ 时也有 $|S_{N+1}(z)-f(z)|<\frac{\varepsilon}{3}$.
> 又 $S_{N+1}(z)=f_{1}(z)+\cdots+f_{N+1}(z)$ 在 $z_{0}$ 连续, 对上述 $\varepsilon>0$, $\exists\delta>0$, 当 $|z-z_{0}|<\delta$ 时 $|S_{N+1}(z)-S_{N+1}(z_{0})|<\frac{\varepsilon}{3}$.
> 则当 $|z-z_{0}|<\delta$ 时,
> $$
> |f(z)-f(z_{0})|\leq|f(z)-S_{N+1}(z)|+|S_{N+1}(z)-S_{N+1}(z_{0})|+|S_{N+1}(z_{0})-f(z_{0})|
> <\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon.
> $$
> 故 $f(z)$ 在 $z_{0}$ 连续, 由 $z_{0}$ 的任意性得 $f(z)$ 在 $D$ 上连续.



> **定理**
>
> 若 $\sum f_{n}(z)$ 在 $C$ 上一致收敛到 $f(z)$, 且每个 $f_{n}(z)$ 在 $C$ 上连续, 则可逐项积分:
> $$
> \int_{C}\sum_{n=1}^{\infty}f_{n}(z)\,dz=\sum_{n=1}^{\infty}\int_{C}f_{n}(z)\,dz.
> $$



> **定理**
>
> 若 $f_{n}(z)$ 都在区域 $D$ 上解析, 且 $\sum f_{n}(z)$ 在 $D$ 上一致收敛于 $f(z)$, 则 $f(z)$ 在 $D$ 上解析, 且可以逐项求任意阶导数:
> $$
> f^{(k)}(z)=\sum_{n=1}^{\infty}f_{n}^{(k)}(z).
> $$



> **证明**
>
> (1) 先证 $f(z)$ 解析: 任取 $D$ 内围线 $C$, $\sum f_{n}(z)$ 在 $C$ 上一致收敛于 $f(z)$. 则 $\oint_{C}f(z)\,dz=\sum_{n=1}^{\infty}\oint_{C}f_{n}(z)\,dz$. 由柯西积分定理, $\oint_{C}f_{n}(z)\,dz=0$, 于是 $\oint_{C}f(z)\,dz=0$. 由 Morera 定理, $f(z)$ 在 $D$ 内解析.
>
> (2) 求任意阶导数: $\forall z\in D$, 取内部含 $z$ 的围线 $C$, $\sum_{n=1}^{\infty}f_{n}(z)$ 在 $C$ 上一致收敛到 $f(z)$, 进而 $\forall k\in\mathbb{N}^{+}$, $\sum_{n=1}^{\infty}\frac{k!}{2\pi i}\frac{f_{n}(\zeta)}{(\zeta-z)^{k+1}}$ 在 $C$ 上一致收敛到 $\frac{k!}{2\pi i}\frac{f(\zeta)}{(\zeta-z)^{k+1}}$. 再逐项积分可知, $\sum_{n=1}^{\infty}\frac{k!}{2\pi i}\oint_{C}\frac{f_{n}(\zeta)}{(\zeta-z)^{k+1}}\,d\zeta=\frac{k!}{2\pi i}\oint_{C}\frac{f(\zeta)}{(\zeta-z)^{k+1}}\,d\zeta$, 即 $\sum_{n=1}^{\infty}f_{n}^{(k)}(z)=f^{(k)}(z)$.




### 幂级数



#### 幂级数的收敛圆



> **定义**
>
> 一个复数列 $\{c_{n}\}$ 和复数 $a$ 决定下列形式的函数项级数:
> $$
> c_{0}+c_{1}(z-a)+c_{2}(z-a)^{2}+\cdots=\sum_{n=0}^{\infty}c_{n}(z-a)^{n},
> $$
> 称为一个幂级数. 特别地, $a=0$ 时 $\sum_{n=0}^{\infty}c_{n}z^{n}$.



> **注**
>
> 收敛域一定不是空集: 在 $z=a$ 处一定收敛.



> **定理**
>
> [Abel 定理]
> 若 $\sum c_{n}z^{n}$ 在一点 $z_{0}\neq0$ 处收敛, 则在圆域 $|z|<|z_{0}|$ 上 $\sum c_{n}z^{n}$ 绝对且内闭一致收敛.
> 若 $\sum c_{n}z^{n}$ 在一点 $z_{0}$ 处发散, 则在圆域 $|z|>|z_{0}|$ 上 $\sum c_{n}z^{n}$ 发散.



> **证明**
>
> $\sum c_{n}z_{0}^{n}$ 收敛 $\Rightarrow c_{n}z_{0}^{n}\to0\Rightarrow\{c_{n}z_{0}^{n}\}$ 有界, 记 $|c_{n}z_{0}^{n}|\leq M$.
>
> 当 $|z|<|z_{0}|$ 时, $|c_{n}z^{n}|=|c_{n}z_{0}^{n}\cdot(\frac{z}{z_{0}})^{n}|\leq M\cdot|\frac{z}{z_{0}}|^{n}=M\cdot r^{n}\ (r<1)$.
>
> 由正项级数判别法知 $\sum|c_{n}z^{n}|$ 收敛, 即 $\sum c_{n}z^{n}$ 绝对收敛.
>
> 在 $K$ 内任取一个小闭圆: $|z|\leq\rho\ (\rho<|z_{0}|)$,
> $|c_{n}z^{n}|\leq M\cdot(\frac{\rho}{|z_{0}|})^{n}=M\cdot r^{n}\ (0<r<1)$,
> 由 Weierstrass 判别法, $\sum c_{n}z^{n}$ 在 $|z|\leq\rho$ 上一致收敛.
>
> 若 $\sum c_{n}z^{n}$ 在 $z_{0}$ 发散, 当 $|z|>|z_{0}|$ 时显然发散 (反证法可得).



> **推论**
>
> 若 $\sum c_{n}z^{n}$ 不仅在 $z=0$ 收敛, 也不是在 $z$ 平面上处处收敛, 则存在 $R=\sup\{|z|:\sum c_{n}z^{n}\text{收敛}\}$ 使 $|z|<R$ 时 $\sum c_{n}z^{n}$ 绝对且内闭一致收敛, 当 $|z|>R$ 时 $\sum c_{n}z^{n}$ 发散. $R$ 称为收敛半径.



> **注**
>
> 若 $\sum c_{n}z^{n}$ 仅在 $z=0$ 收敛, 则 $R=0$; 若在 $z$ 平面上处处收敛, 则 $R=+\infty$.



> **定义**
>
> 若 $\sum c_{n}z^{n}$ 的收敛半径 $R>0$, 则称圆域 $K:|z|<R$ 为其收敛圆.



> **注**
>
> 幂级数 $\sum c_{n}z^{n}$ 在其收敛圆内绝对且内闭一致收敛, 在其外部发散, 在圆周 $|z|=R$ 上至少有一点不解析 (奇点).
>
> 例如: $\sum_{n=0}^{\infty}\frac{z^{n}}{n!}$ 在全平面收敛 ($R=+\infty$); $\sum_{n=0}^{\infty}n!z^{n}$ 仅在 $z=0$ 收敛 ($R=0$);
> $\sum_{n=0}^{\infty}z^{n}=\frac{1}{1-z}$ 在 $|z|<1$ 绝对收敛 (但不一致收敛).



> **定理**
>
> 已知幂级数 $\sum c_{n}(z-a)^{n}$:
>
> 1. 若 $\lim\limits_{n\to\infty}\bigl|\frac{c_{n+1}}{c_{n}}\bigr|=\rho$, 则 $R=\frac{1}{\rho}$;
> 1. 若 $\lim\limits_{n\to\infty}\sqrt[n]{|c_{n}|}=\rho$, 则 $R=\frac{1}{\rho}$;
> 1. 若 $\limsup\limits_{n\to\infty}\sqrt[n]{|c_{n}|}=\rho$, 则 $R=\frac{1}{\rho}$.
>



> **注**
>
> 这里 $\rho=0$ 时 $R=+\infty$, $\rho=+\infty$ 时 $R=0$. 证明同于实分析.


以上对 $\sum c_{n}(z-a)^{n}$ 也成立, 同样可定义收敛半径、收敛圆.


#### 幂级数和函数的解析性



> **定理**
>
> 设 $\sum c_{n}(z-a)^{n}$ 的收敛半径 $R>0$, 在收敛圆 $|z-a|<R$ 内, 其和函数 $f(z)$ 解析, 且可逐项求任意阶导数:
> $$
> f^{(k)}(z)=\Bigl(\sum_{n=0}^{\infty}c_{n}(z-a)^{n}\Bigr)^{(k)}
> =\sum_{n=0}^{\infty}\bigl(c_{n}(z-a)^{n}\bigr)^{(k)}
> =\sum_{n=k}^{\infty}n(n-1)\cdots(n-k+1)c_{n}(z-a)^{n-k}.
> $$



> **证明**
>
> 由 Abel 引理和一致收敛的性质, 显然成立.




### 解析函数的幂级数展式



#### Taylor 展开定理



> **定理**
>
> 设 $f(z)$ 在区域 $D$ 上解析, $a\in D$, 记 $K:|z-a|<R$ 且 $K\subset D$, 则 $f(z)$ 在 $K$ 内可展成 $z-a$ 的幂级数:
> $$
> f(z)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(z-a)^{n}.
> $$



> **证明**
>
> 任取 $z\in K$. 取 $\rho$ 使 $|z-a|<\rho<R$, 记 $\Gamma_{\rho}:|\zeta-a|=\rho$. 由柯西积分公式,
> $$
> f(z)=\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(\zeta)}{\zeta-z}\,d\zeta
> =\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(\zeta)}{\zeta-a}\cdot
> \frac{1}{1-\frac{z-a}{\zeta-a}}\,d\zeta.
> $$
> 因为 $\left|\frac{z-a}{\zeta-a}\right|<1$, 可在 $\Gamma_{\rho}$ 上一致展开为几何级数, 从而逐项积分:
> $$
> f(z)=\sum_{n=0}^{\infty}
> \left[\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta\right](z-a)^{n}
> =\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(z-a)^{n}.
> $$



> **定义**
>
> 上式称为 $f(z)$ 在 $z=a$ 的泰勒级数, 其系数 $c_{n}=\frac{f^{(n)}(a)}{n!}$ 称为泰勒系数.



> **推论**
>
> [展式唯一性]
> 若 $f(z)$ 在 $z=a$ 展成 $z-a$ 的幂级数 $f(z)=\sum_{n=0}^{\infty}c_{n}(z-a)^{n}$, 则 $c_{n}=\frac{f^{(n)}(a)}{n!}$, 即展式唯一.



> **证明**
>
> 取 $\Gamma_{\rho}:|z-a|=\rho$ ($\rho$ 很小), 由 $\sum c_{n}(z-a)^{n}$ 内闭一致收敛,
> $$
> \frac{f(z)}{(z-a)^{k+1}}=\frac{c_{0}}{(z-a)^{k+1}}+\frac{c_{1}}{(z-a)^{k}}+\cdots+\frac{c_{k}}{z-a}+c_{k+1}+\cdots
> $$
> 两边积分: $\oint_{\Gamma_{\rho}}\frac{f(z)}{(z-a)^{k+1}}\,dz=c_{k}\cdot2\pi i$, 故 $c_{k}=\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(z)}{(z-a)^{k+1}}\,dz=\frac{f^{(k)}(a)}{k!}$.



> **推论**
>
> $f(z)$ 在 $D$ 内解析 $\Leftrightarrow$ $f(z)$ 在 $D$ 内任一点 $a$ 的邻域可展成 $z-a$ 的幂级数.



> **证明**
>
> $\Rightarrow$ 由 Taylor 定理. $\Leftarrow$ 由幂级数的和函数解析.



#### 常见函数的 Taylor 展式



1. $e^{z}=1+z+\frac{z^{2}}{2!}+\cdots=\sum_{n=0}^{\infty}\frac{z^{n}}{n!}$, $|z|<+\infty$.
1. $\frac{1}{1-z}=1+z+z^{2}+\cdots=\sum_{n=0}^{\infty}z^{n}$, $|z|<1$.
1. $\sin z=\dfrac{e^{iz}-e^{-iz}}{2i}=z-\frac{z^{3}}{3!}+\frac{z^{5}}{5!}-\cdots=\sum_{n=0}^{\infty}(-1)^{n}\frac{z^{2n+1}}{(2n+1)!}$, $|z|<+\infty$;
  $\cos z=\dfrac{e^{iz}+e^{-iz}}{2}=1-\frac{z^{2}}{2!}+\frac{z^{4}}{4!}-\cdots=\sum_{n=0}^{\infty}(-1)^{n}\frac{z^{2n}}{(2n)!}$, $|z|<+\infty$.
1. $\ln(1+z)=z-\frac{z^{2}}{2}+\frac{z^{3}}{3}-\cdots=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{z^{n}}{n}$, $|z|<1$.
1. $(1+z)^{\alpha}=1+\alpha z+\frac{\alpha(\alpha-1)}{2!}z^{2}+\cdots=\sum_{n=0}^{\infty}\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}z^{n}$, $|z|<1$.



> **注**
>
> 上述展式 4 (对数展式) 和 5 (二项式展式) 均取主值支.



> **例**
>
> 将 $f(z)=e^{z}\sin z$ 展成 $z$ 的幂级数.
> $$
> f(z)=e^{z}\sin z=e^{z}\cdot\frac{e^{iz}-e^{-iz}}{2i}
> =\frac{1}{2i}\bigl(e^{(1+i)z}-e^{(1-i)z}\bigr)
> =\frac{1}{2i}\sum_{n=0}^{\infty}\frac{(1+i)^{n}-(1-i)^{n}}{n!}z^{n},\quad|z|<+\infty.
> $$



> **例**
>
> 将 $f(z)=e^{z}(\cos z+i\sin z)$ 展成 $z$ 的幂级数. 由 $\cos z+i\sin z=e^{iz}$,
> $$
> f(z)=e^{z}\cdot e^{iz}=e^{(1+i)z}=\sum_{n=0}^{\infty}\frac{(1+i)^{n}}{n!}z^{n}
> =\sum_{n=0}^{\infty}\frac{(\sqrt{2}\,e^{i\pi/4})^{n}}{n!}z^{n},\quad |z|<+\infty.
> $$



> **例**
>
> 将 $f(z)=\frac{1}{(z-1)(z-2)}$ 展成 $z$ 的幂级数.
>
>
> 解:
> $$
> f(z)=\frac{1}{(z-1)(z-2)}=\frac{1}{z-2}-\frac{1}{z-1}
> =\frac{1}{1-z}-\frac{1}{2}\frac{1}{1-\frac{z}{2}}
> =\sum_{n=0}^{\infty}\Bigl(1-\frac{1}{2^{n+1}}\Bigr)z^{n},\quad|z|<1.
> $$




### 解析函数的一般性及最大模原理



#### 解析函数的零点



> **定义**
>
> 若解析函数 $f(z)$ 在点 $a$ 满足 $f(a)=0$, 则称 $a$ 是 $f(z)$ 的一个零点.



> **定义**
>
> 若 $f(z)$ 在 $a$ 点解析, 且 $f(a)=f'(a)=\cdots=f^{(m-1)}(a)=0$, $f^{(m)}(a)\neq0$ ($m\geq1$), 则称 $a$ 是 $f(z)$ 的 $m$ 级零点.


例如: $f(z)=z^{2}$ 在 $z=0$ 是 2 级零点; $f(z)=(z-3)^{5}$ 在 $z=3$ 是 5 级零点; $f(z)=z-\sin z$ 在 $z=0$ 是 3 级零点.


> **注**
>
> 非零的解析函数的零点存在时必有级 (实分析中不一定成立).



> **定理**
>
> $a$ 是 $f(z)$ 的 $m$ 级零点 $\Leftrightarrow$ $f(z)=(z-a)^{m}\varphi(z)$, 其中 $\varphi(z)$ 在 $a$ 解析且 $\varphi(a)\neq0$.



> **证明**
>
> 若 $a$ 是 $m$ 级零点, 则在 $a$ 的邻域内
> $$
> f(z)=\frac{f^{(m)}(a)}{m!}(z-a)^{m}+\frac{f^{(m+1)}(a)}{(m+1)!}(z-a)^{m+1}+\cdots
> =(z-a)^{m}\varphi(z),
> $$
> 其中 $\varphi$ 在 $a$ 解析且 $\varphi(a)=\frac{f^{(m)}(a)}{m!}\neq0$.
>
> 反之, 若 $f(z)=(z-a)^{m}\varphi(z)$ 且 $\varphi(a)\neq0$, 将 $\varphi$ 在 $a$ 展成 Taylor 级数, 由展开唯一性可知
> $f(a)=f'(a)=\cdots=f^{(m-1)}(a)=0$, 且 $f^{(m)}(a)=m!\varphi(a)\neq0$, 故 $a$ 是 $m$ 级零点.



#### 零点的孤立性



> **定理**
>
> [零点孤立性定理]
> 若 $f(z)$ 在 $D$ 上解析且不恒为零, $a$ 是 $f(z)$ 的零点, 则存在 $a$ 的某邻域, 在该邻域内除 $a$ 外 $f(z)$ 无其他零点.



> **证明**
>
> 由上一定理, $f(z)=(z-a)^{m}\varphi(z)$, 其中 $\varphi$ 在 $a$ 解析且 $\varphi(a)\neq0$. 由连续性, 存在 $a$ 的某邻域使 $\varphi(z)\neq0$. 在该邻域内, $f(z)$ 的零点只能是 $z=a$.



> **推论**
>
> 设 $f(z)$ 在圆域 $K$ 上解析, $\{z_{n}\}\subset K$, $z_{n}\to a\in K$, $z_{n}\neq a$, 且 $f(z_{n})=0$, 则 $f\equiv0$ 于 $K$.



> **证明**
>
> 由连续性 $f(a)=0$. 由零点孤立性, $f$ 在 $a$ 的某邻域内 $f\equiv0$, 于是 $f(a)=f^{(n)}(a)=0$ ($n=1,2,\cdots$).
> 由 Taylor 定理, 在 $z=a$ 有 $f$ 的幂级数恒为 $0$, 故在圆域上 $f\equiv0$.



#### 解析函数的唯一性



> **定理**
>
> [唯一性定理]
> 设 $f(z)$ 与 $g(z)$ 在区域 $D$ 上都解析, 且存在 $D$ 上收敛于 $a\in D$ 的点列 $\{z_{n}\}$, $z_{n}\neq a$, 使得 $f(z_{n})=g(z_{n})$, 则在 $D$ 上 $f(z)\equiv g(z)$.



> **证明**
>
> 记 $F=f-g$. $\{z_{n}\}$ 与 $a$ 均为 $F$ 的零点. 由推论, $\exists a$ 的邻域 $K_{0}:|z-a|<\rho_{0}$ 使在 $K_{0}$ 上 $F\equiv0$.
> $\forall b\in D$, 下证 $F(b)=0$:
> 用 $D$ 内折线连接 $a$ 到 $b$, 加入分点 $a=z_{0},z_{1},\cdots,z_{n-1},z_{n}=b$.
> 以 $z_{0},\cdots,z_{n-1}$ 为圆心作小圆 $K_{0},K_{1},\cdots,K_{n-1}$ 且 $K_{i}\subset D$,
> $z_{i}\in K_{i-1}$ ($i=1,\cdots,n-1$), $b\in K_{n-1}$.
> 于是在 $K_{0}$ 内 $F\equiv0$, 类似在 $K_{1}$ 内 $F\equiv0$, $\cdots$, 这样在 $K_{n-1}$ 上 $F\equiv0$, 而 $b\in K_{n-1}$, 于是 $F(b)=0$.
> 由 $b$ 的任意性, $F\equiv0$, 即 $f\equiv g$.



#### 最大模原理



> **定理**
>
> [最大模原理]
> 设 $f(z)$ 在区域 $D$ 上解析且非常数, 则 $|f(z)|$ 在 $D$ 上没有最大值.



> **证明**
>
> 记 $\sup_{z\in D}|f(z)|=M$.
> 若 $M=+\infty$, 结论显然成立.
> 若 $0<M<+\infty$, 若 $\exists z_{0}\in D$ 使 $|f(z_{0})|=M$,
> 取 $K:|z-z_{0}|<R$ 使 $K\subset D$, 由平均值定理,
> $$
> f(z_{0})=\frac{1}{2\pi}\int_{0}^{2\pi}f(z_{0}+\rho e^{i\theta})\,d\theta\quad(0<\rho<R).
> $$
> $$
> M=|f(z_{0})|\leq\frac{1}{2\pi}\int_{0}^{2\pi}|f(z_{0}+\rho e^{i\theta})|\,d\theta
> \leq\frac{1}{2\pi}\cdot M\cdot2\pi=M.
> $$
> 若 $\exists\theta_{0}$ 使 $|f(z_{0}+\rho e^{i\theta_{0}})|<M$, 则上式中间 $<M$, 矛盾. 故在 $|z-z_{0}|=\rho$ 上 $|f(z)|\equiv M$. 由 $\rho$ 的任意性, 在 $K:|z-z_{0}|<R$ 上 $|f(z)|\equiv M$.
> 于是 $f$ 在 $K$ 上恒为常数. 由唯一性定理, $f(z)$ 在 $D$ 上恒为常数,
> 与条件矛盾. 故 $|f(z)|$ 在 $D$ 上取不到最大值.



> **推论**
>
> 若 $f(z)$ 在有界闭区域 $\overline{D}=D+C$ 上连续, 在 $D$ 上解析, 则 $|f(z)|$ 的最大值在边界 $C$ 上取到, 当 $f(z)$ 非常数时 $|f(z)|$ 的最大值在 $D$ 内取不到.



> **定理**
>
> [最小模定理]
> 设 $f(z)$ 在区域 $D$ 上解析、非常数且在 $D$ 上无零点, 则 $|f(z)|$ 在 $D$ 内取不到最小值.



> **证明**
>
> $F(z)=1/f(z)$ 在 $D$ 上解析且非常数. 若 $|f|$ 在 $D$ 内某点取到正的最小值,
> 则 $|F|=1/|f|$ 在该点取到最大值, 与最大模原理矛盾.



> **推论**
>
> 设 $f$ 在有界闭区域 $\overline D=D\cup C$ 上连续, 在 $D$ 上解析、非常数且无零点,
> 则 $|f|$ 的最大值与最小值都在边界 $C$ 上取到.



#### Schwarz 引理



> **定理**
>
> [Schwarz 引理]
> 设 $f(z)$ 在 $|z|<1$ 上解析, 且 $f(0)=0$, $|f(z)|\leq1$, 则:
> (1) 在 $|z|<1$ 上 $|f(z)|\leq|z|$;
> (2) 若存在一点 $z_{0}$ 满足 $0<|z_{0}|<1$ 且 $|f(z_{0})|=|z_{0}|$, 则 $f(z)=e^{i\alpha}z$;
> (3) $|f'(0)|\leq1$.



> **证明**
>
> (1) $f(z)$ 在 $z=0$ 处展成 Taylor 级数: $f(z)=f(0)+f'(0)z+\frac{f''(0)}{2!}z^{2}+\cdots=z(f'(0)+\frac{f''(0)}{2!}z+\cdots)=z\cdot\varphi(z)$,
> 其中
> $$
> \varphi(z)=
> \begin{cases}
> \dfrac{f(z)}{z}, & 0<|z|<1,\\[4pt]
> f'(0), & z=0
> \end{cases}
> $$
> 在 $|z|<1$ 上解析.
>
> $\forall z_{0}$, $|z_{0}|<1$. 若 $z_{0}=0$, 则 $|f(0)|=0\leq0$, 显然成立.
> 若 $|z_{0}|<1$ 且 $z_{0}\neq0$, 取 $\Gamma_{\rho}:|z|=\rho$ 满足 $|z_{0}|<\rho<1$, 由最大模原理:
> $|\varphi(z_{0})|\leq\max_{z\in\Gamma_{\rho}}|\varphi(z)|\leq\max_{z\in\Gamma_{\rho}}\bigl|\frac{f(z)}{z}\bigr|\leq\frac{1}{\rho}$.
> 令 $\rho\to1^{-}$, 得 $|\varphi(z_{0})|\leq1$, 即 $|f(z_{0})|\leq|z_{0}|$.
>
> (2) 若 $\exists z_{0}$, $0<|z_{0}|<1$ 使 $|f(z_{0})|=|z_{0}|$, 则 $|\varphi(z_{0})|=1$.
> 于是 $\varphi(z)$ 在 $\Gamma_{\rho}$ 内取到最大模, $\varphi(z)$ 在 $|z|<\rho$ 上恒为常数.
> 由 $|z_{0}|<\rho<1$ 知 $\varphi(z)$ 在 $|z|<1$ 上恒为常数, $|\varphi(z)|=1$.
> 记 $\varphi(z)=e^{i\alpha}$, 在 $|z|<1$ 上 $f(z)=e^{i\alpha}z$.
>
> (3) $f'(0)=\lim_{z\to0}\frac{f(z)}{z}$, 由 $\bigl|\frac{f(z)}{z}\bigr|\leq1$, 得 $|f'(0)|\leq1$.



> **例**
>
> 假设 $f(z)$ 在 $|z|<1$ 上解析且 $|f(z)|<1$, 则 $|f'(0)|\leq1-|f(0)|^{2}$.
>
> > **证明**
> >
> > 构造 $F(z)=\frac{f(z)-f(0)}{1-\overline{f(0)}f(z)}$, 则 $F(z)$ 在 $|z|<1$ 上解析且 $F(0)=0$, $|F(z)|<1$.
> > 由 Schwarz 引理, $|F'(0)|\leq1$. 而
> > $$
> > F'(z)=\frac{f'(z)[1-\overline{f(0)}f(z)]+\overline{f(0)}f'(z)[f(z)-f(0)]}{(1-\overline{f(0)}f(z))^{2}}
> > \xrightarrow{z=0}\frac{f'(0)}{1-|f(0)|^{2}},
> > $$
> > 于是 $|f'(0)|\leq1-|f(0)|^{2}$.
>




### 习题课


基本原理与结论：

1. 幂级数在收敛圆内绝对且内闭一致收敛, 且和函数是解析函数.
1. 在区域 $D$ 上解析的函数 $f(z)$ 在 $D$ 内任一点可展成 $z-a$ 的 Taylor 级数.
1. $m$ 级零点的判别法: $f(z)=(z-a)^{m}\varphi(z)$, $\varphi(a)\neq0$.
1. 零点的孤立性定理与解析函数的唯一性定理.
1. 最大模原理.



#### 综合练习



> **例**
>
> 设 $f(z)$ 是整函数, 且 $\forall z\in\mathbb{R}$, $f(z)=\sin z$, 则 $f(z)=\sin z$ (由唯一性定理).



> **例**
>
> (1) 对任意 $\rho>0$，在 $\Gamma_{\rho}:|z|=\rho$ 上至少存在一点 $z_{0}$ 使 $|\cos z_{0}|>1$.
>
> > **证明**
> >
> > $f(z)=\cos z$ 是整函数, 由 $\cos0=1$ 及最大模原理,
> > $|\cos0|<\max_{z\in\Gamma_{\rho}}|\cos z|\Rightarrow\exists z_{0}\in\Gamma_{\rho}$ s.t. $|\cos z_{0}|>|\cos0|=1$.
>
>
> (2) $f(z)$ 在区域 $D$ 上解析、在闭区域 $\overline{D}=D\cup C$ 上连续,
> 且 $\exists m>0,z_{0}\in D$ 使 $|f(z_{0})|<m$ 且
> $\min_{z\in C}|f(z)|>m$, 则 $f(z)$ 在 $D$ 内至少有一个零点.
>
> > **证明**
> >
> > 若 $f$ 在 $D$ 内无零点且非常数，则由最小模原理，
> > $|f(z_{0})|\geq\min_{z\in C}|f(z)|>m$，与 $|f(z_{0})|<m$ 矛盾。
> > 若 $f$ 为常数，同一矛盾也直接成立。因此 $f$ 在 $D$ 内必有零点.
>



> **例**
>
> 设 $f(z),g(z)$ 都在区域 $D$ 上解析, 且 $\exists z_{0}\in D$ 使
> $f^{(n)}(z_{0})=g^{(n)}(z_{0})$, $n=0,1,2,\cdots$, 则在 $D$ 上
> $f(z)\equiv g(z)$.
>
>
>
> > **证明**
> >
> > 将 $f(z),g(z)$ 分别在 $z_{0}$ 的某邻域内展成 Taylor 级数有相同系数, 即 $f(z)\equiv g(z)$ 在 $z_{0}$ 的某邻域成立. 由唯一性定理, $f(z)\equiv g(z)$ 在 $D$ 上成立.
>



> **例**
>
> 设 $f(z)$ 是整函数且 $\exists M>0,R>0,k\in\mathbb{N}^{+}$ s.t. $|z|>R$ 时 $|f(z)|\leq M|z|^{k}$, 则 $f(z)$ 是一个至多 $k$ 次的多项式函数.
>
> > **证明**
> >
> > $f(z)$ 在 $z=0$ 展成 Taylor 级数: $f(z)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}z^{n}$, $|z|<+\infty$.
> > 取 $\Gamma_{\rho}:|z|=\rho\ (\rho>R)$,
> > $$
> > |f^{(n)}(0)|=\Bigl|\frac{n!}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(z)}{z^{n+1}}\,dz\Bigr|
> > \leq\frac{n!}{2\pi}\cdot\frac{M\rho^{k}}{\rho^{n+1}}\cdot2\pi\rho=M\cdot n!\cdot\rho^{k-n}.
> > $$
> > 当 $n>k$ 时令 $\rho\to+\infty$, 得 $f^{(n)}(0)=0$, 则 $f(z)=\sum_{n=0}^{k}\frac{f^{(n)}(0)}{n!}z^{n}$ 为至多 $k$ 次多项式.
>



> **例**
>
> 设 $f(z)$ 在包含闭单位圆的某个区域上解析, $f(0)=0$, $f(1)=1$,
> 且在 $|z|\leq1$ 上 $|f(z)|\leq1$, 则 $|f'(1)|\geq1$.
>
> > **证明**
> >
> > $f(z)$ 在 $|z|<1$ 上满足 Schwarz 引理, 则 $|f(z)|\leq|z|$.
> > 当 $z\in(-1,1)$ 时有 $|f(z)|\leq|z|$, 于是
> > $$
> > |f'(1)|=\lim_{z\to1}\Bigl|\frac{f(z)-f(1)}{z-1}\Bigr|
> > =\lim_{z\to1^{-}}\frac{|1-f(z)|}{1-z}
> > \geq\lim_{z\to1^{-}}\frac{1-|f(z)|}{1-z}
> > \geq\lim_{z\to1^{-}}\frac{1-z}{1-z}=1.
> > $$
>



> **例**
>
> 设 $C$ 是一条逆时针围线, $D$ 为 $C$ 的外部无界区域. 若 $f(z)$ 在 $D$ 上解析, 在 $D\cup C$ 上连续, 且 $\lim_{z\to\infty}f(z)=A$, 则
> $$
> \frac{1}{2\pi i}\oint_{C}\frac{f(s)}{s-z}\,ds=
> \begin{cases}
> A-f(z), & z\in D,\\
> A, & z\notin\overline{D}.
> \end{cases}
> $$
>
> > **证明**
> >
> > (1) $z\in D$ 时, 以 $z$ 为圆心作圆 $\Gamma_{\rho}:|s-z|=\rho$, $\rho$ 很大使 $C$ 含在 $\Gamma_{\rho}$ 内.
> > 由复围线的柯西积分公式,
> > $$
> > f(z)=\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(s)}{s-z}\,ds-\frac{1}{2\pi i}\oint_{C}\frac{f(s)}{s-z}\,ds,
> > $$
> > $$
> > \frac{1}{2\pi i}\oint_{C}\frac{f(s)}{s-z}\,ds
> > =-f(z)+\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(s)}{s-z}\,ds
> > =-f(z)+\frac{1}{2\pi}\int_{0}^{2\pi}f(z+\rho e^{i\theta})\,d\theta
> > =-f(z)+\lim_{\rho\to+\infty}\frac{1}{2\pi}\int_{0}^{2\pi}f(z+\rho e^{i\theta})\,d\theta
> > =-f(z)+\frac{1}{2\pi}\int_{0}^{2\pi}\lim_{\rho\to+\infty}f(z+\rho e^{i\theta})\,d\theta
> > =-f(z)+A.
> > $$
> >
> > (2) $z\notin\overline{D}$ 时, $\frac{1}{2\pi i}\oint_{\Gamma_{\rho}+C^{-}}\frac{f(s)}{s-z}\,ds=0$
> > ($\frac{f(s)}{s-z}$ 在复连域上解析). 于是
> > $$
> > \frac{1}{2\pi i}\oint_{C}\frac{f(s)}{s-z}\,ds
> > =\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(s)}{s-z}\,ds
> > =\frac{1}{2\pi}\int_{0}^{2\pi}\lim_{\rho\to+\infty}f(z+\rho e^{i\theta})\,d\theta=A.
> > $$
>





[目录与前言](../viewer.html?md=Complex-Analysis-Notes) · [下一章 →](../viewer.html?md=Complex-Analysis-Notes-Chapter-5)
