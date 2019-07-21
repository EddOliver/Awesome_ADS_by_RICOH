# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:46:47 2019

@author: VAI
"""

import pickle

check=1

with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(check, f)
