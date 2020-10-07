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

def degree(tCel):
	tFahr = (9/5)*tCel + 32
	return tFahr

print("La température en Fahrenheit est:", degree(100))
