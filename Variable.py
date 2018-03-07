# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 10:00:36 2018

@author: l
"""

import tensorflow as tf
x=tf.Variable([1,2])
a=tf.constant([3,3])
#增加一个减法op
sub=tf.subtract(x,a)
#增加一个加法op
add=tf.add(x,sub)

#变量初始化
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))
    
#创建一个计数变量 初始为0,命名为counter
    
state=tf.Variable(0,name='counter')
#创建一个op，作用是state加1
new_state=tf.add(state,1)
#创建op
update=tf.assign(state,new_state)
#变量初始化
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))