# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:38:56 2018
@author: MahZaky
<<< SirMahZaky >>>
"""



import scipy.misc as misc 
import numpy as np
import matplotlib.pyplot as plt 


def mag( x ) :
    return np.sqrt( x[1]**2 + x[0]**2 + x[2]**2 ) 


o =plt.imread( r'NonPy\PRclf400s.png' )
f = np.asarray(o , dtype=np.float32 ) 
r,c,h = f.shape
magn = np.zeros( (r,c) , dtype = np.float32 ) ; 

for i in range( r ) :
    for j in range( c) :
        x = mag( f[i,j,:] ) ;
        if x :
            f[i,j,:] =f[i,j,:] / x
        magn[ i,j ] = x ;
        
plt.subplot( 1, 3 ,1) 
plt.imshow( f ) 
plt.subplot( 1,3,2) 
plt.imshow( o ) ;
plt.subplot( 1,3,3)
plt.imshow(magn , cmap = 'gray' ) 
 
plt.show()  
