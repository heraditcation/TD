"""
__author__ = "Andrew PICORNELL"
__date__ = "Lundi 5 Octobre"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // picornellandrew@gmail.com"
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""
from math import *
def module(a,b):
	mod = sqrt(a**2 + b**2)
	print("Le module est:")
	return mod

def argument(a,b):
	if (a > 0):
		argu = atan(b / a)
	elif (a < 0):
		if (b > 0):
			argu = atan(b / a) + pi
		else:
			argu = atan(b / a) - pi
	else:
		if (b > 0):
			argu = (pi/2)
		else:
			argu = -(pi/2)
	print("L'argument est:")
	return argu

print(module(3,4))
print(argument(3,4))
