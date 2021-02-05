# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:19:32 2018
@author: MahZaky
<<< SirMahZaky >>>
"""
import numpy as np 
import matplotlib.pyplot as plt


def freq( im ) :
    #im is agray image range from 0->255
    if im.dtype != np.uint8 :
        return 
    A = np.zeros((256,) ) ;
    for r in im :
        for e in r :
            A[e] += 1 ;
    return A 

def Strtch( A , old , new ) :
    a,b = old ; c,d = new ; 
    def f( x ) :
        if x < a or x > b :
            return a 
        return int(np.round( ( x-a)*(d-c)/(b-a) + c ) ) 
    oldtr = A[a:b+1].copy() ; A[a:b+1] = 0 
    for i in range( a,b+1 ) :
        A[ f(i) ] += oldtr[ i-a ] ;
    #l00k UP table 
    lk = np.zeros( (256, )) 
    for i in range( 256 ) :
        lk[i] = f( i) ; 
    return lk 

def effstr( lk , ima ) :
    im = ima.copy()
    r,c = im.shape 
    for i in range( r ) :
        for j in range( c ):
            im[i,j] = lk[im[i,j]] 
    return im 

def equali( A , L ) :
    acc = np.zeros_like( A ) 
    for i in range (A.size ) :
        acc[i] = sum( A[0:i+1] ) ; 
    p = (L-1)/acc[-1] ; 
    lk = np.zeros_like( A ) ;
    for i in range( lk.size ) :
        lk[ i ] = int (np.round(acc[i]*p) )  
    return lk 



    
plt.subplot( 2 , 2 , 1 ) ; 
A = plt.imread( "NonPy\CaM.jpg" ) ; 
fr = freq( A ) ;
plt.imshow( A , cmap = 'gray' ) ;
plt.subplot( 2 , 2 , 2 ) ; 
plt.plot( fr ) ;
lk = Strtch( fr , (150,200) , (50 , 255 ) ) ;
A = effstr( lk , A ) ;
plt.subplot( 2 , 2 , 3 ) ;   
plt.imshow( A  , cmap = 'gray') ; 
plt.subplot( 2 , 2 , 4 ) ; 
plt.plot( fr   )


