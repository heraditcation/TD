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
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[0,2,4], [1,3,5], [1,5,9]])
c = np.dot(a,b)
print(c)
