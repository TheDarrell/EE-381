# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:03:38 2017

@author: 012722695
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
import random as r
def state2():
    times = 15
    stepA = [None] * (times)
    stepB = [None] * (times)
    stateA = 1
    stateB = reverse(stateA)
    stepA[0] = stateA
    stepB[0] = stateB
    for x in range (1,times):
        m = np.random.rand()
        if stateA == 1:
            if m < 0.8:
                stateA = 1
            else:
                stateA = 0
        if stateA == 0:
            if m < 0.5:
                stateA = 1
            else:
                stateA = 0
        stepA[x] = stateA
        stepB[x] = reverse(stateA)
    
    list2 = [x for x in range(1, times+1)]
    
    plt.close('all')
    
    fig1 = plt.figure(1)
    plt.plot(list2, stepA, 'b--', marker = 'o')
    plt.plot(list2, stepB, 'r--', marker = 'o')
    
def state2Mult():
    trials = 10000
    times = 15
    stepA = [None] * (times)
    stepB = [None] * (times)
    
    for z in range (0, times):
        stepA[z] = 0
        stepB[z] = 0
    
    for y in range (0, trials):
        m = np.random.rand()
        if m < 0.4:
            stateA = 1
        else:
            stateA = 0
        
        stateB = reverse(stateA)
        stepA[0] = stepA[0] + stateA
        stepB[0] = stepB[0] + stateB
        for x in range (1,times):
            m = np.random.rand()
            if stateA == 1:
                if m < 0.8:
                    stateA = 1
                else:
                    stateA = 0
            if stateA == 0:
                if m < 0.5:
                    stateA = 1
                else:
                    stateA = 0
            #print(stepA[x] + stateA)
            stepA[x] = stepA[x] + stateA
            stepB[x] = stepB[x] + reverse(stateA)
    
    list2 = [x for x in range(1, times+1)] 
    
    for x in range (0,times):
        stepA[x] = stepA[x]/trials
        stepB[x] = stepB[x]/trials
    
    plt.close('all')
    
    fig1 = plt.figure(1)
    plt.plot(list2, stepA, 'b--', marker = 'o')
    plt.plot(list2, stepB, 'r--', marker = 'o')
    
    #Calculation
    calcA = [None] * (times)
    calcB = [None] * (times)
    calcA[0] = 0.4
    calcB[0] = 0.6
    w, h = 2, 2;
    matrix = [[0 for x in range(w)] for y in range(h)]
    matrix[0][0] = 0.8
    matrix[0][1] = 0.2
    matrix[1][0] = 0.5
    matrix[1][1] = 0.5
    
    for x in range (1, times):
        calcA[x] = (calcA[x-1]*matrix[0][0]) + (calcB[x-1]*matrix[1][0])
        calcB[x] = (calcA[x-1]*matrix[0][1]) + (calcB[x-1]*matrix[1][1])
    
    fig2 = plt.figure(2)
    plt.plot(list2, calcA, 'b--', marker = 'o')
    plt.plot(list2, calcB, 'r--', marker = 'o')

    
    
def reverse(s):
    if s == 1:
        return 0
    if s == 0:
        return 1
   
#state2()
state2Mult()
    
    