[← 上一章](../viewer.html?md=Real-Analysis-Notes-Chapter-3)

## Lebesgue积分



### 非负可测函数的积分


在讨论一般的积分之前, 我们先定义下方图形, 这个概念实际上是Lebesgue积分的几何意义.




> **定义**
>
> 设$f$是定义在$E$上的非负可测函数, 则称$f$的下方图形称为$G(E,f)=\{(x,z)\in \mathbb{R}^2: x\in E, 0\leqslant z< f(x)\}$.
>
>



> **注**
>
> 这里我们要求$0\leqslant z< f(x)$, 实际上$0\leqslant z\leqslant f(x)$所表达的几何意义是一样的, 但按照后者定义证明函数Lebesgue可测时需要更深层次的分析技术.
>
>


下面我们依次定义特征函数和简单函数的Lebesgue积分, 后面我们将用这些函数来定义一般的非负可测函数的Lebesgue积分.




> **定义**
>
> 设$f(x)=\chi_{A}(x)$, 则$\int_{E}f(x)\mathrm{d}x=1\cdot m(A\cap E)$称为$f(x)$在$E$上的Lebesgue积分.
>
>
> 设$f(x)=\sum_{k=1}^{N}c_k\cdot \chi_{A_k}(x)$, 则$\int_{E}f(x)\mathrm{d}x=\sum_{k=1}^{N}c_k\cdot m(A_k\cap E)$称为$f(x)$在$E$上的Lebesgue积分.
>
>



> **注**
>
> 显然可以得到特征函数和简单函数的Lebesgue积分的几何意义就是对应的下方图形的测度.
>
>



> **引理**
>
> 设$f$和$g$是定义在$E$上的非负简单函数, 则:
>
>
>
> - $\int_{E}f(x)\mathrm{d}x\geqslant 0$.
> - 若$f(x)\leqslant g(x)$, 则$\int_{E}f(x)\mathrm{d}x\leqslant \int_{E}g(x)\mathrm{d}x$.
> - $\int_{E}(af(x)+bg(x))\mathrm{d}x=a\int_{E}f(x)\mathrm{d}x+b\int_{E}g(x)\mathrm{d}x$, 其中$a,b\in \mathrm{R}^{+}$.
>


下面我们定义一般的非负可测函数的Lebesgue积分.




> **定义**
>
> 设$f:E\rightarrow [c,d]$是非负可测函数, 则$f$在$E$上有Riemann积分$\lim_{|\lambda|\rightarrow 0}\sum_{k=1}^{N}f(\xi_k)\cdot \Delta x_k$, 类似地, 我们有Lebesgue积分$\lim_{|\lambda|\rightarrow 0}\sum_{k=1}^{N}\eta_k\cdot m(E_k)$.
>
>


不难注意到, 这里的$\eta_k$是$f$在$E_k$上的平均值, 而$m(E_k)$是$E_k$的测度, 因此$\eta_k\cdot m(E_k)$实际上是下方图形的面积. 但从严格证明的角度, 这种方式并不方便处理抽象测度的集合, 因此我们考虑下面这种定义方式:




> **定义**
>
> 设$f:E\rightarrow [c,d]$是非负可测函数, 则$f$在$E$上有Lebesgue积分$\lim_{k\to \infty}\int_{E}\phi_k(x)\mathrm{d}x$, 其中$\phi_k(x)$为单增简单函数, 且$\phi_k(x)\rightarrow  f(x)$, $\forall x\in E$.
>
>


这种定义方式看似简单, 但实际上需要证明$\phi_k(x)$的存在性, 并且若出现$\phi_k(x)$和$\psi_k(x)$时, 需要进一步说明$\lim_{k\to \infty}\int_{E}\phi_k(x)\mathrm{d}x=\lim_{k\to \infty}\int_{E}\psi _k(x)\mathrm{d}x$.




> **定义**
>
> 设$f:E\rightarrow [c,d]$是非负可测函数, 则$f$在$E$上有Lebesgue积分$\sup\left\{\int_{E}\phi(x)\mathrm{d}x: 0\leqslant \phi(x) \leqslant f(x)\right\}$, 其中 $g(x)$是一列非负简单函数.
>
>


后面的各种Lebesgue积分的问题中我们都只采用第三种方式定义, 但可以证明三种定义方式时等价的.




> **引理**
>
> 设$f$和$g$是定义在$E$上的非负可测函数, 则:
>
>
>
> - $\int_{E}f(x)\mathrm{d}x\geqslant 0$.
> - 若$f(x)\leqslant g(x)$, 则$\int_{E}f(x)\mathrm{d}x\leqslant \int_{E}g(x)\mathrm{d}x$.
> - $\int_{E}(af(x)+bg(x))\mathrm{d}x=a\int_{E}f(x)\mathrm{d}x+b\int_{E}g(x)\mathrm{d}x$, 其中$a,b\in \mathrm{R}^{+}$.
>



> **定理**
>
> 设$f$是定义在$E$上的非负可测函数, 则$\int_{E}f(x)\mathrm{d}x=m(G(E,f))$.
>
>



> **证明**
>
> 由$f$是非负可测函数, 则$\exists \phi_k(x)$是单增简单函数, 且$\phi_k(x)\rightarrow f(x)$, $\forall x\in E$.
>
>
> 于是$m(G(E,\phi_k))\leqslant m(G(E,f))$. 于是$\int_{E}f(x)\mathrm{d}x\leqslant m(G(E,f))$. 下证$\int_{E}f(x)\mathrm{d}x\geqslant m(G(E,f))$:
>
>
> $\forall (x,z)\in G(E,f), x \in E, 0\leqslant z<f(x)$, 则$\exists \phi_{k0}(x)$满足$0\leqslant z<\phi_k(x)<f(x)$, $\forall x\in E$.
>
>
> 即$(x,z)\in G(E,\phi_{k_0})\subset \bigcup_{k=1}^{\infty}G(E,\phi_{k})\subset G(E,f)$.
>
>
> 由$(x,z)$的任意性, 有$m(G(E,f))\subset \bigcup_{k=1}^{\infty}(G(E,\phi_k))$.
>
>
> 于是$m(G(E,f))=\lim_{k\to \infty}m(G(E,\phi_k))$. 即$\int_{E}f(x)\mathrm{d}x\geqslant m(G(E,f))$.
>
>


下面围绕非负可测函数的Lebesgue积分, 我们讨论一些性质.




> **推论**
>
> 设$f\in \mathcal{M} (E)$, $f\geqslant 0$, 若$\int_{E}f(x)\mathrm{d}x=0$, 则$f(x)=0$, a.e. on $E$.
>
>



> **证明**
>
> 假设$m(E[f\ne 0])>0$, 则$m(E[f> 0])>0$, 于是$m(\bigcup_{n=1}^{\infty}E[f>\frac{1}{n}])$.
>
>
> 于是$\exists n_0>0, \delta>0, m(E[f>\frac{1}{n_0}])\geqslant \delta>0$.
>
>
> 此时就会有$\int_{E}f(x)\mathrm{d}x\geqslant \frac{1}{n_0}\cdot m(E[f>\frac{1}{n_0}])\geqslant \frac{\delta}{n_0}>0$.
>
>



> **推论**
>
> 设$f\in \mathcal{M} (E)$, $m(E)\geqslant 0$, $f>0$ a.e. on $E$, 则$\int_{E}f(x)\mathrm{d}x>0$.
>
>



> **证明**
>
> 由$f>0$ a.e. on $E$, 则$m(E[f>0])>0$. 于是$\forall \varepsilon >0, m(E[f>\varepsilon])>0$.
>
>
> 于是$\int_{E}f(x)\mathrm{d}x\geqslant \varepsilon\cdot m(E[f>\varepsilon])>0$.
>
>



> **定理**
>
> (Levi) 设${f_n}\in \mathcal{M}(E)$, $f_n(x)\geqslant 0$ a.e. on $E$, 且$f_n(x)$单增收敛至$f(x)$, 则$f\in \mathcal{M}(E)$, 且$\lim_{n \to \infty}\int_{E}f_n(x)\mathrm{d}x= \int_{E}f(x)\mathrm{d}x$.
>
>



> **证明**
>
> 考虑证明$\lim_{n \to \infty}G(E,f_n) = G(E,f)$:
>
>
> $\lim_{n \to \infty}G(E,f_n) \subset G(E,f)$: $\forall (x,z)\in G(E,f_n), x\in E, 0\leqslant z<f_n(x)$, 则$\exists N>0, \forall n\geqslant N, f_n(x)\leqslant f(x)$, 于是$(x,z)\in G(E,f)$.
>
>
> $\lim_{n \to \infty}G(E,f_n) \supset G(E,f)$: $\exists f_{n_0}(x)$满足$0\leqslant z<f_{n_0}(x)<f(x)$, $\forall x\in E$, 则$(x,z)\in G(E,f_{n_0})\subset \bigcup_{n=1}^{\infty}G(E,f_n)=\lim_{n \to \infty}G(E,f_n)\subset G(E,f)$.
>
>
> 因此$\lim_{n \to \infty}G(E,f_n) = G(E,f)$.
>
>



> **推论**
>
> (Lebesgue 逐项积分) 设${f_n}\in \mathcal{M}(E)$, $f_n(x)\geqslant 0$ a.e. on $E$, $\forall n$, 则$\int_{E}\left(\sum_{n=1}^{\infty}f_n(x)\right)\mathrm{d}x = \sum_{n=1}^{\infty}\left(\int_{E}f_n(x)\mathrm{d}x\right)$.
>
>



> **证明**
>
> 记$P_n(x)=\sum_{k=1}^{n}f_k(x)$, 则$P_n(x)$是单增的, 且$P_n(x)\rightarrow \sum_{k=1}^{\infty}f_k(x)$ a.e. on $E$.
>
>
> 由Levi定理, $\lim_{n \to \infty}\int_{E}P_n(x)\mathrm{d}x= \int_{E}\left(\sum_{k=1}^{\infty}f_k(x)\right)\mathrm{d}x$.
>
>
> 由于$P_n(x)=\sum_{k=1}^{n}f_k(x)$, 则$\int_{E}P_n(x)\mathrm{d}x=\sum_{k=1}^{n}\left(\int_{E}f_k(x)\mathrm{d}x\right)$.
>
>
> 于是$\sum_{k=1}^{\infty}\left(\int_{E}f_k(x)\mathrm{d}x\right)= \int_{E}\left(\sum_{k=1}^{\infty}f_k(x)\right)\mathrm{d}x$.
>
>



> **定理**
>
> (Fatou) 设${f_n}\in \mathcal{M}(E)$, $f_n(x)\geqslant 0$ a.e. on $E$, 则$\int_{E}\liminf_{n \to \infty}f(x)\mathrm{d}x\leqslant \liminf_{n \to \infty}\int_{E}f_n(x)\mathrm{d}x$.
>
>



> **证明**
>
> $\liminf_{n \to \infty}f_n(x)=\lim_{N \to \infty}\inf_{n\geqslant N}f_n(x)$, 记$g_N(x) = \inf_{n\geqslant N}f_n(x)$, 于是$\inf_{n\geqslant N}\int_{E}f_n(x)\mathrm{d}x\geqslant \int_{E}g_N(x)$.
>
>
> 两边取极限有$\lim_{N \to \infty}\inf_{n\geqslant N}\int_{E}f_n(x)\mathrm{d}x\geqslant \int_{E}\left(\liminf_{n \to \infty}f_n(x)\right)\mathrm{d}x$.
>
>




### 一般可测函数的积分


对于一般可测函数, 我们考虑将其分成正部函数和负部函数, 于是有下面的定义:




> **定义**
>
> $f$在$E$上的Lebesgue积分定义为$\int_{E}f(x)\mathrm{d}x=\int_{E}f^{+}(x)\mathrm{d}x-\int_{E}f^{-}(x)\mathrm{d}x$.
>
>



> **引理**
>
> 考虑$f$在$E$上的积分存在和可积的充要条件, 我们有:
>
>
>
> - $f$在$E$上积分存在, 即$\int_{E}f^{+}(x)\mathrm{d}x$ 和$\int_{E}f^{-}(x)\mathrm{d}x$至多一个为$\infty$.
> - $f$在$E$上可积, 即$\int_{E}f^{+}(x)\mathrm{d}x$ 和$\int_{E}f^{-}(x)\mathrm{d}x$均有限.
>



> **证明**
>
> $f$在$E$上积分存在, 即$\int_{E}f(x)\mathrm{d}x=\int_{E}f^{+}(x)\mathrm{d}x-\int_{E}f^{-}(x)\mathrm{d}x$可以运算, 显然需要$f^{+}$和$f^{-}$至少有一个是有限的.
>
>
> $f$在$E$上可积, 即$|\int_{E}f(x)\mathrm{d}x|<+\infty$, 则$\int_{E}f^{+}(x)\mathrm{d}x$ 和$\int_{E}f^{-}(x)\mathrm{d}x$均有限.
>
>


下面给出一些一般可测函数的性质:




> **命题**
>
>
> - 若$f=g$ a.e. on $E$, 则$\int_{E}f(x)\mathrm{d}x=\int_{E}g(x)\mathrm{d}x$.
>
>
> - 若$f\in L(E_1)$, $f\in L(E_2)$, 则$f\in L(E_1\cup E_2)$.
>
>
> - 若$f\in L(E)$, 则$\left|\int_{E}f(x)\mathrm{d}x\right|\leqslant \int_{E}|f(x)|\mathrm{d}x$.
>
>
> - 若$f\in L(E)$, 则$f$在$E$上几乎处处有限.
>
>
>



> **证明**
>
>
> - 由$f=g$ a.e. on $E$, 则$m(E[f\ne g])=0$, 于是$\int_{E}f(x)\mathrm{d}x=\int_{E}g(x)\mathrm{d}x$, 其中$\int_{E[f\ne g]}f(x)\mathrm{d}x=\int_{E[f\ne g]}g(x)\mathrm{d}x=0$.
>
>
> - 由$f\in L(E_1)$, $f\in L(E_2)$, 则$\int_{E_1\cup E_2}f^{+}(x)\mathrm{d}x<\int_{E_1}f^{+}(x)\mathrm{d}x+\int_{E_2}f^{+}(x)\mathrm{d}x<+\infty$, $\int_{E_1\cup E_2}f^{-}(x)\mathrm{d}x<\int_{E_1}f^{-}(x)\mathrm{d}x+\int_{E_2}f^{-}(x)\mathrm{d}x<+\infty$, 于是$\int_{E_1\cup E_2}f(x)\mathrm{d}x<+\infty$.
>
>
> - 由$f\in L(E)$, 则$\int_{E}|f(x)|\mathrm{d}x<+\infty$, 于是$\left|\int_{E}f(x)\mathrm{d}x\right|=\left|\int_{E}f^{+}(x)\mathrm{d}x-\int_{E}f^{-}(x)\mathrm{d}x\right|\leqslant \left|\int_{E}f^{+}(x)|\mathrm{d}x\right|+\left|\int_{E}f^{-}(x)|\mathrm{d}x\right|=\int_{E}\left|f(x)\right|\mathrm{d}x$.
>
>
> - $f$ a.e. 有限等价于$f^{+}$和$f^{-}$ a.e. 有限. 由$f\in L(E)$, $\int_{E}f^{+}(x)\mathrm{d}x\geqslant \int_{E[f^{+}=\infty]}f^{+}(x)\mathrm{d}x\geqslant N\cdot m(E[f^{+}=\infty]), \forall N \in \mathbb{N}$. 于是$m(E[f^{+}=\infty])<\frac{a}{N}, \forall N\in \mathbb{N}$. 即$m(E[f^{+}=\infty])=0$. $f^{-}(x)$同理可证. 于是$f$在$E$上几乎处处有限.
>
>
>



> **注**
>
> 若$f\in L(E_i), i=1,2,\cdots$, 未必有$f\in L\left(\bigcup_{i=1}^{\infty}E_i\right)$, 也未必有$f$在$\bigcup_{i=1}^{\infty}E_i$上积分存在.
>
>
> 例如$f(x)=1$, $E_i=[i,i+1]$, $\bigcup_{i=1}^{\infty}E_i=\left[1\right.\left.,\infty\right)$, 此时$f$在$\left[1\right.\left.,\infty\right)$上不可积.
>
>
> 另可取$f(x)=(-1)^{i}$, $E_i=[i,i+1]$, 此时$f$在$\bigcup_{i=1}^{\infty}E_i$上积分不存在.
>
>


下面考虑一种方法, 用来控制$f_n$在$E$上的积分值, 为了说明这个特点, 我们首先需要引入绝对连续性, 并结合上面提及过的依测度收敛给出下面一个定理.




> **定义**
>
> 设$f\in L(E)$, 若$\forall \varepsilon >0, \exists \delta >0, \forall e\subset E, m(e)<\delta$, 有$\left|\int_{e}f(x)\mathrm{d}x\right|<\int_{e}\left|f(x)\right|\mathrm{d}x<\varepsilon$, 则称$f$在$E$上绝对连续.
>
>



> **定理**
>
> 设$f\in L(E)$, 则$f$在$E$上绝对连续.
>
>



> **证明**
>
> 由$f\in L(E)$, 则$\int_{E}|f(x)|\mathrm{d}x<+\infty$, 下面考虑取${\varphi_k}$单增简单函数逼近$f$, 于是$\int_{E}|f|\mathrm{d}x=\lim_{k \to \infty}\int_{E}\varphi_k(x)\mathrm{d}x$.
>
>
> 即$\forall \varepsilon >0, \exists K>0, \forall k>K, \left|\int_{E}|f|\mathrm{d}x-\int_{E}\varphi_k(x)\mathrm{d}x\right|<\frac{\varepsilon}{2}$.
>
>
> 考虑$f$可积, 于是$|f|=\sum_{k=1}^{n}c_k\chi_{E_k}(x)$, 记$M=\sup \{c_k:k=1,2,\cdots\}\geqslant |f|$, 则有$\int_{e}f(x)\mathrm{d}x\leqslant \int_{e}M\mathrm{d}x\leqslant M\cdot m(e) = M\cdot \delta$, $\forall e\subset E$.
> 取$\delta = \frac{\varepsilon}{2M}$, 则$\int_{e}|f(x)|\mathrm{d}x\leqslant \frac{\varepsilon}{2}+\frac{\varepsilon}{2M}\cdot M=\varepsilon$.
>
>
> 于是$ \exists \delta >0, \forall e\subset E, m(e)<\delta$, 有$\left|\int_{e}f(x)\mathrm{d}x\right|<\int_{e}\left|f(x)\right|\mathrm{d}x<\varepsilon$.
>
>
> 这说明$f$在$E$上绝对连续.
>
>



> **定理**
>
> (Lebesgue 控制收敛) 设$f_n$几乎处处有限且可测, $F(x)\geqslant |f_n(x)|$, 其中$F$可积, $f_n\Rightarrow f$在$E$上, 则$f\in L(E)$, 且$\int_{E}f(x)\mathrm{d}x=\lim_{n\to \infty} \int_{E}f_n(x)\mathrm{d}x$.
>
>



> **证明**
>
> 由在$E$上$f_n\Rightarrow f$, $\exists f_{n_k}, f_{n_k}\rightarrow f$ a.e. on $E$, 又有$F(x)\geqslant |f_{n_k}(x)|$, 则$|f|\leqslant F$, 于是$f$在$E$上可积.
>
>
> 下证$\int_{E}f(x)\mathrm{d}x=\lim_{n\to \infty} \int_{E}f_n(x)\mathrm{d}x$:
>
>
> 考虑$E=\bigcup_{k=1}^{\infty}E_k$, 其中$\{E_k\}$递增可测.
>
>
> 由$0\leqslant \int_{E}F(x)\mathrm{d}x=\lim_{k\to \infty}\int_{E_k}F(x)\mathrm{d}x<+\infty$, $\forall \varepsilon >0, \exists k\in \mathrm{N}, \int_{E\backslash E_k}F(x)\mathrm{d}x<\frac{\varepsilon}{4}$.
>
>
> 于是有$\lim_{n\to \infty}\int_{E_k}f_n(x)\mathrm{d}x=\int_{E_k}f(x)\mathrm{d}x$. 下面考虑$\left|\int_{E_k}(f-f_n)\mathrm{d}x\right|=\left|\int_{E_k}f\mathrm{d}x-\int_{E_k}f_n\mathrm{d}x\right|<\frac{\varepsilon}{2}$.
>
>
> 于是有$\exists N\in \mathrm{N}, n\geqslant N, \left|\int_{E}f\mathrm{d}x-\int_{E}f_n\mathrm{d}x\right|=\left|\int_{E}(f-f_n)\mathrm{d}x\right|\leqslant \frac{\varepsilon}{2}+2\int_{E\backslash E_k}F\mathrm{d}x=\varepsilon$.
>
>
> 即$\int_{E}f(x)\mathrm{d}x=\lim_{n\to \infty} \int_{E}f_n(x)\mathrm{d}x$.
>
>



> **注**
>
> Lebesgue控制收敛定理中依测度收敛可以改成几乎处处收敛, 而且在全空间测度有限的情况下有几乎处处收敛函数列必定近乎一致收敛, 因此也有对应于近乎一致收敛的定理.
>
>


类似地, 我们还有Lebesgue有界收敛定理, 可以表示如下:




> **推论**
>
> (Lebesgue 有界收敛) 设$f_n$几乎处处有限且可测, $m(E)<+\infty$, $\exists K >0, K\geqslant |f_n(x)|$, $f_n\Rightarrow f$在$E$上, 则$f\in L(E)$, 且$\int_{E}f(x)\mathrm{d}x=\lim_{n\to \infty} \int_{E}f_n(x)\mathrm{d}x$.
>
>



> **注**
>
> 其证明过程和Lebesgue控制收敛定理完全相同, 因为这里要求有界性是一致的.
>
>
> 事实上, 在面对具体函数时, 使用Lebesgue有界收敛定理更方便, 因为判断函数列的界比判断其极限的有限性更简单.
>
>




### Lebesgue积分与Riemann积分的关系


在讨论完基本的Lebesgue积分性质后, 我们回到最初的问题, 即分析Lebesgue积分为什么在一定程度上可以代替Riemann积分, 以及两者之间的关系. 为了明确Riemann积分的特点, 我们首先给出一个描述振幅函数的引理.




> **引理**
>
> 设$f$是定义在$[a,b]$上的有界函数, 记$\omega(x)$为$f$在$x$处的振幅函数, 则有$\int_{[a,b]}\omega(x)\mathrm{d}x=\overline{\int_{a}^{b}}f(x)\mathrm{d}x-\underline{\int_{a}^{b}}f(x)\mathrm{d}x$.
>
>
> 其中$\int_{[a,b]}\omega(x)\mathrm{d}x$是$f$在$[a,b]$上的Lebesgue积分, $\overline{\int_{a}^{b}}f(x)\mathrm{d}x$和$\underline{\int_{a}^{b}}f(x)\mathrm{d}x$分别是$f$在$[a,b]$上的上Riemann积分和下Riemann积分.
>
>



> **证明**
>
> 由$f$是有界函数, $\omega(x)$也是有界函数, 因此是可积的.
>
>
> 对$[a,b]$作划分$a=x_0<x_1<\cdots<x_n=b$, 令$M_i=\sup \{f(x): x_{i-1}<x<x_{i}\}, m_i=\inf \{f(x): x_{i-1}<x<x_{i}\}$, 则有$\overline{\int_{a}^{b}}f(x)\mathrm{d}x=\lim_{n \to \infty}\sum_{i=1}^{n}M_i\cdot (x_i-x_{i-1})$, $\underline{\int_{a}^{b}}f(x)\mathrm{d}x=\lim_{n \to \infty}\sum_{i=1}^{n}m_i\cdot (x_i-x_{i-1})$.
>
>
> 于是可以作函数列$\omega_{n}(x)=\begin{cases}
> M_i-m_i, & x\in (x_{i-1},x_i), i=1,2,\cdots,n-1\\
> 0, & x=x_i, i=1,2,\cdots,n
> \end{cases}$, 记分点全体为$E$, 则有$m(E)=0$, $\lim_{n \to \infty}\omega_{n}(x)=\omega(x)$ a.e. on $[a,b]$.\par
> 注意到$\omega_{n}(x)$是单增有界函数,于是有$\lim_{n \to \infty}\int_{[a,b]}\omega_{n}(x)\mathrm{d}x=\int_{[a,b]}\omega(x)\mathrm{d}x$.
>
>
> 事实上我们有$\int_{[a,b]}\omega_{n}(x)\mathrm{d}x=\sum_{i=1}^{n}(M_i-m_i)(x_i-x_{i-1})=\sum_{i=1}^{n}M_i\cdot (x_i-x_{i-1})-\sum_{i=1}^{n}m_i\cdot (x_i-x_{i-1})$.
>
>
> 于是$\int_{[a,b]}\omega(x)\mathrm{d}x=\lim_{n \to \infty}\int_{[a,b]}\omega_{n}(x)\mathrm{d}x=\lim_{n \to \infty}\left(\overline{\int_{a}^{b}}f(x)\mathrm{d}x-\underline{\int_{a}^{b}}f(x)\mathrm{d}x\right)$.
>
>
> 即$\int_{[a,b]}\omega(x)\mathrm{d}x=\overline{\int_{a}^{b}}f(x)\mathrm{d}x-\underline{\int_{a}^{b}}f(x)\mathrm{d}x$.
>
>



> **定理**
>
> (Riemann可积) 设$f$是区间$[a,b]$上的有界函数, 则$f$在$[a,b]$上Riemann可积的充要条件是$f$在$[a,b]$上几乎处处连续.
>
>



> **证明**
>
> 由$f$在$[a,b]$上Riemann可积, 可知$f$在$[a,b]$上的Darboux上积分和Darboux下积分相等, 因此由上面的引理知, $\int_{[a,b]}\omega(x)\mathrm{d}x=0$.
>
>
> 由于$\omega(x)$是$f$在$x$处的振幅函数, 在$[a,b]$上几乎处处为零, 因此$f$在$[a,b]$上几乎处处连续.
>
>
> 反之, 若$f$在$[a,b]$上几乎处处连续, 则$\omega(x)$几乎处处为零, 因此由上面的引理知, $\int_{[a,b]}\omega(x)\mathrm{d}x=0$.
>
>
> 于是$f$在$[a,b]$上的Darboux上积分和下积分相等, $f$在$[a,b]$上Riemann可积.
>
>



> **注**
>
> 上面的结果告诉我们, 一个函数的Riemann可积性是取决于其在一个函数值有界的区间上的连续点全体的测度, 而不是不连续点的函数值.
>
>



> **定理**
>
> 若$f$是Riemann可积的, 则$f$在$[a,b]$上Lebesgue可积, 且$\int_{[a,b]}f(x)\mathrm{d}x=\int_{a}^{b}f(x)\mathrm{d}x$.
>
>



> **证明**
>
> 首先我们知道, $f$Riemann可积时一定有$f$在$[a,b]$上几乎处处连续, 于是$f$在$[a,b]$上Lebesgue可积.
>
>
> 下面来说明两种积分值也是相同的:
>
>
> 对$[a,b]$作任意划分$a=x_0<x_1<\cdots<x_n=b$, 令$M_i=\sup \{f(x): x_{i-1}<x<x_{i}\}, m_i=\inf \{f(x): x_{i-1}<x<x_{i}\}$, 则有$\int_{[a,b]}f(x)\mathrm{d}x=\sum_{i=1}^{n}\int_{[x_{i-1},x_i]}f(x)\mathrm{d}x$.
>
>
> 另一方面考虑$m_i(x_{i-1}-x_{i})\leqslant \int_{[x_{i-1},x_i]}f(x)\mathrm{d}x\leqslant M_i(x_{i-1}-x_{i})$, 于是有$\sum_{i=1}^{n}m_i(x_{i-1}-x_{i})\leqslant \int_{[a,b]}f(x)\mathrm{d}x\leqslant \sum_{i=1}^{n}M_i(x_{i-1}-x_{i})$.
>
>
> 上式左右两边取上下确界有$\underline{\int_{a}^{b}}f(x)\mathrm{d}x= \int_{[a,b]}f(x)\mathrm{d}x= \overline{\int_{a}^{b}}f(x)\mathrm{d}x$.
>
>
> 这说明$f$在$[a,b]$上Lebesgue可积, 且$\int_{[a,b]}f(x)\mathrm{d}x=\int_{a}^{b}f(x)\mathrm{d}x$.
>
>



> **注**
>
> 上述结论反之不一定成立, 即Lebesgue可积的函数不一定是Riemann可积的.
>
>


下面我们考虑广义积分, 在Riemann积分的意义下, 其本质是累次极限, 但在这里我们有下面的结果, 说明广义的Lebesgue积分是绝对收敛的积分.




> **定理**
>
> 设$\{E_k\}$单增可测, 且$\bigcup_{k=1}^{\infty}E_k=E$, $f$在$E_K$上可积, 若$\lim_{k \to \infty}\int_{E_k}|f(x)|\mathrm{d}x$存在, 则$f$在$E$上可积, 且$\int_{E}f(x)\mathrm{d}x=\lim_{k \to \infty}\int_{E_k}f(x)\mathrm{d}x$.
>
>



> **证明**
>
> 取$F_k(x)=|f(x)|\chi_{E_k}(x)$, 则$F_k$在$E_k$上可积, 且$\int_{E_k}F_k(x)\mathrm{d}x=\int_{E_k}|f(x)|\mathrm{d}x$, $\forall k\in \mathbb{N}$.
>
>
> 由Levi, $\lim_{k \to \infty}\int_{E_k}F_k(x)\mathrm{d}x=\int_{E}F(x)\mathrm{d}x$, 其中$F(x)=|f(x)|\chi_{E}(x)$.
>
>
> 由于$\lim_{k \to \infty}\int_{E_k}|f(x)|\mathrm{d}x$存在, 则$\int_{E}F(x)\mathrm{d}x=\lim_{k \to \infty}\int_{E_k}|f(x)|\mathrm{d}x<+\infty$.
>
>
> 即$f$在$E$上可积, 且$\int_{E}f(x)\mathrm{d}x=\lim_{k \to \infty}\int_{E_k}f(x)\mathrm{d}x$.
>
>



> **注**
>
> 事实上我们可以发现, 广义积分和Lebesgue积分都是对Riemann积分的一种推广, 而又有这样的例子说明广义积分存在的函数总可积时这种积分对区域不具备可加性.
>
>




### 重积分与累次积分的关系


在以往的分析中, 我们已经讨论过重积分和累次积分的关系, 而这里为了给出更完善的结果, 我们进一步讨论在Lebesgue积分意义下的重积分和累次积分的关系.




> **定理**
>
> 在Riemann积分的意义下, 若$f$在$E=\left[a_1,b_1\right]\times \left[a_2,b_2\right]$上Riemann可积, 则$\int_{E}f(x,y)\mathrm{d}x\mathrm{d}y=\int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}f(x,y)\mathrm{d}y\right)\mathrm{d}x=\int_{a_2}^{b_2}\left(\int_{a_1}^{b_1}f(x,y)\mathrm{d}x\right)\mathrm{d}y$.
>
>



> **注**
>
> 这个结果是显然的, 我们不再证明, 但同时需要注意到, 这种想法是很难直接迁移到Lebesgue积分上的.
>
>


类似地, 我们首先讨论非负可测函数的结果, 并推广至一般可测函数.




> **引理**
>
> 设$f(x,y)$是定义在$\mathbb{R}^n=\mathbb{R}^p\times \mathbb{R}^q$上的非负可测函数, 若$f$满足:
>
>
>
> - $f(x,y)$是对于几乎处处的$x\in \mathbb{R}^p$都关于$y$非负可测的函数.
> - $F_f(x)=\int_{\mathbb{R}^q}f(x,y)\mathrm{d}y$是$\mathbb{R}^p$上关于$x$的可测函数.
> - $\int_{\mathbb{R}^p}F_f(x)\mathrm{d}x=\int_{\mathbb{R}^p}\mathrm{d}x\int_{\mathbb{R}^q}f(x,y)\mathrm{d}y=\int_{\mathbb{R}^n}f(x,y)\mathrm{d}x\mathrm{d}y$.
>
> 则称$f\in \mathcal{F}$.
>
>
> 对于$f,g\in \mathcal{F}$, 有:
>
>
>
> - $\forall a \geqslant 0, af\in \mathcal{F}$.
> - $f+g\in \mathcal{F}$.
> - 若$f(x,y)-g(x,y)\geqslant 0$, 且$g$是在$\mathbb{R}^n$上可积的, 则$f-g\in \mathcal{F}$.
> - 若单增函数列$f_k\in \mathcal{F}$, 且$f_k(x,y)\rightarrow f(x,y)$ a.e. on $\mathbb{R}^n$, 则$f\in \mathcal{F}$.
>



> **证明**
>
> 根据积分的性质, 第一条和第二条是显然的.
>
>
> 对于第三条, 若$g\in \mathcal{F}$, 则$F_g(x)$几乎处处有限, 于是根据$(f(x,y)-g(x,y))+g(x,y)=f(x,y)$, 有$f-g\in \mathcal{F}$.
>
>
> 对于第四条, 往证$f$满足上面三条性质, 事实上第一条是显然的. 由于$f_k \in \mathcal{F}$, 因此$\int_{\mathbb{R}^q}f(x,y)\mathrm{d}y=\lim_{k \to \infty}\int_{\mathbb{R}^q}f_k(x,y)\mathrm{d}y$, 也是非负可测的.
>
>
> 最后考虑$\int_{\mathbb{R}^n}f(x,y)\mathrm{d}x\mathrm{d}y=\lim_{k \to \infty}\int_{\mathbb{R}^n}f_k(x,y)\mathrm{d}x\mathrm{d}y=\lim_{k \to \infty}\int_{\mathbb{R}^p}\mathrm{d}x\int_{\mathbb{R}^q}f_k(x,y)\mathrm{d}y$.
>
>
> 由$f_k(x,y)\rightarrow f(x,y)$ a.e. on $\mathbb{R}^n$,
>
>
> 我们有$\lim_{k \to \infty}\int_{\mathbb{R}^p}\mathrm{d}x\int_{\mathbb{R}^q}f_k(x,y)\mathrm{d}y\int_{\mathbb{R}^p}\mathrm{d}x\int_{\mathbb{R}^q}\lim_{k \to \infty}f_k(x,y)\mathrm{d}y=\int_{\mathbb{R}^p}\mathrm{d}x\int_{\mathbb{R}^q}f(x,y)\mathrm{d}y$.
>
>
> 于是$f\in \mathcal{F}$.
>
>



> **定理**
>
> (Tonelli) 所有的非负可测函数$f$都满足$f\in\mathcal{F}$.
>
>



> **证明**
>
> 事实上由上面的引理, 我们只需要证明所有的非负可测简单函数都满足$f\in \mathcal{F}$. 
>
>
> 更进一步, 根据上面的线性性质, 我们只需要说明所有在可测集上示性函数都满足$f\in \mathcal{F}$. 
>
>
> 下面我们将仿照乘积测度的证明, 分若干步得到这个结果:
>
>
> 若$E=I_1\times I_2$, 则显然有$\int_{E}\chi_E(x,y)\mathrm{d}x\mathrm{d}y=\int_{I_1}\mathrm{d}x\int_{I_2}\mathrm{d}y=m(I_1)m(I_2)=|I_1||I_2|=m(E)$.
>
>
> 另一方面可以很自然验证$\chi_{E}(x,y)$是对于几乎处处的$x\in I_1$, $\chi_{E}(x,y)$关于$y$的非负可测函数.
>
>
> 若$E$为开集, 则可以找到一列区间的并, 类似也有结果.
>
>
> 若$E$为有界闭集, 则$E$可以表示为两个有界开集的差, 由上面引理的第三条结果可以得到.
>
>
> 若$E$为有界可测集, 则可以找到一列有界闭集的并, 由上面引理的第四条结果可以得到.
>
>
> 若$E$为一般的可测集, 则可以考虑$E=\left(\bigcup_{k=1}^{\infty}F_k\right)\cup \mathbb{Z}$, 其中$F_k$均为有界闭集, 因此$\chi_{E_k}(x,y)\in \mathcal{F}$.
>
>
> 另外由于$m(\mathbb{Z})=0$, 因此$\chi_{\mathbb{Z}}(x,y)$也是可测的, 于是$\chi_{E}(x,y)=\lim_{k \to \infty}\chi_{\bigcup_{k=1}^{\infty} F_k}(x,y)+\chi_{\mathbb{Z}}(x,y)$, 由上面引理的第四条和第二条结果可以得到.
>
>



> **注**
>
> Tonelli定理中要求的三个结果可以对$x$和$y$交换顺序, 这是十分显然的.
>
>


下面类似地, 我们把一般可测函数分为正部和负部, 也可以得到类似的性质.




> **定理**
>
> (Fubini) 所有的可测函数$f$都满足$f\in\mathcal{F}$.
>
>



> **证明**
>
> 令$f(x,y)=f^{+}(x,y)-f^{-}(x,y)$, 其中$f^{+}(x,y)=\max\{f(x,y),0\}, f^{-}(x,y)=\max\{-f(x,y),0\}$, 则$f^{+}$和$f^{-}$都是非负可测函数.
>
>
> 由Tonelli定理, $f^{+}\in \mathcal{F}$, $f^{-}\in \mathcal{F}$, 又有$f=f^{+}-f^{-}$, 因此由上面引理的第三条结果, 有$f\in \mathcal{F}$.
>
>





[目录与前言](../viewer.html?md=Real-Analysis-Notes) · [下一章 →](../viewer.html?md=Real-Analysis-Notes-Chapter-5)
