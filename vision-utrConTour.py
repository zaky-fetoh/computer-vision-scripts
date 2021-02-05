# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 05:05:25 2018
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np 
import matplotlib.pyplot as plt 


di = [0, -1 ,0 ,1 ] ; 
dj = [1, 0 ,-1 ,0  ] ; 

  
def iDFS( im, ik, jk ) :
    r,c = im.shape
    Stk = list() ; 
    Stk .append( (ik,jk) ) 
    
    cont = np.zeros_like( im ) ; 
    
    
    while len(Stk ):
        i,j = Stk[-1] ; del Stk[-1] ; 
        im[i,j] = 2 
        
        for k in range( len(di) ):
            ni,nj = i+di[k] , j+dj[k] ; 
            if 0 <= ni < r and 0 <= nj < c :
                if im[ni,nj]== 1  : 
                    Stk.append( (ni,nj) ) 
                elif im[ni,nj] == 0 : 
                    cont[i,j] = 255
    return cont 

def ocont( im ) :
    r,c = im.shape 
    cont = np.zeros_like( im ) ; 
 
    for i in range( r ) :
        for j in range( c) :
            if im[i,j] == 255 :
                cont =cont +  iDFS( im , i, j ) ;
    return cont  
                