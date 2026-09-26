[← 上一章](../viewer.html?md=Complex-Analysis-Notes-Chapter-4)

## 圆环上解析函数的洛朗展式及孤立奇点



### 圆环上解析函数的洛朗展式



#### 双边幂级数的收敛性



> **定义**
>
> 由两个数列 $\{c_{n}\}$ 所确定的下列形式的函数项级数
> $$
> \sum_{n=-\infty}^{+\infty}c_{n}(z-a)^{n}
> =\cdots+\frac{c_{-1}}{z-a}+c_{0}+c_{1}(z-a)+\cdots
> $$
> 称为 $z-a$ 的双边幂级数.


双边幂级数的收敛圆环. 已知
$$
\sum_{n=-\infty}^{+\infty}c_{n}(z-a)^{n}
=\sum_{n=1}^{\infty}\frac{c_{-n}}{(z-a)^{n}}+\sum_{n=0}^{\infty}c_{n}(z-a)^{n}.
$$

1. $\displaystyle\sum_{n=1}^{\infty}\frac{c_{-n}}{(z-a)^{n}}\stackrel{\xi=1/(z-a)}{=}\sum_{n=1}^{\infty}c_{-n}\xi^{n}$. 若 $\exists r\geq0$ 使 $|\xi|<1/r$ 时该级数绝对且内闭一致收敛, 进而当 $|z-a|>r$ 时 $\sum_{n=1}^{\infty}\frac{c_{-n}}{(z-a)^{n}}$ 绝对且内闭一致收敛.
1. $\sum_{n=0}^{\infty}c_{n}(z-a)^{n}$, $\exists R\geq0$ 使 $|z-a|<R$ 时绝对且内闭一致收敛.

当 $0\leq r<R$ 时, 双边幂级数在圆环 $D:r<|z-a|<R$ 上绝对且内闭一致收敛.
于是双边幂级数在收敛圆环 $D$ (若存在) 上的和函数解析, 且可以逐项求导.


#### 洛朗展开定理



> **定理**
>
> [洛朗定理]
> 设 $f(z)$ 在圆环 $D:r<|z-a|<R$ ($0\leq r<R\leq+\infty$) 上解析, 则 $f(z)$ 在 $D$ 内可展成双边幂级数:
> $$
> f(z)=\sum_{n=-\infty}^{+\infty}c_{n}(z-a)^{n},
> $$
> 其中
> $$
> c_{n}=\frac{1}{2\pi i}\oint_{C}\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta,\quad n=0,\pm1,\pm2,\cdots,
> $$
> $C$ 为圆环内绕 $a$ 的任一正向围线.



> **证明**
>
> $\forall z\in D$, 作 $\Gamma_{\rho_{1}}:|z-a|=\rho_{1}$, $\Gamma_{\rho_{2}}:|z-a|=\rho_{2}$, 其中 $r<\rho_{1}<|z-a|<\rho_{2}<R$.
> 由复围线 $\Gamma_{\rho_{2}}+\Gamma_{\rho_{1}}^{-1}$ 上的柯西积分公式,
> $$
> f(z)=\frac{1}{2\pi i}\oint_{\Gamma_{\rho_{2}}+\Gamma_{\rho_{1}}^{-1}}\frac{f(s)}{s-z}\,ds
> =\frac{1}{2\pi i}\oint_{\Gamma_{\rho_{2}}}\frac{f(s)}{s-z}\,ds
> +\frac{1}{2\pi i}\oint_{\Gamma_{\rho_{1}}}\frac{f(s)}{z-s}\,ds
> =I_{1}+I_{2}.
> $$
> 对于 $I_{1}$: 在 $\Gamma_{\rho_{2}}$ 上 $|\frac{z-a}{s-a}|<1$,
> $$
> I_{1}=\frac{1}{2\pi i}\oint_{\Gamma_{\rho_{2}}}\frac{f(s)}{(s-a)(1-\frac{z-a}{s-a})}\,ds
> =\sum_{n=0}^{\infty}\Bigl[\frac{1}{2\pi i}\oint_{\Gamma_{\rho_{2}}}\frac{f(s)}{(s-a)^{n+1}}\,ds\Bigr](z-a)^{n}.
> $$
> 对于 $I_{2}$: 在 $\Gamma_{\rho_{1}}$ 上 $|\frac{s-a}{z-a}|<1$,
> $$
> I_{2}=\frac{1}{2\pi i}\oint_{\Gamma_{\rho_{1}}}\frac{f(s)}{(z-a)(1-\frac{s-a}{z-a})}\,ds
> =\sum_{n=1}^{\infty}\Bigl[\frac{1}{2\pi i}\oint_{\Gamma_{\rho_{1}}}\frac{f(s)}{(s-a)^{-n+1}}\,ds\Bigr](z-a)^{-n}.
> $$
> 令 $c_{n}=\frac{1}{2\pi i}\oint_{C}\frac{f(s)}{(s-a)^{n+1}}\,ds$ ($n=0,\pm1,\pm2,\cdots$), 即得 Laurent 展式.



> **注**
>
> (1) 上式称为 $f(z)$ 在圆环上的 Laurent 展式, $c_{n}$ 为 Laurent 系数.
> (2) 若 $f(z)$ 在圆环上展成双边幂级数, 则展式唯一 (证法同于泰勒级数的唯一性).
> (3) 若 $f(z)$ 在 $|z-a|\leq r$ 上也解析, 则 $c_{n}=0$ ($n=-1,-2,\cdots$), 这时 Laurent 级数变为 Taylor 级数.
> (4) 可有 $0\leq r<+\infty$, $0<R\leq+\infty$; 特别 $0<|z-a|<+\infty$ 即 $|z-a|>0$.


洛朗展式分为两部分:

- 正则部分: $\sum_{n=0}^{\infty}c_{n}(z-a)^{n}$, 在 $|z-a|<R$ 内收敛到解析函数.
- 主要部分: $\sum_{n=1}^{\infty}c_{-n}(z-a)^{-n}$, 在 $|z-a|>r$ 内收敛到解析函数.



> **例**
>
>
> 1. $f(z)=e^{\frac{1}{z}}$ 在 $|z|>0$ 上的洛朗展式: $f(z)=\sum_{n=0}^{\infty}\frac{1}{n!\,z^{n}}$.
> 1. $f(z)=\frac{\sin z}{z}$ 在 $|z|>0$ 上的洛朗展式: $f(z)=1-\frac{z^{2}}{3!}+\frac{z^{4}}{5!}-\cdots$.
>



> **例**
>
> 将 $f(z)=\frac{1}{(z-1)(z-2)}=\frac{1}{z-2}-\frac{1}{z-1}$ 在下列圆环展成洛朗展式:
>
> 1. $1<|z|<2$:
>   $$
>   f(z)=-\frac{1}{z}\frac{1}{1-\frac{1}{z}}-\frac{1}{2}\frac{1}{1-\frac{z}{2}}
>   =-\sum_{n=1}^{\infty}\frac{1}{z^{n}}-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{n+1}}.
>   $$
> 1. $|z|>2$:
>   $$
>   f(z)=\frac{1}{z}\frac{1}{1-\frac{2}{z}}-\frac{1}{z}\frac{1}{1-\frac{1}{z}}
>   =\sum_{n=0}^{\infty}\frac{2^{n}-1}{z^{n+1}}.
>   $$
> 1. $0<|z-2|<1$: 令 $w=z-2$, 则
>   $$
>   f(z)=\frac{1}{w}-\frac{1}{w+1}
>   =\frac{1}{z-2}-\sum_{n=0}^{\infty}(-1)^{n}(z-2)^{n}.
>   $$
> 1. $|z-2|>1$:
>   $$
>   f(z)=\frac{1}{z-2}-\frac{1}{z-2}\frac{1}{1+\frac{1}{z-2}}
>   =\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{(z-2)^{n+1}}.
>   $$
>




### 解析函数在孤立奇点的性质



#### 孤立奇点的分类



> **定义**
>
> 若 $f(z)$ 在 $z=a$ 的某去心邻域内解析, 在 $z=a$ 为奇点, 则称 $z=a$ 为 $f(z)$ 的孤立奇点.


例如: $f(z)=e^{\frac{1}{z}}$, $f(z)=\frac{\sin z}{z}$, $f(z)=\sin\frac{1}{z}$ 均以 $z=0$ 为孤立奇点.

设 $f(z)$ 以 $z=a$ 为孤立奇点, $f(z)$ 在 $z=a$ 的 Laurent 展式为
$$
f(z)=\sum_{n=-\infty}^{+\infty}c_{n}(z-a)^{n}
=\underbrace{\sum_{n=1}^{\infty}\frac{c_{-n}}{(z-a)^{n}}}_{\text{主要部分}}+\underbrace{\sum_{n=0}^{\infty}c_{n}(z-a)^{n}}_{\text{正则部分}}.
$$
按主要部分的项数分类:

1. 可去奇点: 主要部分为零, 即 $c_{-n}=0$ ($n=1,2,\cdots$).
1. $m$ 级极点: 主要部分只有有限项, 即存在 $m\geq1$ 使 $c_{-m}\neq0$, 且 $c_{-n}=0$ ($n>m$).
1. 本性奇点: 主要部分有无穷多项.



#### 孤立奇点的性质



> **定理**
>
> [可去奇点的判定]
> 设 $a$ 为 $f(z)$ 的孤立奇点, 则下列命题等价:
>
> 1. $a$ 是 $f(z)$ 的可去奇点 (主要部分为 $0$).
> 1. $\lim_{z\to a}f(z)=A$ (有限).
> 1. $f(z)$ 在 $a$ 的某去心邻域内有界.
>



> **证明**
>
> (1)$\Rightarrow$(2): $f(z)=c_{0}+c_{1}(z-a)+\cdots$, $\lim_{z\to a}f(z)=c_{0}$.
>
> (2)$\Rightarrow$(3): 由极限的局部有界性即得.
>
> (3)$\Rightarrow$(1): 设 $|f(z)|\leq M$. 取 $\Gamma_{\rho}:|z-a|=\rho$, 对 $n=-1,-2,\cdots$,
> $$
> |c_{n}|=\Bigl|\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(z)}{(z-a)^{n+1}}\,dz\Bigr|
> \leq\frac{1}{2\pi}\cdot\frac{M}{\rho^{n+1}}\cdot2\pi\rho=M\rho^{-n}\to0\quad(\rho\to0),
> $$
> 故主要部分系数全为零.



> **注**
>
> 可去奇点可通过补充 $f(a)=\lim_{z\to a}f(z)$ 使 $f(z)$ 在 $z=a$ 也解析, 故经常将可去奇点看成解析点. 例如
> $f(z)=\frac{\sin z}{z}$, $F(z)=\begin{cases}\frac{\sin z}{z},&z\neq0\\1,&z=0\end{cases}$.



> **定理**
>
> [极点的判定]
> 设 $a$ 为 $f(z)$ 的孤立奇点, 则下列命题等价:
>
> 1. $f$ 在 $a$ 的 Laurent 展式主要部分为有限项
>   $\frac{c_{-m}}{(z-a)^{m}}+\cdots+\frac{c_{-1}}{z-a}$，其中 $m\geq1$ 且 $c_{-m}\neq0$.
> 1. $f(z)=\frac{\lambda(z)}{(z-a)^{m}}$, 其中 $\lambda$ 在 $a$ 的邻域内解析且 $\lambda(a)\neq0$.
> 1. $a$ 是 $1/f(z)$ 的 $m$ 级零点.
> 1. $\lim_{z\to a}f(z)=\infty$.
>



> **证明**
>
> (1)$\Rightarrow$(2): $f(z)$ 在 $z=a$ 的 Laurent 展式为 $f(z)=\frac{c_{-m}}{(z-a)^{m}}+\cdots+\frac{c_{-1}}{z-a}+c_{0}+c_{1}(z-a)+\cdots$. 于是
> $$
> f(z)=\frac{1}{(z-a)^{m}}\bigl[c_{-m}+c_{-m+1}(z-a)+\cdots+c_{-1}(z-a)^{m-1}+c_{0}(z-a)^{m}+\cdots\bigr]
> =\frac{\lambda(z)}{(z-a)^{m}},
> $$
> 这里 $\lambda(z)$ 在 $z=a$ 解析, 且 $\lambda(a)=c_{-m}\neq0$.
>
> (2)$\Rightarrow$(3): $f(z)=\frac{\lambda(z)}{(z-a)^{m}}\Rightarrow\frac{1}{f(z)}=(z-a)^{m}\cdot\frac{1}{\lambda(z)}=(z-a)^{m}\cdot\varphi(z)$, 其中 $\varphi(z)=\frac{1}{\lambda(z)}$ 在 $z=a$ 解析且 $\varphi(a)=\frac{1}{c_{-m}}\neq0$, 故 $\frac{1}{f(z)}$ 以 $z=a$ 为 $m$ 级零点.
>
> (3)$\Rightarrow$(4): $\frac{1}{f(z)}=(z-a)^{m}\varphi(z)\Rightarrow\lim_{z\to a}\frac{1}{f(z)}=0\Leftrightarrow\lim_{z\to a}f(z)=\infty$.
>
> (4)$\Rightarrow$(1): $\lim_{z\to a}f(z)=\infty\Rightarrow\lim_{z\to a}\frac{1}{f(z)}=0$.
> 将 $1/f$ 在 $a$ 补定义为 $0$ 后，它在 $a$ 解析且以 $a$ 为零点，故存在正整数
> $m$ 使 $\frac{1}{f(z)}$ 以 $z=a$ 为 $m$ 级零点. 记
> $\frac{1}{f(z)}=(z-a)^{m}\varphi(z)$, $\varphi(z)$ 在 $z=a$ 解析且
> $\varphi(a)\neq0$. 将 $\frac{1}{\varphi(z)}$ 展成 Taylor 级数:
> $\frac{1}{\varphi(z)}=c_{-m}+c_{-m+1}(z-a)+\cdots$, $c_{-m}\neq0$. 于是
> $$
> f(z)=\frac{1}{(z-a)^{m}}\cdot\frac{1}{\varphi(z)}=\frac{c_{-m}}{(z-a)^{m}}+\cdots+\frac{c_{-1}}{z-a}+c_{0}+\cdots,
> $$
> 表明 $f(z)$ 在 $z=a$ 的 Laurent 展式主要部分为有限项, 即 $a$ 是 $m$ 级极点.



> **定理**
>
> [本性奇点的判定]
> 设 $a$ 为 $f(z)$ 的孤立奇点, 则 $a$ 为本性奇点
> $\Leftrightarrow\lim_{z\to a}f(z)$ 在扩充复平面中不存在,
> 即该极限既不是有限复数, 也不是 $\infty$.



#### 本性奇点的进一步讨论



> **定理**
>
> [Weierstrass-Casorati 定理]
> 设 $f(z)$ 以 $z=a$ 为本性奇点, 则对任意复数 $A$ (含 $\infty$), 都存在 $z_{n}\to a$ ($z_{n}\neq a$) s.t. $f(z_{n})\to A$.
>
>
> 即 $f(z)$ 在本性奇点的任意邻域内可以取到任意接近任何复数的值.



> **证明**
>
> (1) 若 $A=\infty$, 由后面推论 (2), 本性奇点邻域内无界, 故 $\exists z_{n}\to a$ 使 $f(z_{n})\to\infty$.
> (2) 若 $A$ 有限. 若已有 $z_{n}\to a$ 使 $f(z_{n})=A$, 则结论成立. 否则在某去心邻域 $f(z)\neq A$, 记 $g(z)=\frac{1}{f(z)-A}$. 由推论 (1), $g$ 也以 $a$ 为本性奇点. 再由 (1), $\exists z_{n}\to a$ 使 $g(z_{n})\to\infty$, 从而 $f(z_{n})\to A$.


例如: $f(z)=\frac{\sin z}{z}$ 以 $z=0$ 为可去奇点; $f(z)=\frac{1}{z^{3}}$ 以 $z=0$ 为 3 级极点; $f(z)=\sin\frac{1}{z}$, $f(z)=e^{\frac{1}{z}}$ 以 $z=0$ 为本性奇点.


> **推论**
>
>
> 1. 若 $f(z)$ 以 $z=a$ 为本性奇点，且存在 $z=a$ 的某去心邻域使
>   $f(z)\neq0$，则 $\dfrac{1}{f(z)}$ 也以 $z=a$ 为本性奇点；
> 1. 若 $f(z)$ 在孤立奇点 $z=a$ 的任意邻域内无界，则 $f(z)$ 以
>   $z=a$ 为极点或本性奇点。
>


> **证明**
>
> 先证 (1)。由假设，$1/f$ 在 $z=a$ 的某去心邻域内解析，因而
> $z=a$ 是它的孤立奇点。若
> $\lim_{z\to a}1/f(z)=A\in\mathbb{C}$，则当 $A=0$ 时
> $f(z)\to\infty$，故 $a$ 是 $f$ 的极点；当 $A\neq0$ 时
> $f(z)\to1/A$，故 $a$ 是 $f$ 的可去奇点。若 $1/f(z)\to\infty$，
> 则 $f(z)\to0$，$a$ 仍是 $f$ 的可去奇点。这些情况均与 $a$ 是
> $f$ 的本性奇点矛盾，所以 $a$ 只能是 $1/f$ 的本性奇点。
>
> 对 (2)，若 $a$ 是可去奇点，则 $f$ 在 $a$ 的某个邻域内有界，
> 与假设矛盾。由孤立奇点的分类，$a$ 只能是极点或本性奇点。



> **定理**
>
> [Picard 定理]
> 若 $f(z)$ 以 $z=a$ 为本性奇点, 则对任意复数 $A$ (最多一个除外), 都存在 $z_{n}\to a$ ($z_{n}\neq a$) s.t. $f(z_{n})=A$.


例如: $f(z)=e^{\frac{1}{z}}$ 以 $z=0$ 为本性奇点, $\forall A\in\mathbb{C}$ ($A\neq0$), $\exists z_{n}\to0$ 使 $e^{1/z_{n}}=A$.



### 解析函数在无穷远点的性质



#### $\infty$ 为孤立奇点的分类



> **定义**
>
> 对 $r>0$, 称 $r<|z|<+\infty$ 为 $\infty$ 的一个邻域.
>
>
> $\infty$ 为孤立奇点: $f(z)$ 在 $r<|z|<+\infty$ 内解析, 则称 $f(z)$ 以 $\infty$ 为孤立奇点.
>
>
> $\infty$ 为 $f(z)$ 的 $m$ 级零点: $f(z)$ 在 $r<|z|<+\infty$ 内可表示为
> $f(z)=\frac{\lambda(z)}{z^{m}}$, 这里 $\lambda(z)$ 在该邻域解析且
> $\lim_{z\to\infty}\lambda(z)=A\in\mathbb C\setminus\{0\}$.


$f(z)$ 在 $\infty$ 点的 Laurent 展式: 在 $r<|z|<+\infty$ 上,
$$
f(z)=\sum_{n=-\infty}^{+\infty}c_{n}z^{n}
=\underbrace{c_0+\sum_{n=1}^{\infty}c_{-n}z^{-n}}_{\text{正则部分}}
+\underbrace{\sum_{n=1}^{\infty}c_{n}z^{n}}_{\text{主要部分}}.
$$


#### 无穷远点孤立奇点的性质



> **定理**
>
> 设 $\infty$ 为 $f(z)$ 的孤立奇点, 则在变换 $\zeta=\frac{1}{z}$ 下, 上述结论均可由上一节的定理推出. 具体地:
>
> 1. $\infty$ 为可去奇点 $\Leftrightarrow$ 主要部分为零 $\Leftrightarrow$ $\lim_{z\to\infty}f(z)=A$ (有限) $\Leftrightarrow$ $f(z)$ 在 $\infty$ 某邻域内有界.
> 1. $\infty$ 为某个有限级极点 $\Leftrightarrow$ 存在 $m\geq1$ 使主要部分为 $\sum_{n=1}^{m}c_{n}z^{n}$ ($c_{m}\neq0$)
>   $\Leftrightarrow$ $f(z)=z^{m}\varphi(z)$, 其中 $\varphi$ 在 $\infty$ 的某邻域解析且
>   $\lim_{z\to\infty}\varphi(z)=A\in\mathbb C\setminus\{0\}$
>   $\Leftrightarrow$ $1/f(z)$ 以 $\infty$ 为 $m$ 级零点 $\Leftrightarrow$ $\lim_{z\to\infty}f(z)=\infty$.
> 1. $\infty$ 为本性奇点 $\Leftrightarrow$ 主要部分有无穷多项 $\Leftrightarrow$ $\lim_{z\to\infty}f(z)$ 不存在且非 $\infty$.
>


例如: $f(z)=\frac{1}{z}$, $f(z)=\frac{1}{z^{2}}+e^{\frac{1}{z}}$, $f(z)=\sin\frac{1}{z}$ 以 $\infty$ 为可去奇点;
$f(z)=z^{2}+e^{\frac{1}{z}}$, $f(z)=1+z+z^{2}$ 以 $\infty$ 为极点;
$f(z)=\sin z$, $f(z)=e^{z}$ 以 $\infty$ 为本性奇点.


> **注**
>
> (1) 若 $f(z)$ 以 $\infty$ 为孤立奇点, 在变换 $\zeta=\frac{1}{z}$ 下, $f(\frac{1}{\zeta})$ 以 $\zeta=0$ 为孤立奇点, 且奇点类型对应相同. 以上三个定理的证明同上节.
>
> (2) 若 $f(z)$ 以 $\infty$ 为 $m$ 级极点或本性奇点, 则 $f(z)$ 在 $\infty$ 的某邻域内无界.
>
> (3) Picard 大、小定理对 $z=\infty$ 也成立.





[目录与前言](../viewer.html?md=Complex-Analysis-Notes) · [下一章 →](../viewer.html?md=Complex-Analysis-Notes-Chapter-6)
