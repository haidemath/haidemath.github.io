## 基础集合论



### 集合的运算



> **定义**
>
> 设$A,B$是集合, 则有如下集合间运算和关系的定义:
>
>
>
> - 
>   $A\bigcup B=\{x|x\in A\text{或}x\in B\}$, 称为$A$和$B$的并集.
> - 
>   $A\bigcap B=\{x|x\in A\text{且}x\in B\}$, 称为$A$和$B$的交集.
> - 
>   $A\backslash B=\{x|x\in A\text{且}x\notin B\}$, 称为$A$和$B$的差集.
> - 
>   $A\subseteq B$表示$A$是$B$的子集, 即$\forall x\in A, x\in B$.
> - 
>   $A=B$表示$A$和$B$相等, 即$\forall x, x\in A\Leftrightarrow x\in B$.
> - 
>   若$A\subset S, B=S\backslash A$, 则称$A$是$B$的补集, 记作$A^{c}$.
>
>

针对抽象的集合, 我们有如下定义:



> **定义**
>
> 设$\varLambda $是一集合, 则称$\{A_{\lambda}\}$是一集族, 其中$\lambda\in\varLambda$.
>
>
> 特别的, 若$\varLambda=\{1,2,\cdots,n\}$, 则称$\{A_{1},A_{2},\cdots,A_{n}\}$是一集列.
>
>


集合的运算满足下面的定律:



> **定理**
>
> 设$A,B,C$是集合, 则下列命题成立:
>
>
>
> - $A\cup (B\cup C)=(A\cup B)\cup C$.
> - $A\cap (B\cap C)=(A\cap B)\cap C$.
> - $A\bigcap (\bigcup_{\lambda \in \varLambda}B_{\lambda})=\bigcup_{\lambda \in \varLambda}(A\bigcap B_{\lambda})$.
> - $A\bigcup (\bigcap_{\lambda \in \varLambda}B_{\lambda})=\bigcap_{\lambda \in \varLambda}(A\bigcup B_{\lambda})$.
> - $(\bigcap_{\lambda \in \varLambda}A_{\lambda})^{c}=\bigcup_{\lambda \in \varLambda}A_{\lambda}^{c}$.
> - $(\bigcup_{\lambda \in \varLambda}A_{\lambda})^{c}=\bigcap_{\lambda \in \varLambda}A_{\lambda}^{c}$.
>



> **证明**
>
> 证明略.


基于上面给出的集合间运算的性质, 我们作下面的特殊定义, 这些定义将会在未来某些测度论的定理中用到.



> **定义**
>
> 设$\{A_n\}$是一集列, 则称集合$\underset{N=1}{\overset{\infty}{\bigcap}}\underset{n=N}{\overset{\infty}{\bigcup}}A_n$为集列$\{A_n\}$的上限集, 记作$\limsup_{n \to \infty}A_n$.
>
>
> 设$\{A_n\}$是一集列, 则称集合$\underset{N=1}{\overset{\infty}{\bigcup}}\underset{n=N}{\overset{\infty}{\bigcap}}A_n$为集列$\{A_n\}$的下限集, 记作$\liminf_{n \to \infty}A_n$.
>
>


针对上限集和下限集, 我们有如下等价定义:



> **定理**
>
> 设$\{A_n\}$是一集列, 则有如下等价定义:
>
>
>
> - $x\in \limsup_{n \to \infty}A_n\Leftrightarrow \forall N, \exists n_0\geqslant N, x\in A_{n_0}$.
> - $x\in \liminf_{n \to \infty}A_n\Leftrightarrow \exists N, \forall n\geqslant N, x\in A_{n}$.
>


> **证明**
>
> 上面的等价定义是利用命题的存在性和任意性得到的, 这种证明方法会在后续经常用到. 通俗来讲, 即: 并集表示存在性, 交集表示任意性.
>
>


现在我们给出下面一些性质, 很好的描述了上限集和下限集在给定的集列上的关系:



> **定理**
>
> 给定$\{A_n\}$是一集列, 则下列命题成立:
>
>
>
> - $(\limsup_{n \to \infty}A_n)^{c}=\liminf_{n \to \infty}(A_n)^{c}$.
> - $(\liminf_{n \to \infty}A_n)^{c}=\limsup_{n \to \infty}(A_n)^{c}$.
> - $\bigcap_{n}^{\infty}A_n \subset \liminf_{n \to \infty}A_n\subset \liminf_{n \to \infty}(A_n)\subset \bigcup_{n}^{\infty}A_n$.
>



> **证明**
>
> 前两个命题是利用上面给出的等价定义得到的. 这两个命题实际上解释了上限集和下限集的关系.
>
>
> 对于第三个命题, 首先考虑$\liminf_{n \to \infty}A_n\subset \liminf_{n \to \infty}(A_n)\subset$: 若$x\in \liminf_{n \to \infty}A_n$, 则$\exists N, \forall n\geqslant N, x\in A_n$, 这说明$x$在无穷多个$A_n$中出现, 因此$x\in \liminf_{n \to \infty}(A_n)$.
>
>
> 再考虑$\bigcap_{n}^{\infty}A_n \subset \liminf_{n \to \infty}A_n$: 若$x\in \bigcap_{n}^{\infty}A_n$, 则$\forall n, x\in A_n$, 因此$x\in \liminf_{n \to \infty}A_n$.
>
>
> 类似地我们也有$\liminf_{n \to \infty}(A_n)\subset \bigcup_{n}^{\infty}A_n$: 若$x\in \liminf_{n \to \infty}(A_n)$, 则$\exists N, \forall n\geqslant N, x\in A_n$, 因此$x\in \bigcup_{n}^{\infty}A_n$.
>
>



> **定义**
>
> 集列$\{A_n\}$是收敛的, 当且仅当$\limsup_{n \to \infty}A_n=\liminf_{n \to \infty}A_n$. 此时记$\lim_{n \to \infty} A_n=\limsup_{n \to \infty}A_n=\liminf_{n \to \infty}A_n$为集列$\{A_n\}$的极限.
>
>



> **推论**
>
> 若递增集列$\{A_n\}$是收敛的, 则$\limsup_{n \to \infty}A_n=\liminf_{n \to \infty}A_n=\bigcup_{n}^{\infty}A_n$.
>
>
> 若递减集列$\{A_n\}$是收敛的, 则$\limsup_{n \to \infty}A_n=\liminf_{n \to \infty}A_n=\bigcap_{n}^{\infty}A_n$.
>
>


> **证明**
>
> 递增集列有$\forall n, A_n\subset A_{n+1}$, 因此$\bigcup_{n}^{\infty}A_n=\lim_{n \to \infty}A_n =\limsup_{n \to \infty}A_n=\liminf_{n \to \infty}A_n$.
>
>
> 递减集列有$\forall n, A_n\supset A_{n+1}$, 因此$\bigcap_{n}^{\infty}A_n=\lim_{n \to \infty}A_n =\limsup_{n \to \infty}A_n=\liminf_{n \to \infty}A_n$.
>
>


下面我们给出一类特殊的集合, 为了定义这种集合, 我们首先定义环和$\sigma$-代数的概念.




> **定义**
>
> 设$\mathcal{A}\subset 2^{X}$, 且满足$\forall A,B\in \mathcal{A}$, 都有$A\cup B\in \mathcal{A}$, $A\backslash B\in \mathcal{A}$, 则称$\mathcal{A}$为一个环.
>
>
> 若$\mathcal{A}$满足$\emptyset\in \mathcal{A}$, $\forall A\in \mathcal{A}$, $A^{c}\in \mathcal{A}$, $A_k \in \mathcal{A}, \bigcup_{k=1}^{+\infty}A_k\in \mathcal{A}$, 则称$\mathcal{A}$为一个$\sigma$-代数.
>
>
> $\mathbb{R}^n$中所有包含开集的$\sigma$-代数称为Borel集.
>
>




### 集合的对等



> **定义**
>
> 设$A,B$是集合, 则称$A$和$B$是对等的, 当且仅当$\exists f:A\to B$, $f$是双射. 此时记$A\sim B$表示$A$和$B$是对等的.
>
>



> **引理**
>
> 若$A\sim B$, $C \sim D$, $A\cap C=\emptyset$, $B\cap D=\emptyset$, 则$A\cup C\sim B\cup D$.
>
>



> **证明**
>
> 设$f:A\to B$是双射, $g:C\to D$是双射, 则定义映射$h:A\cup C\to B\cup D$如下:
> $$
> h(x)=
> \begin{cases}
> f(x), & x\in A\\
> g(x), & x\in C
> \end{cases}
> $$
> 显然$h$是单射, 且对于任意$y\in B\cup D$, 存在$x\in A\cup C$, 使得$h(x)=y$, 因此$h$是满射. 因此$h$是双射, 即$A\cup C\sim B\cup D$.
>
>



> **定理**
>
> 若$A\sim B$, $C \sim D$, 且这两个对等关系可以用同一个映射$\phi$来表示, $C\subset A$, $D\subset B$, 则$A\backslash C\sim B\backslash D$.
>
>



> **证明**
>
> $\forall x \in A\backslash C$, 令$f(x)=\phi(x)\in B$, 下证$f(x)\in B\backslash D$:
>
>
> 若$f(x)\in D$, 则$\exists x_0 \in C$, $f(x)= \phi(x)= \phi(x_0)$.
>
>
> 于是$A\backslash C\sim B\backslash D$.
>
>



> **命题**
>
> 对于任何映射$\phi$, 都有:
>
>
>
> - $\phi(A\cup B) = \phi(A)\cup \phi(B)$.
> - $\phi(A\cap B) \subset \phi(A)\cap \phi(B)$.
> - $\phi^{-1}(A\cup B) = \phi^{-1}(A)\cup \phi^{-1}(B)$.
> - $\phi^{-1}(A\cap B) = \phi^{-1}(A)\cap \phi^{-1}(B)$.
>



> **注**
>
> 这里不再证明上述命题, 这些命题是映射的基本性质, 其证明可以通过直接验证映射的定义来完成.
>
>


下面我们自然会想到, 这种描述集合对等的想法是否和集合本身的性质有关, 于是有下面的定理:




> **定理**
>
> (Bernstein) 若$A\sim B_0\subset B$, $B\sim A_0\subset A$, 则$A\sim B$.
>
>



> **证明**
>
> 为了证明这个事实, 我们需要利用一个引理, 说明集合在一个给定映射下的分解.
>
>
> 若有$f: X\rightarrow Y$, $g: Y\rightarrow X$, 则存在分解$X=A\cup A^{\sim}$, $Y=B\cup B^{\sim}$, 其中$f(A)= B$, $g(B^{\sim})=A^{\sim}$, $A\cap A^{\sim} = \emptyset$, $B\cap B^{\sim} = \emptyset$.
>
>
> 设$A\sim B_0\subset B$, 则存在$f: A\to B$是双射, $g: B_0\to A_0$是双射, 则定义映射$h: A\cup A^{\sim}\to B\cup B^{\sim}$如下:
>
>
> $$
> h(x)=
> \begin{cases}
> f(x), & x\in A\\
> g(x), & x\in A^{\sim}
> \end{cases}
> $$
> 显然$h$是单射, 且对于任意$y\in B\cup B^{\sim}$, 存在$x\in A\cup A^{\sim}$, 使得$h(x)=y$, 因此$h$是满射. 因此$h$是双射, 即$A\cup A^{\sim}\sim B\cup B^{\sim}$.
>
>
> 于是$A\sim B$.
>
>




### 集合的基数


在上面, 我们抽象讨论了集合的基数的一些性质, 现在为了更进一步分析不同的集合, 并且引入在Lebesgue测度中常用到的可列集, 我们首先作下面的这些定义:




> **定义**
>
> 若存在$n\in \mathbb{N}$满足$A\sim M_{n}$, 则称$A$是有限集, 其中$M_{n}=\{1,2,\cdots,n\}$. 否则称为无限集.
>
>
> 若$\mathbb{N}$满足$A\sim \mathbb{N}$, 则称$A$是可列集.
>
>



> **注**
>
> 这里的可列集是指可以和自然数集$\mathbb{N}$一一对应的集合, 也就是可以被自然数标号的集合.
>
>
> 另一方面, 在一些实分析的参考书中, 可列集也被称为可数集, 这里的定义是一致的, 因此我们统一称之为可列集.
>
>



> **定理**
>
> 任何无限集都有一个可列的真子集.
>
>



> **证明**
>
> 由题, $\exists a_1\in A$, $A\backslash \{a_1\} \ne \emptyset$. 于是$\exists a_2 \in A\backslash \{a_1\}$,  $A\backslash \{a_1,a_2\} \ne \emptyset$.
>
>
> 类似地, 我们有$\exists a_k, a_k \in A\backslash \{a_1,a_2,\cdots,a_{k-1}\}$, $A\backslash \{a_1,a_2,\cdots,a_k\} \ne \emptyset$.
>
>
> 于是可以取$A'=\{a_1,a_2,\cdots\}$, 则$A'$是$A$的一个可列的真子集.
>
>
> 真子集是由永远可以再取一个元保证的.
>
>


在讨论下面的性质之前, 我们首先需要定义集合的基数. 通俗来解释, 这就是集合的大小.




> **定义**
>
> 设$A,B$是集合, 则称$A$的基数为$|A|$, 定义如下:
>
>
>
> - 若$A\sim \mathbb{N}$, 则称$|A|=\aleph_{0}$.
> - 若$A\sim M_n$, 则称$|A|=n$.
>



> **注**
>
> 能够从定义中很自然的得到下面的一系列性质:
>
>
>
> - 若$A\sim B$, 则$|A|=|B|$.
> - 若$A\subset B$, 则$|A|\leqslant |B|$.
>



> **定理**
>
> 可列集的无限子集一定可列.
>
>



> **证明**
>
> 取$A= B_0\subset B$, $\phi: A\rightarrow A$, 于是有$|A|\leqslant |B|$.
>
>
> 设$B$可列, 于是有$|B|=\aleph_{0}$, 因此$|A|\leqslant |B|=\aleph_{0}$.
>
>
> 由于$\exists C\subset B$为无限的, 因此$|B|\geqslant |C|$, 下证$\exists D, |D|=\aleph_{0}$.
>
>
> 由于$B$是可列集, 因此可以找到一个可列的真子集$D\subset B$, 且$|D|=\aleph_{0}$.
>
>
> 于是$A$的无限子集$C$也是可列的, 即$|C|=\aleph_{0}$.
>
>
> 因此可列集的无限子集一定可列.
>
>


针对上面给出的定义, 我们再来讨论基数的运算:




> **命题**
>
>
> - 若$|A|=\aleph_{0}$, $|B|=\aleph_{0}$, 则$|A\cup B|=\aleph_{0}$.
> - 若$|A|=\aleph_{0}$, $|B|=n$, 则$|A\cup B|=\aleph_{0}$.
> - 若$|A_i|=\aleph_{0}, i =1,2,\cdots, n$, 则$|\sum_{i=1}^{n}A_i|=\aleph_{0}$.
> - 若$|A_i|=\aleph_{0}, i =1,2,\cdots$, 则$|\sum_{i=1}^{\infty}A_i|=\aleph_{0}$.
>


下面我们讨论集合的乘积, 这事实上是由一般集合构造而成的, 我们这里给出其定义, 并相应给出其运算的性质:




> **定义**
>
> 设$A,B$是集合, 则称$A\times B=\{(a,b)|a\in A, b\in B\}$为$A$和$B$的笛卡尔积, 又称为集合的乘积.
>
>



> **命题**
>
> 集合的乘积的基数具有以下性质:
>
>
>
> - 若$|A|=n$, $|B|=m$, 则$|A\times B|=nm$.
> - 若$|A|=\aleph_{0}$, $|B|=\aleph_{0}$, 则$|A\times B|=\aleph_{0}$.
> - 若$|A|=\aleph_{0}$, $|B|=n$, 则$|A\times B|=\aleph_{0}$.
> - 若$|A_i|=\aleph_{0}, i =1,2,\cdots, n$, 则$|\prod_{i=1}^{n}A_i|=\aleph_{0}$.
>



> **注**
>
> 这里的关于基数的性质和上面的性质类似, 我们都不再单独证明.
>
>


事实上下面我们会考虑在一般的微积分中讨论的区间, 区间的基数事实上很复杂, 因为我们不能利用上面给出的任何集合来表示区间, 所以我们定义如下:




> **定义**
>
> 区间$[0,1]$的基数为$\aleph_{1}$, 又记为$c$.
>
>



> **注**
>
> 事实上区间$[0,1]$的基数是$\aleph_{1}$说明了任何区间的基数都为$\aleph_{1}$, 因为任何区间都可以和$[0,1]$一一对应.
>
>



> **定理**
>
> $[0,1]$不是可列集.
>
>



> **证明**
>
> 假设$[0,1]$是可列集, 则$[0,1]\sim \{1,2,\cdots\}$, 于是$[0,1]=\{a_1,a_2,\cdots\}$.
>
>
> 下面我们说明$\exists x \in [0,1]$, 但$x\ne a_k$, $\forall k\in \mathbb{N}$.
>
>
> 令$a_1=0.a_{11}a_{12}a_{13}\cdots$, $a_2=0.a_{21}a_{22}a_{23}\cdots$, $\cdots$, $a_k=0.a_{k1}a_{k2}a_{k3}\cdots$, $\cdots$.
>
>
> 作$b=0.b_{11}b_{22}b_{33}\cdots$, 其中$a_{kk}=1$时$b_{kk}=2$, $a_{kk}\ne 1$时$b_{kk}=2$.
>
>
> 令$b=x$, 则$b\in [0,1]$, 且$b\ne a_k$, $\forall k\in \mathbb{N}$.
>
>
> 于是$[0,1]$不是可列集.
>
>


和上面的结果类似, 我们下面开始讨论基数为$\aleph_{1}$的集合的基数.




> **命题**
>
>
> - 若$|A|=\aleph_{1}$, $|B|=\aleph_{1}$, 则$|A\cup B|=\aleph_{1}$.
> - 若$|A|=\aleph_{1}$, $|B|=\aleph_{0}$, 则$|A\cup B|=\aleph_{1}$.
> - 若$|A_i|=\aleph_{1}, i =1,2,\cdots, n$, 则$|\sum_{i=1}^{n}A_i|=\aleph_{1}$.
> - 若$|A_i|=\aleph_{1}, i =1,2,\cdots$, 则$|\sum_{i=1}^{\infty}A_i|=\aleph_{1}$.
>



> **证明**
>
> 对于第一个性质, 我们只需要证明两个区间的并还是区间即可, 这是显然的.
>
>
> 对于第二个性质, 由于$|A|=\aleph_{1}$, $|B|=\aleph_{0}$, 因此对于可列集, 可以把可列的那一部分放到不可列集中, 因此$|A\cup B|=\aleph_{1}$.
>
>
> 对于第三个性质和第四个性质, 我们只需要证明$[0,1]^{n}\sim [0,1]$和$[0,1]^{\infty}\sim [0,1]$即可, 这是显然的.
>
>


上面的性质告诉我们, 实数集的基数为$\aleph_{1}$, 有理数集的基数为$\aleph_{0}$. 于是我们有下面的一系列结果.




> **推论**
>
> 以整数 (或有理数) 为系数的多项式全体可列.
>
>
> 以实数为系数的多项式全体不可列.
>
>



> **证明**
>
> 以整数 (或有理数) 为系数的多项式全体可以看作是$\mathbb{N}$的有限次笛卡尔积, 因此是可列的.
>
>
> 以实数为系数的多项式全体可以看作是$\mathbb{R}$的有限次笛卡尔积, 因此是不可列的.
>
>


更进一步, 我们还希望讨论这两种基数之间的关系, 事实上我们有:




> **定理**
>
> $2^{\aleph_{0}}=\aleph_{1}$.
>
>



> **证明**
>
> 设$A$是可列集, 则$A\sim \mathbb{N}$, 因此$|A|=\aleph_{0}$.
>
>
> 于是$2^{A}=\{f:A\to \{0,1\}\}$, $|2^{A}|=2^{\aleph_{0}}$.
>
>
> 而$2^{A}$的基数是$\aleph_{1}$, 因为$2^{A}$是不可列的.
>
>
> 因此$2^{\aleph_{0}}=\aleph_{1}$.
>
>



> **定理**
>
> (Cantor) 对于任意集合$A$, 都有$|A|<|2^{A}|$.
>
>



> **证明**
>
> 若$|A|=n$, 则$|2^{A}|=2^{n}$, 因此$|A|<|2^{A}|$.
>
>
> 若$|A|=\aleph_{0}$, 则$|2^{A}|=2^{\aleph_{0}}=\aleph_{1}$, 因此$|A|<|2^{A}|$.
>
>
> 若$|A|>\aleph_{0}$, 假设$\exists \phi: A\to 2^{A}$.
>
>
> 记$A_1=\{x:x\notin \phi(x)\}$, 则$A_1\subset 2^{A}$.
>
>
> 由于$A_1\ne \phi(x)$, $\forall x\in A$, 因此$A_1\notin \phi(A)$.
>
>
> 于是$|A|<|2^{A}|$.
>
>




### 距离空间


下面我们讨论距离和空间, 在这之前, 我们首先定义区间. 并相应得到距离的定义.




> **定义**
>
> $I=\left\{x\in (x_1,\cdot, x_n): a_i<x_i<b_i,i=1,2,\cdots,n\right\}$称为开区间.
>
>
> 对任意区间, 都有$|l|=\prod_{i=1}^{n}(b_i-a_i)$称为区间的体积.
>
>


在区间中任取两点, 都可以定义它们之间的距离, 于是我们有下面的定义:



> **定义**
>
> 设$x=(x_1,x_2,\cdots,x_n), y=(y_1,y_2,\cdots,y_n)$是$\mathbb{R}^n$中的两点, 则称$x$和$y$之间的距离为$\rho(x,y)=\left|\sum_{i=1}^{n}(x_i-y_i)^2\right|^{\frac{1}{2}}$.
>
>



> **注**
>
> 虽然上面的定义是在区间中定义的, 但事实上我们知道任何两点都可以在区间中找到, 因此上面的定义是可以推广到任意两点的, 这也就随之产生了距离的定义.
>
>
> 另一方面, 这里我们选择的是抽象的距离, 这是因为距离在更加广泛的空间中会有不同的定义, 但它们都表示两个点在对应空间中的相对“远近”.
>
>



> **命题**
>
> 对空间中任意给出的三个点$x$, $y$, $z$, 其距离满足如下性质:
>
>
>
> - (非负性) $\rho(x,y)\geqslant 0$.
> - (对称性) $\rho(x,y)=\rho(y,x)$.
> - (三角不等式) $\rho(x,y)+\rho(y,z)\geqslant \rho(x,z)$.
> - (自反性) $\rho(x,y)=0\Leftrightarrow x=y$.
>



> **证明**
>
> 这里的性质是欧氏距离的基本性质, 其证明可以通过直接验证距离的定义来完成, 因此不再证明.
>
>



> **定义**
>
> 若$m \to +\infty$时$\rho(x,x_m)\to 0$, 则称点列$\{x_m\}$收敛于点$x$, 记作$\lim_{m \to +\infty}x_m= x$.
>
>


下面给出一个关于收敛的基本定理, 事实上在一般的数学分析中适用的定理大多都可以类似得到.




> **定理**
>
> 若$x_m \to x$, $y_m \to y$, 则$m \to +\infty$时$\rho(x_m,y_m)\to \rho(x,y)$.
>
>



> **证明**
>
> 由$x_m \to x$和$y_m \to y$, 则$m \to +\infty$时$\rho(x_m,x)\to 0$和$\rho(y_m,y)\to 0$.
>
>
> 于是有$\rho(x_m,y_m)\leqslant \rho(x_m,x)+\rho(x,y)+\rho(y,y_m)\to \rho(x,y)$.
>
>
> 即$m \to +\infty$时$\rho(x_m,y_m)\to \rho(x,y)$.
>
>


类似地, 有了距离的定义之后我们就可以定义邻域, 进而得到许多特殊的集合的定义.




> **定义**
>
> 若$x_0\in \mathbb{R}^n$, $\forall \delta>0$, 称$x_0$的$\delta$-邻域为$O(x_0, \delta)=\{x\in \mathbb{R}^n: \rho(x,x_0)<\delta\}$.
>
>



> **注**
>
> 这里邻域的定义实际上表达的含义是以$x_0$为圆心, $\delta$为半径的一个开球的内部. 类似我们可以定义闭邻域, 但在实分析中很少用到.
>
>


于是更进一步, 我们有一列数列收敛的等价表述:




> **定理**
>
> $x_m \to x$当且仅当$\forall \delta >0, \exists N >0 , \forall n\geqslant N, x_n \in O(x,\delta)$.
>
>



> **证明**
>
> $x_m \to x$即当$m \to +\infty$时$\rho(x_m,x)\to 0$, 因此对于任意$\delta >0$, 都存在$N>0$, 使得当$n\geqslant N$时, $\rho(x_n,x)<\delta$.
>
>
> 于是有$x_n \in O(x,\delta)$.
>
>


下面我们定义一系列常用但有特殊性质的集合, 在这之前, 我们首先给出一个在实分析中常用定理的推广.




> **定义**
>
> 若$\exists x \in \mathbb{R}^n$, $\delta >0$, 使得$A\subset O(x,\delta)$, 则称$A$为有界集.
>
>
> 此时对于有界集$A$, 定义其直径为$\text{diam}(A)=\sup \left\{\rho(x,y): x,y\in A\right\}$.
>
>



> **定理**
>
> (Bolzano-Weierstrass) 设$A\subset \mathbb{R}^n$是有界集, 则$A$中存在一个收敛的子列.
>
>



> **证明**
>
> 设$A=\{x_m\}_{m=1}^{\infty}$, 则$\exists M>0$, $\forall m, \rho(x_m,0)<M$.
>
>
> 于是$\{x_m\}$是有界的, 因此根据一维的Bolzano-Weierstrass定理, $\{x_m\}$中存在一个收敛的子列.
>
>
> 即$A$中存在一个收敛的子列.
>
>


下面我们对一个集合进行划分, 得到下面三种点的类型:




> **定义**
>
> $E\subset \mathbb{R}^n$, $x_0 \in \mathbb{R}^n$:
>
>
>
> - 若$\exists O(x_0, \delta) \subset E$, 则$x_0$是$E$的内点.
> - 若$\exists O(x_0, \delta)$, $O(x_0,\delta)\cap E = \emptyset$, 则$x_0$是$E$的外点.
> - 若$\exists O(x_0, \delta)$, $O(x_0,\delta)\cap E \ne \emptyset$, $O(x_0,\delta)\cap E^{c} \ne \emptyset$, 则$x_0$是$E$的边界点.
>



> **命题**
>
> $E$和$E^{c}$的边界点相同.
>
>



> **证明**
>
> 设$x_0$是$E$的边界点, 则$\exists O(x_0, \delta)$, $O(x_0,\delta)\cap E \ne \emptyset$, $O(x_0,\delta)\cap E^{c} \ne \emptyset$.
>
>
> 于是$x_0$也是$E^{c}$的边界点.
>
>
> 反之, 若$x_0$是$E^{c}$的边界点, 则同理可得$x_0$也是$E$的边界点.
>
>


事实上, 我们还有类似的点的定义, 下面给出常用的一些点的定义:




> **定义**
>
> 设$E\subset \mathbb{R}^n$, 则称$x_0$为$E$的聚点, 当且仅当$\forall \delta >0$, $\exists x\in E$, $x\ne x_0$, 使得$x\in O(x_0,\delta)$.
>
>
> 称$x_0$为$E$的孤立点, 当且仅当$\exists \delta >0$, 使得$O(x_0,\delta)\cap E=\{x_0\}$.
>
>



> **注**
>
> 事实上聚点的定义还有相关等价形式, 描述的内容都是当邻域范围很小时总能找到一个在这个邻域内不同于这个点的点.
>
>


下面我们给出一些关于上面点的全体的定义, 这实际上是下面定义开集和闭集所需要的.




> **定义**
>
> $E$中边界点全体称为边界, 记为$\partial E$.
>
>
> $E$中聚点全体称为导集, 记为$E'$.
>
>
> $E\cup E'$称为闭包, 记为$\overline{E}$.
>
>



> **定理**
>
> 设$A,B\subset \mathbb{R}^n$, 则:
>
>
>
> - $A\subset B \Rightarrow A'\subset B'$.
> - $A\subset B \Rightarrow \overline{A}\subset \overline{B}$.
> - $\left(A\cup B\right)'=A'\cup B'$.
> - $\overline{A\cup B}=\overline{A}\cup \overline{B}$.
>



> **证明**
>
> 设$A,B\subset \mathbb{R}^n$, 则$A\subset B \Rightarrow A'\subset B'$是显然的, 因为$A'$是$A$的聚点全体, 而$B'$是$B$的聚点全体, 因此$A'$中的点也一定在$B'$中.
>
>
> 同理, $A\subset B \Rightarrow \overline{A}\subset \overline{B}$也是显然的.
>
>
> 对于$\left(A\cup B\right)'=A'\cup B'$, 由于$A\cup B$的聚点是$A$和$B$的聚点的并, 因此$\left(A\cup B\right)'=A'\cup B'$.
>
>
> 对于$\overline{A\cup B}=\overline{A}\cup \overline{B}$, 由于$\overline{A\cup B}= (A\cup B)\cup (A\cup B)'$, 而$(A\cup B)'= A'\cup B'$, 因此$\overline{A\cup B}=\overline{A}\cup \overline{B}$.
>
>


最后我们再给出一个定义, 用于描述集合的密集程度.




> **定义**
>
> 若$B$中任意点的任意邻域中都有$A$中的点, 则称$A$在$B$中是稠密的.
>
>
> 特别地, 若$A$在$\mathbb{R}^n$中是稠密的, 则称$A$是稠密集.
>
>
> 若不在任何集合中稠密, 则称$A$是疏朗集.
>
>



> **注**
>
> 我们通过一个例子来理解稠密性: $\mathbb{Q}$在$\mathbb{R}$中是稠密的, 因为对于任意实数$x$和任意$\delta >0$, 都可以找到一个有理数$q\in \mathbb{Q}$, 使得$q\in O(x,\delta)$.
>
>
> 类似地, 我们也有$\mathbb{Q}$在$\mathbb{R}\backslash \mathbb{Q}$中是稠密的, $\mathbb{R}\backslash \mathbb{Q}$在$\mathbb{Q}$中也是稠密的.
>
>



> **定理**
>
> $A$在$B$中稠密当且仅当$B\subset \overline{A}$.
>
>



> **证明**
>
> 设$A$在$B$中稠密, 则对于任意点$x\in B$, $\forall \delta >0$, $\exists y\in A$, 使得$y\in O(x,\delta)$.
>
>
> 于是$\forall x\in B$, $x\in \overline{A}$, 因此$B\subset \overline{A}$.
>
>
> 反之, 若$B\subset \overline{A}$, 则对于任意点$x\in B$, $\forall \delta >0$, $\exists y\in A$, 使得$y\in O(x,\delta)$.
>
>
> 因此$A$在$B$中稠密.
>
>



> **定义**
>
> 若集合$E$的每一点都为$E$的孤立点, 则$E$为孤立集.
>
>
> 若集合$E$满足$E'=\emptyset$, 则$E$为离散集.
>
>



> **注**
>
> 可以验证, 离散集一定是孤立集, 但反之未必, 例如$\mathbb{Z}$是离散集, 但不是孤立集.
>
>




### 开集、闭集及其构造


上一节我们具体讨论了利用距离来定义点的类型, 以及一些特殊的集合, 现在我们利用这些点的类型来定义开集和闭集.




> **定义**
>
> 若$E$中的全部点均为$E$的内点, 则称$E$为开集.
>
>
> 若$E$包含$E$的全部聚点, 则称$E$为闭集.
>
>



> **注**
>
> $\emptyset$和$\mathbb{R}^n$都是既为开集又为闭集, 可以通过定义来验证.
>
>



> **定理**
>
> 开集有如下等价定义:
>
>
>
> - $E$是开集当且仅当$E\cap (\partial E)=\emptyset$.
> - $E$是开集当且仅当$E^c$是闭集.
>



> **定理**
>
> 闭集有如下等价定义:
>
>
>
> - $E$是闭集当且仅当$E'\subset E$.
> - $E$是闭集当且仅当$E^c$是开集.
> - $E$是闭集当且仅当$E=\overline{E}$.
> - $E$是闭集当且仅当$\partial E\subset E$.
>



> **注**
>
> 上面的结果可以根据定义自然得到, 因此这里我们不作证明.
>
>
> 事实上, 开集和闭集的定义是相对的, 这里我们利用距离来定义开集和闭集, 但我们还可以从拓扑的角度利用连续映射来定义开集和闭集. 在对应的条件下, 我们还可以得到相对开集和相对闭集的定义.
>
>


下面我们讨论开集和闭集作运算后的性质:




> **定理**
>
> 设$A_1,A_2,\cdots A_n \subset \mathbb{R}^n$, $B_1,B_2,\cdots \subset \mathbb{R}^n$, 则:
>
>
>
> - $A_i$均为闭集时, $\bigcup_{i=1}^{n}A_i$是闭集.
> - $A_i$均为开集时, $\bigcap_{i=1}^{n}A_i$是开集.
> - $B_i$均为闭集时, $\bigcap_{i=1}^{\infty}B_i$是闭集.
> - $B_i$均为开集时, $\bigcup_{i=1}^{\infty}B_i$是开集.
>



> **证明**
>
> 我们只证明针对闭集的情形, 因为开集可以根据余集得到闭集.
>
>
> 设$A_i$均为闭集, 则$A_i=\overline{A_i}$, 因此$\bigcup_{i=1}^{n}A_i=\overline{\bigcup_{i=1}^{n}A_i}$. 于是$\bigcup_{i=1}^{n}A_i$是闭集.
>
>
> 同理, 对于$B_i$均为闭集的情形, 则$\left(\bigcap_{i=1}^{\infty}B_i\right)'\subset \left(\bigcap_{i=1}^{\infty}B_i'\right)\subset \bigcap_{i=1}^{\infty}B_i$, 因此$\bigcap_{i=1}^{\infty}B_i$是闭集.
>
>



> **注**
>
> 上述结果中$A_i$若为可列个时未必成立, 例如$\bigcup_{k=1}^{+\infty}\left[-1+\frac{1}{k},1-\frac{1}{k}\right]=(-1,1)$和$\bigcup_{k=1}^{+\infty}\left(-1-\frac{1}{k},1+\frac{1}{k}\right)=[-1,1]$.
>
>


我们发现, 开集和闭集都拥有许多优良的性质, 因此我们给这类集合一个新的定义, 这里具体的性质在可测集中有所体现.




> **定义**
>
> 若$E$可表示为一列闭集的并, 则称$E$为$F_{\sigma}$集.
>
>
> 若$E$可表示为一列开集的交, 则称$E$为$G_{\delta}$集.
>
>



> **推论**
>
> $F_{\sigma}^c$集是$G_{\delta}$集, $G_{\delta}^c$集是$F_{\sigma}$集.
>
>
> $F_{\sigma}$集和$G_{\delta}$集都是Borel集.
>
>



> **证明**
>
> 由开集和闭集的性质可得$F_{\sigma}^c$集是$G_{\delta}$集, $G_{\delta}^c$集是$F_{\sigma}$集.
>
>
> Borel集事实上是由开集和闭集通过有限次的并、交、补运算得到的集合, 因此$F_{\sigma}$集和$G_{\delta}$集都是Borel集. (可以通过验证定义得到)
>
>


下面我们考虑在一维实空间中成立的有限覆盖定理, 这里我们有更具体和一般的表述.




> **定理**
>
> 有界闭集$E\subset \mathbb{R}^n$的任意开覆盖存在有限子覆盖.
>
>



> **注**
>
> 这个定理的证明是不太显然的, 但它是实分析中一个非常重要的定理, 其证明可以通过紧性来完成, 我们会在泛函分析中更进一步讨论.
>
>


下面我们来讨论开集和闭集的构造, 在讨论一般的情形前, 我们首先讨论最特殊的区间.




> **定义**
>
> 若$(\alpha, \beta)\subset G$且$\alpha \notin G$, $\beta \notin G$, 则称$(\alpha, \beta)$为$G$的构成区间.
>
>



> **引理**
>
> 任意两个$G$的构成区间不交.
>
>



> **证明**
>
> 设$(\alpha_1, \beta_1)$和$(\alpha_2, \beta_2)$是$G$的两个构成区间, 则$\alpha_1 < \beta_1$, $\alpha_2 < \beta_2$.
>
>
> 假设$(\alpha_1, \beta_1)$和$(\alpha_2, \beta_2)$相交, 则$\alpha_1 < \alpha_2 < \beta_1$或$\alpha_2 < \alpha_1 < \beta_2$.
>
>
> 但这与$\alpha_i \notin G$和$\beta_i \notin G$矛盾.
>
>



> **注**
>
> 上面的引理说明了构成区间是不交的, 这也就说明了构成区间是唯一的, 因为任意一个开集都可以由一系列不交的构成区间来表示.
>
>



> **定理**
>
> 任意开集$G\subset \mathbb{R}$都可以表示为至多可数个不交的构成区间的并, 即$G=\bigcup_{i=1}^{\infty}(a_i,b_i)$, 其中$(a_i,b_i)$均为构成区间.
>
>



> **证明**
>
> 设$G$是开集, 则$G$中任意点都是内点, 因此对于任意点$x\in G$, $\exists \delta >0$, 使得$(x-\delta,x+\delta)\subset G$.
>
>
> 于是可以将$G$表示为所有这样的区间的并, 即$G=\bigcup_{x\in G}(x-\delta,x+\delta)$.
>
>
> 而由于构成区间是不交的, 因此可以将这些区间进行合并, 得到至多可数个不交的构成区间的并.
>
>
> 即$G=\bigcup_{i=1}^{\infty}(a_i,b_i)$, 其中$(a_i,b_i)$均为构成区间.
>
>


于是我们可以得到闭集的构造, 事实上闭集可以看作开集的补集, 因此我们有下面的结论:




> **定理**
>
> 任意闭集$F\subset \mathbb{R}$都可以表示为$\mathbb{R}$和至多可数个不交的构成区间的余集的交.
>
>



> **证明**
>
> 由闭集的余集为开集可立即得到.
>
>


下面我们再来讨论一般的$\mathbb{R}^n$中的开集和闭集的构造, 事实上我们可以将$\mathbb{R}^n$中的开集和闭集看作是$\mathbb{R}$中的开集和闭集的推广.




> **定理**
>
> 任意开集$G\subset \mathbb{R}^n$都可以表示为至多可数个开区间的并, 即$G=\bigcup_{i=1}^{\infty}I_i$, 其中$I_i$是$\mathbb{R}^n$中的开区间.
>
>



> **证明**
>
> 我们以二维空间为例, 高维空间类似可证.
>
>
> 设$G\subset \mathbb{R}^2$是开集, 则$G$中任意点都是内点, 因此对于任意点$(x,y)\in G$, $\exists \delta >0$, 使得$(x-\delta,x+\delta)\times (y-\delta,y+\delta)\subset G$.
>
>
> 于是可以将$G$表示为所有这样的开区间的并, 即$G=\bigcup_{(x,y)\in G}(x-\delta,x+\delta)\times (y-\delta,y+\delta)$.
>
>
> 而由于开区间是不交的, 因此可以将这些开区间进行合并, 得到至多可数个开区间的并.
>
>
> 即$G=\bigcup_{i=1}^{\infty}I_i$, 其中$I_i$是$\mathbb{R}^n$中的开区间.
>
>




### Cantor集


前面我们讨论了许多关于开集和闭集的性质, 现在我们来讨论一个特殊的集合, 这个集合在Lebesgue测度意义下十分重要, 因为它体现了Lebesgue测度并不能完美解决所有Riemann积分的问题.




> **定义**
>
> 考虑取$[0,1]$, 将其分为三段, 即$[0,\frac{1}{3}]$, $(\frac{1}{3},\frac{2}{3})$, $[\frac{2}{3},1]$, 然后去掉中间的$(\frac{1}{3},\frac{2}{3})$, 剩下的部分是$C_1=[0,\frac{1}{3}]\cup [\frac{2}{3},1]$.
>
>
> 然后再将$C_1$分为三段, 即$[0,\frac{1}{9}]$, $(\frac{1}{9},\frac{2}{9})$, $[\frac{2}{9},\frac{1}{3}]\cup [\frac{2}{3},\frac{7}{9}]\cup [\frac{8}{9},1]$, 然后去掉中间的$(\frac{1}{9},\frac{2}{9})\cup (\frac{2}{9},\frac{7}{9})$, 剩下的部分是$C_2=[0,\frac{1}{9}]\cup [\frac{2}{9},\frac{1}{3}]\cup [\frac{2}{3},\frac{7}{9}]\cup [\frac{8}{9},1]$.
>
>
> 以此类推, 我们可以得到一系列的集合$C_n$, 其中$C_n$是$C_{n-1}$去掉中间的部分后得到的集合.
>
>
> 最终我们定义Cantor集为$C=\bigcap_{n=1}^{\infty}C_n$, 即Cantor集是所有$C_n$的交.
>
>



> **注**
>
> 通过这种方法定义的集合还有很多种, 例如胖Cantor集, 其定义方法与Cantor集类似, 但去掉的部分不同. 这些集合在Lebesgue测度中有着重要的地位, 都是后面Lebesgue测度论中的典型反例.
>
>


下面我们进一步讨论Cantor集的性质.




> **命题**
>
> Cantor集$C$中的每个点都是聚点.
>
>



> **证明**
>
> 设$x\in C$, 则$x$是$C_n$的聚点, 因为$C_n$是由去掉中间部分后得到的集合, 而去掉的部分是开区间, 因此对于任意$\delta >0$, 都可以找到一个点在$C_n$中, 且在$x$的$\delta$邻域内.
>
>
> 由于$C=\bigcap_{n=1}^{\infty}C_n$, 因此$x$也是所有$C_n$的聚点, 即$x$是Cantor集中的聚点.
>
>



> **推论**
>
> Cantor集是闭集.
>
>



> **命题**
>
> Cantor集是疏朗集.
>
>



> **证明**
>
> 假设Cantor集是不疏朗的, 则存在$\delta >0$, 使得$C$的每个点的$\delta$邻域内都有Cantor集中的点.
>
>
> 但由于Cantor集是由去掉中间部分后得到的集合, 其中不含任何区间, 因此对于任意点$x\in C$, $\exists \varepsilon >0$, 使得$(x-\varepsilon,x+\varepsilon)\cap C=\emptyset$.
>
>
> 这与假设矛盾, 因此Cantor集是疏朗集.
>
>





[目录与前言](../viewer.html?md=Real-Analysis-Notes) · [下一章 →](../viewer.html?md=Real-Analysis-Notes-Chapter-2)
