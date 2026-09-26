[← 上一章](../viewer.html?md=Real-Analysis-Notes-Chapter-1)

## Lebesgue测度




### 外测度


在一般的微积分中, 我们会选择区间和对应的长度来衡量集合的大小, 因为我们发现这是定义和运算微积分的前提. 而对于在第一章中定义的各种不同集合, 我们也需要类似的一种方法来定义集合的大小, 这就自然考虑到下面提及的外测度和测度.




> **定义**
>
> 设$E\subset \mathbb{R}^n$, 则称$E$的外测度为
> $$
> m^{*}(E)=\inf\left\{\sum_{i=1}^{\infty}|I_i|: E\subseteq \bigcup_{i=1}^{\infty}I_i\right\},
> $$
> 其中$I_i$是$\mathbb{R}^n$中的开区间, $|I_i|$是$I_i$的体积.
>
>



> **例**
>
> 考虑两个最特殊的集合$\mathbb{R}$和$\phi$, 我们有$m^{*}(\mathbb{R})=\infty$和$m^{*}(\phi)=0$.
>
>



> **命题**
>
> 外测度具有如下性质:
>
>
>
> - (外测度非负性) $m^{*}(E)\geqslant 0$.
> - (外测度的等价定义) $m^{*}(E)=a<\infty \Leftrightarrow \forall \varepsilon >0, \exists \{I_k\}, E\subset \bigcup_{k=1}^{\infty}I_k, \sum_{k=1}^{\infty}|I_k|<a+\varepsilon$
>



> **证明**
>
> 考虑到外测度是由若干开区间的并构成的, 且开区间的体积总是非负的, 因此外测度一定非负.
>
>
> 根据下确界的定义, 如果$m^{*}(E)=\inf\left\{\sum_{i=1}^{\infty}|I_i|: E\subseteq \bigcup_{i=1}^{\infty}I_i\right\}$.
>
>
> 则$\forall \varepsilon >0$, 都存在一组开区间$\{I_k\}$, 使得$E\subset \bigcup_{k=1}^{\infty}I_k$且$\sum_{k=1}^{\infty}|I_k|<m^{*}(E)+\varepsilon$.
>
>



> **推论**
>
> $\mathbb{R}^n$中可列点集的外测度为0.
>
>



> **证明**
>
> 首先考虑$\mathbb{R}^1$上的情形, 设$E=\{r_1,r_2,\cdots\}$, 并且首先考虑$r_1$, 此时应当有$\forall \delta >0, I_{\delta} = (p-\delta,p+\delta)\supset E$.
>
>
> 于是$m^{*}(\{r_1\})=\inf\left\{\sum_{i=1}^{\infty}|I_i|: E\subseteq \bigcup_{i=1}^{\infty}I_i\right\}\leqslant |I_{\delta}|=2\delta.$
>
>
> 令$\delta \to 0$, 则$m^{*}(\{r_1\})=0$.
>
>
> 对于$r_2$, 同理有$m^{*}(\{r_2\})=0$.
>
>
> 于是对于$\{r_1,r_2,\cdots\}$, 由于$\{r_1,r_2,\cdots\}$是可列点集, 因此可以找到一组开区间$\{I_k\}$, 使得$E\subset \bigcup_{k=1}^{\infty}I_k$且$\sum_{k=1}^{\infty}|I_k|<\varepsilon$.
>
>
> 而对于$\mathbb{R}^n$上的情形, 可将其看作$\mathbb{R}^1$上的可列点集的乘积, 因此同样有$m^{*}(E)=0$.
>
>



> **命题**
>
> (外测度的单调性) 若$E\subset F$, 则$m^{*}(E)\leqslant m^{*}(F)$.
>
>



> **证明**
>
> 由外测度的定义, $\exists \{I_k\}, F\subset \bigcup_{k=1}^{\infty}I_k, \sum_{k=1}^{\infty}|I_k|<m^{*}(F)+\varepsilon$.
>
>
> 因为$E\subset F$, 所以$E\subset \bigcup_{k=1}^{\infty}I_k$, 因此$m^{*}(E)\leqslant m^{*}(F)$.
>
>



> **推论**
>
> $m^{*}((a,b))=b-a$, $m^{*}([a,b])=b-a$.
>
>



> **证明**
>
> 显然$(a,b)$和$[a,b]$都可以被开区间$(a-\varepsilon,b+\varepsilon)$所覆盖, 且其体积为$b-a+2\varepsilon$, 因此当$\varepsilon \to 0$时, 有$m^{*}((a,b))=b-a$和$m^{*}([a,b])=b-a$.
>
>



> **注**
>
> 上述结论推广至$\mathbb{R}^n$上也是成立的, 综合上面两个推论的证明即可.
>
>
> 对于区间某一端点为开的情形, 结论也是成立的, 这里只需要考虑开区间的另一端即可.
>
>



> **定理**
>
> (外测度的平移不变性) 设$E\subset \mathbb{R}^n$, $x+E=\{x+y:y\in E\}$, 则$m^{*}(E)=m^{*}(x+E)$.
>
>



> **证明**
>
> 这是很显然的, 因为对于每个满足$m^{*}(E)=\inf\left\{\sum_{i=1}^{\infty}|I_i|: E\subseteq \bigcup_{i=1}^{\infty}I_i\right\}$的开区间$I_i$, 都可以通过平移得到满足$m^{*}(x+E)=\inf\left\{\sum_{i=1}^{\infty}|J_i|: x+E\subseteq \bigcup_{i=1}^{\infty}J_i\right\}$的开区间.
>
>
> 而对于每个$I_i$和$J_i$, 都有$|I_i|=|J_i|$, 因此有$m^{*}(E)=m^{*}(x+E)$.
>
>


上面讨论了外测度的各种基本性质, 在一般微积分中我们可以自然做集合的各种运算, 其长度都是良好定义的, 因此接下来我们将讨论外测度的可加性.




> **定理**
>
> (外测度的次可加性) 设$E_1, \cdots, E_n\subset \mathbb{R}^n$, 则有$m^{*}\left(\bigcup_{k=1}^{\infty}E_k\right)\leqslant \sum_{k=1}^{\infty}m^{*}(E_k)$.
>
>



> **证明**
>
> 若$\exists E_{n_0}, m^{*}(E_{n_0})=\infty$, 则$\sum_{k=1}^{\infty}m^{*}(E_k)=\infty$, 此时显然成立.
>
>
> 若$\forall n, m^{*}(E_n)<\infty$, 则$\forall E_k$ 都有$\forall \varepsilon >0, \exists \{I_{k_j}\}, E_k\subset \bigcup_{k=1}^{\infty}I_{k_j}, m^{*}(E_k)\leqslant \sum_{j=1}^{\infty}|I_{k_j}|<m^{*}(E_k)+\frac{\varepsilon}{2^k}$.
>
>
> 于是$\sum_{k=1}^{\infty}m^{*}(E_k)+\varepsilon \geqslant m^{*}(\bigcup_{k=1}^{\infty}E_k)$. 即成立.
>
>



> **定理**
>
> (外测度的分离可加性) 设$E_1, \cdots, E_n\subset \mathbb{R}^n$, 若$\forall i,j, \rho(E_i,E_j)>0$, 则有$m^{*}\left(\bigcup_{k=1}^{\infty}E_k\right)= \sum_{k=1}^{\infty}m^{*}(E_k)$.
>
>



> **证明**
>
> 若$\forall i,j, \rho(E_i,E_j)>0$, 则总可以把每个$E_i$都拆成若干不相交的小区间, 即$E_i=\bigcup_{k=1}^{\infty}E_{i_k}$, $E_j=\bigcup_{k=1}^{\infty}E_{j_k}$且$\left(\bigcup_{k=1}^{\infty}E_{i_k}\right)\cap \left(\bigcup_{k=1}^{\infty}E_{j_k}\right) = \phi $.
>
>
> 于是对于每个$E_i$, 都可以找到恰好满足$m^{*}(E_i)=\sum_{i=1}^{\infty}m^{*}(E_{i_k})$的开区间, 使得$E_i\subset \bigcup_{k=1}^{\infty}I_{i_k}$.
>
>
> 因此有$m^{*}\left(\bigcup_{i=1}^{\infty}E_i\right)= \sum_{i=1}^{\infty}m^{*}(E_i)$.
>
>



> **注**
>
> 一般情形的集合的外测度不满足可列可加性.
>
>




### 可测集及其测度


上一节我们提到外测度的可加性是必须满足一定条件才能成立的, 因此对于更特殊的集合, 始终满足可加性的集合就说明其存在一种良好的性质. 因此这里我们就从可加性的角度来考虑集合可测性.




> **定理**
>
> 设$E$和$F$是定义在$\mathbb{R}^n$上的开区间, 若$E\cap F = \phi$, 则$m^{*}(E\cup F)= m^{*}(E)+m^{*}(F)$.
>
>



> **证明**
>
> 首先由次可加性有$m^{*}(E\cup F)\leqslant m^{*}(E)+m^{*}(F)$. 因此下面证明另一个方向的不等式.
>
>
> 考虑$E\subset \bigcup_{i=1}^{\infty}(E\cap I_i)$, 其中$I_i$是开区间, 于是有$m^{*}(E)\leqslant \sum_{i=1}^{\infty}|E\cap I_i|$.
>
>
> 对于$F$, 也有$m^{*}(F)\leqslant \sum_{i=1}^{\infty}|F\cap J_i|$.
>
>
> 由于$E\cap F = \phi$, $I_i=(I_i\cap E)\cup (I_i\cap F)\cup (I_i\backslash (E\cup F))$. 因此$|I_i|\geqslant |I_i\cap E|+|I_i\cap F|$.
>
>
> 由外测度定义可知, $\forall \varepsilon >0, \exists \{I_i\}, m^{*}(E\cup F)\leqslant \sum_{i=1}^{\infty}|I_i|\leqslant m^{*}(E\cup F)+\varepsilon$.
>
>
> 于是$m^{*}(E\cup F)+\varepsilon \geqslant \sum_{i=1}^{\infty}|I_i\cap E|+|I_i\cap F|\geqslant m^{*}(E)+m^{*}(F)$.
>
>
> 因此有$m^{*}(E\cup F)= m^{*}(E)+m^{*}(F)$.
>
>



> **注**
>
> 如果考虑集合的等价表示, 上面的定理还有另一种写法.
>
>



> **推论**
>
> 设$E$和$F$是定义在$\mathbb{R}^n$上的开区间, 若$E\cap F = \phi$, $E\cup F=I$ 则$m^{*}(E\cup F)= m^{*}(I\cap E)+m^{*}(I\cap E^c)$.
>
>



> **推论**
>
> 设$E$和$F$是定义在$\mathbb{R}^n$上的任意集合, $\exists I$是开区间, 使得$E\subset I$, $F\subset I^c$, 则$m^{*}(E\cup F)= m^{*}(E)+m^{*}(F)$.
>
>



> **证明**
>
> 类似地, 作$m^{*}(E)\leqslant \sum_{k=1}^{\infty}|I\cap I_k|$和$m^{*}(F)\leqslant \sum_{k=1}^{\infty}|I^c\cap I_k|$.
>
>
> 则由$E\cap F=\phi$, $I_k=(I_k\cap I)\cup (I_k\cap I^c)$, 此时有$|I_k|=|I_k\cap I|+|I_k\cap I^c|$.
>
>


我们发现, 上面的定理和推论都满足可加性, 这说明这些集合具有良好的性质. 而对于一般的集合, 满足这种可加性被称为Carathéodory条件, 其定义如下:




> **定义**
>
> 设$E\subset \mathbb{R}^n$, 则称$E$满足Carathéodory条件, 当且仅当$\forall T\subset \mathbb{R}^n, m^{*}(T)=m^{*}(T\cap E)+m^{*}(T\cap E^c)$.
>
>



> **注**
>
> 上面的定义说明, 满足Carathéodory条件的集合, 在任意集合上都满足可加性. 这为下面定义可测集提供了一种方式.
>
>



> **定义**
>
> 设$E\subset \mathbb{R}^n$, 则$E$是可测集当且仅当$E$满足Carathéodory条件.
>
>
> 若$E$是可测的, 则定义其测度为$m(E)=m^{*}(E)$.
>
>
> 记$\mathcal{M}$为所有可测集的集合, $\mathcal{M}$表示可测集族.
>
>



> **注**
>
> 由次可加性知, 从定义角度说明一个集合可测只需证$\forall T\subset \mathbb{R}^n, m^{*}(T)\geqslant m^{*}(T\cap E)+m^{*}(T\cap E^c)$.
>
>
> 另一方面, 可以发现测度是外测度的一个限制, 因此测度满足外测度的所有性质, 但反之未必.
>
>
> 此外, 任何集合都可以定义外测度, 但并不是所有集合都可以定义测度.
>
>


上面这种条件是针对所有集合的可测性来分析的, 下面我们给出一些定理, 说明一些特殊的集合的可测性可以通过更简单的方法得到.




> **定理**
>
> (余集的可测性) $E$可测等价于$E^c$可测.
>
>



> **证明**
>
> 由Carathéodory条件知, $\forall T\subset \mathbb{R}^n, m^{*}(T)=m^{*}(T\cap E)+m^{*}(T\cap E^c)$.
>
>
> 则有$m^{*}(T)=m^{*}(T\cap E^c)+m^{*}(T\cap E)$, 因此$E^c$满足Carathéodory条件, 即$E^c$可测. 反之亦然.
>
>



> **定理**
>
> 若$m^{*}(E)=0$, 则$E$是可测的.
>
>



> **证明**
>
> 由定义, 只需验证$\forall T\subset \mathbb{R}^n, m^{*}(T)\geqslant m^{*}(T\cap E)+m^{*}(T\cap E^c)$.
>
>
> 由$m^{*}(E)=0$, 有$m^{*}(T\cap E)\leqslant m^{*}(E)=0$.
>
>
> 再考虑$T\cap E\subset E$, $(T\cap E)\cup (T\cap E^c)=T$, 于是$m^{*}(T\cap E^c)\leqslant m^{*}(T)$.
>
>
> 因此有$m^{*}(T)\geqslant m^{*}(T\cap E)+m^{*}(T\cap E^c)$, 即$E$是可测的.
>
>



> **推论**
>
> 可列集是可测集.
>
>



> **证明**
>
> 由上面的定理, 外测度为0的集合可测. 而可列集的外测度为0, 因此可列集是可测集.
>
>



> **定理**
>
> $E$是可测集, $A\subset E$, $B\subset E^c$当且仅当$m^{*}(A\cup B)=m^{*}(A)+m^{*}(B)$.
>
>



> **证明**
>
> 由Carathéodory条件知, $\forall T\subset \mathbb{R}^n, m^{*}(T)=m^{*}(T\cap E)+m^{*}(T\cap E^c)$.
>
>
> 由$T$的任意性, 令$A=T\cap E$, $B=T\cap E^c$, 则有$m^{*}(T)=m^{*}(A)+m^{*}(B)$.
>
>
> 考虑反方向, 设$T=A\cup B$, 由$E$可测, 有$m^{*}(T)=m^{*}(A\cup B)=m^{*}(A)+m^{*}(B)$.
>
>
> 于是有$m^{*}(T\cap E)=m^{*}(A)$, $m^{*}(T\cap E^c)=m^{*}(B)$. 即说明$E$可测.
>
>


我们再进一步考虑可测集之间作运算, 是否有类似的结果. 事实上可测集之间的运算是封闭的, 其性质如下:




> **命题**
>
> (集合运算的封闭性) 设$E,F$是可测集, 则:
>
>
>
> - $E\cup F$是可测集.
> - $E\cap F$是可测集.
> - $E\backslash F$是可测集.
>



> **证明**
>
> 首先考虑$E\cup F$, 往证$\forall T\subset \mathbb{R}^n, m^{*}(T)=m^{*}(T\cap (E\cup F))+m^{*}(T\cap (E\cup F)^c)$.
>
>
> 注意到$m^{*}(T\cap (E\cup F))=m^{*}(T\cap E)+m^{*}((T\cap F)\backslash E)$, 再由$E$和$F$可测, 有$m^{*}(T)=m^{*}(T\cap E)+m^{*}(T\cap E^c)$, $m^{*}(T\cap E^c)=m^{*}(T\backslash (E\cup F))+m^{*}(T\cap (F\backslash E))$.
>
>
> 于是$\forall T\subset \mathbb{R}^n, m^{*}(T)=m^{*}(T\cap (E\cup F))+m^{*}(T\cap (E\cup F)^c)$.
>
>
> 考虑$E\cap F$, 注意到$E\cup F$已经可测, 因此取余集, $E^c$和$F^c$可测可推出$E\cap F=(E^c\cup F^c)^c$也是可测的.
>
>
> 对于$E\backslash F$, 注意到$E\backslash F=E\cap F^c$, 因此由上面的结论可知$E\backslash F$也是可测的.
>
>



> **推论**
>
> (有限并的封闭性) 设$E_1,\cdots, E_n$是两两不交的可测集, 则:
>
>
>
> - $m^{*}(T\cap (\bigcup_{i=1}^{n}E_i))=\sum_{i=1}^{n}m^{*}(T\cap E_i)$.
> - $m(\bigcup_{i=1}^{n}E_i)=\sum_{i=1}^{n}m(E_i)$.
>



> **证明**
>
> 由上面的结论, 用归纳法, $\forall T\subset \mathbb{R}^n, m^{*}(T\cap (E_1 \cup E_2))=m^{*}(T\cap E_1)+m^{*}(T\cap E_2)$. 依次作有限次可得.
>
>
> 对于一般情形, 取$T=\mathbb{R}^n$即可.
>
>



> **推论**
>
> (可列并的封闭性) 设$E_1,\cdots, E_n,\cdots $是两两不交的可测集, 则:
>
>
>
> - $m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i))=\sum_{i=1}^{\infty}m^{*}(T\cap E_i)$.
> - $m(\bigcup_{i=1}^{\infty}E_i)=\sum_{i=1}^{\infty}m(E_i)$.
>



> **证明**
>
> 考虑$\forall T\subset \mathbb{R}^n, m^{*}(T)=m^{*}(T\cap (\bigcup_{i=1}^{n}E_i))+m^{*}(T\cap (\bigcup_{i=1}^{n}E_i)^c)$.
>
>
> 注意到$m^{*}(T)=m^{*}(T\cap (\bigcup_{i=1}^{n}E_i))= \sum_{i=1}^{n}m^{*}(T\cap E_i)$, $m^{*}(T\cap (\bigcup_{i=1}^{n}E_i)^c)\geqslant m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i)^c)$.
>
>
> 于是$m^{*}(T)\geqslant \sum_{i=1}^{n}m^{*}(T\cap E_i)+m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i)^c)$.
>
>
> 令$n\to \infty$, 则有$m^{*}(T)\geqslant \sum_{i=1}^{\infty}m^{*}(T\cap E_i)+m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i)^c)\geqslant m^{*}(\bigcup_{i=1}^{\infty}(T\cap E_i))+m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i)^c) = m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i))+m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i)^c)$.
>
>
> 因此有$m^{*}(T\cap (\bigcup_{i=1}^{\infty}E_i))=\sum_{i=1}^{\infty}m^{*}(T\cap E_i)$.
>
>
> 对于一般情形, 取$T=\mathbb{R}^n$即可.
>
>


这里我们进一步讨论了无穷多个可测集的性质, 更进一步, 我们还可以讨论单调集列的可测性, 并对应得到这些集列的极限的集合的测度的计算方法.




> **定理**
>
> (下连续性) 设$\{E_n\}$是递增集列, 则$\lim_{n \to \infty}E_n$可测, 且$m(\bigcup_{n=1}^{\infty}E_n)=\lim_{n \to \infty}m(E_n)$.
>
>
> (上连续性) 设$\{E_n\}$是递减集列, 且$\exists E_{n_0}, m(E_{n_0})<\infty$, 则$\lim_{n \to \infty}E_n$可测, 且$m(\bigcap_{n=1}^{\infty}E_n)=\lim_{n \to \infty}m(E_n)$.
>
>



> **证明**
>
> 先证明下连续性, 显然递增集列有$m(\bigcup_{n=1}^{\infty}E_n)=m(\lim_{n \to \infty}E_n)$.
>
>
> 取$F_k=E_k \backslash E_{k-1}, \forall k \geqslant 2$, $F_1=E_1$, $E_0=\phi$, 则$\{F_k\}$是两两不交的可测集, 且$\bigcup_{k=1}^{\infty}F_k=\bigcup_{n=1}^{\infty}E_n$.
>
>
> 于是$m(\bigcup_{n=1}^{\infty}E_n)=m(\bigcup_{k=1}^{\infty}F_k) = \sum_{k=1}^{\infty}m(F_k)=\lim_{n \to \infty} m(\bigcup_{k=1}^{n}F_k)=\lim_{n \to \infty}m(E_n)$.
>
>
> 对于上连续性, 我们首先构造$F_{i}=E_1\backslash E_{i}$, 则当$\exists E_{n_0}, m(E_{n_0})<\infty$时有$\{F_i\}$单增可测.
>
>
> 于是由下连续性可得.
>
>



> **推论**
>
> 设$\{E_n\}$可测, 且$\sum_{i=1}^{\infty}m(E_i)<\infty$, 则$m(\limsup_{i \to \infty} E_i)=0$.
>
>



> **证明**
>
> $m(\limsup_{i \to \infty} E_i)=\lim_{k \to \infty} m(\bigcup_{i=k}^{\infty}E_i)\leqslant \sum_{i=k}^{\infty}m(E_i)$.
>
>



> **注**
>
> 这实际上是Borel- Cantelli引理, 其结果将在各种收敛关系的证明中用到.
>
>


最后我们再讨论一些特殊集合的测度.




> **命题**
>
> Cantor集的测度为0.
>
>



> **证明**
>
> Cantor集是通过不断去掉中间的三分之一部分得到的, 因此其外测度为0. 因此测度为0.
>
>




### 可测集族


在讨论了一般的可测集的性质后, 我们更进一步讨论可测集族的性质. 这是一种很自然的想法, 例如讨论定义在区间上的微积分, 我们实际上是讨论了一般区间的一些性质. 因此这里我们也从区间开始研究.




> **定理**
>
> $\mathbb{R}^n$上任意区间$I$可测, 且$m(I)=|I|$.
>
>



> **证明**
>
> 易知区间的外测度$m^{*}(I)=|I|$. 同时区间又满足测度的可加性, 因此区间可测.
>
>



> **推论**
>
> $m(\mathbb{R}^n)=\infty$.
>
>



> **证明**
>
> 由上可知, $\mathbb{R}^n$可以被任意大的区间所覆盖, 因此其测度为无穷大.
>
>


下面我们考虑更一般的可测集, 因此首先我们考虑用更一般的集合来定义外测度.




> **引理**
>
> 设$E\subset \mathbb{R}^n$, 则$m^{*}(E)=\inf\{m(G): E\subset G \}$. 其中$G$为开集.
>
>



> **证明**
>
> 由外测度的单调性, $m^{*}(E)\leqslant m^{*}(G)=m(G)$.
>
>
> 若$m^{*}(E)=\infty$, 则显然成立.
>
>
> 若$m^{*}(E)<\infty$, 则$\exists \{I_k\}, E\subset \bigcup_{k=1}^{\infty}I_k, m^{*}(E)\leqslant \sum_{k=1}^{\infty}|I_k|<m^{*}(E)+\varepsilon<\infty$.
>
>
> 此时令$G=\bigcup_{k=1}^{\infty}I_k$, 则$E\subset G$, 且$m(G)\leqslant \sum_{k=1}^{\infty}|I_k|<m^{*}(E)+\varepsilon$.
>
>
> 于是有$m^{*}(E)\leqslant m(G)$, 因此$m^{*}(E)=\inf\{m(G): E\subset G \}$.
>
>



> **引理**
>
> 开集和闭集均为可测集.
>
>



> **证明**
>
> 由上面的引理, 对于开集$G$, 有$m^{*}(G)=\inf\{m(H): G\subset H \}$, 其中$H$为开集.
>
>
> 因此$G$满足Carathéodory条件, 即$G$是可测集.
>
>
> 对于闭集$F$, 注意到$F^c$是开集, 因此由上面的引理知$m^{*}(F^c)=\inf\{m(G): F^c\subset G \}$, 其中$G$为开集.
>
>
> 因此$F^c$满足Carathéodory条件, 即$F^c$是可测集. 于是由余集的可测性知, $F$也是可测集.
>
>



> **定理**
>
> Borel集是可测集.
>
>



> **证明**
>
> Borel集是由开集和闭集通过有限次并、交、补运算得到的集合, 由于开集和闭集都是可测集, 因此由上面的结论知, Borel集也是可测集.
>
>


通过上面的讨论, 我们更进一步得到Borel集和可测集的关系, 即Borel集是可测集的一个子集. 事实上, 这是一个真子集. 接下来我们给出可测集的另外一些等价定义.




> **引理**
>
> 以下命题等价:
>
>
>
> - $E$是可测集.
> - $\forall \varepsilon>0, \exists F\subset E\subset G, m^{*}(G\backslash F)<\varepsilon $, 其中$F$为闭集, $G$为开集.
>



> **证明**
>
> 若$E$是可测集, 则$\exists F\subset E, m(E\backslash F)<\frac{\varepsilon}{2}$, 其中$F$为开集.
>
>
> 同理$\exists G^c\subset E^c, m(E^c\backslash G^c)=m(G\backslash E)<\frac{\varepsilon}{2}$, 其中$G^c$为开集.
>
>
> 于是$F\subset E\subset G$, 且$m(G\backslash F)<m(E\backslash F)+m(G\backslash E)<\varepsilon$.
>
>
> 反之, 若$\exists F\subset E\subset G, m^{*}(G\backslash F)<\varepsilon $, 其中$F$为闭集, $G$为开集. 下证$E$可测.
>
>
> 于是$\forall k>0, \exists F_k\subset E\subset G_k, m^{*}(G_k\backslash F_k)<\frac{1}{k}$. 其中$F_k$为闭集, $G_k$为开集.
>
>
> $m^{*}(E\backslash F_k)\leqslant m^{*}(G_k\backslash F_k)<\frac{1}{k}$, 因此$\lim_{k \to \infty}m^{*}(E\backslash F_k)=0$.
>
>
> 即$m^{*}(E\cap (\bigcup_{k=1}^{\infty}F_k))=0$. $E\cap (\bigcup_{k=1}^{\infty}F_k)$可测.
>
>
> 又有$\bigcup_{k=1}^{\infty}F_k$可测, 于是$E$可测.
>
>



> **定理**
>
> 以下命题等价:
>
>
>
> - $E$是可测集.
> - $\exists H\supset E, m^{*}(H\backslash E)=0$, 其中$H$为$G_{\delta}$集.
> - $\exists K\subset E, m^{*}(E\backslash K)=0$, 其中$K$为$F_{\sigma}$集.
> - $\exists K\subset E\subset H, m(H\backslash K)=0$, 其中$K$为$F_{\sigma}$集, $H$为$G_{\delta}$集.
>



> **证明**
>
> 由上面的定理, 我们已经有$E$可测当且仅当$\forall \varepsilon>0, \exists F\subset E\subset G, m^{*}(G\backslash F)<\varepsilon $, 其中$F$为闭集, $G$为开集.
>
>
> 首先考虑$E$可测推出$\exists H\supset E, m^{*}(H\backslash E)=0$, 其中$H$为$G_{\delta}$集.
>
>
> 由$E$可测, $\forall k>0, \exists F\subset E\subset G, m^{*}(G\backslash F)<\frac{1}{k} $, 其中$F$为闭集, $G$为开集.
>
>
> 于是$H=\bigcap_{k=1}^{\infty}G_k$是$G_{\delta}$集, 且$H\supset E$, $m^{*}(H\backslash E)\leqslant m^{*}(G_k\backslash F_k)<\frac{1}{k}$.
>
>
> 令$k\to \infty$, 则$m^{*}(H\backslash E)=0$. 由$H$可测知$E$可测.
>
>
> 类似地, 也可以得到$\exists K\subset E, m^{*}(E\backslash K)=0$, 其中$K$为$F_{\sigma}$集.
>
>
> 反之, 若$\exists H\supset E, m^{*}(H\backslash E)=0$, 其中$H$为$G_{\delta}$集. 下证$E$可测.
>
>
> 由$H$为$G_{\delta}$集, $\exists G_k\supset E, m^{*}(G_k\backslash E)<\frac{1}{k}$, 其中$G_k$为开集.
>
>
> 于是$E\subset G_k$, 且$m^{*}(G_k\backslash E)<\frac{1}{k}$. 令$k \to \infty$, 则$m^{*}(H\backslash E)=0$. 由$H$可测知$E$可测.
>
>
> 类似地, 也可以得到$\exists K\subset E, m^{*}(E\backslash K)=0$, 其中$K$为$F_{\sigma}$集.
>
>
> 下证$E$可测当且仅当$\exists K\subset E\subset H, m(H\backslash K)=0$, 其中$K$为$F_{\sigma}$集, $H$为$G_{\delta}$集.
>
>
> 考虑$E$可测有$\exists H\supset E, m^{*}(H\backslash E)=0$, 其中$H$为$G_{\delta}$集. $\exists K\subset E, m^{*}(E\backslash K)=0$, 其中$K$为$F_{\sigma}$集.
>
>
> 于是有$m^{*}(H\backslash K)\leqslant m^{*}(H\backslash E)+m^{*}(E\backslash K)=0+0=0$. 由$H$为$G_{\delta}$集, $K$为$F_{\sigma}$集, 则$m(H\backslash K)=0$.
>
>
> 下证反方向的命题, 设$\exists K\subset E\subset H, m(H\backslash K)=0$, 其中$K$为$F_{\sigma}$集, $H$为$G_{\delta}$集.
>
>
> 考虑$m^{*}(H\backslash E)\leqslant m^{*}(H\backslash K)=0$, $m^{*}(E\backslash K)\leqslant m^{*}(H\backslash K)=0$.
>
>
> 又有$H$为$G_{\delta}$集, $K$为$F_{\sigma}$集, 于是有$E$可测.
>
>


更进一步讨论, 我们有关于可测集族的更显然的性质.




> **定理**
>
> 可测集族构成$\sigma$-代数.
>
>



> **证明**
>
> 可测集族具有封闭性: 设$E,F$是可测集, 则$E\cup F$, $E\cap F$和$E\backslash F$都是可测集.
>
>
> 再考虑可测集族的补运算, 由余集的可测性知, 若$E$是可测集, 则$E^c$也是可测集.
>
>
> 最后考虑可测集族的可列并和交运算, 由上面的定理知, 可测集族在有限并和交下封闭. 因此在可列并和交下也封闭.
>
>
> 综上所述, 可测集族在补、并、交下封闭, 因此构成$\sigma$-代数.
>
>




### 不可测集


上面所有的讨论都是围绕可测集展开的, 下面我们考虑这样的定义方式是否会导致一些不可测集的出现. 然而在实际问题中, 我们发现尽管不可测集总是存在的, 但其总是不如可测集出现的频繁, 更进一步, 我们还需要讨论不可测集和可测集的数量的比较.




> **定理**
>
> (Vitali集) $\mathbb{R}$上存在不可测集.
>
>



> **证明**
>
> 首先考虑$\mathbb{R}$上的开区间$E=(0,1)$, 我们下面构造$A\subset E$, 使得$A$不可测.
>
>
> 对于$x,y \in E$, 若$x-y \in \mathbb{Q}$, 则称$x$和$y$是等价的.
>
>
> 下面我们将$E$上所有点进行分类, 所有有同一等价关系的点集中任取一点, 记为$A$, 则$A$是不可测的.
>
>
> 事实上, 根据可测集的推论可知, 不可测集的外测度一定大于0, 即$\exists x\in \left(A-A\right)\cap \mathbb{Q}, x\ne 0$.
>
>
> 于是$\exists y,z \in A, y-z=x, y\ne z$, 与$A$的构成矛盾.
>
>
> 因此$A$是不可测集.
>
>
> 类似地, 在$\mathbb{R}$上也可以构造类似的可测集.
>
>



> **注**
>
> 事实上这种可测集的构造是很常见的, 而且这种构造方法可以推广到$\mathbb{R}^n$上, 例如在$\mathbb{R}^2$上, 我们可以考虑所有点的笛卡尔积, 然后将其划分为等价类, 每个等价类中取一个点, 形成一个不可测集.
>
>
> 这种不可测集的构造方法被称为Vitali集, 它的存在说明Lebesgue测度并不能解决全部的不可积函数问题.
>
>


下面我们进一步讨论不可测集的性质, 以及在Lebesgue测度下不可测体现的集合的具体性质.




> **命题**
>
> 若$V$不可测, 则$\exists \varepsilon >0, A\supset V, B\supset V^c$, 使得$m(A\cap B)=\varepsilon$.
>
>



> **证明**
>
> 由Vitali集的构造知, $\exists A\supset V, B\supset V^c$, 使得$A$和$B$都是可测集.
>
>
> 由于$V$不可测, 则$m(A\cap B)=m(A)+m(B)-m(A\cup B)>0$. 因此存在$\varepsilon >0$, 使得$m(A\cap B)=\varepsilon$.
>
>



> **注**
>
> 上面的结果说明不可测集的不良性质可以表述为不可测集本身和其余集中的点无法通过一种方法分割, 这也和Carathéodory条件的想法是类似的.
>
>



> **命题**
>
> $\mathbb{R}^n$上不可测集全体的基数为$2^{\aleph_0}$.
>
>



> **证明**
>
> 由Cantor定理知, $\mathbb{R}^n$的基数为$2^{\aleph_0}$.
>
>
> 而不可测集的构造方法是通过将$\mathbb{R}^n$上的点划分为等价类, 每个等价类中取一个点, 形成一个不可测集.
>
>
> 由于$\mathbb{R}^n$上的点的个数是$2^{\aleph_0}$, 因此不可测集的个数也是$2^{\aleph_0}$.
>
>



> **注**
>
> 上面的结果说明不可测集和可测集的个数是相同的.
>
>




### 乘积测度


在讨论了可测集和不可测集的性质后, 我们进一步考虑乘积测度的问题. 乘积测度本身具有非常广泛的应用, 能够解决有限维空间中作笛卡尔积后形成的集合的测度问题.




> **定理**
>
> 设$A\subset \mathbb{R}^p, B\subset \mathbb{R}^q$是可测集, 则$A\times B$是可测集, 且$m(A\times B)=m(A)m(B)$.
>
>



> **证明**
>
> 我们首先考虑$A,B$均为区间的情形, 此时有$A=\left(\right.a_1,b_1\left.\right]\times \cdots \times \left(\right.a_p,b_p\left.\right]$, $B=\left(\right.a_{p+1},b_{p+1}\left.\right]\times \cdots \times \left(\right.a_{p+q},b_{p+q}\left.\right]$.
>
>
> 于是$A\times B=\left(\right.a_1,b_1\left.\right]\times \cdots \times \left(\right.a_p,b_p\left.\right]\times \left(\right.a_{p+1},b_{p+1}\left.\right]\times \cdots \times \left(\right.a_{p+q},b_{p+q}\left.\right]$.
>
>
> 由区间的测度可知, $m(A\times B)=|\left(a_1,b_1\right]| \cdots |\left(a_p,b_p \right]| \cdot |\left(a_{p+1},b_{p+1}\right]| \cdots |\left(a_{p+q},b_{p+q}\right]| = \prod_{i=1}^{p+q}(b_i-a_i)$.
>
>
> 下面考虑$A$和$B$均为开集, 此时有$A=\bigcup_{i=1}^{\infty}I_i$, $B=\bigcup_{j=1}^{\infty}J_j$, 其中$I_i$和$J_j$均为开区间.
>
>
> 于是$A\times B=\bigcup_{i=1}^{\infty}\bigcup_{j=1}^{\infty}(I_i\times J_j)$.
>
>
> 由于开区间的乘积仍然是开集, 因此$A\times B$是开集.
>
>
> 由开集的测度可知, $m(A\times B)=\sum_{i=1}^{\infty}\sum_{j=1}^{\infty}m(I_i\times J_j)$.
>
>
> 由于$A$和$B$均为可测集, 因此$A\times B$也是可测集.
>
>
> 由$I_i\times J_j$不交可知, $m(A\times B)=\sum_{i=1}^{\infty}\sum_{j=1}^{\infty}m(I_i)m(J_j)$.
>
>
> 因此$A\times B$也是可测集.
>
>
> 进一步, 若$A$和$B$均为有界$G_{\delta}$集, 则$A\times B$也是有界$G_{\delta}$集.
>
>
> 此时$A=\bigcap_{k=1}^{\infty}A_k$, $B=\bigcap_{l=1}^{\infty}B_l$, 其中$G_k$和$H_l$均为单减开集列.
>
>
> 考虑$\bigcap_{k=1}^{\infty}A_k \times \bigcap_{l=1}^{\infty}B_l = \bigcup_{k=1,l=1}^{\infty}(A_k \times B_l)$.
>
>
> 由$A, B$有界, $A_k, B_l$也是有界的, 考虑$m(A\times B)=m\left(\bigcap_{k=1,l=1}^{\infty}(A_k\times B_l)\right)\leqslant m\left(\bigcap_{k=1}^{\infty}(A_k\times B_k)\right)=\lim_{k \to \infty}m(A_k \times B_k)$.
>
>
> 考虑$A_k, B_l$均有界, 于是$\lim_{k \to \infty}m(A_k \times B_k)=\lim_{k \to \infty}m(A_k)\times \lim_{k \to \infty}m(B_k)=m(A)\times m(B)$.
>
>
> 另一方面, 我们有$m(A\times B)\leqslant m(\inf (A_k\times B_l))=m(A)\times m(B)$.
>
>
> 于是$m(A\times B)=m(A)\times m(B)$.
>
>
> 最后考虑$A$和$B$均为有界可测集, 此时$\exists H_A\supset A, H_B\supset B, m(H_A\backslash A)=0, m(H_B\backslash B)=0$, 其中$H_A$和$H_B$均为$G_{\delta}$集.
>
>
> 下面我们有$H_A\times H_B = (A\times B)\cup ((H_A\backslash A)\times B) \cup (A\times (H_B\backslash B)) \cup ((H_A\backslash A)\times (H_B\backslash B))$.
>
>
> 记$F=H_A\backslash A, E=H_B\backslash B$, 则$F$和$E$均为可测集.
>
>
> 由上可知$m(H_A\times H_B)=m(H_A)\times m(H_B)=m(A)\times m(B)$, $m(H_A\times H_B)=m(A)\times m(B)$.
>
>
> 因此$m(A\times B)=m(H_A\times H_B)-m(F\times B)-m(A\times E)-m(F\times E)$.
>
>
> 由于$F$和$E$均为可测集, 且$m(F\times B)=m(F)m(B)$, $m(A\times E)=m(A)m(E)$, $m(F\times E)=m(F)m(E)$.
>
>
> 于是$m(A\times B)=m(H_A\times H_B)-m(F)m(B)-m(A)m(E)-m(F)m(E)$.
>
>
> 由于$m(H_A\backslash A)=0, m(H_B\backslash B)=0$,
> 因此$m(F)=m(H_A\backslash A)=0, m(E)=m(H_B\backslash B)=0$.
>
>
> 于是$m(A\times B)=m(H_A\times H_B)-0-0-0=m(H_A\times H_B)=m(A)m(B)$. 即$m(A\times B)=m(A)m(B)$.
>
>
> 最后考虑一般的情形, 此时考虑$\mathbb{R}^{p+q}=\bigcup_{k=1}^{\infty}\left((-k,k)\times (-k,k)\right)$.
>
>
> 由于$A$和$B$均为可测集, 于是$(A\times B)\cap \mathbb{R}^{p+q}=(A\times B)\cap (\bigcup_{k=1}^{\infty} I_k)=\bigcup_{k=1}^{\infty} (A\cap I_{A_k})\times \bigcup_{k=1}^{\infty} (B\cap I_{B_k})$.
>
>
> 其中$I_k=(-k,k)\times (-k,k)$, $I_{A_k}=A\cap I_k$, $I_{B_k}=B\cap I_k$.
>
>
> 于是$\lim_{k \to \infty}m((A\times B)\cap I_k)=\lim_{k \to \infty}m(A\cap I_{A_k})\times \lim_{k \to \infty}m(B\cap I_{B_k})=m(A)\times m(B)$.
>
>


乘积测度的结果有许多明显的推论, 我们这里仅讨论最显然的一个例子.




> **推论**
>
> 设$A=\prod_{i=1}^{n}A_i$, 若$\exists A_i, m(A_i)=0$, 则$m(A)=0$.
>
>



> **证明**
>
> 由乘积测度的结果知, $m(A)=\prod_{i=1}^{n}m(A_i)$.
>
>
> 若$\exists A_i, m(A_i)=0$, 则$\prod_{i=1}^{n}m(A_i)=0$, 因此$m(A)=0$.
>
>



> **注**
>
> 上面的推论仅对有限维空间成立, 在无限维空间中, 乘积测度的性质会有所不同.
>
>




[目录与前言](../viewer.html?md=Real-Analysis-Notes) · [下一章 →](../viewer.html?md=Real-Analysis-Notes-Chapter-3)
