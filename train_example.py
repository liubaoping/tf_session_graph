# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 10:49:00 2018

@author: l
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def fig(a,b,i):
    plt.subplot(3,4,i)
    plt.plot(x_data,y_data)
    plt.plot(x_data,x_data*a+b)
    
    

#使用numpy生成100个随机点
global x_data,y_data
x_data=np.random.rand(100)
y_data=x_data*0.1+0.2
#print(zip(x_data,y_data))

#构造一个线性模型
b=tf.Variable(1.)
k=tf.Variable(2.)
y=k*x_data+b

#二次代价函数
loss=tf.reduce_mean(tf.square(y_data-y))

#定义一个梯度下降法作为 训练的优化器
optimizer=tf.train.GradientDescentOptimizer(0.2)
#最小化代价函数
train=optimizer.minimize(loss)

#初始化变量
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    i=1
    for step in range(201):
        sess.run(train)
        if step%20==0:
            print(step,sess.run([k,b]))
            fig(sess.run(k),sess.run(b),i)
            i=i+1