第四次作业
=================

摘要
----------------
计算物理作业1.3，题目要求模拟阻力。首先根据常微分方程轻松解出解析解，随后用欧拉方法进行模拟，画图比对二者

正文
----------------
本题需要解决的常微分方程为$$\frac{dv}{dt}=a-bv$$
由解析方法解得$$v=\frac{[a-(a-bv_{0})e^{-bt}]}{b}$$
按照书上的建议，我取了a=10，b=1
从解析解容易看出，无论$v_{0}$的取值为何，最终都应趋向于$$v_{0}=10$$
下面贴上$v_{0}=10，1，20$的图，以期给个直观的认识

$v_{0}=10$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v=10.png)

$v_{0}=1$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v=1.png)

$v_{0}=20$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v=20.png)

用欧拉公式近似计算得到的结果与解析符合得如何呢？以0.006为步长，仍以以上三个值作为比较

$v_{0}=10$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v=10_compare.png)

$v_{0}=1$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v=1_compare.png)

$v_{0}=20$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v=20_compare.png)

速度取得很小会怎么样呢
符合得很好以至于让我不忍直视。我想还是改变一下步长吧，把步长改为0.06，有肉眼可见偏差了，见下图
$v_{0}=20$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/20_006.png)

**注：时间总长度选择6s是因为速度在这时候已趋于稳定，并且比较直观**

下面贴上一些比较极端的图，以下各图步长均为0.006
$v_{0}=-10000$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v%3D-10000.png)
$v_{0}=10000$
![enter image description here](https://github.com/wdwycpt/computationalphysics_N2013301020128/blob/master/v%3D10000.png)
最终还是10m/s！

结论
--------------
从解析解可以看出得出以上各个结果都是不让人意外的，不过在步长取得小得时候，欧拉方法对其的模拟也是恰当的。不过近期决定拜读冯康老师的著作以期对数值模拟有更深入的理解。
