# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:11:24 2018
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
    return np.arctan( imx / imy ) ; 




    