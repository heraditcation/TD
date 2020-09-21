"""
__author__ = "Andrew PICORNELL"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // "
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""
nbr = int(input("Nombre: "))
while (nbr < 10 or nbr > 20):
	if (nbr < 10):
		print("Plus grand !")
		nbr = int(input("Nombre: "))
	elif (nbr > 20):
		print("Plus petit !")
		nbr = int(input("Nombre: "))
if (nbr >= 10 and nbr <= 20):
	print(nbr)
