#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:23:08 2019

@author: azrahaseki
"""

# This program calculates and graphs the transmittance of pure water at 10 m, 
#1 m, 1 cm, and 1 micrometer. The values for the decadic absorbtivities for 
#pure water were taken from the 1980 paper "The Ultraviolet Absorption of 
#Liquid Water" by T.I. Quickenden and J.A. Irvin.

#importing useful libraries
import matplotlib.pyplot as plt                                      
from numpy import array, zeros

#creating wavelength array, assigning values from 196 to 320 nanometers
wavelength = array(range(196, 321))

#creating absorbtivity constant array of zeros
ab_const = array(zeros(125))

#assigning absorbtivity values taken from Quikenden paper, units 10^-2 m^-1
ab_const[0] = 126.0
ab_const[1] = 85.2
ab_const[2] = 56.7
ab_const[3] = 41.1
ab_const[4] = 32.4
ab_const[5] = 26.4
ab_const[6] = 23.0
ab_const[7] = 19.2
ab_const[8] = 16.8
ab_const[9] = 15.6
ab_const[10] = 15.0
ab_const[11] = 14.0
ab_const[12] = 13.4
ab_const[13] = 12.5
ab_const[14] = 12.6
ab_const[15] = 11.7
ab_const[16] = 11.4
ab_const[17] = 11.0
ab_const[18] = 10.6
ab_const[19] = 10.1
ab_const[20] = 9.88
ab_const[21] = 9.46
ab_const[22] = 9.31
ab_const[23] = 9.18
ab_const[24] = 8.05
ab_const[25] = 7.86
ab_const[26] = 7.37
ab_const[27] = 7.14
ab_const[28] = 7.00
ab_const[29] = 6.50
ab_const[30] = 6.69
ab_const[31] = 6.43
ab_const[32] = 6.15
ab_const[33] = 6.00
ab_const[34] = 5.95
ab_const[35] = 5.78
ab_const[36] = 5.42
ab_const[37] = 5.34
ab_const[38] = 5.35
ab_const[39] = 5.42
ab_const[40] = 5.10
ab_const[41] = 4.93
ab_const[42] = 4.52
ab_const[43] = 4.71
ab_const[44] = 4.83
ab_const[45] = 4.68
ab_const[46] = 4.39
ab_const[47] = 4.19
ab_const[48] = 4.05
ab_const[49] = 3.92
ab_const[50] = 3.99
ab_const[51] = 4.01
ab_const[52] = 3.92
ab_const[53] = 3.90
ab_const[54] = 3.76
ab_const[55] = 3.36
ab_const[56] = 3.51
ab_const[57] = 3.59
ab_const[58] = 3.48
ab_const[59] = 3.26
ab_const[60] = 3.23
ab_const[61] = 3.23
ab_const[62] = 3.06
ab_const[63] = 3.28
ab_const[64] = 3.08
ab_const[65] = 3.31
ab_const[66] = 2.79
ab_const[67] = 2.85
ab_const[68] = 2.73
ab_const[69] = 2.51
ab_const[70] = 2.64
ab_const[71] = 2.36
ab_const[72] = 2.33
ab_const[73] = 2.39
ab_const[74] = 2.36
ab_const[75] = 2.34
ab_const[76] = 1.96
ab_const[77] = 2.14
ab_const[78] = 2.25
ab_const[79] = 2.16
ab_const[80] = 1.98
ab_const[81] = 2.15
ab_const[82] = 2.08
ab_const[83] = 2.09
ab_const[84] = 2.22
ab_const[85] = 2.13
ab_const[86] = 1.80
ab_const[87] = 1.77
ab_const[88] = 1.85
ab_const[89] = 1.78
ab_const[90] = 1.75
ab_const[91] = 1.64
ab_const[92] = 1.68
ab_const[93] = 1.59
ab_const[94] = 1.63
ab_const[95] = 1.60
ab_const[96] = 1.57
ab_const[97] = 1.60
ab_const[98] = 1.51
ab_const[99] = 1.45
ab_const[100] = 1.44
ab_const[101] = 1.23
ab_const[102] = 1.14
ab_const[103] = 1.24
ab_const[104] = 1.24
ab_const[105] = 1.46
ab_const[106] = 1.08
ab_const[107] = 1.38
ab_const[108] = 1.27
ab_const[109] = 1.12
ab_const[110] = 1.22
ab_const[111] = 1.16
ab_const[112] = 1.04
ab_const[113] = 1.25
ab_const[114] = 1.12
ab_const[115] = 1.30
ab_const[116] = 1.19
ab_const[117] = 1.13
ab_const[118] = 1.01
ab_const[119] = 1.05
ab_const[120] = 0.96
ab_const[121] = 1.03
ab_const[122] = 0.93
ab_const[123] = 1.08
ab_const[124] = 1.00

#calculating transmittance for 10 m
T_10m = array(zeros(125)) #T_10m: array of transmittance values at 10 m
for x in range(125):
    k = ab_const[x] * 0.01 #k: absorbtivity, converting to m^-1
    T_10m[x] = 10 ** (-10 * k) #calculate transmittance and assign to relevant index
    
plt.plot(wavelength, T_10m, "ro") #plotting wavelength on the horizontal and transmittance on the vertical
plt.axis([190,350,0,1]) #setting axis maxima and minima 
plt.xlabel("Wavelength (nm)") #titling x axis
plt.ylabel("Transmittance") #titling y axis
plt.title("Transmittance of Pure Water at 10 m") #titling graph
plt.show() #display graph

#calculating transmittance for 1 m
T_m = array(zeros(125)) #T_m: array of transmittance values at 1 m
for x in range(125):
    k = ab_const[x] * 0.01 #k: absorbtivity, converting to m^-1
    T_m[x] = 10**(-k) #calculate transmittance and assign to relevant index
    
plt.plot(wavelength, T_m, "ro") #plotting wavelength on the horizontal and transmittance on the vertical
plt.axis([190,350,0,1]) #setting axis maxima and minima 
plt.xlabel("Wavelength (nm)") #titling x axis
plt.ylabel("Transmittance") #titling y axis
plt.title("Transmittance of Pure Water at 1 m") #titling graph
plt.show() #display graph

#calculating transmittance for 1 cm
T_cm = array(zeros(125)) #T_cm: array of transmittance values for 1 cm
for x in range(125):
    k = ab_const[x] * 0.01 #k: absorbtivity, converting to m^-1
    T_cm[x] = 10**(-k * 0.01) #calculate transmittance and assign to relevant index
    
plt.plot(wavelength, T_cm, "ro") #plotting wavelength on the horizontal and transmittance on the vertical
plt.axis([190,350,0,1]) #setting axis maxima and minima 
plt.xlabel("Wavelength (nm)") #titling x axis
plt.ylabel("Transmittance") #titling y axis
plt.title("Transmittance of Pure Water at 1 cm") #titling graph
plt.show() #display graph

#calculating transmittance for 1 micro metre
T_um = array(zeros(125)) #T_um: array of transmittance values for 1 micro metre
for x in range(125):
    k = ab_const[x] * 0.01  #k: absorbtivity, converting to m^-1
    T_um[x] = 10**(-k * (10 ** -6)) #calculate transmittance and assign to relevant index
    
plt.plot(wavelength, T_um, "ro")  #plotting wavelength on the horizontal and transmittance on the vertical
plt.axis([190,350,0,1]) #setting axis maxima and minima 
plt.xlabel("Wavelength (nm)")  #titling x axis
plt.ylabel("Transmittance")  #titling y axis
plt.title("Transmittance of Pure Water at 1 \u03BCm") #titling graph
plt.show() #display graph
















































































