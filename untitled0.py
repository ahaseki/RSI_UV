#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:32:01 2019

For constructed seawaters:
Prebiotic seawater: NO3- (1 uM), Fe2+ (100 uM), Br- (1.5 mM), I- (100 uM)
Modern seawater: Br- (840 uM), NO3- (50 uM), NO2- (50 uM)


@author: azrahaseki
"""

#importing useful libraries
import matplotlib.pyplot as plt
import numpy as np
import pdb

#importing data 
wv_purest, molabs_purest = np.genfromtxt('./Processed-Data/smithbaker_purest.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1
wv_modern_constructed, molabs_modern_constructed = np.genfromtxt('./Processed-Data/constructed_modern_ocean.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1...maybe, some confusion. 
wv_prebiotic_constructed, molabs_prebiotic_constructed = np.genfromtxt('./Processed-Data/constructed_prebiotic_ocean.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1...maybe, some confusion. 

#graphing
fig, axes = plt.subplots(1,figsize=(6.,5.))

#graphing molar absorptivities
axes.plot(wv_purest, molabs_purest, "co", label="Purest Natural Waters")
axes.plot(wv_modern_constructed, molabs_modern_constructed, "go", label="Constructed Modern")
axes.plot(wv_prebiotic_constructed, molabs_prebiotic_constructed, "mo", label="Constructed Prebiotic")

axes.set_xlabel("Wavelength (nm)") #titling x axis
axes.set_ylabel("Absorptivity (cm^-1)") #titling y axis
axes.set_title("Absorbtivities")
axes.legend(loc="best", ncol=1,borderaxespad=0, fontsize=8) #creating legend
axes.set_yscale("log")