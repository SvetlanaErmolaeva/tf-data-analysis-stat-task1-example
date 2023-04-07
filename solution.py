import pandas as pd
import numpy as np


chat_id = 411069874 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 10
    n = len(x)
    mu = -29
    sigma = np.exp(1)
    errors = np.random.normal(mu, sigma, n)
    a = errors/t
    return a.mean()
