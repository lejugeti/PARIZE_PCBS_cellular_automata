**Automate Cellulaire et distributions de populations**
==

Le but du projet était de créer un automate cellulaire sur la base des règles
de l'automate de Cohen, puis de comparer des distributions de populations.
Cet automate se base sur une population initiale de cellules distribuées sur
une grille de 100 cases par 100, et conçoit les générations futures en fontion
de l'organisation de l'ensemble des cellules.

En fait, pour chaque case de la grille, l'automate va scanner les 8 cases
directement adjacentes à la case d'intérêt, et va déterminer son état, à savoir
"vivant" ou "mort", en fonction du nombre de cases vivantes. Cela est effectué grâce à la fonction scan définie dans le programme.

    def scan(m,n, pop):
        """scanne les 8 cellules environnantes et renvoie le nombre de cellules vivantes"""
        return np.sum(pop[(m-1):(m+2), (n-1) : (n+2)]) - pop[m,n]

L'ensemble des règles utilisées par l'algorithme sont listées ci-dessous :
- Le nombre de cellules nécessaire pour la survie d'une cellule
- Le nombre de cellules nécessaire à la naissance d'une cellule
- Le nombre de cellules entraînant une mort par surpopulation

Trois algorithmes ont été utilisés dans mon projet : l'automate cellulaire à
proprement parler contenu dans "cell_auto.py", un algorithmes créé pour
réaliser les représentations graphiques des distributions de proportions de
population, et un algorithme de test contenu dans "test.py" incluant une
interface graphique pygame qui m'a aidé à la création et au debogage de mon
algorithme final (jouer avec la représentation graphique était très amusant par ailleurs pour voir les progressions des populations).

Comme je l'ai dit plus haut le but était de comparer des distributions de populations créées par l'automate à partir d'un nombre fini de population initiales et de générations successives, tous deux déterminés arbitrairement.

Pour ce faire j'ai implémenté dans mon programme plusieurs boucles faisant
varier les règles énoncées auparavant : nb_survie de 0 à 8, nb_surpopulation de
1 à 8, et le nombre de naissance de 1 à 8. J'ai aussi fait varier la proportion
initiale de cellules vivantes de la première population entre 0.1 et 0.9.
Pour chaque condition, 100 simulations ont été effectuées sur la base de 50
générations consécutives chacunes.

    NB_SURVIES = range(0,9)
    NB_SURPOPULATION = range(1,9)
    NB_NAISSANCE = range(1,9)
    PROP_INITIALE = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    N_SIM = 100
    NB_GENERATION = 50
    for i_surv, nb_survie in enumerate(NB_SURVIES):
        for i_surpop, nb_surpopulation in enumerate(NB_SURPOPULATION):
            for i_naiss, nb_naissance in enumerate(NB_NAISSANCE):
                for i_prop, proportion_initiale in enumerate(PROP_INITIALE):
                    for i_sim in range(N_SIM):
                        stats[i_surv, i_surpop, i_naiss, i_prop, i_sim] = proportion_moyenne(nb_survie, nb_surpopulation, nb_naissance , proportion_initiale, TAILLE_GRILLE)

La valeur retenue pour chaque simulation était la proportion de cellules
"vivantes" occupant la grille après les 50 générations consécutives.

Le projet demandant de gérer un grand nombre de données, j'ai stocké toutes les mesures dans une matrice numpy à 5 dimensions, puis j'ai utilisé la fonction `dump()` de numpy qui écrit et sauvegarde un objet numpy dans un fichier texte.

    stats.dump("matrice_cell_auto.txt")

Pour récupérer la matrice à partir du fichier créé, j'ai utilisé la fonction
`load()` de numpy, qui permet de charger un objet numpy à partir d'un fichier texte.

    import numpy as np
    stats = np.load("matrice_cell_auto.txt")

Pour réaliser les représentations graphique j'ai utilisé la fonction `distplot()` du module seaborn, et le module pyplot de matplotlib.
Par exemple :

    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    a = np.load("matrice_cell_auto.txt")
    sns.distplot(a[0,0,0,0,:], hist = 0, color =(0,0,0.25), label = "bonjour")
    #On signifie que hist=0 pour avoir seulement les courbes des distributions
    plt.legend(loc = 0) #avec 0 pour la meilleure position de légendes
    plt.show()

Hypothèses
--

- 1 ) plus le nb de survie augmente plus la prop est grande
- 2 ) plus le nb nécessaire pour les naissance augmente moins la prop est grande
- 3 ) plus le nb de surpopulation est grand plus la proportion sera grande
- 4 ) plus la proportion initiale sera haute plus la proportion finale sera grande saufpour la plus haute valeur 0.9 car surpopulation.
