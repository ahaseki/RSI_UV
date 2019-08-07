#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:51:12 2019

@author: azrahaseki
"""

#importing useful libraries
import matplotlib.pyplot as plt
import numpy as np
import pdb

s = 100 #setting depth in units cm

#specifiying concentrations of ions
M_no3_lake = 0.000001 #1 uM
M_so3_lake = 0.000050 #50 uM
M_hso3_lake = 0.000050 #50 uM

#importing data
wv_quickenden, molabs_quickenden = np.genfromtxt('./Processed-Data/quickenden.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 
wv_no3, molabs_no3 = np.genfromtxt('./Processed-Data/mack_no3.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1
wv_so3, molabs_so3 = np.genfromtxt('./Processed-Data/hayon_so3.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1
wv_hso3, molabs_hso3 = np.genfromtxt('./Processed-Data/hayon_hso3.dat', skip_header=2, unpack=True, usecols=(0,1))#nm, M^=1 cm^-1

#interpolating to Quickenden wavelength
molabs_no3_adjusted = np.interp(wv_quickenden, wv_no3, molabs_no3)
molabs_so3_adjusted = np.interp(wv_quickenden, wv_so3, molabs_so3)
molabs_hso3_adjusted = np.interp(wv_quickenden, wv_hso3, molabs_hso3)

print(molabs_hso3_adjusted)
print(molabs_so3_adjusted)

#calculating total absorptivity
absorptivity_total = molabs_no3_adjusted * M_no3_lake + molabs_so3_adjusted * M_so3_lake + molabs_hso3_adjusted * M_hso3_lake
np.savetxt("./Processed-Data/constructed_lake.dat", np.column_stack((wv_quickenden, absorptivity_total)), delimiter=",", newline="\n", fmt="%3.1f %1.6e", header="Constructed molar absorbtivity of the modern ocean\nWavelength (nm), Absorptivities (cm^-1)")


#calculating absorbances
absorbance_no3 = molabs_no3_adjusted * M_no3_lake * s
absorbance_so3 = molabs_so3_adjusted * M_so3_lake * s
absorbance_hso3 = molabs_hso3_adjusted * M_hso3_lake * s
absorbance_total = absorbance_no3 + absorbance_so3 + absorbance_hso3  

#calculating transmittances
trans_no3 = 10 ** (-1 * absorbance_no3)
trans_so3 = 10 ** (-1 * absorbance_so3)
trans_hso3 = 10 ** (-1 * absorbance_hso3)
trans_total = 10 ** (-1 * absorbance_total) 
################################ graphing lake ################################
fig, axes = plt.subplots(4,figsize=(6.5,12.))

#graphing molar absorptivities
axes[0].plot(wv_quickenden, molabs_no3_adjusted, "bo", label="NO$_3^-$")
axes[0].plot(wv_quickenden, molabs_so3_adjusted, "go", label="SO$_3^2-$")
axes[0].plot(wv_quickenden, molabs_hso3_adjusted, "yo", label="HSO$_3^-$")

axes[0].set_xlabel("Wavelength (nm)") #titling x axis
axes[0].set_ylabel("Molar Absorptivity (M^-1 cm^-1)") #titling y axis
axes[0].set_title("Molar Absorbtivities")
axes[0].legend(loc="best", ncol=2,borderaxespad=0.4, fontsize=10) #creating legend
axes[0].set_yscale("log")
#axes[0].set_xlim([195,320])

#graphing absorptivities
axes[1].plot(wv_quickenden, molabs_no3_adjusted * M_no3_lake, "bo", label="%.2e NO$_3^-$" %(M_no3_lake))
axes[1].plot(wv_quickenden, molabs_so3_adjusted * M_so3_lake, "go", label="%.2e SO$_3^2-$" %(M_so3_lake))
axes[1].plot(wv_quickenden, molabs_hso3_adjusted * M_hso3_lake, "yo", label="%.2e HSO$_3^-$" %(M_hso3_lake))
axes[1].plot(wv_quickenden, absorptivity_total, "ro", label="Total absorbtivity")

axes[1].set_xlabel("Wavelength (nm)") #titling x axis
axes[1].set_ylabel("Absorptivities (cm^-1)") #titling y axis
axes[1].set_title("Absorbtivities")
axes[1].legend(loc="best", ncol=2,borderaxespad=0.4, fontsize=10) #creating legend
axes[1].set_yscale("log")

#graphing absorbance
axes[2].plot(wv_quickenden, absorbance_no3, "bo", label="%.2e NO$_3^-$" %(M_no3_lake))
axes[2].plot(wv_quickenden, absorbance_so3, "go", label="%.2e SO$_3^2-$" %(M_so3_lake))
axes[2].plot(wv_quickenden, absorbance_hso3, "yo", label="%.2e HSO$_3^-$" %(M_hso3_lake))
axes[2].plot(wv_quickenden, absorbance_total, "ro", label="Total")

axes[2].set_xlabel("Wavelength (nm)") #titling x axis
axes[2].set_ylabel("Absorbance") #titling y axis
axes[2].set_title("Absorbance at %s cm" %(s))
axes[2].legend(loc="best", ncol=2,borderaxespad=0.4, fontsize=8) #creating legend
axes[2].set_yscale("log")
#axes[2].set_xlim([195,320])


#graphing transmittance
axes[3].plot(wv_quickenden, trans_no3, "bo", label="%.2e NO$_3^-$" %(M_no3_lake))
axes[3].plot(wv_quickenden, trans_so3, "go", label="%.2e SO$_3^2-$" %(M_so3_lake))
axes[3].plot(wv_quickenden, trans_hso3, "yo", label="%.2e HSO$_3^-$" %(M_hso3_lake))
axes[3].plot(wv_quickenden, trans_total, "ro", label="Total")

axes[3].set_xlabel("Wavelength (nm)") #titling x axis
axes[3].set_ylabel("Transmittance") #titling y axis
axes[3].set_title("Transmittance at %s cm" %(s))
axes[3].legend(loc="best", ncol=1,borderaxespad=0.4, fontsize=8) #creating legend
#axes[2].set_yscale("log")
#axes[3].set_xlim([195,320])

leg = plt.legend()
leg.get_frame().set_edgecolor('k')

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
#plt.savefig("Lake.pdf", orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf
plt.show() #display graph##