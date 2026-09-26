[← 上一章](../viewer.html?md=Real-Analysis-Notes-Chapter-4)

## 习题集



> **注**
>
> 这里收集了一些常见的例子和反例, 以帮助理解集合论和测度论中的一些概念. 题目可能没有按照理解Lebesgue测度的顺序安排, 但足够体现实分析的整体特点.
>
>



> **例**
>
> 集合可以与其真子集对等.



> **证明**
>
> 在连续集和离散集中均存在例子, 考虑$\mathbb{N}$和$\mathbb{N}\backslash \{1\}$, 则$\mathbb{N}$和$\mathbb{N}\backslash \{1\}$是等势的.
>
>
> 另考虑$\mathbb{R}$和$[0,1]$, 可以构造双射$f:\mathbb{R}\rightarrow [0,1]$, 例如$f(x)=\frac{x}{1+|x|}$, 则$f$是双射, 且$f(\mathbb{R})=[0,1]$.
>
>
> 于是$\mathbb{R}$和$[0,1]$是等势的.
>
>



> **例**
>
> 稠密集的余集不一定是疏朗集.



> **证明**
>
> 考虑$\mathbb{Q}$和$\mathbb{R}\backslash \mathbb{Q}$, 则$\mathbb{Q}$和$\mathbb{R}\backslash \mathbb{Q}$均为稠密集, 但$\mathbb{R}\backslash \mathbb{Q}$的余集$\mathbb{Q}$不是疏朗集.
>
>



> **例**
>
> $A \backslash C =  B \backslash C \nRightarrow A = B$.



> **证明**
>
> 反例可取$A=\{1,2,3\}, B=\{1,3\}, C=\{2\}$, 则$A \backslash C = \{1\} \nRightarrow B \backslash C = \{1,3\}$. 但$A=B$.
>
>



> **例**
>
> 全体有理系数多项式是可数集.



> **证明**
>
> 设$P_n(x)=a_0+a_1x+\cdots+a_nx^n$, 其中$a_i\in \mathbb{Q}$, 则$P_n(x)$的系数个数为$n+1$, 因此全体有理系数多项式的个数为$\bigcup_{n=0}^{\infty}\mathbb{Q}^{n+1}$.
>
>
> 由于$\mathbb{Q}$是可数集, $\mathbb{Q}^{n+1}$是可数集, 因此$\bigcup_{n=0}^{\infty}\mathbb{Q}^{n+1}$是可数集.
>
>



> **例**
>
> 开集一定是某一列闭集的并集.



> **证明**
>
> 设$E$是开集, 则$\forall x\in E, \exists r>0, B(x,r)\subset E$, 于是$E=\bigcup_{x\in E}B(x,r)$.
>
>
> 由于$B(x,r)$是闭集, 因此$E$是某一列闭集的并集.
>
>



> **例**
>
> 任意多个可测集的交集不一定是可测集.



> **证明**
>
> 只能说明至多可列的情形是成立的.
>
>



> **例**
>
> 外测度有限的集合不一定是有界集.
>
>



> **证明**
>
> 例如$\mathbb{N}$, 外测度有限, 但$\mathbb{N}$无界.
>
>



> **例**
>
> 孤立集是至多可数集, 但可能有聚点.
>
>



> **证明**
>
> 例如$\{\frac{1}{n}\}$是孤立集, 但$0$是其聚点.
>
>



> **例**
>
> 设映射$\varphi : A \to B$, $B \subset \varphi(\varphi^{-1}(B))$不一定成立.



> **证明**
>
> 例如考虑$A=\{1\}, B=\{1,2\}$, $\varphi(1)=1$, $\varphi^{-1}(B)=\{1\}$, $\varphi(\varphi^{-1}(B))=\{1\}$, 但$B \nsubseteq \{1\}$.
>
>



> **例**
>
> 测度大于零的可测集中必定含有不可测的子集.
>
>



> **证明**
>
> 不可测集的必要条件为外测度大于0, 因此根据Vitali的构造方法, 一定有测度大于零的可测集含有不可测的子集.
>
>



> **例**
>
> 几乎处处收敛的可测函数列不一定是依测度收敛的函数列.



> **证明**
>
> 由Lebesgue定理, 在测度非无限的情形时成立, 例如$f_n(x)=\chi_{[n,n+1]}(x)$, 则$f_n(x)\rightarrow 0$ a.e. on $\mathbb{R}$, 但$\int_{\mathbb{R}}f_n(x)\mathrm{d}x=1$, 因此不依测度收敛.
>
>



> **例**
>
> 设集合$A,B$不相交, 则$m^{*}(A \cup B) \leqslant m^{*}(A) + m^{*}(B)$.



> **证明**
>
> 当$A,B$满足两个集合的距离严格大于0时才有$m^{*}(A \cup B) = m^{*}(A) + m^{*}(B)$, 对于一般情形由次可加性有$m^{*}(A \cup B) \leqslant m^{*}(A) + m^{*}(B)$.
>
>



> **例**
>
> 两个非空闭集如果不相交, 则两个集合之间的距离可以等于0.



> **证明**
>
> 事实上当两个集合是紧的时候才有上面的结果成立.
>
>



> **例**
>
> 集合的边界点要么是该集合的孤立点, 要么是该集合的聚点.



> **证明**
>
> 根据定义可知, 边界点和聚点的全体构成这个集合.



> **例**
>
> 若点$p$同时是集合$E$, $F$的聚点, 则$p$不一定是$E \cap F$的聚点.



> **证明**
>
> 例如$E=\{1/n: n=1,2,\cdots\}, F=\{-1/n: n=1,2,\cdots\}$, 则$0$是$E$和$F$的聚点, 但$E \cap F = \emptyset$, 因此$0$不是$E \cap F$的聚点.
>
>



> **例**
>
> 设集合$A, B$对等, $C \subset A$, $D \subset B$ 满足$C \sim D$, 则$A \backslash C$与$B \backslash D$可能不对等.



> **证明**
>
> 例如$A=\{1,2,3\}, B=\{4,5,6\}, C=\{1,2\}, D=\{4,5\}$, 则$C \sim D$, 但$A \backslash C = \{3\}, B \backslash D = \{6\}$.
>
>
> 因此$A \backslash C$与$B \backslash D$不对等.
>
>



> **例**
>
> 设$\varphi$是集合之间的映射, 则$\varphi(A\cap B) = \varphi(A) \cap \varphi(B)$, $\varphi^{-1}(A \cap B) \subset \varphi^{-1}(A) \cap \varphi^{-1}(B)$.



> **证明**
>
> 由映射的定义, $\varphi(A\cap B) = \{y: \exists x\in A\cap B, y=\varphi(x)\} = \{y: \exists x\in A, y=\varphi(x)\} \cap \{y: \exists x\in B, y=\varphi(x)\} = \varphi(A) \cap \varphi(B)$.
>
>
> 对于第二个结论, 由$\varphi^{-1}(A \cap B) = \{x: y\in A\cap B, x=\varphi^{-1}(y)\} = \{x: y\in A, x=\varphi^{-1}(y)\} \cap \{x: y\in B, x=\varphi^{-1}(y)\} = \varphi^{-1}(A) \cap \varphi^{-1}(B)$.
>
>



> **例**
>
> 若$f$是可测集$E$上处处有限的函数, 若$\forall a\in \mathbb{R}$, $E[f = a]$均可测, 则$f$不一定是$E$上的可测函数.



> **证明**
>
> 反例可取$f=\begin{cases}
> x, x\in A\\
> -x, x\notin A
> \end{cases}$, 其中$A$为可测集$E$上的一个不可测子集.\par



> **例**
>
> 设$\{f_n\}_{n=1}^{\infty}$是$E$上的一列实函数, 令$f(x) = \inf \{f_n(x), n = 1, 2, \cdots\}$, 则对所有的$a\in \mathbb{R}$有$E[f > a] \subset \bigcap_{n=1}^{\infty}E[f_n > a]$, 但$\{f_n\}_{n=1}^{\infty}$可测时$f$也可测.



> **证明**
>
> 注意到$f>a$时一定有$f_n>a$, 但反之不一定成立.
>
>
> 对于第二部分, 事实上$f_n$的可测性和$f$的可测性是等价的.
>
>



> **例**
>
> 设集列$\{A_k\}$满足$A_k=\begin{cases}
> \left[1,2-\frac{1}{k+1}\right), k =1,3,5,\cdots\\
> \left[0,1+\frac{2}{k}\right), k=2,4,6,\cdots
> \end{cases}$, 则集列$\{A_k\}$的下限集是$\{1\}$, 上限集是$\left[0\right.,\left. 2\right)$.



> **证明**
>
> $\{A_k\}$满足$\limsup = \bigcap_{N=1}^{\infty} \bigcup_{n=N}^{\infty}A_n= \bigcap_{N=1}^{\infty} \left[0,2\right)=\left[0,2\right)$和$\liminf = \bigcup_{N=1}^{\infty} \bigcap_{n=N}^{\infty}A_n= \bigcup_{N=1}^{\infty} \{1\}=\{1\}$.
>
>





[目录与前言](../viewer.html?md=Real-Analysis-Notes)
