"""
__author__ = "Andrew PICORNELL"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // "
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""
largeur = float(input("Largeur du rectangle (cm): "))
longueur = float(input("Longueur du rectangle (cm): "))

if (largeur > longueur):
    print("Impossible, la largeur est forcement inferieur a la longueur")

else:
    peri = (largeur + longueur)*2
    print("Le rectangle a un perimetre de :", peri, "cm")
