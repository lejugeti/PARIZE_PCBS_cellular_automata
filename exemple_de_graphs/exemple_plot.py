"""programme pour plot un exemple de distributions de populations en fonction de
 l'ensemble des nombres de survie possible """

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import random

a = np.load("matrice_test_plot.txt")


for i_surpop in range(0,2): #nb surpopulation 3 et 4
    for i_naiss in [0]: #nb pour naissance 3
        for i_surv in range(0,8): #nb survie 2
            sns.distplot(a[i_surv, i_surpop,i_naiss,0,:], hist = 0, color =(random(),random(),random()), \
            axlabel = f'proportion avec i_surpop de {i_surpop+3}' ,label = f'i_surv = {i_surv}')
        plt.legend(loc = 0)
        plt.show()
