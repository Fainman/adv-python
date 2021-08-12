#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/12/2021
Purpose: Explore SciPy
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# --------------------------------------------------
def get_data():
    ages = np.genfromtxt('ages.csv', delimiter=',', skip_header=1)
    # print(ages)  # 2d array
    years = ages[:, 0] # full slice of the first element
    males = ages[:, 1]
    # print(x)
    # print(males)
    # Here years and males are values to approximate some function: males = f(years)
    # print(type(males))
    f = interp1d(years, males)
    new_years = [1896, 1907, 1923, 1929, 1933, 1939, 1947 ,1953, 1969, 1989, 1996, 1998]
    new_males = f(new_years)
    print(new_males)

    plt.plot(years, males, '-', new_years, new_males, 'o')
    plt.show()



def main():
    """Make your noise here"""
    get_data()


# --------------------------------------------------
if __name__ == '__main__':
    main()
