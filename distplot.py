import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

a = np.load("matrice_cell_auto.txt")


sns.distplot(a[0,0,0,0,:], hist = 0, color =(0,0,0.25), label = "beebe")
sns.distplot(a[0,1,0,0,:],  hist = 0,color =(0,0,0.5), label = "allez")
sns.distplot(a[1,0,0,0,:], hist = 0, color =(0,0,0.75), label = "bim")
sns.distplot(a[1,1,0,0,:], hist = 0, color =(0,0,1), label = "message")

plt.legend(loc = 0)
plt.show()
