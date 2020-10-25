"""
__author__ = "Andrew PICORNELL"
__date__ = "Mardi 20 Octobre"
__copyright__ = "Copyright 2020, All rights reserved"
__version__ = "1.0.0"
__email__ = "andrew.picornell@etu.u-pec.fr // picornellandrew@gmail.com"
__github__ = "https://github.com/heraditcation"
__linkedin__ = "https://www.linkedin.com/in/andrewpicornell/"
__status__ = "C/Python Dev + Master Git/Shell (zsh/sh)"
"""
import numpy as np
from numpy import *
from random import *

def partition(n):
	a = np.random.uniform(0,1,n)
	b = np.array([0,1])
	c = np.concatenate((a,b),axis=None)
	c = np.sort(c)
	print(c)

partition(9)
