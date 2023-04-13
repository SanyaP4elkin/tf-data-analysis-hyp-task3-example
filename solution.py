import pandas as pd
import numpy as np


chat_id = 1126746074 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    
    m_ar = []
    for i in range(1000):
        m = np.random.randint(0, 2, size = len(x))
        m_ar.append(np.mean(x[m == 1]))
    
    if np.mean(m_ar) > 300:
        return False
    else:
        return True
