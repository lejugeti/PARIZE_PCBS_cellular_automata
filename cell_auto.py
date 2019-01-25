"""Programme simulant des proportions de population 100 fois pour chaque valeur des règles de l'automate.

Les résultats sont stockés dans un document texte pour pouvoir être réutilisés plus tard."""

import numpy as np
from math import sqrt
from joblib import Memory

def first_gen(proportion, shape):
    """ retourne un vecteur mélangé à une dimension contenant un nombre de 1
    correspondant à la proportion donnée en input
    input :
        proportion : proportion d'occupation de la grille par la population initiale

        shape : la forme de la matrice, qui peut ne pas être carrée

    output :
        population, vecteur de population initiale mélangé"""

    population = np.zeros(shape)
    population[1:-1, 1:-1] = np.random.binomial(1, proportion, (shape[0]-2, shape[1]-2))  #on insère des 1 dans une matrice plus petite pour ne pas gérer les bords
    #[1:-1] pour s'arrêter à l'avant dernière ligne/colonne
    return population

def next_generation(pop, nb_survie, nb_surpopulation, nb_naissance) :
    """renvoie la nouvelle génération n+1 à partir de pop en input"""
    new = np.zeros(pop.shape)  #création next generation remplie de 0. pop.shape pour avoir meme forme
    for ligne in range(1, pop.shape[0] - 1):
        for colonne in range (1, pop.shape[1] - 1):
            compteur_vie = scan(ligne,colonne, pop)
            if pop[ligne,colonne] == 1 :
                if compteur_vie < nb_survie:
                    new[ligne,colonne] = 0
                elif nb_survie <= compteur_vie < nb_surpopulation:
                    new[ligne,colonne] = 1
                elif compteur_vie >= nb_surpopulation :
                    new[ligne,colonne] = 0
            else:
                if compteur_vie >= nb_naissance :
                    new[ligne,colonne] = 1
    return new

def final_generations(pop, nb_survie, nb_surpopulation, nb_naissance, NB_GENERATION):
    """renvoie la dernière generation des n generations définies au préalable"""
    for i_generation in range(NB_GENERATION):
        pop = next_generation(pop, nb_survie, nb_surpopulation, nb_naissance)
        if np.mean(pop) == 0 or np.mean(pop) == 1:
            break
    return pop

def scan(m,n, pop):
    """scanne les 8 cellules environnantes et renvoie le nombre de cellules vivantes"""
    return np.sum(pop[(m-1):(m+2), (n-1) : (n+2)]) - pop[m,n]

#On crée un décorateur pour proportion_moyenne grâce à Memory de joblib pour
#mettre en cache les calculs déjà effectués comme il y a bcp de calculs à faire
memory = Memory('cache_cell_auto', verbose = 0)
@memory.cache
def proportion_moyenne(nb_survie, nb_surpopulation, nb_naissance , proportion_initiale, TAILLE_GRILLE, i_sim):
    """renvoie la proportion moyenne de la population finale après N générations"""
    pop = first_gen(proportion_initiale, TAILLE_GRILLE)
    final_gen = final_generations(pop, nb_survie, nb_surpopulation, nb_naissance, NB_GENERATION)
    return np.mean(final_gen)

if __name__ == "__main__":


    TAILLE_GRILLE = (100,100)
    NB_SURVIES = range(1,9)
    NB_SURPOPULATION = range(0,9)
    NB_NAISSANCE = range(1,9)
    PROP_INITIALE = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    N_SIM = 100
    NB_GENERATION = 50
    DECOMPTE_MESURES = len(NB_SURVIES)*len(NB_SURPOPULATION)*len(NB_NAISSANCE)*len(PROP_INITIALE)*N_SIM
    stats = np.zeros((len(NB_SURVIES),len(NB_SURPOPULATION), len(NB_NAISSANCE), len(PROP_INITIALE), N_SIM))

    compteur = 0
    for i_surv, nb_survie in enumerate(NB_SURVIES):
        for i_surpop, nb_surpopulation in enumerate(NB_SURPOPULATION):
            for i_naiss, nb_naissance in enumerate(NB_NAISSANCE):
                for i_prop, proportion_initiale in enumerate(PROP_INITIALE):
                    for i_sim in range(N_SIM):
                        stats[i_surv, i_surpop, i_naiss, i_prop, i_sim] = proportion_moyenne(nb_survie, nb_surpopulation, nb_naissance , proportion_initiale, TAILLE_GRILLE,i_sim)
                        compteur += 1
                        print(f'{round(compteur/DECOMPTE_MESURES, 2)} %    prop = {stats[i_surv, i_surpop, i_naiss, i_prop, i_sim]}')
                        #utile pour voir la progression de l'algorithme

stats.dump("matrice_cell_auto.txt")

print("""
FIN
""")
