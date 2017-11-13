# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:58:15 2017

@author: 012722695
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
import random as r
def bearPop():
    bear = 1000000
    mu = 75
    sig = 7.5
    size = 200
    b = mu + np.random.randn(bear) * sig
    mean = [None] * (size)
    top95 = [None] * (size)
    bottom95 = [None] * (size)
    top99 = [None] * (size)
    bottom99 = [None] * (size)
    for c in range (0,size):
        n = c+1 
        x = b[r.sample(range(bear), n)]
       
        mean[c] = np.sum(x)/n
        std = sig/m.sqrt(n)
        top95[c] = mu + 1.96*(std)
        bottom95[c] = mu - 1.96*(std)
        top99[c] = mu + 2.58*(std)
        bottom99[c] = mu - 2.58*(std)
   
    list2 = [x for x in range(1, size+1)] 
    
    plt.close('all')
    
    fig1 = plt.figure(1)
    plt.scatter(list2, mean, c = 'Blue', marker = 'x')
    plt.plot(list2, top95, 'r--')
    plt.plot(list2, bottom95, 'r--')
    plt.title('Sample Means & 95% confidence intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x_bar')
    
    fig2 = plt.figure(2)
    plt.scatter(list2, mean, c = 'Blue', marker = 'x')
    plt.plot(list2, top99, 'g--')
    plt.plot(list2, bottom99, 'g--')
    plt.title('Sample Means & 99% confidence intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x_bar')
    
    #Part 2
    trials = 10000
    Part2Calc(b,bear, mu, trials, 2.78, 4.6, 5)
    Part2Calc(b,bear, mu, trials, 2.02, 2.7, 40)
    Part2Calc(b,bear, mu, trials, 1.98, 2.62, 120)
    
def Part2Calc(b,bear,mu,trials,t95,t99,size):
    successZ95 = 0
    successZ99 = 0
    successT95 = 0
    successT99 = 0
    sample = size
    for z in range (0, trials):
        y = b[r.sample(range(bear), sample)]
        yMean = np.sum(y)/sample
        total = 0
        for a in range(0, len(y)):
            total = total + (y[a]-yMean) ** 2
        yS = total/(sample-1)
        yS = m.sqrt(yS)
        yStd = yS/m.sqrt(sample)
        
        yTop95 = yMean + 1.96*(yStd)
        yBottom95 = yMean - 1.96*(yStd)
        yTop99 = yMean + 2.58*(yStd)
        yBottom99 = yMean - 2.58*(yStd)
        
        tTop95 = yMean + t95*(yStd)
        tBottom95 = yMean - t95*(yStd)
        tTop99 = yMean + t99*(yStd)
        tBottom99 = yMean - t99*(yStd)
        
        if yBottom95 <= mu and yTop95 >= mu:
            successZ95 += 1
        if yBottom99 <= mu and yTop99 >= mu:
            successZ99 += 1
        if tBottom95 <= mu and tTop95 >= mu:
            successT95 += 1
        if tBottom99 <= mu and tTop99 >= mu:
            successT99 += 1
    
    print('Success Rate using normal, sample = %d,' % sample, '95% confidence interval')
    print(successZ95/trials)
    print('Success Rate using normal, sample = %d,' % sample, '99% confidence interval')
    print(successZ99/trials)
    print('Success Rate using student t, sample = %d,' % sample, '95% confidence interval')
    print(successT95/trials)
    print('Success Rate using student t, sample = %d,' % sample, '99% confidence interval')
    print(successT99/trials)
    print('')
    
bearPop()