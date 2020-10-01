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

a = "tomate", 2, 3, 10 		# Création d'un tuple (vérification possible avec 'type')
print(a[0]) 				# Affiche le premier élément du tuple, donc "tomate"
# Fonctionnement de 'for' particulier, 'while' est plus facile d'utilisation
for i in a: 
	print(i)
# Utilisation de in pour check si il y a un élément de a
if "tomate" in a:
	print("Oui, l'élément est dans le tuple")
else:
	print("Non, l'élément n'est pas dans le tuple")
# Affiche la longeur grace a "l'opérateur" 'len'
print(len(a))
# Methode simple pour une valeur mais on se perd vite si trop de valeur
# donc peu fiable mais la suffit largement (a vous de voir)
add = input("Ajoute? ")
a = a + (add,)
print(a)
# Supprime la variable donc supprime le typle (check avec 'print(a)')
del a
