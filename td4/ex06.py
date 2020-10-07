"""
__author__ = "Andrew PICORNELL"
__date__ = "Mercredi 7 Octobre"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // picornellandrew@gmail.com"
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""

def line(N,Plein):
	if (N == 1):
		print("*")
	if (N > 1):
		if (Plein == "True"):
			n = N * "*"
			print(n)
		elif (Plein == "False"):
			n = "*" + ((N-2) * " ") + "*"
			print(n)

def tri(B,Plein):
	x = 1
	if (Plein == "True"):
		while (x <= B + 1):
			line(x,"True")
			x = x + 1
		x = B 
		while (x <= B + 1 and x >= 1):
			line(x,"True")
			x = x - 1
	elif (Plein == "False"):
		while (x <= B + 1):
			line(x,"False")
			x = x + 1
		x = B
		while (x <= B + 1 and x >= 1):
			line(x,"False")
			x = x - 1

tri(3,"False")			
