# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:43:39 2017

@author: 012722695
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
def expRV():
    np.set_printoptions(threshold=np.inf)
    N = 10000
    s = [None] * N
    t = np.random.exponential(0.5, N)
    for x in range (0,N):
        if t[x] >= 0:
            s[x] = 2 * m.exp(-2 * t[x])
        else:
            s[x] = 0

    nbins = 30
    edgecolor = 'w'
    bins = [float (x) for x in np.linspace(0,3,nbins+1)]
    h1, bin_edges = np.histogram(s, bins, density = True)
    
    barwidth = 1/30
    
    plt.close('all')
    
    fig1 = plt.figure(1)
    plt.bar(t,s, width=barwidth, edgecolor = edgecolor)
    plt.title('Comparison of simulated exponential distribution w/ actual plot')
    plt.xlabel('Random Variable (X)')
    plt.ylabel('f(x) = 2exp(-2x) if x >=0 0 if x < 0')
    
    
    smooth = 30 
    list2 = [x*(1/smooth) for x in range(0, smooth*3)]
    
    g = [None] * (smooth*3)
    c = 0
    
    for x in range(0, smooth*3):
        g[x] = 2 * m.exp(-2 * c)
        c+= 1/smooth
    
    plt.plot(list2,g, color = 'red')
    
expRV()

