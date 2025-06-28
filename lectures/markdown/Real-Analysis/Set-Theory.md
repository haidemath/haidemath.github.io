# 实分析-集合论基础

## 1 集合的计算

集合作为我们在分析中讨论的最基础的一种对象, 其本身就已经足够复杂, 因此我们首先讨论集合的基础计算等概念.

\begin{definition}
对于集合$A$和$B$, 我们作如下定义, 用来表示两个集合间的运算:

$A\bigcup B=\{x|x\in A\text{或}x\in B\}$, 称为$A$和$B$的并集.

$A\bigcap B=\{x|x\in A\text{且}x\in B\}$, 称为$A$和$B$的交集.

$A\backslash B=\{x|x\in A\text{且}x\notin B\}$, 称为$A$和$B$的差集.
\end{definition}

类似地, 我们可以作集合相等和包含的定义:

\begin{definition}
对于集合$A$和$B$, 我们作如下定义, 用来表示两个集合间的相等和包含关系:

$A\subseteq B$表示$A$是$B$的子集, 即$\forall x\in A, x\in B$.

$A=B$表示$A$和$B$相等, 即$\forall x, x\in A\Leftrightarrow x\in B$.

若$A\subset S, B=S\backslash A$, 则称$A$是$B$的补集, 记作$A^{c}$.
\end{definition}

例如下面这些例子:

\begin{example}
$A=B^{c}$时有$A\bigcap B = \phi$

$A=B^{c}$时有$A\backslash B= \phi$
\end{example}

而对于很多数量的集合, 我们可以做下面的定义:

\begin{definition}
设$\varLambda $是一集合, 则称$\{A_{\lambda}\}$是一集族, 其中$\lambda\in\varLambda$.

特别的, 若$\varLambda=\{1,2,\cdots,n\}$, 则称$\{A_{1},A_{2},\cdots,A_{n}\}$是一集列.
\end{definition}

事实上对于这两种集合, 我们需要作一些区分, 因为在实际应用中能够用自然数集表示的集列和一般的集族具有不同的性质.