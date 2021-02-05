# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:43:52 2018
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np 
import matplotlib.pyplot as plt 
import skimage


def harris( img ) :
    
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
    
        
    def differnMasksf( ) :
        fy = np.zeros((3,3) ) 
        fy[0,:] = [ -1, -2, -1] 
        fy[2,:] = [ 1, 2, 1]  ;
        return np.transpose(fy) , fy ;
        
    def gerdiantf( im) :
        fx , fy = differnMasksf() ;
        imx = convolvo( im , fx ) ;
        imy = convolvo( im ,fy ) ;
        return imx, imy 
    
    im= img.astype( np.float ) 
    ix,iy = gerdiantf( im ) ;
    ixy = ix*iy ; ix2 = ix**2 ; iy2= iy**2 ;
    r,c = im.shape 
    
    R= np.zeros_like( img ,np.float) ;
    E= np.zeros_like( img ,np.float) ;
    
    mr = mc = 2
    #construction Of E,R matrix
    for i in range( mr,r-mr ):
        for j in range( mc, c-mc ) :
            
            Ix2 = np.sum( ix2[i-mr:i+mr+1 , j-mc:j+mc+1] ) ;
            Iy2 = np.sum( iy2[i-mr:i+mr+1 , j-mc:j+mc+1] ) ;
            Ixy =  np.sum(ixy[i-mr:i+mr+1 , j-mc:j+mc+1] ) ;
            
            M = np.asarray( [[Ix2,Ixy] ,[Ixy,Iy2]], dtype= np.float ) ;
            E[i,j]= np.min(np.linalg.eigvalsh(M))
            R[i,j]= np.linalg.det(M) - .04*((Ix2+Iy2)**2) ;
    
    E -= np.min(E); E/=np.max(E);
    
    R -= np.min(R);R/=np.max(R);
    
    E = skimage.img_as_ubyte(E) ;
    R = skimage.img_as_ubyte(R) ;
    
    return E,R 
    
img1 = plt.imread( 'NonPy\Mah.jpg' ) ;
r, g, b = img1[:,:,0], img1[:,:,1], img1[:,:,2]
img = 0.2989 * r + 0.5870 * g + 0.1140 * b
E,R = harris( img ) ; 

plt.imshow( img1 ,cmap= 'gray') 
x,y = np.where( E> 128 );

plt.plot( y,x,'r+') 
plt.show() 
            
            
    
    
    
    
    
    
    
    
    
    
    