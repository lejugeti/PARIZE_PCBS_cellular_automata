import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import random
a = np.load("matrice_test_plot.txt")


for i in range(10):
    sns.distplot(a[0, 1,0,1,:], hist = 0, color =(random(),random(),random()), label = "bonjour")
    plt.legend(loc = 0)
    plt.show()
