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

a = input("first string?")
b = input("second string?")
if (len(a) > len(b)):
	print(a)
elif (len(a) < len(b)):
	print(b)
else:
	print("a est aussi grand que b")
