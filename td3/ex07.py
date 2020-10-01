"""
__author__ = "Andrew PICORNELL"
__date__ = "Jeudi 1 Octobre"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // picornellandrew@gmail.com"
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""

liste = ["T","O","A","p","t","p","l","o","e","s","t","t","r","s","t","t","t","u","m","m","p"]
# Methode avec le slicing (plus simple avec 'enumerate')
print(liste[0::2])

# Methode avec enumerate (en com pour pas faire bug le code)
""" 
for id, elem in enumerate(liste):
 	if id % 2 == 0:
		print(elem)
"""
# On associe a une liste son indice(id) et sa valeur(elem)
# On fais un modulo 2 pour regarder les indince pair
# Ex: 2 % 2 = 0 mais 3 % 2 = 1 
# On a donc pour tt les nombre pair x % 2 = 0
# Ainsi on affiche elem 
