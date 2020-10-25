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

def without(str1):
	strlen = len(str1)
	strrev = str1[strlen::-1]
	if (str1 == strrev):
		print(str1, "est un palindrome")
	else:
		print(str1, "n'est pas un palindrome")

def within(str2):
	strlen2 = len(str2)
	strrev2 = []
	while (strlen2 > 0):
		strrev2 += str2[strlen2 - 1]
		strlen2 = strlen2 - 1
	if (list(str2) == strrev2):
		print(str2, "est un palindrome")
	else:
		print(str2, "n'est pas un palindrome")

without("radar")
within("radar")
