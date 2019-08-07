#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:26:26 2019
@author: azrahaseki
"""

#importing important libraries
import matplotlib.pyplot as plt
import numpy as np
import pdb

s = 100 #depth in units of cm

#specifiying modern concentrations of ions
M_br_mod = 0.000840 #840 uM
M_no3_mod = 0.00000147 #1.470 uM
M_no2_mod = 0.000000463 #1 uM
M_i_mod = 0.0000005 #0.5 uM

#importing data 
wv_br, molabs_br = np.genfromtxt('./Processed-Data/johnson_br.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1..
wv_febf4, molabs_febf4 = np.genfromtxt('./Processed-Data/fontana_fe2bf4.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1
wv_i, molabs_i = np.genfromtxt('./Processed-Data/guenther_i.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1,
wv_no2, molabs_no2 = np.genfromtxt('./Processed-Data/mack_no2.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...
wv_no3, molabs_no3 = np.genfromtxt('./Processed-Data/mack_no3.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1

wv_quickenden, molabs_quickenden = np.genfromtxt('./Processed-Data/quickenden.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 


#interpolating to Fe wavelength
molabs_br_adjusted = np.interp(wv_febf4, wv_br, molabs_br)
molabs_no3_adjusted = np.interp(wv_febf4, wv_no3, molabs_no3)
molabs_i_adjusted = np.interp(wv_febf4, wv_i, molabs_i)
molabs_no2_adjusted = np.interp(wv_febf4, wv_no2, molabs_no2)
molabs_quickenden_adjusted = np.interp(wv_febf4, wv_quickenden, molabs_quickenden)

def calculate_modern_ocean(): 
    return (molabs_br_adjusted * M_br_mod + molabs_no3_adjusted * M_no3_mod + molabs_no2_adjusted * M_no2_mod + molabs_i_adjusted * M_i_mod + molabs_quickenden_adjusted) #calculating molar absorptivity of the modern ocean

modern_absorptivity = calculate_modern_ocean()
np.savetxt("./Processed-Data/constructed_modern_ocean.dat", np.column_stack((wv_febf4, modern_absorptivity)), delimiter=",", newline="\n", fmt="%3.1f %1.6e", header="Constructed molar absorbtivity of the modern ocean\nWavelength (nm), Absorptivities (cm^-1)")

#calculating absorbances
absorbance_br = molabs_br_adjusted * M_br_mod * s
absorbance_no3 = molabs_no3_adjusted * M_no3_mod * s
absorbance_no2 = molabs_no2_adjusted * M_no2_mod * s
absorbance_i = molabs_i_adjusted * M_i_mod * s
absorbance_total = absorbance_br + absorbance_no3 + absorbance_no2 + absorbance_i 

#calculating transmittances
trans_br = 10 ** (-1 * absorbance_br)
trans_no3 = 10 ** (-1 * absorbance_no3)
trans_no2 = 10 ** (-1 * absorbance_no2)
trans_i = 10 ** (-1 * absorbance_i)
trans_total = 10 ** (-1 * absorbance_total) 

#calculating total absorptivity for modern ocean
absorptivity_total =  molabs_quickenden_adjusted + molabs_br_adjusted * M_br_mod + molabs_no3_adjusted * M_no3_mod + molabs_no2_adjusted * M_no2_mod + molabs_i_adjusted * M_i_mod 
#saving absorptivity for the modern ocean
#np.savetxt("./Processed-Data/constructed_modern_ocean.dat", np.column_stack((wv_febf4, absorptivity_total)), delimiter=",", newline="\n", fmt="%3.1f %1.6e", header="Constructed molar absorbtivity of the modern ocean\nWavelength (nm), Absorptivities (cm^-1)")

###################### graphing the modern ocean ############################
fig, axes = plt.subplots(4,figsize=(6.5,12.))

#graphing molar absorptivities
axes[0].plot(wv_febf4, molabs_br_adjusted, "go", label="Br$^-$")
axes[0].plot(wv_febf4, molabs_no3_adjusted, "mo", label="NO$_3^-$")
axes[0].plot(wv_febf4, molabs_no2_adjusted, "bo", label="NO$_2^-$")
axes[0].plot(wv_febf4, molabs_i_adjusted, "yo", label="I$^-$")

axes[0].set_xlabel("Wavelength (nm)") #titling x axis
axes[0].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
axes[0].set_title("Molar Absorbtivities")
axes[0].legend(loc="best", ncol=2,borderaxespad=0.5, fontsize=8) #creating legend
axes[0].set_yscale("log")
axes[0].set_xlim([195,320])

#graphing  absorptivities
axes[1].plot(wv_febf4, molabs_br_adjusted * M_br_mod, "go", label="%.2e Br$^-$" %(M_br_mod))
axes[1].plot(wv_febf4, molabs_no3_adjusted * M_no3_mod, "mo", label="%.2e NO$_3^-$" %(M_no3_mod))
axes[1].plot(wv_febf4, molabs_no2_adjusted * M_no2_mod, "bo", label="%.2e NO$_2^-$" %(M_no2_mod))
axes[1].plot(wv_febf4, molabs_i_adjusted * M_i_mod, "yo", label="%.2e I$^-$" %(M_i_mod)) 
axes[1].plot(wv_febf4, absorptivity_total, "ro", label="Total absorptivity")

axes[1].set_xlabel("Wavelength (nm)") #titling x axis
axes[1].set_ylabel("Absorptivity (cm^-1)") #titling y axis
axes[1].set_title("Absorptivities")
axes[1].legend(loc="best", ncol=2,borderaxespad=0.5, fontsize=7.5) #creating legend
axes[1].set_yscale("log")
axes[1].set_xlim([195,320])

#graphing absorbance
axes[2].plot(wv_febf4, absorbance_br, "go", label="%.2e Br$^-$" %(M_br_mod))
axes[2].plot(wv_febf4, absorbance_no3, "mo", label="%.2e NO$_3^-$" %(M_no3_mod))
axes[2].plot(wv_febf4, absorbance_no2, "bo", label="%.2e NO$_2^-$" %(M_no2_mod))
axes[2].plot(wv_febf4, absorbance_i, "yo", label="%.2e I$^-$" %(M_i_mod))
axes[2].plot(wv_febf4, absorbance_total, "ro", label="Total")

axes[2].set_xlabel("Wavelength (nm)") #titling x axis
axes[2].set_ylabel("Absorbance") #titling y axis
axes[2].set_title("Absorbance at %s cm" %(s))
axes[2].legend(loc="best", ncol=2,borderaxespad=0.5, fontsize=8) #creating legend
axes[2].set_yscale("log")
axes[2].set_xlim([195,320])


#graphing transmittance
axes[3].plot(wv_febf4, trans_br, "go", label="%.2e Br$^-$" %(M_br_mod))
axes[3].plot(wv_febf4, trans_no3, "mo", label="%.2e NO$_3^-$" %(M_no3_mod))
axes[3].plot(wv_febf4, trans_no2, "bo", label="%.2e NO$_2^-$" %(M_no2_mod))
axes[3].plot(wv_febf4, trans_i, "yo", label="%.2e I$^-$" %(M_i_mod))
axes[3].plot(wv_febf4, trans_total, "ro", label="Total")

axes[3].set_xlabel("Wavelength (nm)") #titling x axis
axes[3].set_ylabel("Transmittance") #titling y axis
axes[3].set_title("Transmittance at %s cm" %(s))
axes[3].legend(loc="best", ncol=1,borderaxespad=0.5, fontsize=8) #creating legend
#axes[2].set_yscale("log")
axes[3].set_xlim([195,320])


plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
plt.savefig("Modern_Ocean.pdf", orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf
plt.show() #display graph##
