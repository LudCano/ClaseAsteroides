# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:33:41 2021

@author: HP
"""

import pandas as pd

data = pd.read_csv("data.csv")

data2 = data.sample(n = 200)

data2.to_csv("data2.csv", index =False)