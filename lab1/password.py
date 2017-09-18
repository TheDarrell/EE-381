# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:55:18 2017

@author: 012722695
"""
import numpy as np
import matplotlib.pyplot as plt
def password(N, m):
    count = 0
    z = 26 ** (4)
    for x in range (0, N):
        p = np.random.randint(0,z)
        hack = np.random.randint(0,z,m)
        if p in hack:
            count += 1
    print('Count =', count)
    print('Hack =', m)
    print('Total =', N)
    print('Probability =', count/N)
    print()
    
password(1000, 10 ** (5))
password(1000, 10 **(6))
password(1000, int(3.2 * (10 ** (5))))
password(1000, int((26 ** (4))/2))