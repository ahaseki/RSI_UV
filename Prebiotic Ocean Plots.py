#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:41:21 2019

@author: azrahaseki

legend: molabs_ion: the molar absorptivity constansts (in M^-1 cm^-1) for that ion.
"""

#importing important libraries
import matplotlib.pyplot as plt
import numpy as np
import pdb

#specifying prebiotic concentrations of ions
M_fe_prebio = 0.000100 #10-600 uM, really important 
M_br_prebio = 0.0015 #1-3 mM
M_no3_prebio = 0.000001 #maximum 1 uM
M_fecl2_prebio = 0.00001
M_feso4_prebio = 0.00001
M_i_prebio =0.0001 #10-120 uM

s = 100 #depth in units of cm

#importing data 
wv_br, molabs_br = np.genfromtxt('./Processed-Data/johnson_br.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 
wv_no3, molabs_no3 = np.genfromtxt('./Processed-Data/johnson_no3.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 
wv_febf4, molabs_febf4 = np.genfromtxt('./Processed-Data/fontana_fe2bf4.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 
wv_fecl2, molabs_fecl2 = np.genfromtxt('./Processed-Data/fontana_fecl2.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 
wv_feso4, molabs_feso4 = np.genfromtxt('./Processed-Data/fontana_feso4.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 
wv_cl, molabs_cl = np.genfromtxt('./Processed-Data/perkampus_kcl.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1
wv_so4, molabs_so4 = np.genfromtxt('./Processed-Data/hayon_so4_acid.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1, 
wv_so4, molabs_so4 = np.genfromtxt('./Processed-Data/hayon_so4_base.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1,
wv_i, molabs_i = np.genfromtxt('./Processed-Data/guenther_i.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1,
molabs_fecl2_synthetic=molabs_febf4 + 2.0*np.interp(wv_febf4, wv_cl, molabs_cl) #M^-1 cm^-1
molabs_feso4_synthetic=molabs_febf4 + np.interp(wv_febf4, wv_so4, molabs_so4) #M^-1 cm^-1
wv_pure, molabs_pure = np.genfromtxt('./Processed-Data/smithbaker_purest.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 

def calculate_fe_oceanic(fecl2_to_feso4_ratio):
    """
    Takes: ratio of Fe in FeCl2 vs Fe in FeSO4 (expected to be high since much more Cl than SO4)
    """
    return ((fecl2_to_feso4_ratio)/(1.0+fecl2_to_feso4_ratio))*molabs_fecl2 + ((1.0)/(1.0+fecl2_to_feso4_ratio))*np.interp(wv_fecl2, wv_feso4, molabs_feso4)

molabs_fe_oceanic=calculate_fe_oceanic(0.5/(40.0e-6)) #calculating "constructed" molar absorbtivity of Fe2+
#np.savetxt("./Processed-Data/constructed_Fe_molarabsorptivity.dat", np.column_stack((wv_fecl2, molabs_fe_oceanic)), delimiter=",", newline="\n", fmt="%3.1f %1.6e", header="Constructed molar absorbtivity of Fe2+ in the prebiotic ocean\nWavelength (nm), Molar Absorptivities (M^-1 cm^-1)")



#interpolating to Fe wavelength
molabs_br_adjusted = np.interp(wv_febf4, wv_br, molabs_br)
molabs_no3_adjusted = np.interp(wv_febf4, wv_no3, molabs_no3)
molabs_i_adjusted = np.interp(wv_febf4, wv_i, molabs_i)
molabs_pure_adjusted = np.interp(wv_febf4, wv_pure, molabs_pure)

#calculating absorbances
absorbance_br = molabs_br_adjusted * M_br_prebio * s
absorbance_no3 = molabs_no3_adjusted * M_no3_prebio * s
absorbance_fe = molabs_fe_oceanic * M_fe_prebio * s
absorbance_i = molabs_i_adjusted * M_i_prebio * s
absorbance_total = absorbance_br + absorbance_no3 + absorbance_fe + absorbance_i

#calculating transmittances
trans_br = 10 ** (-1 * absorbance_br)
trans_no3 = 10 ** (-1 * absorbance_no3)
trans_fe = 10 ** (-1 * absorbance_fe)
trans_i = 10 ** (-1 * absorbance_i)
trans_total = 10 ** (-1 * absorbance_total)

#####################graphing ############################
fig, axes = plt.subplots(4,figsize=(6.,12.))

#graphing molar absorptivities
axes[0].plot(wv_febf4, molabs_br_adjusted, "go", label="Br-")
axes[0].plot(wv_febf4, molabs_no3_adjusted, "mo", label="NO3-")
axes[0].plot(wv_fecl2, molabs_fe_oceanic, "bo", label="Oceanic Fe (simulated)")
axes[0].plot(wv_fecl2, molabs_i_adjusted, "yo", label="I-")

axes[0].set_xlabel("Wavelength (nm)") #titling x axis
axes[0].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
axes[0].set_title("Molar Absorbtivities")
axes[0].legend(loc="best", ncol=1,borderaxespad=0, fontsize=8) #creating legend
axes[0].set_yscale("log")

#graphing  absorptivities
axes[1].plot(wv_febf4, molabs_br_adjusted * M_br_prebio, "go", label="%s Br-" %(M_br_prebio))
axes[1].plot(wv_febf4, molabs_no3_adjusted * M_no3_prebio, "mo", label="%s NO3-" %(M_no3_prebio))
axes[1].plot(wv_fecl2, molabs_fe_oceanic * M_fe_prebio, "bo", label="%s Fe2+" %(M_fe_prebio))
axes[1].plot(wv_fecl2, molabs_i_adjusted * M_i_prebio, "yo", label="%s I-" %(M_i_prebio)) 

axes[1].set_xlabel("Wavelength (nm)") #titling x axis
axes[1].set_ylabel("Absorptivity (cm^-1)") #titling y axis
#axes.set_title("Measured and Constructed Ferrous Compounds' Spectra")
axes[1].legend(loc="best", ncol=1,borderaxespad=0, fontsize=8) #creating legend
axes[1].set_yscale("log")

#graphing absorbance
axes[2].plot(wv_febf4, absorbance_br, "go", label="%s Br-" %(M_br_prebio))
axes[2].plot(wv_febf4, absorbance_no3, "mo", label="%s NO3-" %(M_no3_prebio))
axes[2].plot(wv_febf4, absorbance_fe, "bo", label="%s Fe2+" %(M_fe_prebio))
axes[2].plot(wv_febf4, absorbance_i, "yo", label="%s I-" %(M_i_prebio))
axes[2].plot(wv_febf4, absorbance_total, "ro", label="Total")

axes[2].set_xlabel("Wavelength (nm)") #titling x axis
axes[2].set_ylabel("Absorbance") #titling y axis
axes[2].set_title("Absorbance at %s cm" %(s))
axes[2].legend(loc="best", ncol=1,borderaxespad=0, fontsize=8) #creating legend
axes[2].set_yscale("log")

#graphing transmittance
axes[3].plot(wv_febf4, trans_br, "go", label="%s Br-" %(M_br_prebio))
axes[3].plot(wv_febf4, trans_no3, "mo", label="%s NO3-" %(M_no3_prebio))
axes[3].plot(wv_febf4, trans_fe, "bo", label="%s Fe2+" %(M_fe_prebio))
axes[3].plot(wv_febf4, trans_i, "yo", label="%s I-" %(M_i_prebio))
axes[3].plot(wv_febf4, trans_total, "ro", label="Total")

axes[3].set_xlabel("Wavelength (nm)") #titling x axis
axes[3].set_ylabel("Transmittance") #titling y axis
axes[3].set_title("Transmittance at %s cm" %(s))
axes[3].legend(loc="best", ncol=1,borderaxespad=0, fontsize=8) #creating legend
#axes[2].set_yscale("log")

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
plt.savefig("Prebiotic_Ocean.pdf", orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf
plt.show() #display graph##


