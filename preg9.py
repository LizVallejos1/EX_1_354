# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:20:30 2023

@author: liz
"""

""" 9. Con PYTHON sin librerías construya los índices de al menos dos ciclos
 para un Split de Train 80 y test de 20, apliquelo en el dataset iris. """
 
import random
import pandas as pd
import numpy as np
 
from sklearn.datasets import load_iris
data = load_iris()
x= data.data
y=data.target
print(y,y[10])


#Dividir dataset en conjunto de entrenamiento y test
from sklearn.model_selection import train_test_split
X_entre,X_test, y_entre,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
Yt=y_entre.T
print(y_entre)
print(y_entre.shape)
 
print(Yt.shape)
print(y_test.shape)



