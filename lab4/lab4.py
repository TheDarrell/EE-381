# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:18:57 2017

@author: 012722695
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
def centralLimit(n):
    s = [None] * 10000
    a=1
    b=3
    for x in range(0, 10000):
        w = np.random.uniform(a,b,n)
        #print(w)
        s[x] = np.sum(w)
        #print(s)
        #s = w
    
    #print(s)
    
    nbins = 30
    edgecolor = 'w'
    bins = [float (x) for x in np.linspace(n*a,n*b,nbins+1)]
    h1, bin_edges = np.histogram(s, bins, density = True)
    
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0]
    plt.close('all')
        
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor = edgecolor)
    label = 'Book stack height for n = %d' % n
    plt.title('PDF of %d book stack height & comparison w/ Gaussian' % n)
    plt.xlabel(label)
    plt.ylabel('PDF')    
        
    ow = ((b-a) ** 2) / 12
    ow = m.sqrt(ow)
    os = ow*m.sqrt(n)
    uw = (a+b)/2
    us = n*uw
    
    smooth = 30 
    # Number of points used to plot the normal distribution function
    
    g = [None] * (smooth*(n*b-n*a)+1)
    c = n*a
    
    list2 = [x*(1/smooth) for x in range(smooth*n*a, smooth*n*b+1)]
    #print(list2)
    
    for x in range (0, smooth*(n*b-n*a)+1):
        g[x] = (1/(os*m.sqrt(2*m.pi)))*m.exp(-((c-us) ** 2)/(2*(os ** 2)))
        #print(c, " ", g[x])
        c+= 1/smooth
    plt.plot(list2,g, color = 'red')
    
#centralLimit(1)
#centralLimit(2)
#centralLimit(5)
#centralLimit(10)
centralLimit(15)
