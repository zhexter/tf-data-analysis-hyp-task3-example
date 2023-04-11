import pandas as pd
import numpy as np
import scipy.stats as sps

chat_id = 12162367 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборки на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pvalue = sps.mannwhitneyu(x, y, alternative='less')[1]
    alpha = 0.09
    return pvalue < alpha # Ваш ответ, True или False
