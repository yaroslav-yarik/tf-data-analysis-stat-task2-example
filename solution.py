import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 561049466 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #b = np.var(x) ** 0.5 * 2 + 0.098
    #mu = (b + 0.098) / 2
    #eps = p / 2 / (b - 0.098)
    mu = np.mean(x)
    eps = (mu - 0.098) * p
    return (mu-eps, mu + eps)
