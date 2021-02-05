# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:39:43 2018
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np 
import matplotlib.pyplot as plt 
from skimage.color import rgb2gray


temp = plt.imread( 'NonPy\CaM2.bmp' ) ;
tar  = plt.imread( 'NonPy\CaM.jpg' ) 
temp = rgb2gray( temp ) ;

def correl( im , ma ) :
    
    bb =  np.ones_like( ma ) ;
    bb[0,:] = bb[-1,:] = 0 ;
    bb[:,0 ] = bb[:,-1] = 0 ; 
    
    
    ret = np.zeros_like( im ) ; 
    r,c = im.shape
    mr, mc = [x //2 for x in ma.shape ] 
    
    for i in range(mr ,  r-mr ) :
        for j in range( mc , c-mc ):
            ret[i,j] = np.sum( im[i-mr:i+mr , j-mc : j+mc] * ma ) ;
    x,y = np.where( ret == np.max(ret) ) ; 
    return im[x[0]-mr:x[0]+mr , y[0]-mc : y[0]+mc] 
    
    


ret = correl ( tar  , temp );



plt.subplot( 2 , 2 ,1 ) ; 
plt.imshow( tar , cmap = 'gray' ) ;

plt.subplot( 2 , 2 ,2 ) ; 
plt.imshow( temp , cmap = 'gray' ) ;

plt.subplot( 2 , 2 ,3) ; 
plt.imshow( ret , cmap = 'gray' ) ;












