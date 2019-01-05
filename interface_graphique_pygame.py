import numpy as np
import pygame
from math import sqrt
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH,HEIGHT = 500,500
cote = 5    #coté des carrés affichés
NB_GENERATION = 50

def dessin(cote,next_gen):
    """fonction pour dessiner"""

    for ligne in range(len(next_gen)):
        for colonne in range(len(next_gen[1])):
            if next_gen[ligne,colonne] == 1:
                pixel = pygame.Rect(colonne*cote, ligne*cote, cote, cote)
                pygame.draw.rect(screen, BLACK, pixel)

def first_gen(proportion,TAILLE_GRILLE):
    """ retourne un vecteur mélangé à une dimension contenant un nombre de 1
    correspondant à la proportion donnée en input
    input :
        proportion : proportion d'occupation de la grille par la population initiale

    output :
        population, vecteur de population initiale mélangé"""

    population = np.zeros(TAILLE_GRILLE)
    for index in range(int(TAILLE_GRILLE*proportion)):
        population[index] = 1
    np.random.shuffle(population)
    return population.reshape(int(sqrt(TAILLE_GRILLE)),int(sqrt(TAILLE_GRILLE)))

def next_generation(pop, nb_survie, nb_surpopulation, nb_naissance) :
    """renvoie la nouvelle génération n+1 à partir de pop en input"""
    new = np.zeros((len(pop),len(pop[1])))  #création next generation remplie de 0
    for ligne in range(len(pop)):
        for colonne in range (len(pop[1])):
            compteur_vie = scan(ligne,colonne,pop)
            if pop[ligne,colonne] == 1 :
                if compteur_vie < nb_survie:
                    new[ligne,colonne] = 0
                elif nb_survie <= compteur_vie < nb_surpopulation:
                    new[ligne,colonne] = 1
                elif compteur_vie >= nb_surpopulation :
                    new[ligne,colonne] = 0
            if pop[ligne,colonne] == 0:
                if compteur_vie >= nb_naissance :
                    new[ligne,colonne] = 1
    return new

def final_generations(pop, nb_survie, nb_surpopulation, nb_naissance):
    """renvoie la dernière generation des n generations définies au préalable"""
    for i_generation in range(NB_GENERATION):
        pop = next_generation(pop, nb_survie, nb_surpopulation, nb_naissance)
    return pop

def scan(m,n, pop):
    """scanne les 8 cellules environnantes"""
    return np.sum(pop[(m-1):(m+2), (n-1) : (n+2)]) - pop[m,n]

TAILLE_GRILLE = 49
nb_survie = 2
nb_surpopulation = 4
nb_naissance = 3
#proportion_initiale = 0.5
if __name__ == "__main__":
    TAILLE_GRILLE = 10000
    nb_survie = 2
    nb_surpopulation = 2
    nb_naissance = 3
    proportion_initiale = 0.05

    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    done = False
    while not done :
        pop = first_gen(proportion_initiale, TAILLE_GRILLE)

        for loop in range(50):
            screen.fill(WHITE)
            pop = next_generation(pop, nb_survie, nb_surpopulation, nb_naissance) #on attribue la next_gen
            dessin(cote, pop)
            pygame.display.update()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
                            pygame.quit()
            if done == True:
                break
