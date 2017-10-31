# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:07:45 2017

@author: 012722695
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
def sumRV(): 
    a=300
    b=2000
    n = 24
    N = 10000
    s = [None] * N
   
    
    for x in range(0, N):
       t = np.random.exponential(45,n)
       s[x] = np.sum(t)
    
    nbins = 30
    edgecolor = 'w'
    bins = [float (x) for x in np.linspace(a,b,nbins+1)]
    h1, bin_edges = np.histogram(s, bins, density = True)
    
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0]
    plt.close('all')
        
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor = edgecolor)
    plt.title('PDF of lifetime of a 24 batteries carton & comparison w/ Gaussian')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('PDF')    
        
    ot = 45
    oc = ot*m.sqrt(n)
    ut = 45
    uc = n*ut
    
    size = int(b-a+1)
    g = [None] * size
    
    c = a
    
    list2 = [a+x for x in range(0, size)]
    
    for x in range (0, size):
        g[x] = (1/(oc*m.sqrt(2*m.pi)))*m.exp(-((c-uc) ** 2)/(2*(oc ** 2)))
        c+= 1
    #print(list2[0], " ", g[0])
    #print(list2[1095-a], " ", g[1095-a])
    print(list2[size-1], " ", g[size-1])
    plt.plot(list2,g, color = 'red')

    fig2 = plt.figure(2)
    h2 = np.cumsum(h1)*barwidth
    plt.bar(b1,h2, width=barwidth, edgecolor = edgecolor)
    plt.title('CDF of lifetime of a 24 batteries carton')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('CDF')

sumRV()