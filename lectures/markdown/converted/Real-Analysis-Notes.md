# Real Analysis

Lecture Notes

作者：Stone Sun  
时间：2025 年 7 月 5 日  
联系方式：hefengzhishui@outlook.com


## 章节目录

<details class="chapter-outline">
<summary>第 1 章 · 基础集合论</summary>
<a class="chapter-read" href="../viewer.html?md=Real-Analysis-Notes-Chapter-1">阅读本章 →</a>
<ul>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-1#section-1">集合的运算</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-1#section-2">集合的对等</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-1#section-3">集合的基数</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-1#section-4">距离空间</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-1#section-5">开集、闭集及其构造</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-1#section-6">Cantor集</a></li>
</ul>
</details>

<details class="chapter-outline">
<summary>第 2 章 · Lebesgue测度</summary>
<a class="chapter-read" href="../viewer.html?md=Real-Analysis-Notes-Chapter-2">阅读本章 →</a>
<ul>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-2#section-1">外测度</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-2#section-2">可测集及其测度</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-2#section-3">可测集族</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-2#section-4">不可测集</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-2#section-5">乘积测度</a></li>
</ul>
</details>

<details class="chapter-outline">
<summary>第 3 章 · 可测函数</summary>
<a class="chapter-read" href="../viewer.html?md=Real-Analysis-Notes-Chapter-3">阅读本章 →</a>
<ul>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-3#section-1">可测函数的定义和性质</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-3#section-2">可测函数的收敛性</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-3#section-3">可测函数的连续性</a></li>
</ul>
</details>

<details class="chapter-outline">
<summary>第 4 章 · Lebesgue积分</summary>
<a class="chapter-read" href="../viewer.html?md=Real-Analysis-Notes-Chapter-4">阅读本章 →</a>
<ul>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-4#section-1">非负可测函数的积分</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-4#section-2">一般可测函数的积分</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-4#section-3">Lebesgue积分与Riemann积分的关系</a></li>
<li class="outline-level-3"><a href="../viewer.html?md=Real-Analysis-Notes-Chapter-4#section-4">重积分与累次积分的关系</a></li>
</ul>
</details>

<details class="chapter-outline">
<summary>第 5 章 · 习题集</summary>
<a class="chapter-read" href="../viewer.html?md=Real-Analysis-Notes-Chapter-5">阅读本章 →</a>
<ul>
</ul>
</details>


## 前言



谨以此篇, 献给热爱分析的你.








这是一份关于实分析(又名实变函数)的讲义, 主要涵盖了$\mathbb{R}^n$上的集合论与测度论, 同时讨论了Lebesgue可测、Lebesgue积分的基本概念和定理. 这份讲义是基于中国海洋大学的实变函数课程的讲义和笔记而写成的, 也参考了其他一些教材和讲义.


值得注意的是, 这门课程在不同开课学院的所占学分和所需学时是不同的. 所以这份讲义可能更适合每周3学时的同学学习参考.


这份讲义的描述角度是一位数学专业的学生, 因此我可能会采用一些更易于理解, 但不严格符合课程结构的叙述方式和顺序. 这些特性决定了这份讲义不会有太广泛的适用性.


笔者曾经试图撰写过常微分方程、微积分、线性代数等课程的讲义, 但由于时间和精力的限制, 这些讲义都没有完成. 这份讲义是笔者在2025年春季学期和暑期复习这门课程时完成的, 从某种程度上来讲这既是对此前未完成的讲义的一种补偿, 也是对自己本科二年级学习生活的一份总结. 我希望在这份讲义里更多地去体现我对Lebesgue测度的理解和我对分析学的认知. 尽管这些认知可能都是浅显的, 但我仍希望这些想法能够落到具体实际, 以作纪念和方便回顾.


除了上述这些想法之外, 我还希望基于此回忆一些学习时的一些有趣的理解, 作为一名可能对分析方向不太感兴趣的学生, 我的这份讲义可能不会带来任何有益的帮助, 反倒可能对基础分析概念的理解产生许多误解, 因此我更希望读者将这份讲义看作漫谈, 而非一份严谨的参考讲义, 同时我也很期待任何同学能够帮助我修正其中的任何错误.


Stone Sun  
2025 年 7 月 5 日
