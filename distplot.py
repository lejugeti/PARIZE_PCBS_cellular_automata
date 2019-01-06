"""programme générant les représentations graphiques des distributions de proportion de
population pour les différentes hypothèses énoncées dans le README.md"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import random

a = np.load("matrice_cell_auto.txt")

#plot pour la survie
for i_surpop in [5,7]: #nb surpopulation 4 et 6
    for i_naiss in [1,2]: #nb pour naissance 2 et 3
        for i_surv in range(0,9):
            sns.distplot(a[i_surv, i_surpop,i_naiss,3,:], hist = 0, color =(random(),random(),random()), label = f'i_surv = {i_surv}')
        plt.legend(loc = 0)
        plt.show()

#plot pour les naissances
for i_surv in [1,3]: #nb de naissance 2 et 4
    for i_surpop in [3,5]: #nb de survie 2 et 3
        for i_naiss in range(1,9):
            sns.distplot(a[i_surv, i_surpop,i_naiss,3,:], hist = 0, color =(random(),random(),random()), label = f'i_naiss = {i_naiss}')
        plt.legend(loc = 0)
        plt.show()

#plot pour la surpopulation
for i_surv in [1,3]: #nb de naissance 2 et 4
    for i_naiss in [1,2]: #nb pour naissance 2 et 3
        for i_surpop in range(0,9):
            sns.distplot(a[i_surv, i_surpop,i_naiss,3,:], hist = 0, color =(random(),random(),random()), label = f'i_surpop = {i_surpop}')
        plt.legend(loc = 0)
        plt.show()

#plot pour la proportion initiale
for i_surv in [1,3]: #nb de naissance 2 et 4
    for i_surpop in [3,5]: #nb de survie 2 et 3
        for i_naiss in [1,2]: #nb pour naissance 2 et 3
            for i_prop in range(0,8):
                sns.distplot(a[i_surv, i_surpop,i_naiss,3,:], hist = 0, color =(random(),random(),random()), label = f'i_surpop = {i_surpop}')
            plt.legend(loc = 0)
            plt.show()
