"""
__author__ = "Andrew PICORNELL"
__date__ = "Mercredi 14 Octobre"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // picornellandrew@gmail.com"
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""
import numpy as np
from numpy import *
# Attention dot marche que sur des matrice de meme taille:
#		colonne 1er matrice = ligne 2nd matrice 
#		(j'ai passe du temps comprendre le bails)
def mulmatrix(A,B):
	c = np.dot(A,B)
	return c
