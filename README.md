# misc_script
杂七杂八不成类别的脚本。
## 1. 等效角度计算
用于计算靶上出射到一个矩形探测器接收窗口范围内，一个角度范围等效成某个角度值。
输出等效的角度数值，绘制实际角度分布，需自行修改的参数在前些行。

应该看可以用积分计算，再不济也可以用数值积分计算，但是琢磨了一会没太想明白最后还是用蒙特卡罗方法计算了。

工况描述：直径phi(mm)的束斑照射在靶上，在靶相同高度距离为rd(mm)的圆上有一宽w(mm)高h(mm)的探测器窗口，文束流照射到靶上发射各向同性随机方向的产物，在探测器窗口范围内的等效角度。

束流方向为z，朝我方向为x，向上为y方向，其他参考注释。

`20250618`更新：增加立体角计算

## 2. q3d数据临时拷贝到u盘的sh

## 3. 时间计算器
计算一个给定时间，选择加上或减去某用户输入时间段（HH：mm：ss）之后的时间，能够对用户输入的一个时间段（HH：mm：ss）转换单位为（s）或者将时间段（s）转换为（HH：mm：ss）

## 4. 活度计算器
输入活度和半衰期，计算给定时间之前或之后的活度数值，可以配合程序3使用。

## 5. 极其简易半衰期与衰变常数的转换
建议配合3使用

## 6.厚靶共振产额计算
见注释
