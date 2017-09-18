# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random as r
import matplotlib.pyplot as plt
def sum2dice(N):
    count = [None] * N
    #counter = 0
    for x in range (0, N):
        done = 1
        counter = 0
        while done:
            d1 = np.random.randint(1,7)
            d2 = np.random.randint(1,7)
            s = d1 + d2
            #print(x, s)
            counter+=1
            if s == 7:
                done = 0
                count[x] = counter
    #print(count)
    #print()
    b = range(1,30)
    h1, bin_edges = np.histogram(count,bins = b)
    b1 = bin_edges[1:30]
    plt.close('all')
    
    fig2 = plt.figure(2)
    p1 = h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Getting 7 from pair of dice: Probability mass function')
    plt.xlabel('Number of rolls to get 7')
    plt.ylabel('Probability')
    
    #
    #d1 = np.random.randint(1,7,N)
    #d2 = np.random.randint(1,7,N)
    #s = d1 + d2
    #b = range(1,15)
    #h1, bin_edges = np.histogram(s,bins = b)
    #b1 = bin_edges[0:13]
    #plt.close('all')
    #
    #fig1 = plt.figure(1)
    #plt.stem(b1,h1)
    #plt.title('Stem plot - Sum of two dice')
    #plt.xlabel('Sum of two dice')
    #plt.ylabel('Number of occurences')
    
    #
    #fig2 = plt.figure(2)
    #p1 = h1/N
    #plt.stem(b1,p1)
    #plt.title('Stem plot - Sum of two dice: Probability mass function')
    #plt.xlabel('Sum of two dice')
    #plt.ylabel('Probability')
    
