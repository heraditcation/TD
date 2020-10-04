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

mois = "Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout" \
,"Septembre", "Octobre", "Novembre", "Decembre"
n = int(input("Nombre? "))
if n <= 12 and n >= 1:
	print(mois[n-1])
else:
	print("Il n'y a que 12 mois dans l'année, IDIOT")
