#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:21:33 2019

@author: azrahaseki
"""
#This program calculates the molar absorbtivity coefficients and transmittances
#of bromide, nitrate, nitrite, and bisulfide given data taken from the 2002 paper
#"In situ ultraviolet spectrophotometry for high resolution and long-term 
#monitoring of nitrate, bromide and bisulfide in the ocean" by Johnson and 
#Colletti. Figure 1, the absorption spectra of bromide, bisulfide, nitrate 
#and nitrite at concentrations typical of seawater, was digitalised using 
#Digizelt.
#The unit used for absorbitivity constants is M^-1 cm^-1, path length/depth is
#cm and wavelength in nm. 


#importing useful libraries
import matplotlib.pyplot as plt
from numpy import array, zeros
import pdb
import numpy as np


#specifying depth in cm- this is not the depth the paper's measurements were 
#made in, but the depth at which transmittance is calculated
s = 100 #depth in cm

########################### prebiotic recipe ##################################
#specifying prebiotic concentrations of ions
M_fe2_prebio = 0.000100 #10-600 uM, really important
M_br_prebio = 0.0015 #1-3 mM
M_no3_prebio = 0.000001 #maximum 1 uM
M_fecl2_prebio = 0.00001
M_feso4_prebio = 0.00001
#M_no2_prebio = #not really detectable
#M_hs_prebio = #I think it's not really there because the primary source is living stuff?
#M_i_prebio = #is this photoactive enough in the UV to matter? (iodine)

######################### experimental setup ##################################
#specifying experimental/modern ocean molarities for ions. These are the values used in the
#transmittance calculation for the modern ocean
M_br_ex = 0.000840 #experimental molarity of Br- 
M_no3_ex = 0.000030 #experimental molarity of NO3-
M_no2_ex = 0.000030 #experimental molarity of N02-
M_hs_ex = 0.000000001 #experimental molarity of HS-
M_fe2_check = 0.053 #check molarity for FeCl2
M_feso4_check = 0.033 #check molarity for FeSO4

######################### data from Johnson paper #############################

#specifying molarities for ions, as given in the Johnson paper. These are typical
#molarities of the given ions in seawater.
M_br_gv = 0.000840 #given molarity of Br-, 840 uM
M_no3_gv = 0.000030 #given molarity of NO3-, 30 uM
M_no2_gv = 0.000030 #given molarity of NO2-, 30 uM
M_hs_gv = 0.000050 #given molarity of HS-, 50 uM
M_fe2_gv = 0.089 #given molarity of Fe(BF4)2
M_fecl2_gv = 0.053 #given molarity of FeCl2
M_feso4_gv = 0.033 #given molarity of FeSO4
M_so4_gv = 0.02 #given molarity of SO4, Hayon paper


######################### Fe superposition thingy #############################
wv_febf4, molabs_febf4=np.genfromtxt('./Processed-Data/fontana_fe2bf4.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 
wv_fecl2, molabs_fecl2=np.genfromtxt('./Processed-Data/fontana_fecl2.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 
wv_feso4, molabs_feso4=np.genfromtxt('./Processed-Data/fontana_feso4.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...maybe, some confusion. 

wv_cl, molabs_cl=np.genfromtxt('./Processed-Data/perkampus_kcl.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1
wv_so4, molabs_so4=np.genfromtxt('./Processed-Data/hayon_so4_acid.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1, 
wv_so4, molabs_so4=np.genfromtxt('./Processed-Data/hayon_so4_base.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1,
wv_i, molabs_i=np.genfromtxt('./Processed-Data/guenther_i.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1
wv_br, molabs_br=np.genfromtxt('./Processed-Data/johnson_br.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1
wv_gelbstoff, molabs_gelbstoff=np.genfromtxt('./Processed-Data/cleaves_gelbstoff.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1

wv_johnson_no2, molabs_johnson_no2 = np.genfromtxt('./Processed-Data/johnson_no2.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...
wv_mack_no2, molabs_mack_no2 = np.genfromtxt('./Processed-Data/mack_no2.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...
wv_johnson_no3, molabs_johnson_no3 = np.genfromtxt('./Processed-Data/johnson_no3.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...
wv_mack_no3, molabs_mack_no3 = np.genfromtxt('./Processed-Data/mack_no3.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1...


molabs_fecl2_synthetic=molabs_febf4 + 2.0*np.interp(wv_febf4, wv_cl, molabs_cl) #M^-1 cm^-1
molabs_feso4_synthetic=molabs_febf4 + np.interp(wv_febf4, wv_so4, molabs_so4) #M^-1 cm^-1

def calculate_fe_oceanic(fecl2_to_feso4_ratio):
    """
    Takes: ratio of Fe in FeCl2 vs Fe in FeSO4 (expected to be high since much more Cl than SO4)
    """
    return ((fecl2_to_feso4_ratio)/(1.0+fecl2_to_feso4_ratio))*molabs_fecl2 + ((1.0)/(1.0+fecl2_to_feso4_ratio))*np.interp(wv_fecl2, wv_feso4, molabs_feso4)

molabs_fe_oceanic=calculate_fe_oceanic(0.5/(40.0e-6)) #calculating "constructed" molar absorbtivity of Fe2+
np.savetxt("./Processed-Data/constructed_Fe_molarabsorptivity.dat", np.column_stack((wv_fecl2, molabs_fe_oceanic)), delimiter=",", newline="\n", fmt="%3.1f %1.6e", header="Constructed molar absorbtivity of Fe2+ in the prebiotic ocean\nWavelength (nm), Molar Absorptivities (M^-1 cm^-1)")

#plotting Fe2+ complexes
fig, axes = plt.subplots(3,figsize=(6.,12.))

#plotting FeCl2
axes[0].plot(wv_febf4, molabs_febf4, "ro", label="Fe(BF$_4$)$_2$")
axes[0].plot(wv_fecl2, molabs_fecl2, "mo", label="FeCl$_2$ (actual)")
axes[0].plot(wv_febf4, molabs_fecl2_synthetic, "bo", label="FeCl$_2$ (additive)")

axes[0].set_xlabel("wavelength (nm)") #titling x axis
axes[0].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
axes[0].set_title("FeCl2: additive vs actual")
axes[0].legend(loc="best", ncol=1,borderaxespad=0.5, fontsize=8) #creating legend
axes[0].set_yscale("log")
#axes.legend(bbox_to_anchor=(1.25, 0), loc="lower center", ncol=1,borderaxespad=0, fontsize=10) #creating legend

#plotting FeSO4
axes[1].plot(wv_febf4, molabs_febf4, "ro", label="Fe(BF$_4$)$_2$")
axes[1].plot(wv_feso4, molabs_feso4, "mo", label="FeSO$_4$ (actual)")
axes[1].plot(wv_febf4, molabs_feso4_synthetic, "bo", label="FeSO$_4$ (additive)")

axes[1].set_xlabel("wavelength (nm)") #titling x axis
axes[1].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
axes[1].set_title("Feso4: additive vs actual")
axes[1].legend(loc="best", ncol=1,borderaxespad=0.5, fontsize=8) #creating legend
axes[1].set_yscale("log")

#plotting oceanic Fe
axes[2].plot(wv_fecl2, molabs_fecl2, "co", label="FeCl$_2$ (actual)")
axes[2].plot(wv_fecl2, molabs_fe_oceanic, "yo", label="Oceanic Fe (calculated)")
axes[2].plot(wv_feso4, molabs_feso4, "go", label="FeSO$_4$ (actual)")
axes[2].plot(wv_febf4, molabs_febf4, "ro", label="Fe(BF$_4$)$_2$")

axes[2].set_xlabel("wavelength (nm)") #titling x axis
axes[2].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
axes[2].set_title("oceanic fe")
axes[2].legend(loc="best", ncol=1,borderaxespad=0.5, fontsize=8) #creating legend
axes[2].set_yscale("log")

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
plt.savefig("FeCompoundsCheck.pdf", orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf
plt.show() #display graph##

##plotting NO2- values
#fig, axes = plt.subplots(2,figsize=(6.,8.))
#
#axes[0].plot(wv_johnson_no2, molabs_johnson_no2, "bo", label="Johnson")
#axes[0].plot(wv_mack_no2, molabs_mack_no2, "mo", label="Mack")
#
#axes[0].set_xlabel("wavelength (nm)") #titling x axis
#axes[0].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
#axes[0].set_title("NO2- Molar Absorptivity")
#axes[0].legend(loc="best", ncol=1,borderaxespad=0, fontsize=8) #creating legend
#axes[0].set_yscale("log")
#
#axes[1].plot(wv_johnson_no3, molabs_johnson_no3, "bo", label="Johnson")
#axes[1].plot(wv_mack_no3, molabs_mack_no3, "mo", label="Mack")
#
#axes[1].set_xlabel("wavelength (nm)") #titling x axis
#axes[1].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
#axes[1].set_title("NO3- Molar Absorptivity")
#axes[1].legend(loc="best", ncol=1,borderaxespad=0, fontsize=8) #creating legend
#axes[1].set_yscale("log")
#
#plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
#plt.show()
#
##plotting molar absorption coefficients
#plt.plot(wv_br, molabs_br, "go", label="Br-") #plotting Br-
##plt.plot(wv_hs, const_hs, "yo", label="HS-") #plotting HS-
#plt.plot(wv_mack_no3, molabs_mack_no3, "co", label="NO3-") #plotting NO3-
#plt.plot(wv_mack_no2, molabs_mack_no2, "b*", label="NO2-") #plotting NO2-
#plt.plot(wv_febf4, molabs_febf4, "mo", label="Fe2+") #plotting Fe2+
#plt.plot(wv_fecl2, molabs_fecl2, "bo", label="FeCl2") #plotting FeCl2
#plt.plot(wv_feso4, molabs_feso4, "ro", label="FeSO4") #plotting FeSO4
#plt.plot(wv_gelbstoff, molabs_gelbstoff, "ko", label="gelbstoff") #plotting gelbstoff
#plt.plot(wv_i, molabs_i, "yo", label="I-")
##plt.plot(wv_so4, molabs_so4_base, "b*", label="SO4 base" )
##plt.plot(wv_so4, molabs_so4_acid, "r*", label="SO4 acid" )
#plt.xlabel("Wavelength (nm)") #titling x axis
#plt.ylabel("Molar Absorption Coefficient (cm^-1 M^-1)") #titling y axis
#plt.title("Molar Absorption Coefficients") #titling graph
#plt.legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
##plt.savefig("Molar Absorption Coefficients of Salts, Johnson paper.pdf") #saving graph as pdf
#plt.show() #display graph
