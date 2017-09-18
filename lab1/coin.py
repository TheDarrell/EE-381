# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:25:43 2017

@author: 012722695
"""
import numpy as np
import matplotlib.pyplot as plt
def coin2(N):
    count = 0;
    for x in range (0, N):
        coin = np.random.randint(0,2,100)
        heads = sum(coin)
        #print(x, '. Heads = ', heads)
        if heads == 50:
            count += 1
            #print('Count')
    print('probability of 50 Heads = ', count/N)
