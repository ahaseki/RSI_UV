#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:20:04 2019

@author: azrahaseki
"""
#This program calculates and graphs the transmittance of the different 
#freshwaters at any depth passed to the function it defines, "graph". The 
#values for the coefficient of absorption for different freshwater sources
#was taken from the 1933 paper "Transmission of Ultraviolet Radiation by Water"
#by Charles D Hodgeman. The sources of freshwater for which absorption can be 
#graphed are distilled water (referred to in this program as "distilled"), water
#taken from Lake Erie (referred to as "erie"), tap water (referred to as "tap"),
#water taken from Shaker Lake (referred to as "shaker"), water from brook 1 
#(referred to as "brook1"), water from brook 2 (referred to as "brook2"), 
#surface water (referred to as "surface"), and freshly collected melted snow
#(referred to as "snow"). All absorption coefficients are for distance given in
#centimeters, but the program takes a depth value in meters and converts it.

#importing useful libraries
import matplotlib.pyplot as plt
from numpy import array, zeros

#Defining function that will graph transmittance of water types at given depths.
#The function takes two arguments: watertype and depth. 
#Depth must be a number.
#Watertype must be one of the following strings: "distilled", "tap", "shaker",
#"brook1", "brook2", "surface", "snow".
def graph_alone(watertype, depth_m):
    trans = array(zeros(10)) #creating array trans to hold transmittance values
    depth = depth_m * 100 #converting depth from meters to centimeters
    
#setting graph name and absorption constant array to be used
    if watertype == "distilled":
        name = "Distilled Water"
        abs_const = dis_const
    elif watertype == "erie":
        name = "Water from Lake Erie"
        abs_const = erie_const
    elif watertype == "tap":
        name = "Tap Water"
        abs_const = tap_const
    elif watertype == "shaker":
        name = "Water from Shaker Lake"
        abs_const = shaker_const
    elif watertype == "brook1":
        name = "Water from Brook 1"
        abs_const = brook1_const
    elif watertype == "brook2":
        name = "Water from Brook 2"
        abs_const = brook2_const
    elif watertype == "surface":
        name = "Surface Water"
        abs_const = surf_const
    elif watertype == "snow":
        name = "Melted Snow Water"
        abs_const = snow_const
   
#calculating transmittance values    
    for x in range(10):
        k = abs_const[x]
        trans[x] = 10 ** (k * -1 * depth)
        
    plt.plot(wavelength, trans, "ro", label='original') #graphing wavelength on the horizontal and transmittance on the vertical
    plt.plot(wavelength, trans*0.1, "bo",label='new') #graphing wavelength on the horizontal and transmittance on the vertical
    plt.xlabel("Wavelength (nm)") #labelling horizontal axis
    plt.ylabel("Transmittance") #labelling vertical axis
    plt.title("Transmittance of %s at %f m" %(name, depth_m)) #setting graph title
    plt.axis([200, 420, 0, 1]) #setting axis maxima and minima
    plt.legend(loc='best', ncol=1, borderaxespad=0, fontsize=12)
    plt.savefig("%s_%f.pdf" %(watertype, depth_m)) #saving graph as pdf
    plt.show() #displaying graph
    
 #Creating function to graph the absorption coefficients of all water sources on the same axes
def graph_all():
    #graphing seperate sources 
    plt.plot(wavelength,dis_const*100, "ro", label="Distilled Water")
    plt.plot(wavelength, erie_const*100, "bo", label="Lake Erie")
    plt.plot(wavelength, tap_const*100, "go", label="Tap Water")
    plt.plot(wavelength, shaker_const*100, "co", label="Shaker Lake")
    plt.plot(wavelength, brook1_const*100, "mo", label="Brook 1")
    plt.plot(wavelength, brook2_const*100, "ko", label="Brook 2")
    plt.plot(wavelength, surf_const*100, "r^", label="Surface Water")
    plt.plot(wavelength, snow_const*100, "yo", label="Melted Snow")

    plt.xlabel("Wavelength (nm)") #labelling horizontal axis
    plt.ylabel("Absorption Coefficient (m^-1)") #labelling vertical axis
    plt.title("Absorption Coefficients of Modern Freshwater Sources") #titiling graph
    plt.yscale('log') #setting the vertical axis to log scale
    plt.legend(loc="best", ncol=2,borderaxespad=0, fontsize=9) #creating legend
    plt.savefig("Absorption Coefficients of Modern Freshwater Sources.pdf") #saving graph as pdf
    plt.show() #displaying graph
    
#creating wavelength array, assigning values incrementing by 20, 
#ranging from 220 to 400 nm
wavelength = array(range(220,401,20))

#creating coefficient of absorption array for distilled water
dis_const = array(zeros(10))

#assigning values to distilled water values array
dis_const[0] = 0.028
dis_const[1] = 0.021
dis_const[2] = 0.016
dis_const[3] = 0.011
dis_const[4] = 0.009
dis_const[5] = 0.007
dis_const[6] = 0.004
dis_const[7] = 0.004
dis_const[8] = 0.004
dis_const[9] = 0.002

#creating coefficient of absorption array for water from Lake Erie
erie_const = array(zeros(10))

#assigning values to Lake Erie absorption values array
erie_const[0] = 0.58
erie_const[1] = 0.4
erie_const[2] = 0.29
erie_const[3] = 0.23
erie_const[4] = 0.18
erie_const[5] = 0.15
erie_const[6] = 0.12
erie_const[7] = 0.09
erie_const[8] = 0.062
erie_const[9] = 0.046

#creating coefficient of absorption array for tap water
tap_const = array(zeros(10))

#assigning values to tapwater absorption values array
tap_const[0] = 0.12
tap_const[1] = 0.023
tap_const[2] = 0.021
tap_const[3] = 0.021
tap_const[4] = 0.013
tap_const[5] = 0.009
tap_const[6] = 0.004
tap_const[7] = 0.002
tap_const[8] = 0.002
tap_const[9] = 0.002

#creating coefficient of absorption array for water from Shaker Lake
shaker_const = array(zeros(10))

#assigning values to Shaker Lake absorption values array
shaker_const[0] = 0.65
shaker_const[1] = 0.46
shaker_const[2] = 0.34
shaker_const[3] = 0.26
shaker_const[4] = 0.21
shaker_const[5] = 0.17
shaker_const[6] = 0.13
shaker_const[7] = 0.093
shaker_const[8] = 0.062
shaker_const[9] = 0.035

#creating coefficient of absorption array for water from Brook 1
brook1_const = array(zeros(10))

#assigning values to Brook 1 absorption values array
brook1_const[0] = 0.65
brook1_const[1] = 0.40
brook1_const[2] = 0.30
brook1_const[3] = 0.23
brook1_const[4] = 0.17
brook1_const[5] = 0.13
brook1_const[6] = 0.10
brook1_const[7] = 0.074
brook1_const[8] = 0.048
brook1_const[9] = 0.028

#creating coefficient of absorption array for water from Brook 2
brook2_const = array(zeros(10))

#assigning values to Brook 2 absorption values array
brook2_const[0] = 0.43
brook2_const[1] = 0.26
brook2_const[2] = 0.19
brook2_const[3] = 0.15
brook2_const[4] = 0.14
brook2_const[5] = 0.11
brook2_const[6] = 0.093
brook2_const[7] = 0.081
brook2_const[8] = 0.068
brook2_const[9] = 0.033

#creating coefficient of absorption array for surface water
surf_const = array(zeros(10))

#assigning values to surface water absorption values array
surf_const[0] = 0.43
surf_const[1] = 0.30
surf_const[2] = 0.24
surf_const[3] = 0.2
surf_const[4] = 0.18
surf_const[5] = 0.13
surf_const[6] = 0.087
surf_const[7] = 0.071
surf_const[8] = 0.057
surf_const[9] = 0.043

#creating coefficient of absorption array for water from melted snow
snow_const = array(zeros(10))

#assigning values to melted snow absorption values array
snow_const[0] = 0.44
snow_const[1] = 0.25
snow_const[2] = 0.2
snow_const[3] = 0.17
snow_const[4] = 0.15
snow_const[5] = 0.13
snow_const[6] = 0.12
snow_const[7] = 0.1
snow_const[8] = 0.09
snow_const[9] = 0.077

graph_all()

















