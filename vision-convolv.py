# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 07:06:09 2018
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np
import matplotlib.pyplot as plt 


def convolv( im , ma ) :
    
    ret = np.zeros_like( im ) ; 
    r,c = im.shape
    mr, mc = [x //2 for x in ma.shape ] 
    
    for i in range(mr ,  r-mr ) :
        for j in range( mc , c-mc ):
            ret[i,j] = int(np.sum( im[i-mr:i+mr+1 , j-mc : j+mc+1] * ma ) ) ;
    return ret ; 

def med( im ) :
    ma  = np.ones( (3,3) ) 
    ret = np.zeros_like( im ) ; 
    r,c = im.shape
    mr, mc = [x //2 for x in ma.shape ] 
    
    for i in range(mr ,  r-mr ) :
        for j in range( mc , c-mc ):
            ret[i,j] = np.median( im[i-mr:i+mr+1 , j-mc : j+mc+1] * ma )  ;
    return ret ; 



def guass( n, m, sig= 1 ) :
    def G( n,m ) :
        return (1/(2*np.pi* sig**2 )) * np.e **(-( n**2 + m**2 )/2*sig**2)
    ma = np.zeros((n,m)) ;
    ns,ms = n//2 , m//2 
    for i in range( n ) :
        for j in range( m) :
            ma[i,j] = G( i-ns , j-ms ) ;
    return ma


def unshapping_filer( im ) :
    return im + ( im - convolv( im , guass( 3,3 ) ) ) 


def smoth( I ) :
    return convolv( I , guass( 5,5 ,2 ) ) 
    
    
#mask = np.ones( (7,7) ) * 1/49 ; 
mask = guass( 3,3 ) 

Im2 = plt.imread( 'NonPy\CaM.jpg' ) ; 

Im = convolv( Im , mask ) 
plt.subplot( 2 , 1 , 1 ) 
plt.imshow(Im , cmap = 'gray' ) ;
 
plt.subplot( 2 , 1 , 2 ) 
plt.imshow(Im2 , cmap = 'gray' ) ;

