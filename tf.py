# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:23:15 2018

@author: l
"""

import tensorflow as tf

#定义第一个常量
m1=tf.constant([[3,3]])
#定义第二个常量
m2=tf.constant([[2],[3]])
#创建一个矩阵乘法op，把m1,m2传入
product=tf.matmul(m1,m2)
print(product)

#定义一个session,启动默认图
sess=tf.Session()
#调用sess的run方法来执行矩阵乘法op
#run（product）触发了三个op
result=sess.run(product)
print(result)
sess.close()

#第二段代码的另一种表达：此时不用sess.close()
with tf.Session() as sess:
    #调用sess的run方法来执行矩阵乘法op
    #run（product）触发了三个op
    result=sess.run(product)
    print(result)
    sess.close()