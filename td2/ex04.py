"""
__author__ = "Andrew PICORNELL"
__date__ = "[DATE DU PROJET]"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // picornellandrew@gmail.com"
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""
choix = input("Choix? ")
if (choix == "a" or choix == "A"):
	N = int(input("Nombre? "))
	count = N
	n = N
	while (count > 0):
		N = (N - 1) + (count - 1)
		count = count - 1
	print(N)
	n = n * (n - 1) / 2	
	print(n)
elif (choix == "b" or choix == "B"):
	N = int(input("Nombre? "))
	fact = N
	count = N
	if (N < 0):
		print("0")
	elif (N == 0 or N == 1):
		print("1")
	elif (N > 1):
		while (fact > 1):
			N = N * (fact - 1)
			fact = fact - 1
		N = N // count
		print(N)
else:
	print("Choix non valide")
