# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:13:08 2018
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np 
import matplotlib.pyplot as plt 


def prymid( Img ) :
        
    def convolvo( im , ma ) :
        
        ret = np.zeros_like( im ,dtype = np.float ) ; 
        r,c = im.shape
        mr, mc = [x //2 for x in ma.shape ] 
        
        for i in range(mr ,  r-mr ) :
            for j in range( mc , c-mc ):
                ret[i,j] = (np.sum( im[i-mr:i+mr+1 , j-mc : j+mc+1] * ma ) ) ;
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
    
    
    
    def smoth( I ) :
        return convolvo( I , guass( 5,5 ,2 ) ) 
    
    pry= list() 
    pry.append( Img.copy() ) ;
    G= guass(5,5,2 ) ;
    
    def Red( I) :
        r,c = I.shape
        ret = np.zeros( (r//2,c//2),dtype =np.uint8 );
        for i in range( r//2 ) :
            for j in range( c//2 ) :
                
                for ik in range(5) :
                    for jk in range(5):
                        ci,cj = ik-2 , jk-2
                        ii,jj = int(2*i+ci) , int(2*j+cj)
                        if 0<= ii < r and 0<= jj < c :
                            ret[i,j] +=int( G[ik,jk]*I[ii,jj] )
                            
        return ret 
        
    
    for i in range( 5 ) :
        nIm = smoth( pry[i] ) ; nIm = nIm[::2,::2] #Red( nIm )  
        nIm= smoth(nIm) 
        pry.append( nIm.copy() )
        
    return pry 
    
    
    
    
    
    
    
    
    
    