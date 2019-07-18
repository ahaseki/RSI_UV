#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:58:03 2019

@author: azrahaseki
"""

#This program calculates and graphs the transmittance of the clearest modern 
#ocean waters at any depth passed to the function it defines, "graph". The 
#values for the diffuse attenuation coefficient for the irradiance for clearest
#ocean waters was taken from the 1981 paper "Optical Properties of the Clearest
#Natural Waters (200–800 nm)" by Raymond C. Smith and Karen S. Baker.

#importing useful libraries
import matplotlib.pyplot as plt
from numpy import array, zeros

#defining function to graph transmittance at desired depth, which takes one 
#argument of type integer or float, depth (specify in meters)
def graph(depth):
    trans = array(zeros(21)) #creating transmittance array of 21 zeros
    for x in range(21):
        k = ab_const[x] #assiging relevant attenuation value to k 
        trans[x] = 10 ** (depth * -1 * k) #calculating transmittance value
    plt.plot(wavelength, trans, "ro") #plotting wavelength on the horizontal and transmittance on the vertical
    plt.xlabel("Wavelength (nm)") #setting horizontal axis title
    plt.ylabel("Transmittance") #setting vertical axis title
    plt.title("Transmittance of the Clearest Modern Ocean Water at %f m" %(depth)) #setting graph title
    plt.axis([190,410,0,1]) #setting axis maxima and minima
    plt.savefig("%f_modernocean.pdf" %(depth)) #saving plot as pdf
    plt.show() #display plot

#creating wavelength array, assigning values incrementing by 10, 
#ranging from 200 to 400 nm
wavelength = array(range(200, 410, 10))

#creating diffuse attenuation constant array of zeros
ab_const = array(zeros(21))

#assigning diffuse attenuation constant values taken from Smith and Baker paper
#units m^-1
ab_const[0] = 3.14
ab_const[1] = 2.05
ab_const[2] = 1.36
ab_const[3] = 0.968
ab_const[4] = 0.754
ab_const[5] = 0.588
ab_const[6] = 0.481
ab_const[7] = 0.394
ab_const[8] = 0.306
ab_const[9] = 0.230
ab_const[10] = 0.154
ab_const[11] = 0.116
ab_const[12] = 0.0944
ab_const[13] = 0.0765
ab_const[14] = 0.0637
ab_const[15] = 0.0530
ab_const[16] = 0.0439
ab_const[17] = 0.0353
ab_const[18] = 0.0267
ab_const[19] = 0.0233
ab_const[20] = 0.0209

graph(10) #graphing transmittance at 10m
graph(1) #graphing transmittance at 1m
graph(0.01) #graphing transmittance at 1 cm
graph(0.000001) #graphing transmittance at 1 micro meter