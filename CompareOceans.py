#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:32:01 2019

For constructed seawaters:
Prebiotic seawater: NO3- (1 uM), Fe2+ (100 uM), Br- (1.5 mM), I- (10 uM)
Modern seawater: Br- (840 uM), NO3- (50 uM), NO2- (50 uM)


@author: azrahaseki
"""

#importing useful libraries
import matplotlib.pyplot as plt
import numpy as np
import pdb

s = 100 #setting depth in units cm

#importing data 
wv_purest, molabs_purest = np.genfromtxt('./Processed-Data/smithbaker_purest.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1
wv_modern_constructed, molabs_modern_constructed = np.genfromtxt('./Processed-Data/constructed_modern_ocean.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1...maybe, some confusion. 
wv_prebiotic_constructed, molabs_prebiotic_constructed = np.genfromtxt('./Processed-Data/constructed_prebiotic_ocean.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1...maybe, some confusion. 
wv_lake_constructed, molabs_lake_constructed = np.genfromtxt('./Processed-Data/constructed_lake.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1...maybe, some confusion. 
wv_quickenden, molabs_quickenden_base = np.genfromtxt('./Processed-Data/quickenden.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, cm^-1...maybe, some confusion. 

#interpolating data
molabs_lake_adjusted = np.interp(wv_modern_constructed, wv_lake_constructed, molabs_lake_constructed)
molabs_quickenden = np.interp(wv_modern_constructed, wv_quickenden, molabs_quickenden_base)


#calculating absorbance
absorbance_purest = molabs_purest * s
absorbance_modern_constructed = molabs_modern_constructed * s
absorbance_prebiotic_constructed = molabs_prebiotic_constructed * s
absorbance_lake_constructed = molabs_lake_adjusted * s
absorbance_quickenden = molabs_quickenden * s

#calculating transmittance
trans_purest = 10 ** (-1 * absorbance_purest)
trans_modern_constructed = 10 ** (-1 * absorbance_modern_constructed)
trans_prebiotic_constructed = 10 ** (-1 * absorbance_prebiotic_constructed)
trans_lake_constructed = 10 ** (-1 * absorbance_lake_constructed)
trans_quickenden = 10 ** (-1 * absorbance_quickenden)

################################## graphing ####################################
fig, axes = plt.subplots(3,figsize=(6.,12.))

#graphing molar absorptivities
#axes[0].plot(wv_purest, molabs_purest, "co", label="Modern Ocean")
#axes[0].plot(wv_modern_constructed, molabs_modern_constructed, "go", label="Modern Abiotic Ocean")
axes[0].plot(wv_prebiotic_constructed, molabs_prebiotic_constructed, "mo", label= "Prebiotic Ocean")
axes[0].plot(wv_modern_constructed, molabs_lake_adjusted, "bo", label="Prebiotic Lake")
axes[0].plot(wv_modern_constructed, molabs_quickenden, "yo", label="Pure Water")

axes[0].set_xlabel("Wavelength (nm)") #titling x axis
axes[0].set_ylabel("Absorptivity (cm^-1)") #titling y axis
axes[0].set_title("Absorbtivities")
axes[0].legend(loc="best", ncol=1,borderaxespad=0.5, fontsize=11) #creating legend
axes[0].set_yscale("log")
axes[0].set_xlim([200,320])

#graphing absorbances
#axes[1].plot(wv_purest, absorbance_purest, "co", label="Modern Ocean")
#axes[1].plot(wv_modern_constructed, absorbance_modern_constructed, "go", label="Modern Abiotic Ocean")
axes[1].plot(wv_prebiotic_constructed, absorbance_prebiotic_constructed, "mo", label="Prebiotic Ocean")
axes[1].plot(wv_modern_constructed, absorbance_lake_constructed, "bo", label="Prebiotic Lake")
axes[1].plot(wv_modern_constructed, absorbance_quickenden, "yo", label="Pure Water")

axes[1].set_xlabel("Wavelength (nm)") #titling x axis
axes[1].set_ylabel("Absorbance") #titling y axis
axes[1].set_title("Absorbance at %s cm" %(s))
axes[1].legend(bbox_to_anchor=(1.25, 0), loc="lower center", ncol=1,borderaxespad=0, fontsize=10) #creating legend
axes[1].set_yscale("log")
axes[1].set_xlim([200,320])

#graphing transmittance
#axes[2].plot(wv_purest, trans_purest, "co", label="Modern Ocean")
#axes[2].plot(wv_modern_constructed, trans_modern_constructed, "go", label="Modern Abiotic Ocean")
axes[2].plot(wv_prebiotic_constructed, trans_prebiotic_constructed, "mo", label="Prebiotic Ocean")
axes[2].plot(wv_modern_constructed, trans_lake_constructed, "bo", label="Prebiotic Lake")
axes[2].plot(wv_modern_constructed, trans_quickenden, "yo", label="Pure Water")

axes[2].set_ylim([0,1])
axes[2].set_xlim([200,320])

axes[2].set_xlabel("Wavelength (nm)") #titling x axis
axes[2].set_ylabel("Transmittance") #titling y axis
axes[2].set_title("Transmittance at %s cm" %(s))
axes[2].legend(loc="best", ncol=1,borderaxespad=0.5, fontsize=11) #creating legend


plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
plt.savefig("compare_oceans_lake_absorbtivity.pdf", orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf

