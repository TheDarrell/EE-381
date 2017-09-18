# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:10:55 2017

@author: 012722695
"""
import numpy as np
import matplotlib.pyplot as plt
def kind4(N):
    count = 0
    for y in range (0, N):
        deck = np.random.permutation(52)
        hand = deck[0:5]
        for x in range (0, 5):
            hand[x] = hand[x] % 13
        hand = np.sort(hand)
        #print(y, '. hand = ', hand)
        if hand[0] == hand[3]:
            count += 1
            print(y, '. hand = ', hand)
            print('Count')
        elif hand[1] == hand[4]:
            count += 1
            print(y, '. hand = ', hand)
            print('Count')
    print('4 of a Kind:' , count, '     Amount of tests:', N)
    print('Probability:', count/N)
    
kind4(100000)