# first line: 61
    @memory.cache
    def proportion_moyenne(nb_survie, nb_surpopulation, nb_naissance , proportion_initiale, TAILLE_GRILLE):
        """renvoie la proportion moyenne de la population finale après N générations"""
        pop = first_gen(proportion_initiale, TAILLE_GRILLE)
        final_gen = final_generations(pop, nb_survie, nb_surpopulation, nb_naissance, NB_GENERATION)
        return np.mean(final_gen)
