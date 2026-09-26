[← 上一章](../viewer.html?md=Real-Analysis-Notes-Chapter-2)

## 可测函数



### 可测函数的定义和性质


在研究可测函数的性质之前, 我们首先考虑广义实函数的定义:




> **定义**
>
> $f:A\rightarrow \mathbb{R}\cup\{-\infty,+\infty\}=\overline{\mathbb{R} }$称为定义在$A$上的广义实函数.
>
>


类似地, 我们也有广义实函数的有界性的定义:




> **定义**
>
> 设$f:A\rightarrow \overline{\mathbb{R} }$是定义在$A$上的广义实函数, 则称$f$是有界的, 当且仅当$\exists M>0, \forall x\in A, |f(x)|<M$.
>
>



> **注**
>
> 值得注意的是, 有界性和函数有限并不完全一致, 例如$f(x)=\frac{1}{x}$在$A=(0,1)$上是有界的, 但不是有限的. 另一方面, $f(x)=\chi_{(0,1)}$在$A=(0,1)$上是有限的, 但不是有界的.
>
>


事实上, 我们可以给出函数有限的分析定义:




> **定义**
>
> 设$f:A\rightarrow \overline{\mathbb{R} }$是定义在$A$上的广义实函数, 则称$f$是有限的, 当且仅当$\forall x\in A, f(x)\in \mathbb{R}$.
>
>


而对于广义实函数的连续性, 我们也类似地给出定义:




> **定义**
>
> 设$f$在$E$上有限, 则称$f$在$x_0\in E$处是连续的, 当且仅当$ \forall \varepsilon >0, \exists \delta_{x_0,\varepsilon} >0, \forall x\in E, \rho(x,x_0)<\delta$时有$ |f(x)-f(x_0)|<\varepsilon$.
>
>
> 若$f$在$E$上每一点都是连续的, 则称$f$在$E$上是连续的.
>
>
> 设$f$在$E$上有限, 则称$f$在$E$上是一致连续的, 当且仅当$ \forall \varepsilon >0, \exists \delta_{\varepsilon} >0, \forall x\in E, \rho(x,x_0)<\delta$时有$ |f(x)-f(x_0)|<\varepsilon, \forall x_0 \in E$.
>
>



> **注**
>
> 在抽象集合中讨论连续性时, 我们必须要指定讨论的集合范围, 因为在不同的集合上, 同一个函数可能会有不同的连续性. 因此为了方便讨论, 我们下面定义特征函数和简单函数.
>
>



> **定理**
>
> 若$E$,$F$为闭集, $f\in C(E)$, $f\in C(F)$, 则$f\in C(E \cup F)$.
>
>



> **证明**
>
> 若$x_0\in E\cup F$, 则$\forall \varepsilon >0, \exists \delta_{1} >0$, 使得$\forall x\in E, \rho(x,x_0)<\delta_{1}$时有$|f(x)-f(x_0)|<\varepsilon$.
>
>
> 同理, $\forall \varepsilon >0, \exists \delta_{2} >0$, 使得$\forall x\in F, \rho(x,x_0)<\delta_{2}$时有$|f(x)-f(x_0)|<\varepsilon$.
>
>
> 于是取$\delta = \min\{\delta_{1},\delta_{2}\}$, 则$\forall x\in E\cup F, \rho(x,x_0)<\delta$时有$|f(x)-f(x_0)|<\varepsilon$.
>
>
> 若$x_0\in E\backslash F$, 则$\forall \varepsilon >0, \exists \delta_{1} >0$, 使得$\forall x\in E, \rho(x,x_0)<\delta_{1}$时有$|f(x)-f(x_0)|<\varepsilon$.
>
>
> 同时有$\exists \delta_{3} >0$, 使得$O(x_0,\delta_{3})\subset F^c$.
>
>
> 于是取$\delta = \min\{\delta_{1},\delta_{3}\}$, 则$\forall x\in E\cup F, \rho(x,x_0)<\delta$时有$x\in E\backslash F$且$\rho(x,x_0)<\delta_{1}$,$|f(x)-f(x_0)|<\varepsilon$.
>
>
> 对于$x_0\in F\backslash E$, 类似可证.
>
>



> **定义**
>
> 设$E$是集合, 则称$E$的特征函数为$\chi_E(x)=\begin{cases}
> 1, & x\in E \\
> 0, & x\notin E
> \end{cases}$.\par
> 设$E_i$是一集列, 则称$E_i$的简单函数为$f(x)=\sum_{i=1}^{n}c_i\chi_{E_i}(x)$, 其中$c_i\in \mathbb{R}$, 且$E_i$互不交.
>
>
> 特别地, 若$E_i$均为区间, 则称$f$是阶梯函数.
>
>


根据上面的讨论, 我们有一类特殊的例子来表示广义实函数的连续性:




> **例**
>
> $f=\chi_{\mathbb{Q}}(x)$在$\mathbb{Q}$上是连续的, 但在$\mathbb{R}$上是处处不连续的.
>
>


基于此我们给出可测函数的定义:




> **定义**
>
> 设$E$是集合, $f$是定义在$E$上的广义实函数, 则称$f$在$E$上是可测的, 当且仅当$\forall a\in \mathbb{R}, E[f> a]$是可测集.
>
>
> 若$f$在$E$上是可测的, 则称$f$是$E$上的可测函数, 记为$f\in \mathcal{M}(E)$.
>
>



> **定理**
>
> 下面函数均为可测函数:
>
>
>
> - 可测集的特征函数.
>
>
> - 简单函数.
>
>
> - 可测集上的连续函数.
>
>
> - 可测集上的单调函数.
>
>
> - 零测集上的函数.
>
>
>



> **证明**
>
> 对于可测集的特征函数, 由定义可知, $\forall a\in \mathbb{R}, E[\chi_E > a] = E$或$E^c$, 因此是可测的.
>
>
> 对于简单函数, 设$f(x)=\sum_{i=1}^{n}c_i\chi_{E_i}(x)$, 则$\forall a\in \mathbb{R}, E[f>a]=\bigcup_{c_i>a}E_i$, 因此是可测的.
>
>
> 对于可测集上的连续函数, 由连续函数的性质知, $\forall a\in \mathbb{R}, E[f>a]$是开集或闭集, 因此是可测的.
>
>
> 对于可测集上的单调函数, 类似地, $\forall a\in \mathbb{R}, E[f>a]$是开集或闭集, 因此是可测的.
>
>
> 对于零测集上的函数, 由于零测集上的函数在几乎处处上是常数函数, 因此也是可测的.
>
>


事实上可测函数还有一些等价的定义, 我们下面来证明这些定义是等价的.




> **定理**
>
> 设$f$是定义在$E$上的广义实函数, 则下列命题等价:
>
>
>
> - $f$在$E$上是可测的.
> - $\forall a\in \mathbb{R}, E[f>a]$是可测集.
> - $\forall a\in \mathbb{R}, E[f\geqslant a]$是可测集.
> - $\forall a\in \mathbb{R}, E[f<a]$是可测集.
> - $\forall a\in \mathbb{R}, E[f\leqslant a]$是可测集.
>



> **证明**
>
> 由定义知, $f$在$E$上是可测的当且仅当$\forall a\in \mathbb{R}, E[f>a]$是可测集.
>
>
> 首先考虑$E[f\leqslant a]$是$E[f>a]$的余集, 因此$E[f\leqslant a]$的可测性和$E[f>a]$是等价的.
>
>
> 下面考虑$E[f<a]=\bigcup_{k=1}^{\infty}E[f\leqslant a-\frac{1}{k}]$, 而对于每个$a\in \mathbb{R}$, $E[f\leqslant a-\frac{1}{k}]$是可测集, 因此$\bigcup_{k=1}^{\infty}E[f\leqslant a-\frac{1}{k}]$也是可测集.
>
>
> 于是类似地, 由$E[f\geqslant a]$是$E[f<a]$的可测性是等价的知$E[f\geqslant a]$可测也是成立的.
>
>


下面我们利用可测函数的定义来讨论一些初等和基本的性质.




> **命题**
>
> 若$f$在$E$上是可测的, 则$\forall a\in \overline{\mathbb{R}}, E[f=a]$可测.
>
>



> **证明**
>
> 对于$a \in \mathbb{R}$, 我们有$E[f\geqslant a]\cap E[f\leqslant a]=E[f=a]$, 于是可测.
>
>
> 对于$a = +\infty$, 则$E[f=+\infty]=\bigcap_{n=1}^{\infty}E[f\geqslant n]$, 由于$E[f\geqslant n]$是可测集, 因此$E[f=+\infty]$也是可测的.
>
>
> 对于$a = -\infty$, 则$E[f=-\infty]=\bigcap_{n=1}^{\infty}E[f\leqslant -n]$, 由于$E[f\leqslant -n]$是可测集, 因此$E[f=-\infty]$也是可测的.
>
>



> **注**
>
> 上面的结果是充分的, 但不是必要的. 即$\forall a \in \mathbb{R}, E[f=a]$可测不蕴含$f$在$E$上是可测的.
>
>



> **命题**
>
> $f\in \mathcal{M}(E)$当且仅当$\forall E_1\subset E, f\in \mathcal{M}(E_1)$, 其中$E_1$可测.
>
>



> **证明**
>
> 由于$\forall a \in \mathbb{R}$, $E_1[f>a]=E_1\cap E[f>a]$可测, 因此$E_1[f>a]$可测.
>
>



> **命题**
>
> 记$E=\bigcup_{i=1}^{\infty}E_i$, $\{E_i\}$互不交可测, 则$f\in \mathcal{M}(E)\Leftrightarrow f\in \mathcal{M}(E_i), \forall i$.
>
>



> **证明**
>
> 由$E=\bigcup_{i=1}^{\infty}E_i$, $\forall a \in \mathbb{R}$, 有$E[f>a]=\bigcup_{i=1}^{\infty}E_i[f>a]$, 由于$\{E_i\}$互不交可测, 因此$E[f>a]$是可测的当且仅当$\forall i, E_i[f>a]$是可测的.
>
>



> **注**
>
> 上面的结果说明了可测函数具有良好的性质, 即可测函数在可测集上的限制仍然是可测的.
>
>



> **定理**
>
> 若$\{f_n\}\in \mathcal{M}(E)$, 则$\sup \{f_n\}$, $\inf \{f_n\}$, $\limsup_{n \to \infty} f_n$, $\liminf_{n \to \infty} f_n$, $\lim_{n \to \infty} f_n$均在$E$上可测.
>
>



> **证明**
>
> 事实上我们只需要证明$\sup \{f_n\}$和$\inf \{f_n\}$在$E$上可测, 上下极限事实上是由$\sup \{f_n\}$和$\inf \{f_n\}$来定义的, 因此其可测性在上下确界可测时自然成立.
>
>
> 首先考虑$\sup \{f_n\}$, 由定义知, $\forall a \in \mathbb{R}, E[\sup \{f_n\}\leqslant a]=\bigcap_{n=1}^{\infty}E[f_n\leqslant a]$, 由于$\{f_n\}\in \mathcal{M}(E)$, 因此$E[\sup \{f_n\}\leqslant a]$也是可测的.
>
>
> 类似地, 我们有$E[\inf \{f_n\}\geqslant a]=\bigcap_{n=1}^{\infty}E[f_n\geqslant a]$, 其可测性显然.
>
>
> 于是$\sup \{f_n\}$和$\inf \{f_n\}$在$E$上均可测.
>
>
> 由于$\limsup_{n \to \infty} f_n = \inf_{N\geqslant 1} \sup_{n\geqslant N} \{f_n\}$, $\liminf_{n \to \infty} f_n = \sup_{N\geqslant 1} \inf_{n\geqslant N} \{f_n\}$.
>
>
> 其可测性显然, 因为$\sup$和$\inf$的可测性已经证明.
>
>
> 最后考虑$\lim_{n \to \infty} f_n$存在时有$\lim_{n \to \infty} f_n = \limsup_{n \to \infty} f_n = \liminf_{n \to \infty} f_n$, 由于$\limsup_{n \to \infty} f_n$和$\liminf_{n \to \infty} f_n$均在$E$上可测. 因此其可测性也显然.
>
>



> **注**
>
> 上面的结果事实上反映了可测函数列的极限的可测性, 即可测函数列的极限仍然是可测函数.
>
>
> 同时注意到这里我们选择的证明方式是利用可测函数的等价定义构造可测集的可列交得到的, 这和我们证明可测函数的等价定义时的想法是类似的.
>
>


下面我们考虑简单函数列和可测函数的关系, 这里我们首先考虑连续函数列的情形.




> **引理**
>
> 连续函数列的极限在可测集上可测.
>
>



> **证明**
>
> 设$f_n$是定义在$E$上的连续函数列, 且$f_n\to f$, 则$\forall a\in \mathbb{R}$, $E[f_n>a]$是开集, 因此是可测的.
>
>
> 由于$\bigcap_{k=1}^{\infty}E[f_n> a]=E[f>a]$, 因此$E[f>a]$也是可测的.
>
>
> 于是$f$在$E$上是可测的.
>
>



> **推论**
>
> 简单函数列的极限在可测集上可测.
>
>



> **证明**
>
> 设$f_n$是定义在$E$上的简单函数列, 且$f_n\to f$, 则$\forall a\in \mathbb{R}$, $E[f_n>a]$是可测集, 因此是可测的.
>
>
> 由于$\bigcap_{k=1}^{\infty}E[f_n> a]=E[f>a]$, 因此$E[f>a]$也是可测的.
>
>
> 于是$f$在$E$上是可测的.
>
>


下面考虑简单函数列的极限, 我们有下面的结果:




> **定理**
>
> 设$f\geqslant 0$, $f\in \mathcal{M}(E)$, 则$\exists \{\phi_n\}$, $\phi_n$为$E$上单增简单函数列满足$\lim_{n \to \infty} \phi_n = f$.
>
>



> **证明**
>
> $\forall n \in \mathbb{N}$, 将$[0,+\infty]$拆成若干小区间: $[0,\frac{1}{2^n}), [\frac{1}{2^n}, \frac{2}{2^n}), \cdots, [\frac{(n2^n-1)}{2^n},n),[n,+\infty]$.
> 同时也有$E=E[0\leqslant f<\frac{1}{2^n}]\cup E[\frac{1}{2^n}\leqslant f<\frac{2}{2^n}]\cup \cdots \cup E[\frac{(n2^n-1)}{2^n}\leqslant f<n]\cup E[f\geqslant n]$.
>
>
> 于是我们可以定义$\phi_n(x)=\sum_{k=0}^{n} \frac{k}{2^n}\chi_{E[\frac{k}{2^n}\leqslant f<\frac{k+1}{2^n}]}(x)$. 下面说明这就是我们要求的简单函数列.
>
>
> 首先$\phi_n$是单增的, 因为$\forall x\in E$, $\phi_n(x)$是单调递增的.
>
>
> 其次$\phi_n$是简单函数, 因为$\phi_n(x)$是有限个特征函数的线性组合.
>
>
> 最后考虑$\lim_{n \to \infty} \phi_n(x)$, 由于$\phi_n(x)$是单调递增的, 且$\phi_n(x)\leqslant f(x)$, 因此$\lim_{n \to \infty} \phi_n(x) = f(x)$.
>
>
> 于是$\phi_n$是满足要求的单增简单函数列.
>
>


下面我们讨论一般函数的情形, 为了方便起见, 我们这里定义一般函数的非负部分和非正部分:




> **定义**
>
> 设$f$是定义在$E$上的广义实函数, 则称$f$的正部为$f^+=\max\{f,0\}$, 负部为$f^-=\max\{-f,0\}$.
>
>



> **注**
>
> 对于函数的正部和负部, 我们有一些基本结论, 这里不再证明.
>
>
>
> - $f=f^+-f^-$.
> - $|f|=f^++f^-$.
> - $f^+\geqslant 0$, $f^-\geqslant 0$.
>



> **推论**
>
> 设$f\in \mathcal{M}(E)$, 则$\exists \{\phi_n\}$, $\phi_n$为$E$上简单函数列满足$\lim_{n \to \infty} \phi_n = f$.
>
>



> **证明**
>
> 由上面的结果, 把$f$分解为正部和负部, 即$f=f^+-f^-$, 其中$f^+=\max\{f,0\}$, $f^-=\max\{-f,0\}$.
>
>
> 由于$f^+$和$f^-$均为非负可测函数, 因此存在单增简单函数列$\{\phi_n^{+}\}$和$\{\phi_n^{-}\}$逼近$f^+$和$f^-$.
>
>



> **注**
>
> 上面的结果说明了可测函数可以用一列单增的简单函数列逼近, 一方面这是和一般的微积分中的结果是类似的, 另一方面这也为下面研究可测函数提供了重要支持.
>
>


下面我们来讨论可测函数的运算封闭性, 实际上这是由上面简单函数的逼近得到的.




> **定理**
>
> 设$f,g\in \mathcal{M}(E)$, 则$f+g$, $f-g$, $fg$, $\frac{f}{g}$在$E$上有意义时均可测.
>
>



> **证明**
>
> 由于$f$和$g$均为可测函数, 因此$\exists \{\phi_n\}$和$\{\psi_n\}$, $\phi_n$和$\psi_n$均为$E$上单增简单函数列满足$\lim_{n \to \infty} \phi_n = f$, $\lim_{n \to \infty} \psi_n = g$.
>
>
> 于是考虑$f+g$, $f-g$, $fg$, $\frac{f}{g}$的情况:
>
>
>
> - 对于$f+g$, $\exists \{\phi_n+\psi_n\}$, $\phi_n+\psi_n$为$E$上单增简单函数列满足$\lim_{n \to \infty} (\phi_n+\psi_n) = f+g$.
>
>
> - 对于$f-g$, $\exists \{\phi_n-\psi_n\}$, $\phi_n-\psi_n$为$E$上单增简单函数列满足$\lim_{n \to \infty} (\phi_n-\psi_n) = f-g$.
>
>
> - 对于$fg$, $\exists \{\phi_n\cdot\psi_n\}$, $\phi_n\cdot\psi_n$为$E$上单增简单函数列满足$\lim_{n \to \infty} (\phi_n\cdot\psi_n) = fg$.
>
>
> - 对于$\frac{f}{g}$, 若$\forall x\in E, g(x)\neq 0$, 则$\exists \{\frac{\phi_n}{\psi_n}\}$, $\frac{\phi_n}{\psi_n}$为$E$上单增简单函数列满足$\lim_{n \to \infty} (\frac{\phi_n}{\psi_n}) = \frac{f}{g}$.
>
>
>
> 于是$f+g$, $f-g$, $fg$, $\frac{f}{g}$在$E$上均可测.
>
>



> **注**
>
> 上面的结果说明了可测函数在几乎处处有限的情形下构成线性空间, 即可测函数的和、差、积和商（除数不为零时）仍然是可测函数.
>
>


最后我们给出一个关于简单函数列和函数的可测性间关系的最简洁的结果, 这个结果可以用来判断函数的可测性.




> **定理**
>
> $f\in \mathcal{M}(E)$当且仅当$\exists \{\phi_n\}$, $\phi_n$为$E$上简单函数列满足$\lim_{n \to \infty} \phi_n = f$.
>
>



> **证明**
>
> 由上结果可知, 若$f\in \mathcal{M}(E)$, 则$\exists \{\phi_n\}$, $\phi_n$为$E$上单增简单函数列满足$\lim_{n \to \infty} \phi_n = f$.
>
>
> 下证反方向的命题, 设$\exists \{\phi_n\}$, $\phi_n$为$E$上简单函数列满足$\lim_{n \to \infty} \phi_n = f$.
>
>
> 由于$\phi_n$是简单函数, 因此$\forall a\in \mathbb{R}$, $E[\phi_n>a]$是可测集, 因此$\bigcap_{k=1}^{\infty}E[\phi_n>a]$也是可测集.
>
>
> 于是$\forall a\in \mathbb{R}$, $E[f>a] = \bigcap_{k=1}^{\infty}E[\phi_n>a]$是可测集.
>
>
> 由于$\forall a\in \mathbb{R}$, $E[f>a]$是可测集, 因此$f$在$E$上是可测的.
>
>




### 可测函数的收敛性


在讨论函数性质时, 我们自然想到普通微积分中实函数的收敛, 因此我们现在对函数的收敛作如下定义:




> **定义**
>
> 设$f_n,f$是定义在$E$上的函数,
>
> - 称$f_n$逐点收敛到$f$, 当且仅当$\forall x\in E, \lim_{n \to \infty}f_n(x)=f(x)$.
>
>
> - 称$f_n$一致收敛到$f$, 当且仅当$\forall \varepsilon>0, \exists N\in \mathbb{N}, \forall n\geqslant N, |f_n(x)-f(x)|<\varepsilon$.
>
>
> - 称$f_n$几乎处处收敛到$f$, 当且仅当$\exists E_0\subset E, m(E_0) = 0, \forall x\in E\backslash E_0, \lim_{n \to \infty}f_n(x)=f(x)$.
>
>
> - 称$f_n$近乎一致收敛到$f$, 当且仅当$\forall \varepsilon>0, \forall \delta > 0, \exists E_0\subset E, m(E_0) < \delta, \exists N\in \mathbb{N}, \forall n\geqslant N, \forall x\in E\backslash E_0, |f_n(x)-f(x)|<\varepsilon$.
>
>
>



> **例**
>
> 若$f_n(x)=x^n$, $f(x)=0$, 则$f_n(x)$近乎一致收敛到$f$.
>
>
> 这是由于$\forall \delta>0$, 取$E_0 =\left[1-\frac{\delta}{2},1\right]$, 则$m(E_0)=\frac{\delta}{2}<\delta$, $\forall x\in E\backslash E_0$, $|f_n(x)-f(x)|=|x^n|<\varepsilon$.
>
>
> 此时只需要取$N=\left|\frac{\varepsilon}{\log \left(1-\frac{\delta}{2}\right)}\right|$, 使得$\forall n\geqslant N$, $|x^n|<\varepsilon$.
>
>



> **注**
>
> 这里$N$是和$\delta$有关的, 但不能和$x$有关, 否则就不再是一致收敛了.
>
>



> **定理**
>
> 下列命题等价:
>
>
>
> - $\exists E_0\subset E, m(E_0) = 0, \forall x\in E\backslash E_0, \lim_{n \to \infty}f_n(x)=f(x)$.
> - $\lim_{n\to \infty}m(E[f_n \nrightarrow f])=0$.
> - $\forall x\in E[f_n \nrightarrow f], f_n(x)\nrightarrow f(x)$
>



> **引理**
>
> $E[f_n \nrightarrow f] = \bigcup_{\varepsilon} \bigcap_{N=1}^{+\infty} \bigcup_{n=N}^{+\infty}E\left[\left|f_n-f\right|\geqslant \varepsilon\right] = \bigcup_{k=1}^{+\infty} \bigcap_{N=1}^{+\infty} \bigcup_{n=N}^{+\infty}E\left[\left|f_n-f\right|\geqslant \frac{1}{k}\right]$.



> **证明**
>
> 考虑$E[f_n \nrightarrow f]$的定义:
>
>
> $\exists \varepsilon_0>0, \forall N\in \mathbb{N}, \exists n_0\geqslant N, \left|f_n(x)-f(x)\right|\geqslant \varepsilon_0$.
>
>
> 这说明$\exists \varepsilon_0>0, \forall N\in \mathbb{N}, \exists n_0\geqslant N, x\in E\left[\left|f_n-f\right|\geqslant \varepsilon_0\right]$.
>
>
> 于是有$x\in \bigcup_{\varepsilon} \bigcap_{N=1}^{+\infty} \bigcup_{n=N}^{+\infty}E\left[\left|f_n-f\right|\geqslant \varepsilon_0\right]$.
>
>
> 更进一步考虑$\varepsilon$的任意性, 我们有$x \in \bigcup_{k=1}^{+\infty} \bigcap_{N=1}^{+\infty} \bigcup_{n=N}^{+\infty}E\left[\left|f_n-f\right|\geqslant \frac{1}{k}\right]$.
>
>



> **注**
>
> 上面的这种方法在后续的Lebesgue积分中也会用到, 这种方法实际上是利用了$\varepsilon$的任意性来构造一个新的集合, 使得这个集合的测度为0. 但同时考虑到$\varepsilon$是任意的, 因此我们选择$\frac{1}{k}$代替依旧是成立的.
>
>



> **引理**
>
> (Borel-Cantelli) 设$\{A_n\}$是一集列, 则$\sum_{n=1}^{\infty}m(A_n)<\infty \Rightarrow m(\limsup_{n \to \infty}A_n)=0$.



> **证明**
>
> 首先考虑$e_k$和$E$均可测, 则有下面的等价关系:
>
>
> $E\backslash \left(\limsup_{k \to \infty}e_k \right)= \liminf_{k\to \infty}\left(E\backslash e_k\right)$.
>
>
> 事实上我们有$\left(\limsup_{k\to \infty}e_k\right)^{c}=\left(\bigcap_{N=1}^{\infty}\left(\bigcup_{k=N}^{\infty}e_k\right)\right)^{c}=\bigcup_{N=1}^{\infty}\left(\bigcup_{k=N}^{\infty}e_k\right)^{c} = \bigcup_{N=1}^{\infty}\bigcap_{k=N}^{\infty}e_k^c$.
>
>
> 下面再考虑$m(E_k)<\frac{1}{2^k}, \forall k$, 则有$m\left(\bigcup_{k=N}^{\infty}E_k\right)\leqslant \frac{1}{2^{N-1}}$. 记$F_N = \bigcup_{k=N}^{\infty}E_k$, 则$m\left(\bigcap_{N=1}^{\infty}F_N\right)\leqslant m\left(F_N\right)\to 0$.
>
>


下面我们讨论近乎一致收敛, 几乎处处收敛的关系:




> **定理**
>
> 若$f_n,f$在$E$上可测, $f_n$近乎一致收敛到$f$, 则$f_n$几乎处处收敛到$f$.
>
>



> **证明**
>
> $f_n$近乎一致收敛到$f$, 则有$\forall k >0, \exists {e_k}, m(e_k)<\frac{1}{k}, f_n \Rightarrow f \text{on} E\backslash e_k$, 其中$e_k$可测.
>
>
> 往证$m\left(\bigcup_{k=1}^{\infty}\bigcap_{N=1}^{\infty}\bigcup_{n=N}^{\infty} E\left[\left|f_n-f\right|\geqslant \frac{1}{k}\right]\right)=0$. 令$E_0=\limsup_{k \to \infty}e_k$, 则$E\left[f_n\nrightarrow f\right]\subset E_0$.
>
>
> 由Borel-Cantelli引理, 我们有$\sum_{n=1}^{\infty}m\left(E\left[\left|f_n-f\right|\geqslant \frac{1}{k}\right]\right)<\infty$. 
>
>
> 因此$m\left(\limsup_{n \to \infty}E\left[\left|f_n-f\right|\geqslant \frac{1}{k}\right]\right)=0$.
>
>



> **定理**
>
> (Egoroff) 设$m(E)<\infty$, 若$f_n$在$E$上几乎处处收敛到$f$, 则$f_n$近乎一致收敛到$f$.
>
>



> **证明**
>
> 由$f_n \rightarrow f \text{ a.e.} on E$知, $m\left(\bigcup_{k=1}^{\infty}\bigcap_{N=1}^{\infty}\bigcup_{n=N}^{\infty}E\left[|f_n-f|\geqslant \frac{1}{k}\right]\right)=0$.
>
>
> 记$F_k=\bigcap_{N=1}^{\infty}\bigcup_{n=N}^{\infty}E\left[|f_n-f|\geqslant \frac{1}{k}\right]$, 则$m(F_k)=0, \forall k >0$. 由$m(E)<\infty$有$\lim_{k\to \infty}m(F_k) = m(\lim_{k\to \infty}F_k)=0$.
>
>
> 即$\forall k > 0, \forall \delta >0, \exists k_{\delta}>0, \forall k>k_{\delta}, m(F_{k_{\delta}})<\frac{\delta}{2^{k_{\delta}}}$, 于是$m\left(\bigcup_{k\geqslant k_{\delta}}F_k\right)<\sum_{N=1}^{\infty}\frac{\delta}{2^{k_{\delta}}}=\delta$.
>
>
> 令$e=\bigcup_{n\geqslant k_{\delta}}F_k$, 则$m(e)<\delta$, $\forall x\in E\backslash e, |f_n(x)-f(x)|<\frac{1}{k}$, 这说明$f_n$近乎一致收敛到$f$.
>
>


根据上面的讨论, 我们知道近乎一致收敛有下面的表述方法:
$$\forall \delta >0, \forall \varepsilon >0, \exists E_0\subset E, m(E_0)<\delta, \exists N>0, \forall n\geqslant N, |f_n(x)-f(x)|<\varepsilon, \forall x\in E\backslash E_0.$$

事实上, 我们知道这表示$|f_n(x)-f(x)|\geqslant \varepsilon$的集合的测度应当很小, 而又考虑到$\delta$是任意取的, $N$只与$\delta$有关, 于是我们可以作下面的定义:
$$\forall \delta >0, \forall \varepsilon >0, \exists N, n\geqslant N, m\left(E\left[|f_n-f|\geqslant \varepsilon\right]\right)<\delta.$$

更进一步, 这可以写成
$\forall \varepsilon >0, \lim_{n \to \infty}m\left(E\left[|f_n-f|\geqslant \varepsilon\right]\right) = 0.$

这就有了下面依测度收敛的定义:



> **定义**
>
> 设$f_n,f$是定义在$E$可测且几乎处处有限的函数, 则$f_n$依测度收敛到$f$, 当且仅当$\forall \varepsilon >0, \lim_{n \to \infty}m\left(E\left[|f_n-f|\geqslant \varepsilon\right]\right) = 0$. 记作$f_n\Rightarrow f$.


对于这种收敛, 我们继续讨论和其他收敛的关系, 于是有下面的定理:




> **定理**
>
> (Lebesgue) 设$m(E)<\infty$, 若$f_n$几乎处处收敛到$f$, 则$f_n$依测度收敛到$f$.
>
>



> **证明**
>
> 由$f_n$几乎处处收敛到$f$, 则$\exists E_0\subset E, m(E_0)=0, \forall x\in E\backslash E_0, \lim_{n \to \infty}f_n(x)=f(x)$.
>
>
> 于是有$\forall \varepsilon >0, \exists N>0, \forall n\geqslant N, |f_n(x)-f(x)|<\varepsilon$, $\forall x\in E\backslash E_0$.
>
>
> 因此$m\left(E\left[|f_n-f|\geqslant \varepsilon\right]\right)\leqslant m(E_0)=0$, 这说明$f_n$依测度收敛到$f$.
>
>



> **定理**
>
> (Riesz) 若$f_n$依测度收敛到$f$, 则$\exists f_{n_k}$, $f_{n_k}$几乎处处收敛到$f$.
>
>



> **证明**
>
> 对于依测度收敛的函数列$f_n$, 总可以取$k>0$使得$e_k=E\left[|f_{n_k}-f|\geqslant \varepsilon\right]$满足$m(e_k)< \frac{1}{2^k}$. 于是$\sum_{k=1}^{\infty}m(e_k)=1<\infty$.
>
>
> 由Borel-Cantelli引理, 我们有$m\left(\limsup_{k \to \infty}e_k\right)=0$, 令$E_0=\limsup_{k \to \infty}e_k$, 则$\forall x \in E\backslash E_0, \exists k_0, \forall k\geqslant k_0, |f_{n_k}(x)-f(x)|<\varepsilon$.
>
>
> 这说明$f_{n_k}$几乎处处收敛到$f$.
>
>



> **注**
>
> 几乎处处收敛和依测度收敛不是等价的条件, 例如下面两个例子:
>
>
> 令$f_n(x)=\chi_{\left(\right.0,n\left.\right]}$, 则$f_n(x)$几乎处处收敛到$f(x)=\chi_{\left(\right.0,+\infty\left.\right)}$, 但$f_n$不依测度收敛到$f$, 这是因为我们可以验证$\lim_{n \to \infty}m\left(E\left[|f_n-f|\geqslant 1\right]\right) = +\infty$.
>
>
> 令$f_n(x)$按下面的方法排列: $f_1(x)=\chi_{\left[\right.0,\frac{1}{2}\left.\right]}$, $f_2(x)=\chi_{\left(\right.\frac{1}{2},1\left.\right]}$, $f_3(x)=\chi_{\left[\right.0,\frac{1}{4}\left.\right]}$, $f_4(x)=\chi_{\left(\right.\frac{1}{4},\frac{1}{2}\left.\right]}$,$\cdots$, 则$f_n(x)$依测度收敛到$f(x)=\chi_{\left[\right.0,1\left.\right]}$, 但$f_n$处处不收敛到$f$.
>
>


基于上面的结果, 我们下面讨论依测度收敛的性质:




> **例**
>
> 若$f_n\Rightarrow f$, $f_n\Rightarrow g$, 则$f=g$几乎处处成立.
>
>



> **例**
>
> 若$f_n\Rightarrow f$, $g_n\Rightarrow g$, $f_n\geqslant g_n$在$E$上几乎处处成立, 则$f\geqslant g$在$E$上几乎处处成立.
>
>



> **例**
>
> 若$f_n\Rightarrow f$, $a\in \mathbb{R}$, 则$af_n\Rightarrow af$.
>
>
> 若$f_n\Rightarrow f$, $g_n \Rightarrow g$, 则$f_n+g_n\Rightarrow f+g$.
>
>



> **推论**
>
> 若$f_n\Rightarrow 0$, $g_n \Rightarrow 0$, 则$f_ng_n\Rightarrow 0$.
>
>



> **证明**
>
> 往证: $\forall \varepsilon >0, \lim_{n \to \infty}m\left(E\left[|f_ng_n|\geqslant \varepsilon\right]\right) = 0$.
>
>
> 记$E_n=E\left[|g_n|>1\right]$, 则$E_n^c=E\left[|g_n|\leqslant 1\right]$.
>
>
> 于是$E\left[|f_ng_n|\geqslant \varepsilon\right]\subset E_n\left[|f_ng_n|\geqslant \varepsilon\right]\cup E_n^c\left[|f_ng_n|\geqslant \varepsilon\right]\subset E_n\cup E\left[|f_n|\geqslant \varepsilon\right]$.
>
>
> 由$f_n,g_n \Rightarrow 0$, $\exists N_1,N_2$使得$n\geqslant N_1, m(E\left[|f_n|\geqslant \varepsilon\right])<\frac{\delta}{2}$, $n\geqslant N_2, m(E\left[|g_n|\geqslant 1\right])<\frac{\delta}{2}$.
>
>
> 取$N = \max\{N_1,N_2\}$, 则$\forall n\geqslant N$, $m(E\left[|f_ng_n|\geqslant \varepsilon\right])<\frac{\delta}{2}+\frac{\delta}{2}=\delta$.
>
>
> 这说明$\lim_{n \to \infty}m\left(E\left[|f_ng_n|\geqslant \varepsilon\right]\right) = 0$. 即$f_ng_n \Rightarrow 0$.
>
>



> **推论**
>
> 若$f_n\Rightarrow f$, $g_n = g$有界可测, 则$f_ng\Rightarrow fg$.
>
>



> **证明**
>
> 往证: $\forall \varepsilon >0, \lim_{n \to \infty}m\left(E\left[|f_ng-fg|\geqslant \varepsilon\right]\right) = 0$.
>
>
> 由$f_n\Rightarrow f$, $\exists N, \forall n\geqslant N, m(E\left[|f_n-f|\geqslant \frac{\varepsilon}{M}\right])<\delta$.
>
>
> 注意到$E\left[|f_ng-fg|\geqslant \varepsilon\right]\subset  E\left[|f_n-f|\geqslant \frac{\varepsilon}{M}\right]$,其中$M=\sup |g_n|=\sup |g|$.
>
>
> 于是$m\left(E\left[|f_ng-fg|\geqslant \varepsilon\right]\right)\leqslant m\left(E\left[|f_n-f|\geqslant \frac{\varepsilon}{M}\right]\right)<\delta$. 即$f_ng\Rightarrow fg$.
>
>



> **注**
>
> 上面的若干例子说明了依测度收敛的函数列在数乘和加法下是封闭的, 但同时注意到第二个推论中的有界性是必要的, 例如下面这个例子:
>
>
> 令$f_n(x)=\chi_{\left(\right.0,n\left.\right]} \frac{1}{x}$, $g(x)=x$, 则$f_n\Rightarrow 0$, 但$f_n\cdot g = \chi_{\left(\right.0,n\left.\right]}$, $f\cdot g = 1$. 此时并没有$\chi_{\left(\right.0,n\left.\right]}\Rightarrow \chi_{\left(0,\infty\right)}$.
>
>




### 可测函数的连续性


上面讨论的许多收敛都是在可测函数的基础上进行的, 现在我们讨论可测函数的连续性, 这一点是必须的, 这是因为后续我们在建立可积函数, 可测函数与联系函数的关系时会更进一步讨论连续的特点. 




> **引理**
>
> 若$E$是一可测集, 则$C(E)\subset \mathcal{M} (E)$.



> **证明**
>
> 由$E$是可测集, 因此$E[f>a]=E\cap f^{-1}\left(a,\infty\right), \forall a \in \mathbb{R}$. 
>
>
> 由连续映射的定义知, $f^{-1}\left(a,\infty\right)$是开集. 于是$E\cap f^{-1}\left(a,\infty\right)$可测.
>
>
> 即$E[f>a],\forall a \in \mathbb{R}$是可测的. 于是$f$是可测函数.
>
>


上面这个定理说明了连续函数在可测集上是可测的, 下面我们为了得到更强结果的连续性条件, 我们首先考虑下面的一系列问题.




> **引理**
>
> 设$A,B$均为闭集, $A\cap B=\Phi$, 则$\exists g\in C(\mathbb{R}^n), \left.g\right|_A=1, \left.g\right|_B=0$.且$g$满足$|g(x)|\leqslant 1,\forall x\in \mathbb{R}^n$. 
>
>



> **证明**
>
> 可以自然想到距离定义, 于是有$g=\frac{d(x,B)}{d(x,A)+d(x,B)}$.
>
>
> 其中$d(x,A)=\inf_{y\in A}|x-y|$, $d(x,B)=\inf_{y\in B}|x-y|$. 同样可以验证$g(x)$是满足上面的条件的.
>
>


于是我们得到下面的定理, 具体说明了连续函数和可测函数的关系:




> **定理**
>
> (Lusin I) 设$E$是一可测集, $f\in \mathcal{M} (E)$, 则$\forall \delta >0, \exists F\subset E, m(E\backslash F)<\delta,$ 其中$F$是闭集, 且$f$在$F$上连续.
>
>



> **证明**
>
> 由$f\in \mathcal{M} (E)$有, $\exists \psi_k \rightarrow f$, 其中$\psi_k$是简单函数.
>
>
> 若$f$有界可测, 则$\psi_k$有界, $\exists F_k, m(E\backslash F_k)<\frac{\delta}{2^{k+1}}$, 其中$F_k$是闭集. 此时$\psi_k$在$F_k$上连续.
>
>
> 令$F=\bigcap_{k=1}^{\infty}F_k$, 则$m(E\backslash F)\leqslant \sum_{k=1}^{\infty}m(E\backslash F_k)<\delta$. 于是$f$在$F$上连续.
>
>
> 若$f$无界, 构造$g(x)=\frac{f(x)}{1+|f(x)|}$, 则$g$是有界的, 且$g\in \mathcal{M} (E)$.
>
>
> 于是$\exists F\subset E, m(E\backslash F)<\delta$, 其中$F$是闭集, 且$g$在$F$上连续.
>
>
> 由$g(x)=\frac{f(x)}{1+|f(x)|}$, $g(x)+g(x)|f(x)|=f(x)$, 即$g(x)+|g(x)|f(x)=f(x)$, $f(x)=\frac{g(x)}{1-|g(x)|}$, $f$在$F$上连续.
>
>


事实上我们还有$Lusin II$, 可以表示如下:




> **定理**
>
> (Lusin II) 设$E$是一可测集, $f\in \mathcal{M} (E)$, 则$\forall \delta >0, \exists g\in C(\mathbb{R}^n), \exists F\subset E, m(E\backslash F)<\delta,$ 其中$F$是闭集, 且$g(x)=f(x),\forall x \in F$.
>
>



> **证明**
>
> 由Lusin I, 我们有$\exists F\subset E, m(E\backslash F)<\delta,$ 其中$F$是闭集, 且$f$在$F$上连续.
>
>
> 令$g=\left.f\right|_{F}$, 则$g\in C(F)$.
>
>
> 为了证明$g\in C(\mathbb{R}^n)$, 我们构造$g_k(x)=\left\{\begin{array}{ll}
> g(x), & x\in F, \\
> \frac{1}{k}, & x\in E\backslash F.
> \end{array}\right.$\par
> 则$g_k\in C(\mathbb{R}^n)$, 且$\forall x\in F, g_k(x)=g(x)$, $\forall x\in E\backslash F, g_k(x)=\frac{1}{k}$.
>
>
> 于是$\forall x\in E, g_k(x)\rightarrow g(x)$, 这说明$g_k\rightarrow g$在$E$上收敛.
>
>
> 由于$g_k$是连续的, 因此$g\in C(\mathbb{R}^n)$.
>
>




[目录与前言](../viewer.html?md=Real-Analysis-Notes) · [下一章 →](../viewer.html?md=Real-Analysis-Notes-Chapter-4)
