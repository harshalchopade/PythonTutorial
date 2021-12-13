#Till now we have worked with single dimension array
#To use multi dimensional array (2D, 3D etc) we need to install numpy package as python doesn't suppot multi-dim array.
# We can also work with single dimension array as well.
#When we declare multi-dim array not necessaary to mention type of array
#e.g arr = array([1,2,3,4],[3,4,5,6])

#But if still want to mention then use below syntax
#arr = array([1,2,3,4],[3,4,5,6], int)

#Before that we need to use install numpy pacakge.
#Go to Settings (ctrl+alt+s).
#Project > Select Project (by default).
#Select on Python Interpreter.
#Click on '+' icon > open another window.
#Search numpy in that and click on install package button.

from numpy import *
arr = array([1,2,4],[3,4,5,6])
print(arr)

#Also to install numpy on cmd prompt
#Open cmd prompt type 'pip3 install numpy'
#To update pip package type python.exe -m pip install --upgrade pip
