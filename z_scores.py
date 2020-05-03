# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:28:41 2020

@author: ANURAG SINGH
"""

import numpy as np 
import pandas as pd
import scipy.stats as stats

def Z_score(p):
    return(print("z0-value = ",stats.norm.ppf(p)))
  
def chisq_score(p, df):
    return(print("\n z0-value   = ",stats.chi.ppf(p, df)))
  

def t_score(p, df):
      return(print("\n z0-value  = ",stats.t.ppf(p,df)))


def f_score(p, df1, df2):
      return(print("\n z0-value  = ",stats.f.ppf(p,df1 , df2)))

Z_score(0.9264707403903516)
chisq_score(0.9796591226625607,1)
t_score(0.9983882345281028,15)
f_score(0.552786404500042, 2, 1)