# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:30:17 2020

@author: ANURAG SINGH
"""

import numpy as np 
import pandas as pd
import scipy.stats as stats

def Zprob(z0):
    return(print('p-value of z normal distribution = ',stats.norm.cdf(z0)))


def chiprob(z0, alpha):
      return(print('\np-value of chisquare  = ',stats.chi.cdf(z0, alpha)))

def tprob(z0, alpha):
        return(print('\np-value of t distribution = ',stats.t.cdf(z0,alpha)))


def fprob(q,df1, df2):
      return(print('\np-value of f distribution = ',stats.f.cdf(q,df1 , df2)))


Zprob(1.45)
chiprob(2.32,1)
tprob(3.50, 15)
fprob(2,2,1)