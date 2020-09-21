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
fact = nbr
if (nbr < 0):
    print("0")
elif (nbr == 0 or nbr == 1):
    print("1")
while (fact > 1):
    nbr = nbr * (fact - 1)
    fact = fact - 1
print(nbr)
