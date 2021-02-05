# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 07:56:17 2018
@author: MahZaky
<<< SirMahZaky >>>
"""
import numpy as np 
import matplotlib.pyplot as plt 

#roprt
def convol( I , m ) :
    r , c = I.shape 
    Nw = np.zeros_like( I ) ; 
    
    for i in range (r-1) :
        for j in range(c-1) :
            Nw[i,j] = np.sum( I[i:i+2 , j:j+2] *m ) 
    return Nw 
            

def ropertfiltr( I ):
    Mm = np.asarray( [ [1 , 0],[0, 1] ] , dtype = np.int8 ) ;
    Mp = np.asarray( [ [0 , 1],[-1,0] ] , dtype = np.int8 ) ;
    M1 = convol( I , Mm ) ; M2 = convol( I , Mp ) ; 
    Nw = np.zeros_like( I ) ;
    r,c = Nw.shape 
    for i in range( r ) :
        for j in range( c) :
            Nw[i,j] = max( M1[i,j] , M2[i,j] ) ;
    return Nw 

#prewitt and Sopel 
     

def convolv( im , ma ) :
    
    ret = np.zeros_like( im ,dtype = np.int16 ) ; 
    r,c = im.shape
    mr, mc = [x //2 for x in ma.shape ] 
    
    for i in range(mr ,  r-mr ) :
        for j in range( mc , c-mc ):
            ret[i,j] = int(np.sum( im[i-mr:i+mr+1 , j-mc : j+mc+1] * ma ) ) ;
    return ret ; 


def differnMasks( ) :
    fy = np.zeros((3,3) ) 
    fy[0,:] = [ -1, -1, -1] 
    fy[2,:] = [ 1, 1, 1]  ;
    return np.transpose(fy) , fy ;

def gerdiant( im) :
    fx , fy = differnMasks() ;
    imx = convolv( im , fx ) ;
    imy = convolv ( im ,fy ) ;
    return imx, imy 

def magni( imx , imy ) :
    return np.sqrt( imx**2 + imy**2 ) ;

def direct (imx , imy )  :
    return np.arctan( imy / imx ) ; 
















    
    
    
    
def canny ( img ) :
       
    
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
    
    
    im = img.astype( np.float ) 
    im = smoth( im ) 
    imx,imy = gerdiantf( im ) 
    mag=  magni( imx , imy ) 
         
    theta =np.degrees( direct( imx ,imy )*2+ np.pi);
    theta =( (theta +22.5) % 360 ) // 45 
    theta =theta.astype( np.int ) 
    theta[np.where( theta < 0  ) ] = 0 
    
    di=[0 , -1, -1, -1, 0 , 1, 1, 1]
    dj=[1 ,  1,  0, -1,-1 ,-1, 0, 1]
    #maxsup ression 
    sup = np.zeros_like(mag) 
    r,c = sup.shape 
    for i in range( 1 , r-1 ):
        for j in range(1, c-1) :
            d=theta[i,j] ; d1 = (d+4)%8;
            curr= mag[i,j];e1= mag[i+di[d],j+dj[d]];
            e2= mag[i+di[d1],j+dj[d1]];
            if curr > e1 and curr > e2 :
                sup[i,j]  = mag[i,j] 
    #Tresholding 
    tr = sup.mean() ; ltr = tr/6
    
    for i in range(1 , r-1 ) :
        for j in range(1, c-1 ) :
            if ltr <= sup[i,j] < tr :
                for k in range( 8 ):
                    if sup[i + di[k] , j+dj[k] ] != 0 :
                        sup[i,j] = mag[i,j]
                        
    for i in range(1 , r-1 ) :
        for j in range(1, c-1 ) :
            if ltr <= sup[i,j] < tr :
                for k in range( 8 ):
                    if sup[i + di[k] , j+dj[k] ] != 0 :
                        sup[i,j] = mag[i,j]
    
    return sup 
     
    


def edgPrewitt( I ) :
    imx , imy = gerdiant( I ) ;
    return magni( imx, imy  ) ;

import scipy.misc as misc 
import skimage


'''
    
    

face = misc.face( True ) ; 

prewitt = edgPrewitt( face ) ; 

prewitt /= 255

prewitt = skimage.img_as_ubyte ( prewitt ) 

plt.imshow( prewitt , cmap = 'gray' ) 

'''



















    