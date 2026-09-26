[← 上一章](../viewer.html?md=Complex-Analysis-Notes-Chapter-2)

## 复变函数的积分



### 复变函数积分的定义及计算法



#### 复积分的定义



> **定义**
>
> 设 $C$ 是平面上一条光滑或分段光滑的有向曲线段, $a,b$ 是 $C$ 的起终点, $f(z)$ 在 $C$ 上定义. 将 $C$ 从 $a$ 到 $b$ 分成 $n$ 个有向小弧段 $\widehat{z_{0}z_{1}},\cdots,\widehat{z_{n-1}z_{n}}$, 记 $\Delta z_{i}=z_{i}-z_{i-1}$, 记 $\lambda$ 为这 $n$ 个小弧段的最大直径, 任取一点 $\zeta_{i}\in\widehat{z_{i-1}z_{i}}$, 作乘积 $f(\zeta_{i})\Delta z_{i}$, 作和式 $\sum_{i=1}^{n}f(\zeta_{i})\Delta z_{i}$. 若当 $\lambda\to0$ 时, 该和式的极限存在且与分法无关, 则称此极限为 $f(z)$ 沿 $C$ 的积分, 记作 $\int_{C}f(z)\,dz$, 否则称 $f(z)$ 不可积.



> **注**
>
> (1) 复积分本质上也是 Riemann 积分, 当 $f(z)$ 在 $C$ 上有界且几乎处处连续时可积. 可积函数一定有界.
>
> (2) 若 $C$ 是闭曲线, 常记为 $\oint_{C}f(z)\,dz$.



#### 用定义计算复积分



> **例**
>
> (1) $\int_{C}dz=b-a$; (2) $\int_{C}z\,dz=\frac{1}{2}(b^{2}-a^{2})$, 这里 $a,b$ 是 $C$ 的起终点.
>
> > **证明**
> >
> > (1) $f(z)=1$ 连续, 任意分法 $\Delta z_{i}=z_{i}-z_{i-1}$, 作和 $\sum_{i=1}^{n}1\cdot\Delta z_{i}=z_{n}-z_{0}=b-a$, 令 $\lambda\to0$, $\int_{C}dz=b-a$.
> >
> > (2) $f(z)=z$ 连续, 取 $\zeta_{i}=z_{i}$ 或 $\zeta_{i}=z_{i-1}$, 则:
> > $$
> > \sum_{i=1}^{n}f(z_{i})\Delta z_{i}+\sum_{i=1}^{n}f(z_{i-1})\Delta z_{i}
> > =\sum_{i=1}^{n}(z_{i}^{2}-z_{i-1}^{2})=z_{n}^{2}-z_{0}^{2}=b^{2}-a^{2},
> > $$
> > 令 $\lambda\to0$, $\int_{C}z\,dz=\frac{1}{2}(b^{2}-a^{2})$.
>



#### 复积分的计算法



> **定理**
>
> 设 $f(z)=u(x,y)+iv(x,y)$ 在光滑或分段光滑的有向曲线 $C$ 上连续, 则
> $$
> \int_{C}f(z)\,dz=\int_{C}(u\,dx-v\,dy)+i\int_{C}(v\,dx+u\,dy).
> $$



> **证明**
>
> 任意给定分法 $\widehat{z_{i-1}z_{i}}$, $\Delta z_{i}=z_{i}-z_{i-1}$, 记 $z_{i}=x_{i}+iy_{i}$, 则 $\Delta z_{i}=\Delta x_{i}+i\Delta y_{i}$, 任取 $\zeta_{i}=\xi_{i}+i\eta_{i}\in\widehat{z_{i-1}z_{i}}$.
> 比较等式两边积分的和:
> $$
> \begin{aligned}
> \sum_{i=1}^{n}f(\zeta_{i})\Delta z_{i}
> &=\sum_{i=1}^{n}[u(\xi_{i},\eta_{i})+iv(\xi_{i},\eta_{i})]\cdot[\Delta x_{i}+i\Delta y_{i}]\\
> &=\sum_{i=1}^{n}[u(\xi_{i},\eta_{i})\Delta x_{i}-v(\xi_{i},\eta_{i})\Delta y_{i}]
> +i\sum_{i=1}^{n}[u(\xi_{i},\eta_{i})\Delta y_{i}+v(\xi_{i},\eta_{i})\Delta x_{i}].
> \end{aligned}
> $$
> 令 $\lambda\to0$ 得, $\int_{C}f(z)\,dz=\int_{C}(u\,dx-v\,dy)+i\int_{C}(u\,dy+v\,dx)$.



> **注**
>
> $\displaystyle\int_{C}f(z)\,dz\xlongequal{f(z)=u+iv,\;z=x+iy}\int_{C}(u+iv)\,d(x+iy)$.



> **定理**
>
> 设 $f(z)$ 在 $C$ 上连续, $C:z=z(t)$, $t$ 从 $\alpha$ 到 $\beta$, $z'(t)$ 连续, 则
> $$
> \int_{C}f(z)\,dz=\int_{\alpha}^{\beta}f(z(t))z'(t)\,dt.
> $$



> **证明**
>
> 记 $f(z)=u+iv$, $z(t)=x(t)+iy(t)$. 由 Thm 1,
> $$
> \begin{aligned}
> \int_{C}f(z)\,dz
> &=\int_{C}(u\,dx-v\,dy)+i\int_{C}(v\,dx+u\,dy)\\
> &=\int_{\alpha}^{\beta}[u\cdot x'(t)-v\cdot y'(t)]\,dt
> +i\int_{\alpha}^{\beta}[v\cdot x'(t)+u\cdot y'(t)]\,dt\\
> &=\int_{\alpha}^{\beta}(u+iv)\cdot[x'(t)+iy'(t)]\,dt
> =\int_{\alpha}^{\beta}f(z(t))z'(t)\,dt.
> \end{aligned}
> $$



> **注**
>
> $\displaystyle\int_{C}f(z)\,dz\stackrel{z=z(t)}{=}\int_{\alpha}^{\beta}f(z(t))z'(t)\,dt$.



> **例**
>
> 对 $n\in\mathbb Z$，计算 $\int_{C}\frac{1}{(z-a)^{n}}\,dz$, 其中 $C:|z-a|=\rho$ 取逆时针.
>
>
> 解：$C$ 的参数方程: $z=a+\rho e^{i\theta}$, $\theta$ 从 $0$ 到 $2\pi$, $dz=i\rho e^{i\theta}d\theta$.
> $$
> \int_{C}\frac{1}{(z-a)^{n}}\,dz
> =\int_{0}^{2\pi}\frac{1}{\rho^{n}e^{in\theta}}i\rho e^{i\theta}\,d\theta
> =\int_{0}^{2\pi}\frac{ie^{i(1-n)\theta}}{\rho^{n-1}}\,d\theta
> =\begin{cases}
> 2\pi i, & n=1,\\
> \dfrac{i}{\rho^{n-1}}\displaystyle\int_{0}^{2\pi}\bigl[\cos(1-n)\theta+i\sin(1-n)\theta\bigr]\,d\theta=0, & n\neq1,\ n\in\mathbb Z.
> \end{cases}
> $$


一般地, 若 $C$ 是绕 $z=a$ 的闭曲线取逆时针, 则 $\oint_{C}\frac{1}{z-a}\,dz=2\pi i$, $\oint_{C}\frac{1}{(z-a)^{n}}\,dz=0\ (n\neq1)$. 特别地, $\oint_{|z|=\rho}\frac{1}{z}\,dz=2\pi i$, $\oint_{|z|=\rho}\frac{1}{z^{2}}\,dz=0$.


> **例**
>
> 设 $C$ 是实轴上从 $z=0$ 到 $z=2\pi$ 的直线段, 计算 $\int_{C}e^{iz}\,dz$.
> $$
> \int_{C}e^{iz}\,dz=\int_{0}^{2\pi}e^{it}\,dt=\int_{0}^{2\pi}(\cos t+i\sin t)\,dt=0.
> $$



> **注**
>
> 复积分中没有积分中值定理.



#### 复积分的性质


类似第二类曲线积分.

1. $\int_{C}[f(z)\pm g(z)]\,dz=\int_{C}f(z)\,dz\pm\int_{C}g(z)\,dz$.
1. $\int_{C}k f(z)\,dz=k\int_{C}f(z)\,dz\ (k\in\mathbb{C})$.
1. $\int_{C}dz=b-a$ ($a,b$ 为 $C$ 的起点、终点).
1. 若 $C=C_{1}+C_{2}$, 则 $\int_{C}f(z)\,dz=\int_{C_{1}}f(z)\,dz+\int_{C_{2}}f(z)\,dz$.
1. 记 $C^{-}$ 与 $C$ 方向相反: $\int_{C^{-}}f(z)\,dz=-\int_{C}f(z)\,dz$.
1. 若 $|f(z)|\leq M$, $C$ 的长度为 $L$, 则 $\bigl|\int_{C}f(z)\,dz\bigr|\leq\int_{C}|f(z)|\,|dz|\leq ML$.



> **例**
>
> 计算 $\int_{C}\operatorname{Re}z\,dz$, 这里 $C$:
> (1) 从 $z=0$ 到 $z=1+i$ 的直线段;
> (2) 从 $z=0$ 沿正实轴到 $z=1$, 再沿 $x=1$ 到 $z=1+i$.
>
> (1) $C$: $z=(1+i)t$, $t$ 从 $0$ 到 $1$,
> $$
> \int_{C}\operatorname{Re}z\,dz=\int_{0}^{1}t(1+i)\,dt=\frac{1+i}{2}.
> $$
>
> (2) $C=C_{1}+C_{2}$, $C_{1}:z=t$, $t$ 从 $0$ 到 $1$; $C_{2}:z=1+it$, $t$ 从 $0$ 到 $1$,
> $$
> \int_{C}\operatorname{Re}z\,dz=\int_{C_{1}}+\int_{C_{2}}
> =\int_{0}^{1}t\,dt+\int_{0}^{1}1\cdot i\,dt=\frac{1}{2}+i.
> $$
> 可见 $\int_{C}\operatorname{Re}z\,dz$ 与路径有关, 而 $\int_{C}dz$, $\int_{C}z\,dz$ 与路径无关.
> 一般地, $\oint_{C}f(z)\,dz\stackrel{f\text{ 解析}}{=}0$.
> 事实上有 $\oint_{C}1\,dz=0$, $\oint_{C}z\,dz=0$ (例1的结果).




### 柯西积分定理


问题: $\oint_{C}f(z)\,dz\stackrel{?}{\Longleftrightarrow}f(z)$ 解析.


> **定义**
>
> 复平面上光滑或分段光滑的简单有向封闭曲线称为围线.
>
>
> 围线围成一个单连域.



> **定理**
>
> [柯西积分定理]
> 设 $f(z)$ 在单连域 $D$ 上解析, 对 $D$ 内任一条围线 $C$ 都有 $\oint_{C}f(z)\,dz=0$.



> **注**
>
> (1) 1851年前后 Cauchy、Riemann 加强条件: $f'(z)$ 连续的简单证明:
>
> 若 $f(z)$ 解析且 $f'(z)$ 连续, 则 $u_{x}=v_{y}$, $v_{x}=-u_{y}$, 且 $u_{x},v_{x},u_{y},v_{y}$ 连续. 由 Green 公式,
> $$
> \oint_{C}f(z)\,dz=\oint_{C}(u\,dx-v\,dy)+i\oint_{C}(v\,dx+u\,dy)
> =\iint_{D}(-v_{x}-u_{y})\,dxdy+i\iint_{D}(u_{x}-v_{y})\,dxdy\equiv0.
> $$
>
> (2) 1900年 Goursat 给出严格分析证法 (去掉 $f'(z)$ 连续条件):
>
> (1) $C$ 为三角形围线时 $\oint_{C}f(z)\,dz=0$. 由 $\oint dz=0$, $\oint z\,dz=0$ 及导数定义、闭区域套定理可证.
>
> (2) $C$ 为折线所围时, 将 $C$ 分成若干三角形围线 $C_{n}$, 则
> $\oint_{C}f(z)\,dz=\sum\oint_{C_{n}}f(z)\,dz=0$.
>
> (3) 逼近思想: 一致连续、导数定义. $\forall\varepsilon>0$, $\exists$ 与 $C$ 逼近的折线状围线 $C_{1}$ s.t.
> $\bigl|\oint_{C}f(z)\,dz-\oint_{C_{1}}f(z)\,dz\bigr|<\varepsilon$,
> 即 $\bigl|\oint_{C}f(z)\,dz\bigr|<\varepsilon$ ($\oint_{C_{1}}f(z)\,dz=0$), 故 $\oint_{C}f(z)\,dz=0$.



#### 推广


设 $f(z)$ 在围线 $C$ 所围区域 $D$ 内解析, 在闭区域 $\overline{D}=D+C$ 上连续, 则 $\oint_{C}f(z)\,dz=0$.

证明思路: Goursat 方法中 (3) 可证.


> **推论**
>
> 设 $f(z)$ 在单连域 $D$ 内解析, 对 $D$ 的任意封闭曲线 $C$, 都有 $\oint_{C}f(z)\,dz=0$.



> **证明**
>
> $C$ 可分成若干围线 $C_{i}$: $C=C_{1}+\cdots+C_{n}$, $\oint_{C}f=\sum_{i}\oint_{C_{i}}f=0$.



#### 复围线上的柯西积分定理



> **定义**
>
> 设 $C_{0},C_{1},\cdots,C_{n}$ 是复平面上 $n+1$ 条围线, 且 $C_{1},\cdots,C_{n}$ 全含在 $C_{0}$ 内, $C_{1},\cdots,C_{n}$ 互不相交且互不含在内部, 称复合曲线 $C=C_{0}+C_{1}^{-}+\cdots+C_{n}^{-}$ 为复围线.



> **注**
>
> 复围线围成一个有 $n$ 个「洞」的复连域.



> **定理**
>
> [Cauchy 积分定理推广]
> 设复围线 $C=C_{0}+C_{1}^{-}+\cdots+C_{n}^{-}$ ($n\geq1$) 所围区域为 $D$, $f(z)$ 在 $D$ 上解析, 在 $\overline{D}=D+C$ 上连续, 则 $\oint_{C}f(z)\,dz=0$.



> **证明**
>
> 作辅助线 $f_{0}$: 连接 $C_{0}$ 到 $C_{1}$, $f_{1}$: 连接 $C_{1}$ 到 $C_{2}$, $\cdots$, $f_{n}$: 连接 $C_{n}$ 到 $C_{0}$, 这样复连域 $D$ 可分成两个单连域 $D_{1},D_{2}$. 记 $D_{1}$ 与 $D_{2}$ 的正向边界围线为 $L_{1},L_{2}$. 由柯西积分定理, $\oint_{L_{1}}f=0$, $\oint_{L_{2}}f=0$, 故 $\oint_{C}f=\oint_{L_{1}}+\oint_{L_{2}}=0$.


于是 $\oint_{C_{0}}f(z)\,dz=\sum_{i=1}^{n}\oint_{C_{i}}f(z)\,dz$.


> **例**
>
> 设 $C$ 是内部包含 $a$ 的正向围线, $a\notin C$, 则对 $n\in\mathbb{Z}$,
> $$
> \oint_{C}\frac{dz}{(z-a)^{n}}=
> \begin{cases}
> 2\pi i, & n=1,\\
> 0, & n\neq1.
> \end{cases}
> $$
> 事实上, 在 $C$ 内以 $a$ 为圆心作小圆 $\Gamma_{\rho}$ 取逆时针, $\rho$ 很小使 $\Gamma_{\rho}$ 含在 $C$ 内部, 由复围线上的 Cauchy 积分定理,
> $$
> \oint_{C}\frac{dz}{(z-a)^{n}}=
> \oint_{\Gamma_{\rho}}\frac{dz}{(z-a)^{n}},
> $$
> 右端用参数方程 $z=a+\rho e^{i\theta}$ 即可计算.


例如,
$$
\oint_{|z-1|=\frac12}\frac{dz}{z}=0
\quad\text{（柯西积分定理）},\qquad
\oint_{|z-1|=2}\frac{dz}{z}=2\pi i
\quad\text{（例2结果）},
$$
$$
\oint_{|z-1|=\frac12}\frac{dz}{z^{2}}=0
\quad\text{（柯西积分定理）},\qquad
\oint_{|z-1|=2}\frac{dz}{z^{2}}=0
\quad\text{（例2结果）}.
$$


#### 原函数与积分与路径无关



> **定义**
>
> 设 $f(z)$ 在区域 $D$ 上连续, 若对 $D$ 内任意两点 $z_{1}$ 与 $z_{2}$ 及连接 $z_{1}$ 与 $z_{2}$ 的光滑曲线 $C_{1}$ 与 $C_{2}$, 都有 $\int_{C_{1}}f(z)\,dz=\int_{C_{2}}f(z)\,dz$, 则称复积分 $\int f(z)\,dz$ 在 $D$ 内与路径无关.
>
>
> 等价定义: $f(z)$ 在区域 $D$ 上连续, 则 $\int_{C}f(z)\,dz$ 与路径无关 $\Leftrightarrow$ 对 $D$ 内任意封闭曲线 $C$ 有 $\oint_{C}f(z)\,dz=0$.



> **定理**
>
> 设 $f(z)$ 在区域 $D$ 上连续, 且复积分 $\int f(z)\,dz$ 在 $D$ 上与路径无关. 任取定 $z_{0}\in D$, 记 $F(z)=\int_{z_{0}}^{z}f(\zeta)\,d\zeta$, 则 $F$ 在 $D$ 内解析且 $F'(z)=f(z)$.



> **证明**
>
> $\forall z\in D$, 证 $\lim_{\Delta z\to0}\frac{\Delta F(z)}{\Delta z}=f(z)$.
> $$
> \frac{\Delta F(z)}{\Delta z}
> =\frac{1}{\Delta z}\bigl(F(z+\Delta z)-F(z)\bigr)
> =\frac{1}{\Delta z}\Bigl(\int_{z_{0}}^{z+\Delta z}-\int_{z_{0}}^{z}\Bigr)
> =\frac{1}{\Delta z}\int_{z}^{z+\Delta z}f(\zeta)\,d\zeta.
> $$
> $$
> \Bigl|\frac{\Delta F(z)}{\Delta z}-f(z)\Bigr|
> =\Bigl|\frac{1}{\Delta z}\int_{z}^{z+\Delta z}f(\zeta)\,d\zeta
> -\frac{1}{\Delta z}\int_{z}^{z+\Delta z}f(z)\,d\zeta\Bigr|
> \leq\frac{1}{|\Delta z|}\int_{z}^{z+\Delta z}|f(\zeta)-f(z)|\,|d\zeta|.
> $$
> 由于 $f(z)$ 在 $z$ 连续, $\forall\varepsilon>0$, $\exists\delta>0$, 当 $|\zeta-z|<\delta$ 时 $|f(\zeta)-f(z)|<\varepsilon$.
> 当 $|\Delta z|<\delta$ 时, 取直线段积分路径, 有
> $$
> \Bigl|\frac{\Delta F(z)}{\Delta z}-f(z)\Bigr|
> \leq\frac{1}{|\Delta z|}\cdot\varepsilon\cdot|\Delta z|=\varepsilon.
> $$
> $\therefore\lim_{\Delta z\to0}\frac{\Delta F(z)}{\Delta z}=f(z)$, 即 $F'(z)=f(z)$.


于是有下面结论: 任意复积分与路径无关的连续函数都是某解析函数的导函数.


> **定义**
>
> 设 $f(z)$ 在区域 $D$ 上连续, 若存在 $D$ 上解析函数 $\Phi(z)$ 使 $\Phi'(z)=f(z)$, 则称 $\Phi(z)$ 是 $f(z)$ 的一个原函数. $\Phi(z)+C$ 是所有原函数, 称 $\int f(z)\,dz=\Phi(z)+C$ 为 $f$ 的不定积分.



> **推论**
>
> 若 $f(z)$ 在单连域 $D$ 上解析, 任取 $z_{0}\in D$, 记 $F(z)=\int_{z_{0}}^{z}f(\zeta)\,d\zeta$, 则 $F'(z)=f(z)$.



> **定理**
>
> [Newton-Leibniz 公式]
> 设 $f(z)$ 在单连域 $D$ 上解析, $\Phi(z)$ 是 $f(z)$ 的一个原函数, 则对 $D$ 内任意两点 $z_{1},z_{2}$,
> $$
> \int_{z_{1}}^{z_{2}}f(z)\,dz=\Phi(z_{2})-\Phi(z_{1}).
> $$



> **证明**
>
> 记 $F(z)=\int_{z_{0}}^{z}f(\zeta)\,d\zeta$, 则 $F(z)$ 也是 $f(z)$ 的原函数.
> 存在常数 $C$ 使 $\Phi(z)=F(z)+C$, 于是
> $$
> \int_{z_{1}}^{z_{2}}f(z)\,dz=\int_{z_{0}}^{z_{2}}f-\int_{z_{0}}^{z_{1}}f=F(z_{2})-F(z_{1})=\Phi(z_{2})-\Phi(z_{1}).
> $$



> **例**
>
> (1) $\int_{0}^{i}z^{5}\,dz=\frac{z^{6}}{6}\big|_{0}^{i}=-\frac{1}{6}$.
>
> (2) $\int_{0}^{i}\sin z\,dz=-\cos z\big|_{0}^{i}=1-\cos i=1-\frac{1+e^{2}}{2e}$.
>
> (3) 若取 $\sqrt{z}$ 的主值分支, 则 $\oint_{|z-1|=\frac{1}{2}}\sqrt{z}\,dz=0$ (被积函数在该圆及其内部解析).
>
> (4) $\oint_{|z|=\frac{1}{2}}\ln(1+z)\,dz=0$, 但 $\oint_{|z|=1}\ln(1+z)\,dz$ 无意义 (在 $z=-1$ 处无极限).




### 柯西积分公式及推广



#### 柯西积分公式



> **定理**
>
> 设 $f(z)$ 在围线 (或复围线) $C$ 所围区域
> $D$ 上解析, 在 $\overline{D}=D+C$ 上连续, 则对 $D$ 内任一点 $z$ 都有
> $$
> f(z)=\frac{1}{2\pi i}\oint_{C}\frac{f(\zeta)}{\zeta-z}\,d\zeta.
> $$



> **证明**
>
> 记 $F(s)=\dfrac{1}{2\pi i}\dfrac{f(s)}{s-z}$. 对任意固定的 $z\in D$, $F(s)$ 在 $s\in D$ 上除 $z$ 外都解析.
> 以 $z$ 为圆心作 $\Gamma_{\rho}$ 取逆时针且 $\Gamma_{\rho}$ 含在 $C$ 内, 记 $L=C+\Gamma_{\rho}^{-}$.
> 由复围线上的柯西积分定理, $\oint_{L}F(s)\,ds=0$, 即
> $$
> \frac{1}{2\pi i}\oint_{C}\frac{f(s)}{s-z}\,ds=\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(s)}{s-z}\,ds.
> $$
> $f(s)$ 在 $z$ 连续, $\forall\varepsilon>0$, $\exists\delta>0$, 当 $|s-z|<\delta$ 时 $|f(s)-f(z)|<\varepsilon$.
> 当 $\rho<\delta$ 时,
> $$
> \Bigl|f(z)-\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(s)}{s-z}\,ds\Bigr|
> =\frac{1}{2\pi}\Bigl|\oint_{\Gamma_{\rho}}\frac{f(z)-f(s)}{s-z}\,ds\Bigr|
> \leq\frac{1}{2\pi}\cdot\frac{\varepsilon}{\rho}\cdot 2\pi\rho=\varepsilon.
> $$
> 即 $f(z)=\dfrac{1}{2\pi i}\oint_{C}\dfrac{f(s)}{s-z}\,ds$.



#### 柯西积分公式的推广——高阶导数公式



> **定理**
>
> 设 $C$ 为正向围线，$f(z)$ 在 $C$ 所围区域 $D$ 上解析, 在
> $\overline{D}=D+C$ 上连续, 则 $f(z)$ 在 $D$ 内有任意阶导数:
> $$
> f^{(n)}(z)=\frac{n!}{2\pi i}\oint_{C}\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,d\zeta,\quad n=1,2,\cdots
> $$



> **证明**
>
> 对 $n$ 用数学归纳法. $n=1$ 时:
> $$
> \frac{f(z+\Delta z)-f(z)}{\Delta z}
> =\frac{1}{2\pi i\Delta z}\oint_{C}f(\zeta)\Bigl[\frac{1}{\zeta-z-\Delta z}-\frac{1}{\zeta-z}\Bigr]\,d\zeta
> =\frac{1}{2\pi i}\oint_{C}\frac{f(\zeta)}{(\zeta-z-\Delta z)(\zeta-z)}\,d\zeta.
> $$
> 令 $\Delta z\to0$, 由被积函数的一致收敛性, $f'(z)=\frac{1}{2\pi i}\oint_{C}\frac{f(\zeta)}{(\zeta-z)^{2}}\,d\zeta$.
>
> 假设 $n-1$ 时公式成立, 下证 $n$ 时成立:
> $$
> \begin{aligned}
> \frac{f^{(n-1)}(z+\Delta z)-f^{(n-1)}(z)}{\Delta z}
> &=\frac{(n-1)!}{2\pi i\Delta z}\oint_{C}f(\zeta)
> \Bigl[\frac{1}{(\zeta-z-\Delta z)^{n}}-\frac{1}{(\zeta-z)^{n}}\Bigr]\,d\zeta\\
> &=\frac{(n-1)!}{2\pi i\Delta z}\oint_{C}f(\zeta)
> \frac{\bigl[C_{n}^{1}(\zeta-z)^{n-1}\Delta z-\cdots+(-1)^{n+1}(\Delta z)^{n}\bigr]}
> {(\zeta-z-\Delta z)^{n}(\zeta-z)^{n}}\,d\zeta\\
> &=\frac{(n-1)!}{2\pi i}\oint_{C}f(\zeta)
> \frac{C_{n}^{1}(\zeta-z)^{n-1}+\cdots+(-1)^{n+1}(\Delta z)^{n-1}}
> {(\zeta-z-\Delta z)^{n}(\zeta-z)^{n}}\,d\zeta.
> \end{aligned}
> $$
> 于是
> $$
> \Biggl|\frac{n!}{2\pi i}\oint_{C}\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,d\zeta
> -\frac{f^{(n-1)}(z+\Delta z)-f^{(n-1)}(z)}{\Delta z}\Biggr|
> =\frac{n!}{2\pi}\Biggl|\oint_{C}\frac{f(\zeta)\,h(\zeta)\,\Delta z}{(\zeta-z-\Delta z)^{n}(\zeta-z)^{n+1}}\,d\zeta\Biggr|,
> $$
> 其中 $h(\zeta)$ 为由二项式差得到的连续函数.
> 记 $z$ 到 $C$ 的最短距离为 $d$, 当 $|\Delta z|<\frac{d}{2}$ 时,
> $|\zeta-z-\Delta z|\geq\frac{d}{2}$, $|\zeta-z|\geq d$.
> 由 $f(\zeta),h(\zeta)$ 在 $C$ 上连续有界, 记 $|f(\zeta)h(\zeta)|\leq M$,
> 再记 $C$ 的弧长为 $L$, 则上式
> $$
> \leq\frac{n!}{2\pi}|\Delta z|\cdot\frac{M}{\bigl(\frac{d}{2}\bigr)^{n}d^{n+1}}\cdot L.
> $$
> 令 $\Delta z\to0$, 得 $f^{(n)}(z)=\frac{n!}{2\pi i}\oint_{C}\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,d\zeta$.



> **推论**
>
> 若 $f(z)$ 在区域 $D$ 上解析, 则 $f(z)$ 在 $D$ 上有任意阶导数, 即解析函数的导数还是解析函数.



> **证明**
>
> 对 $D$ 内任一点 $z$, 在 $z$ 的某邻域内作小圆 $\Gamma_{\rho}$ 取逆时针, 由柯西积分公式, $f^{(n)}(z)$ 存在 ($n=0,1,\cdots$), 且
> $$
> f^{(n)}(z)=\frac{n!}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,d\zeta.
> $$
> 由 $z$ 的任意性知 $f^{(n)}(z)$ 在 $D$ 上解析.



#### 解析的充要条件



> **定理**
>
> $f(z)=u+iv$ 在区域 $D$ 内解析 $\Leftrightarrow$ $u,v$ 在 $D$ 上有连续偏导数且满足 C-R 条件 $\Leftrightarrow$ $u,v$ 可微且满足 C-R 条件.



> **证明**
>
> 由解析充要条件可知 $\Leftarrow$ 成立.
> 若 $f(z)$ 解析, 则 $f'(z)=u_{x}+iv_{x}=v_{y}-iu_{y}$ 也解析, 故 $u,v$ 有连续偏导数.



#### 平均值定理、柯西不等式与 Liouville 定理



> **定理**
>
> [平均值定理]
> 设 $f(z)$ 在圆域 $D:|z-z_{0}|<R$ 上解析, 在 $\overline{D}$ 上连续. 记 $\Gamma_{\rho}:|z-z_{0}|=\rho$ ($0<\rho\leq R$) 取逆时针方向, 则
> $$
> f(z_{0})=\frac{1}{2\pi}\int_{0}^{2\pi}f(z_{0}+\rho e^{i\theta})\,d\theta.
> $$



> **证明**
>
> 由柯西积分公式,
> $$
> f(z_{0})=\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(z)}{z-z_{0}}\,dz.
> $$
> 令 $z=z_{0}+\rho e^{i\theta}$, $dz=i\rho e^{i\theta}\,d\theta$, 即得
> $$
> f(z_{0})=\frac{1}{2\pi i}\int_{0}^{2\pi}\frac{f(z_{0}+\rho e^{i\theta})}{\rho e^{i\theta}}i\rho e^{i\theta}\,d\theta
> =\frac{1}{2\pi}\int_{0}^{2\pi}f(z_{0}+\rho e^{i\theta})\,d\theta.
> $$



> **定理**
>
> [柯西不等式]
> 设 $f(z)$ 在 $|z-z_{0}|<R$ 上解析, 且 $|f(z)|\leq M(\rho)$ 对 $|z-z_{0}|=\rho<R$ 成立, 则
> $$
> |f^{(n)}(z_{0})|\leq\frac{n!\,M(\rho)}{\rho^{n}}.
> $$



> **证明**
>
> 由高阶导数公式,
> $$
> f^{(n)}(z_{0})=\frac{n!}{2\pi i}\oint_{|z-z_{0}|=\rho}\frac{f(z)}{(z-z_{0})^{n+1}}\,dz.
> $$
> 因此
> $$
> |f^{(n)}(z_{0})|\leq\frac{n!}{2\pi}\cdot\frac{M(\rho)}{\rho^{n+1}}\cdot 2\pi\rho
> =\frac{n!\,M(\rho)}{\rho^{n}}.
> $$



> **定义**
>
> 在全平面上解析的函数称为整函数. 例如, $f(z)=z^{n}$, $f(z)=a_{n}z^{n}+\cdots+a_{0}$.



> **定理**
>
> [Liouville 定理]
> 有界整函数必为常数.



> **证明**
>
> $\forall z\in\mathbb{C}$, 以 $z$ 为圆心作圆 $\Gamma_{\rho}:|\zeta-z|=\rho$ 取逆时针.
> 由柯西积分公式,
> $$
> f'(z)=\frac{1}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(\zeta)}{(\zeta-z)^{2}}\,d\zeta.
> $$
> 当 $|f|$ 有界时, 记 $|f(z)|\leq M$. 由柯西不等式, $|f'(z)|\leq\frac{M}{\rho}$.
> 令 $\rho\to+\infty$, 得 $|f'(z)|\leq0$, 即 $f'(z)=0$. 由 $z$ 任意, $f'(z)\equiv0$, 故 $f$ 为常值函数.



> **例**
>
> 证明 $n$ 次多项式方程在 $\mathbb{C}$ 上有 $n$ 个根 ($n\geq1$).



> **证明**
>
> 若 $P_{n}(z)$ 无零点, 则 $F(z)=\frac{1}{P_{n}(z)}$ 为整函数. 又 $P_{n}(z)\to\infty$ ($z\to\infty$), 故 $F(z)\to0$ ($z\to\infty$), 从而 $F$ 有界. 由 Liouville 定理 $F$ 为常数, 矛盾. 故至少有一个根. 因式分解后对次数归纳, 恰有 $n$ 个根.



> **定理**
>
> [Morera 定理]
> 设 $f(z)$ 在区域 $D$ 上连续, 且对 $D$ 内任意闭曲线 $C$, 都有 $\oint_{C}f(z)\,dz=0$, 则 $f(z)$ 在 $D$ 内解析.



> **证明**
>
> 由条件知 $\int f(z)\,dz$ 在 $D$ 内与路径无关. 取定 $z_{0}\in D$, 定义
> $$
> F(z)=\int_{z_{0}}^{z}f(s)\,ds.
> $$
> 由原函数存在定理, $F'(z)=f(z)$, 故 $F$ 在 $D$ 内解析. 解析函数的导数仍解析, 所以 $f(z)=F'(z)$ 在 $D$ 内解析.



> **定理**
>
> $f(z)$ 在单连域 $D$ 上解析 $\Leftrightarrow$ $f(z)$ 在 $D$ 上连续且对 $D$ 内任意围线 $C$ 都有 $\oint_{C}f(z)\,dz=0$.



> **证明**
>
> $\Rightarrow$ 由柯西积分定理. $\Leftarrow$ 由 Morera 定理.



#### 柯西积分公式应用举例


柯西积分公式: $f^{(n)}(z_{0})=\frac{n!}{2\pi i}\oint_{C}\frac{f(z)}{(z-z_{0})^{n+1}}\,dz$
$\Leftrightarrow\oint_{C}\frac{f(z)}{(z-z_{0})^{n+1}}\,dz=\frac{2\pi i}{n!}f^{(n)}(z_{0})$.


> **例**
>
> 计算下列积分:
> $$
> \begin{array}{l}
> (1)\ \displaystyle\oint_{|z|=1}\frac{\cos z}{z^{3}}\,dz
> =\frac{2\pi i}{2!}(\cos z)''\big|_{z=0}=-\pi i,\\[4pt]
> \displaystyle\oint_{|z|=1}\frac{e^{z}}{z^{5}}\,dz
> =\frac{2\pi i}{4!}(e^{z})^{(4)}\big|_{z=0}=\frac{\pi i}{12}.\\[8pt]
> (2)\ \displaystyle\oint_{|z|=2}\frac{\sin z}{(z-1)^{3}}\,dz
> =\frac{2\pi i}{2!}(\sin z)''\big|_{z=1}=-\pi i\sin 1.\\[8pt]
> (3)\ \displaystyle\oint_{|z-1|=1}\frac{\sin z}{z^{2}-1}\,dz
> =\oint_{|z-1|=1}\frac{\frac{\sin z}{z+1}}{z-1}\,dz
> =2\pi i\cdot\frac{\sin z}{z+1}\Big|_{z=1}=\pi i\sin 1.\\[8pt]
> (4)\ \displaystyle\oint_{|z|=2}\frac{\sin z}{z^{2}-1}\,dz
> =\frac{1}{2}\oint_{|z|=2}\frac{\sin z}{z-1}\,dz
> -\frac{1}{2}\oint_{|z|=2}\frac{\sin z}{z+1}\,dz
> =2\pi i\sin 1.
> \end{array}
> $$




### 习题课



#### 重要定理总结



1. Cauchy 积分定理: $f(z)$ 在围线或复围线 $C$ 所围区域 $D$ 上解析, 在 $\overline{D}$ 上连续, 则 $\oint_{C}f(z)\,dz=0$.
  推论: $f(z)$ 在单连域 $D$ 上解析, 对 $D$ 内任意围线 $C$ 有 $\oint_{C}f(z)\,dz=0$.
1. 原函数存在定理: $f(z)$ 在 $D$ 上连续, 且复曲线积分在 $D$ 内与路径无关, 则一定存在原函数 $F(z)$ 使得 $F'(z)=f(z)$. 这里 $F(z)=\int_{z_{0}}^{z}f(\zeta)\,d\zeta+C$.
1. Cauchy 积分公式及高阶导数公式:
  $$
  f^{(n)}(z)=\frac{n!}{2\pi i}\oint_C\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,d\zeta,
  \quad n=0,1,2,\ldots
  $$
  推论: 解析函数的任意阶导数都存在; 解析函数由边界值决定.
1. Morera 定理 (解析的充要条件): $f(z)$ 在单连域 $D$ 上解析 $\Leftrightarrow$ $f(z)$ 在 $D$ 上连续且对 $D$ 内任意围线 $C$ 都有 $\oint_{C}f(z)\,dz=0$.
1. 柯西不等式: $|f^{(n)}(z_{0})|\leq n!M(\rho)/\rho^{n}$.
  这里 $M=\max_{z\in D}|f(z)|$, 也有 $|f^{(n)}(z_{0})|\leq n!M/\rho^{n}$.
1. 平均值定理: $f(z_{0})=\frac{1}{2\pi}\int_{0}^{2\pi}f(z_{0}+\rho e^{i\theta})\,d\theta$.
1. Liouville 定理: 有界整函数必为常数.



#### 综合练习



> **例**
>
> 设 $f(z)=u+iv$ 是整函数, 且满足 $u\leq M$, 则 $f(z)$ 是常数.
>
>
>
> > **证明**
> >
> > 记 $F(z)=e^{f(z)}$, 则 $F(z)$ 也是整函数, 且 $|F(z)|=e^{u}\leq e^{M}$. 由 Liouville 定理, $F(z)$ 为常数, 故 $f(z)$ 为常数.
>
> 同理满足 $u\geq M$ ($v\leq M$ 或 $v\geq M$) 也有 $f(z)$ 是常数.



> **例**
>
> 设 $f(z)$ 是整函数, 且满足 $\lim_{z\to\infty}\frac{f(z)}{z^{n}}=0$, 则 $f(z)$ 是至多 $n-1$ 次多项式函数.
>
> > **证明**
> >
> > $f(z)$ 是至多 $n-1$ 次多项式函数 $\Leftrightarrow f^{(n)}(z)\equiv0$.
> >
> > 由 $\lim_{z\to\infty}\frac{f(z)}{z^{n}}=0$, $\forall\varepsilon>0$, $\exists R$ s.t. $|z|>R$ 时 $\bigl|\frac{f(z)}{z^{n}}\bigr|<\varepsilon\cdot\frac{1}{2\cdot n!}$.
> >
> > 记 $\Gamma_{\rho}:|z|=\rho$ 且 $\Gamma_{\rho}$ 内含 $z_{0}$, 由 Cauchy 积分公式,
> > $$
> > f^{(n)}(z_{0})=\frac{n!}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(\xi)}{(\xi-z_{0})^{n+1}}\,d\xi
> > =\frac{n!}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(\xi)}{\xi^{n}}\cdot\frac{\xi^{n}}{(\xi-z_{0})^{n+1}}\,d\xi,\quad\forall z_{0}.
> > $$
> > $$
> > |f^{(n)}(z_{0})|\leq\frac{n!}{2\pi}\cdot\varepsilon\cdot\frac{\rho^{n}}{(\rho-|z_{0}|)^{n+1}}\cdot2\pi\rho\cdot\frac{1}{2\cdot n!}
> > =\frac{1}{2}\Bigl(\frac{\rho}{\rho-|z_{0}|}\Bigr)^{n+1}\cdot\varepsilon.
> > $$
> > 又 $\lim_{\rho\to+\infty}\bigl(\frac{\rho}{\rho-|z_{0}|}\bigr)^{n+1}=1$, $\exists R_{1}>R$ s.t. $\rho>R_{1}$ 时 $\bigl(\frac{\rho}{\rho-|z_{0}|}\bigr)^{n+1}<2$.
> >
> > 综上, 当 $\rho>R_{1}$ 时 $|f^{(n)}(z_{0})|<\varepsilon$. 由 $\varepsilon$ 任意性, $f^{(n)}(z_{0})=0$, 由 $z_{0}$ 任意性, $f^{(n)}(z)\equiv0$.
>



> **例**
>
> 证明: $I_{1}=\int_{0}^{2\pi}e^{\cos\theta}\cos(\sin\theta)\,d\theta=2\pi$, $I_{2}=\int_{0}^{2\pi}e^{\cos\theta}\sin(\sin\theta)\,d\theta=0$.
>
>
>
> > **证明**
> >
> > $$
> > I_{1}+iI_{2}=\int_{0}^{2\pi}e^{\cos\theta}(\cos(\sin\theta)+i\sin(\sin\theta))\,d\theta
> > =\int_{0}^{2\pi}e^{\cos\theta}e^{i\sin\theta}\,d\theta
> > =\int_{0}^{2\pi}e^{e^{i\theta}}\,d\theta.
> > $$
> > 令 $z=e^{i\theta}$, 则 $d\theta=\frac{dz}{iz}$,
> > $$
> > I_{1}+iI_{2}=\oint_{|z|=1}\frac{e^{z}}{iz}\,dz
> > =\frac{1}{i}\cdot2\pi i\cdot e^{0}=2\pi.
> > $$
> > 故 $I_{1}=2\pi$, $I_{2}=0$.
>



> **例**
>
> 设 $f(z)$ 在 $D:|z|<1$ 上解析, 且满足 $|f(z)|\leq\frac{1}{1-|z|}$, 则对任意 $n\in\mathbb N^{+}$,
> $|f^{(n)}(0)|\leq(n+1)!\,e$.
>
> > **证明**
> >
> > 记 $\Gamma_{\rho}:|z|=\frac{n}{n+1}$. 由 Cauchy 积分公式,
> > $$
> > f^{(n)}(0)=\frac{n!}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(z)}{z^{n+1}}\,dz.
> > $$
> > 于是
> > $$
> > |f^{(n)}(0)|\leq\frac{n!}{2\pi}\cdot
> > \frac{n+1}{\bigl(\frac{n}{n+1}\bigr)^{n+1}}\cdot2\pi\cdot\frac{n}{n+1}
> > =(n+1)!\cdot\Bigl(\frac{n+1}{n}\Bigr)^{n}<(n+1)!\,e.
> > $$
>



> **例**
>
> 设 $f(z)$ 在 $|z|\leq R$ 上解析, 记
> $M=\max_{|z|=R}|f(z)|$, 则在 $|z|\leq R$ 上 $|f(z)|\leq M$.
>
> > **证明**
> >
> > 对幂函数 $[f(z)]^{n}$ 应用 Cauchy 积分公式, 记 $\Gamma_{R}:|z|=R$.
> > 对任意 $|z|<R$,
> > $$
> > [f(z)]^{n}=\frac{1}{2\pi i}\oint_{\Gamma_{R}}\frac{[f(\xi)]^{n}}{\xi-z}\,d\xi.
> > $$
> > $|f(z)|^{n}\leq M^{n}\frac{R}{d}$, 其中 $d=R-|z|>0$.
> > 于是 $\frac{|f(z)|}{M}\leq\bigl(\frac{R}{d}\bigr)^{1/n}\to1\ (n\to\infty)$, 即 $|f(z)|\leq M$.
>
>
> > **注**
> >
> > 不要求 $D$ 为圆域 (可以为围线所围区域).
>



> **例**
>
> 设 $C$ 是正向简单围线，$z_0$ 在 $C$ 内，$f$ 在 $C$ 及其内部除
> $z_{0}$ 外解析，且 $\lim_{z\to z_{0}}(z-z_{0})f(z)=A$，则
> $\oint_{C}f(z)\,dz=2\pi iA$.
>
> > **证明**
> >
> > $\forall\varepsilon>0$, $\exists\delta>0$, 当 $0<|z-z_{0}|<\delta$ 时 $|(z-z_{0})f(z)-A|<\varepsilon$.
> > 取 $\Gamma_{\rho}:|z-z_{0}|=\rho$, $\rho$ 很小使 $\Gamma_{\rho}$ 含在 $C$ 内.
> > 由复围线的 Cauchy 积分定理, $\oint_{C+\Gamma_{\rho}^{-1}}f(z)\,dz=0\Rightarrow\oint_{C}f(z)\,dz=\oint_{\Gamma_{\rho}}f(z)\,dz=\lim_{\rho\to0}\oint_{\Gamma_{\rho}}f(z)\,dz$.
> > 当 $\rho<\delta$ 时有
> > $$
> > \Bigl|\oint_{\Gamma_{\rho}}f(z)\,dz-2\pi iA\Bigr|
> > =\Bigl|\oint_{\Gamma_{\rho}}\frac{(z-z_{0})f(z)-A}{z-z_{0}}\,dz\Bigr|
> > \leq\frac{\varepsilon}{\rho}\cdot2\pi\rho=2\pi\varepsilon.
> > $$
> > 特别地, 若 $A=0$, 则对绕 $z_{0}$ 的曲线 $C$ 有 $\oint_{C}f(z)\,dz=0$.
>



> **例**
>
> 设 $f(z)$ 在 $|z|>R$ 上解析, 且 $\lim_{z\to\infty}zf(z)=A$, 则对
> $|z|>R$ 中任意正向简单围线 $C$，若 $C$ 的内部包含闭圆盘
> $|z|\leq R$，都有 $\oint_{C}f(z)\,dz=2\pi iA$.
>
> > **证明**
> >
> > 记 $\Gamma_{\rho}:|z|=\rho$, $\rho$ 很大使 $\Gamma_{\rho}$ 内含 $C$. 由复围线的 Cauchy 积分定理,
> > $$
> > \oint_{C}f(z)\,dz=\oint_{\Gamma_{\rho}}f(z)\,dz
> > =\lim_{\rho\to+\infty}\oint_{\Gamma_{\rho}}f(z)\,dz
> > =i\lim_{\rho\to+\infty}\int_{0}^{2\pi}f(\rho e^{i\theta})\rho e^{i\theta}\,d\theta
> > =i\int_{0}^{2\pi}A\,d\theta=2\pi iA.
> > $$
>



> **例**
>
> 设 $f(z)$ 在 $|z-z_{0}|<R$ 上解析并连续到边界, 则
> $\forall n\in\mathbb{N}^{+}$ 和 $\rho\ (0<\rho\leq R)$ 都有
> $$
> f^{(n)}(z_{0})=\frac{n!}{\rho^{n}\pi}\int_{0}^{2\pi}u(z_{0}+\rho e^{i\theta})e^{-in\theta}\,d\theta.
> $$
>
> > **证明**
> >
> > 记 $\Gamma_{\rho}:|z-z_{0}|=\rho$, 由 Cauchy 积分公式,
> > $$
> > f^{(n)}(z_{0})=\frac{n!}{2\pi i}\oint_{\Gamma_{\rho}}\frac{f(z)}{(z-z_{0})^{n+1}}\,dz
> > \stackrel{z=z_{0}+\rho e^{i\theta}}{=}\frac{n!}{2\pi\rho^{n}}\int_{0}^{2\pi}f(z_{0}+\rho e^{i\theta})e^{-in\theta}\,d\theta.
> > $$
> > 再由 Cauchy 积分定理, $n\geq1$ 时有
> > $$
> > 0=\oint_{\Gamma_{\rho}}f(z)(z-z_{0})^{n-1}\,dz
> > \stackrel{z=z_{0}+\rho e^{i\theta}}{=}i\rho^{n}\int_{0}^{2\pi}f(z_{0}+\rho e^{i\theta})e^{in\theta}\,d\theta,
> > $$
> > 取共轭有 $0=\frac{n!}{2\pi\rho^{n}}\int_{0}^{2\pi}\overline{f}(z_{0}+\rho e^{i\theta})e^{-in\theta}\,d\theta$.
> > 两式相加即得关于 $u$ 的公式. 同理两式相减得
> > $$
> > f^{(n)}(z_{0})=\frac{n!}{\rho^{n}\pi}i\int_{0}^{2\pi}v(z_{0}+\rho e^{i\theta})e^{-in\theta}\,d\theta.
> > $$
>



> **例**
>
> 设 $f(z)$ 在 $D:|z-z_{0}|\leq R$ 上连续, 且对 $\rho\ (0<\rho<R)$ 记 $\Gamma_{\rho}:|z-z_{0}|=\rho$, 都有 $\oint_{\Gamma_{\rho}}f(z)\,dz=0$, 则 $\oint_{|z-z_{0}|=R}f(z)\,dz=0$.
>
> > **证明**
> >
> > $\forall\varepsilon>0$, 由于 $f$ 与 $zf$ 在 $|z-z_{0}|\leq R$ 上一致连续, 故 $\exists\delta>0$,
> > 当 $z_{1},z_{2}\in D$ 且 $|z_{1}-z_{2}|<\delta$ 时 $|z_{2}f(z_{2})-z_{1}f(z_{1})|<\varepsilon$ 且 $|f(z_{2})-f(z_{1})|<\varepsilon$.
> > 于是当 $\rho$ 充分接近 $R$ 时,
> > $$
> > \begin{aligned}
> > \Bigl|\oint_{|z-z_{0}|=R}f(z)\,dz\Bigr|
> > &=\Bigl|\oint_{|z-z_{0}|=R}f(z)\,dz-\oint_{\Gamma_{\rho}}f(z)\,dz\Bigr|\\
> > &\leq\Biggl|\int_{0}^{2\pi}\bigl[f(z_{0}+Re^{i\theta})(z_{0}+Re^{i\theta})
> > -f(z_{0}+\rho e^{i\theta})(z_{0}+\rho e^{i\theta})\bigr]\,d\theta\Biggr|\\
> > &\quad+|z_{0}|\Biggl|\int_{0}^{2\pi}\bigl[f(z_{0}+Re^{i\theta})-f(z_{0}+\rho e^{i\theta})\bigr]\,d\theta\Biggr|
> > <(2\pi+2\pi|z_{0}|)\varepsilon.
> > \end{aligned}
> > $$
> > $\varepsilon$ 任意, 故边界积分为 $0$.
>



> **例**
>
> 计算 $\int_{C}\frac{\cos\frac{\pi}{4}z}{z^{2}-1}\,dz$, 这里 $C$:
> (1) $|z-1|=\frac{1}{2}$; (2) $|z+1|=\frac{1}{2}$; (3) $|z|=2$.
>
> (1) $\displaystyle\int_{C}\frac{\cos\frac{\pi}{4}z}{z^{2}-1}\,dz
> =\oint_{|z-1|=\frac{1}{2}}\frac{\frac{\cos\frac{\pi}{4}z}{z+1}}{z-1}\,dz
> =2\pi i\frac{\cos\frac{\pi}{4}z}{z+1}\Big|_{z=1}=\frac{\sqrt{2}}{2}\pi i$.
>
> (2) $\displaystyle\int_{C}\frac{\cos\frac{\pi}{4}z}{z^{2}-1}\,dz
> =\oint_{|z+1|=\frac{1}{2}}\frac{\frac{\cos\frac{\pi}{4}z}{z-1}}{z+1}\,dz
> =2\pi i\frac{\cos\frac{\pi}{4}z}{z-1}\Big|_{z=-1}=-\frac{\sqrt{2}}{2}\pi i$.
>
> (3) $\displaystyle\int_{|z|=2}\frac{\cos\frac{\pi}{4}z}{z^{2}-1}\,dz
> =\oint_{|z-1|=\frac{1}{2}}\frac{\cos\frac{\pi}{4}z}{z^{2}-1}\,dz
> +\oint_{|z+1|=\frac{1}{2}}\frac{\cos\frac{\pi}{4}z}{z^{2}-1}\,dz
> =\frac{\sqrt{2}}{2}\pi i-\frac{\sqrt{2}}{2}\pi i=0$.





[目录与前言](../viewer.html?md=Complex-Analysis-Notes) · [下一章 →](../viewer.html?md=Complex-Analysis-Notes-Chapter-4)
