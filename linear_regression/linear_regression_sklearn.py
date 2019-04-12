import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    df = pd.read_csv('../DATA/data.csv')

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]


   

    model = LinearRegression()
    model.fit(x, y)