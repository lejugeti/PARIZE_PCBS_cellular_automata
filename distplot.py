import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

a = np.load("matrice_cell_auto.txt")


sns.distplot(a[0,0,0,0,:], color =(0,0,0.25))
sns.distplot(a[0,1,0,0,:], color =(0,0,0.5))
sns.distplot(a[1,0,0,0,:], color =(0,0,0.75))
sns.distplot(a[1,1,0,0,:], color =(0,0,1))

plt.legend()
plt.show()
