# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:50:27 2017

@author: 012722695
"""
import numpy as np
import matplotlib.pyplot as plt

def state3():
    times = 15
    stepR = [None] * (times)
    stepN = [None] * (times)
    stepS = [None] * (times)
    
    for z in range (0, times):
        stepR[z] = 0
        stepN[z] = 0
        stepS[z] = 0
    
    #Initial state
    state = 3
    
    if state == 1:
        stepR[0] = 1
        stepN[0] = 0
        stepS[0] = 0
    elif state == 2:
        stepR[0] = 0
        stepN[0] = 1
        stepS[0] = 0
    else: 
        stepR[0] = 0
        stepN[0] = 0
        stepS[0] = 1
    for x in range (1, times):
        m = np.random.rand()
        if state == 1:
            if m < (1/3):
                stepR[x] = stepR[x]+1
                state = 1
            elif m < ((1/3)+(1/3)):
                stepN[x] = stepN[x]+1
                state = 2
            else:
                stepS[x] = stepS[x]+1
                state = 3
        elif state == 2:
            if m < (1/2):
                stepR[x] = stepR[x]+1
                state = 1
            else:
                stepS[x] = stepS[x]+1
                state = 3
        elif state == 3:
            if m < (1/4):
                stepR[x] = stepR[x]+1
                state = 1
            elif m < ((1/4) + (1/4)):
                stepN[x] = stepN[x]+1
                state = 2
            else:
                stepS[x] = stepS[x]+1
                state = 3
      
    list2 = [x for x in range(1, times+1)]
    
    plt.close('all')
    
    fig1 = plt.figure(1)
    plt.yticks([0,1],["0","1"])
    line1, = plt.plot(list2, stepR, label="Rain", 
                      linestyle='--', marker = 'o', color='dodgerblue')
    line2, = plt.plot(list2, stepN, label="Nice", 
                      linestyle='--', marker = 'o', color='forestgreen')
    line3, = plt.plot(list2, stepS, label="Snow", 
                      linestyle='--', marker = 'o', color='grey')
    plt.legend(handles=[line1,line2,line3], loc = 4)
    plt.title('3 State Markov Chain w/ Weather Results from 1 simulation')
    plt.xlabel('Step Number')
    plt.ylabel('State of Chain')
    
def state3Mult():
    trials = 10000
    times = 15
    stepR = [None] * (times)
    stepN = [None] * (times)
    stepS = [None] * (times)
    
    for z in range (0, times):
        stepR[z] = 0
        stepN[z] = 0
        stepS[z] = 0
        
    for y in range (0, trials):
        m = np.random.rand()
        state = 0
        if m < (1/4):
            stepR[0] = stepR[0]+1
            state = 1
        elif m < ((1/4) + (1/2)):
            stepN[0] = stepN[0]+1
            state = 2
        else:
            stepS[0] = stepS[0]+1
            state = 3
        for x in range (1,times):
            m = np.random.rand()
            if state == 1:
                if m < (1/3):
                    stepR[x] = stepR[x]+1
                    state = 1
                elif m < ((1/3)+(1/3)):
                    stepN[x] = stepN[x]+1
                    state = 2
                else:
                    stepS[x] = stepS[x]+1
                    state = 3
            elif state == 2:
                if m < (1/2):
                    stepR[x] = stepR[x]+1
                    state = 1
                else:
                    stepS[x] = stepS[x]+1
                    state = 3
            elif state == 3:
                if m < (1/4):
                    stepR[x] = stepR[x]+1
                    state = 1
                elif m < ((1/4) + (1/4)):
                    stepN[x] = stepN[x]+1
                    state = 2
                else:
                    stepS[x] = stepS[x]+1
                    state = 3
                    
    list2 = [x for x in range(1, times+1)] 
    
    for x in range (0,times):
        stepR[x] = stepR[x]/trials
        stepN[x] = stepN[x]/trials
        stepS[x] = stepS[x]/trials  
    
    plt.close('all')
    
    fig1 = plt.figure(1)   
    line1, = plt.plot(list2, stepR, label="Rain", 
                      linestyle='--', marker = 'o', color='dodgerblue')
    line2, = plt.plot(list2, stepN, label="Nice", 
                      linestyle='--', marker = 'o', color='forestgreen')
    line3, = plt.plot(list2, stepS, label="Snow", 
                      linestyle='--', marker = 'o', color='grey')
    plt.legend(handles=[line1,line2,line3], loc = 4)
    plt.title('3 State Markov Chain w/ Weather using N=%d Simulations' %trials)
    plt.xlabel('Step Number')
    plt.ylabel('Probability')
    
    #Calculation\
    calcR = [None] * (times)
    calcN = [None] * (times)
    calcS = [None] * (times)
    calcR[0] = 1/4
    calcN[0] = 1/2
    calcS[0] = 1/4
    matrix = [[1/3,1/3,1/3]
             ,[1/2,  0,1/2]
             ,[1/4,1/4,1/2]]
    
    for x in range (1, times):
        calcR[x] = (calcR[x-1]*matrix[0][0]) + (calcN[x-1]*matrix[1][0]) + (calcS[x-1]*matrix[2][0])
        calcN[x] = (calcR[x-1]*matrix[0][1]) + (calcN[x-1]*matrix[1][1]) + (calcS[x-1]*matrix[2][1])
        calcS[x] = (calcR[x-1]*matrix[0][2]) + (calcN[x-1]*matrix[1][2]) + (calcS[x-1]*matrix[2][2])
        
    
    fig2 = plt.figure(2)
    line4, = plt.plot(list2, calcR, label="Rain", 
                      linestyle='--', marker = 'o', color='dodgerblue')
    line5, = plt.plot(list2, calcN, label="Nice", 
                      linestyle='--', marker = 'o', color='forestgreen')
    line6, = plt.plot(list2, calcS, label="Snow", 
                      linestyle='--', marker = 'o', color='grey')
    plt.legend(handles=[line4,line5,line6], loc = 4)
    plt.title('3 State Markov Chain w/ Weather using Calculations')
    plt.xlabel('Step Number')
    plt.ylabel('Probability')

def PageRank(s):
    times = 20
    matrix = [[  0,  1,  0,  0,  0]
             ,[1/2,  0,1/2,  0,  0]
             ,[1/3,1/3,  0,  0,1/3]
             ,[  1,  0,  0,  0,  0]
             ,[  0,1/3,1/3,1/3,  0]]
    calcA = [None] * (times)
    calcB = [None] * (times)
    calcC = [None] * (times)
    calcD = [None] * (times)
    calcE = [None] * (times)
    if s == 0:
        calcA[0] = 1/5
        calcB[0] = 1/5
        calcC[0] = 1/5
        calcD[0] = 1/5
        calcE[0] = 1/5
    else:
        calcA[0] = 0
        calcB[0] = 0
        calcC[0] = 0
        calcD[0] = 0
        calcE[0] = 1
    for x in range (1, times):
        calcA[x] = (calcA[x-1]*matrix[0][0]) + (calcB[x-1]*matrix[1][0]) + (calcC[x-1]*matrix[2][0]) + (calcD[x-1]*matrix[3][0]) + (calcE[x-1]*matrix[4][0])            
        calcB[x] = (calcA[x-1]*matrix[0][1]) + (calcB[x-1]*matrix[1][1]) + (calcC[x-1]*matrix[2][1]) + (calcD[x-1]*matrix[3][1]) + (calcE[x-1]*matrix[4][1])
        calcC[x] = (calcA[x-1]*matrix[0][2]) + (calcB[x-1]*matrix[1][2]) + (calcC[x-1]*matrix[2][2]) + (calcD[x-1]*matrix[3][2]) + (calcE[x-1]*matrix[4][2])
        calcD[x] = (calcA[x-1]*matrix[0][3]) + (calcB[x-1]*matrix[1][3]) + (calcC[x-1]*matrix[2][3]) + (calcD[x-1]*matrix[3][3]) + (calcE[x-1]*matrix[4][3])
        calcE[x] = (calcA[x-1]*matrix[0][4]) + (calcB[x-1]*matrix[1][4]) + (calcC[x-1]*matrix[2][4]) + (calcD[x-1]*matrix[3][4]) + (calcE[x-1]*matrix[4][4])
                   
    
    list2 = [x for x in range(1, times+1)]
    
    plt.close('all')
    
    fig1 = plt.figure(1)
    line1, = plt.plot(list2, calcA, label="A", 
                      linestyle='--', marker = 'o', color='blue')
    line2, = plt.plot(list2, calcB, label="B", 
                      linestyle='--', marker = 'o', color='green')
    line3, = plt.plot(list2, calcC, label="C", 
                      linestyle='--', marker = 'o', color='red')
    line4, = plt.plot(list2, calcD, label="D", 
                      linestyle='--', marker = 'o', color='purple')
    line5, = plt.plot(list2, calcE, label="E", 
                      linestyle='--', marker = 'o', color='orange')
    plt.legend(handles=[line1,line2,line3,line4,line5])
    plt.xticks(list2)
    plt.title('Google 5 Page Rank using Calculations with Markov Chains')
    plt.xlabel('Step Number')
    plt.ylabel('Probability')
    
#state3()
#state3Mult()
PageRank(0)
#PageRank(1)
            
        
         