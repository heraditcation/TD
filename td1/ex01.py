"""
__author__ = "Andrew PICORNELL"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // "
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""
art = float(input("Prix de l'article: "))
tps = (art / 100) * 5
tvq = (art / 100) * 7.5
taxes = tps + tvq
print(taxes)
price = taxes + art
pay = float(input("Monnaie que je donne: "))
change = pay - price
if (change > 0):
    print("Je vous rend: ", change)
elif (change < 0):
    change = -change
    print("Vous me devez: ", change)
else:
    print("Vous avez donne pile le bon montant, il reste: ", change)
