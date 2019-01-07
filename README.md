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
- 2 ) plus le nb nécessaire pour les naissances augmente moins la proportion finale est grande
- 3 ) plus le nb pour avoir une surpopulation sera grand plus la proportion sera grande
- 4 ) plus la proportion initiale sera haute plus la proportion finale sera grande sauf pour la plus haute valeur 0.9 car surpopulation.

Résultats
--

Malheureusement, comme le programme demande une grande puissance de calcul et prend beaucoup de temps, je n'ai pas pu calculer les données par manque de matériel. J'ai essayé d'implémenter la mise en cache proposé par le module joblib pour pouvoir reprendre les calculs plusieurs fois, mais le programme ne calculait pas correctement les valeurs. En fait, il assignait la même valeur à toutes les simulations, j'ai donc abandonné. Il serait néanmoins intéressant d'implémenter cette mise en cache et un traitement parallèle des calculs grâce à ce module pour pouvoir réaliser les simulations assez rapidement.

Comme je n'ai pas pu calculer les données par manque de puissance de calcul, j'ai réalisé un fichier d'exemple de plot possible dans le dossier "exemple_de_graphs". En faisant tourner le fichier "exemple_plot.py", vous aurez un aperçu des distributions des proportions de cellules pour toutes les valeurs de survie en fonction de variables fixées arbitrairement. J'avais prévu au départ de limiter les graphs à certaines valeurs de survie, naissance, surpopulation et proportions initiales comme en témoigne le fichier "distplot.py", et c'est donc un peu ce que j'ai fait dans "exemple_plot.py".
Il serait intéressant de réaliser des stats sur les données pour voir si les distributions sont différentes, et si leur dispersion le sont également, comme le suggèrent les graphs générés par "exemple_plot.py".


Ce que j'ai appris avec ce projet
--
En créant ce projet j'ai appris à manipuler numpy et les array du module. J'ai aussi pu voir des affichages graphiques simples grâce à pygame.
J'ai aussi été légèrement introduit aux représentation graphiques des données avec matplotlib.pyplot et seaborn.

J'ai aussi appris à "manipuler" github grâce au terminal. Je trouve ça super car ça m'a vraiment facilité la vie pendant les vacances, comme je travaillais tantôt sur un pc chez moi tantôt sur un autre lorsque j'étais en déplacement. J'aimerais bien faire un projet plus important et en groupe pour continuer à l'utiliser et à apprendre comment ça fonctionne (créer plusieurs branche, les fusionner ou même revenir à une version précédente du projet), car je n'ai pour l'instant utilisé que peu de commandes.
