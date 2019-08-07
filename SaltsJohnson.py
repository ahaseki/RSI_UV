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

#creating wavelength array for Br- and assigning values
wv_br = array(zeros(33))
wv_br[0] = 200
wv_br[1] = 202
wv_br[2] = 204
wv_br[3] = 206
wv_br[4] = 208
wv_br[5] = 210
wv_br[6] = 212
wv_br[7] = 214
wv_br[8] = 216
wv_br[9] = 218
wv_br[10] = 220
wv_br[11] = 222
wv_br[12] = 224
wv_br[13] = 226
wv_br[14] = 228
wv_br[15] = 230
wv_br[16] = 232
wv_br[17] = 234
wv_br[18] = 236
wv_br[19] = 238
wv_br[20] = 240
wv_br[21] = 242
wv_br[22] = 244
wv_br[23] = 246
wv_br[24] = 248
wv_br[25] = 250
wv_br[26] = 252
wv_br[27] = 254
wv_br[28] = 256
wv_br[29] = 258
wv_br[30] = 260
wv_br[31] = 262
wv_br[32] = 264

#creating absorption array for BR- and assigning values
ab_br = array(zeros(33))
ab_br[0] = 2.2107
ab_br[1] = 2.2796
ab_br[2] = 2.3037
ab_br[3] = 2.2486
ab_br[4] = 2.0523
ab_br[5] = 1.6080
ab_br[6] = 1.0914
ab_br[7] = 0.6850
ab_br[8] = 0.3957
ab_br[9] = 0.2235
ab_br[10] = 0.1236
ab_br[11] = 0.0651
ab_br[12] = 0.0341
ab_br[13] = 0.0169
ab_br[14] = 0.0066
ab_br[15] = 0.0066
ab_br[16] = 0.0031
ab_br[17] = 0.0031
ab_br[18] = 0.0003
ab_br[19] = 0.0003
ab_br[20] = 0.0003
ab_br[21] = 0.0003
ab_br[22] = 0.0003
ab_br[23] = 0.0003
ab_br[24] = 0.0003
ab_br[25] = 0.0003
ab_br[26] = 0.0003
ab_br[27] = 0.0003
ab_br[28] = 0.0002
ab_br[29] = 0.0003
ab_br[30] = 0.0003
ab_br[31] = 0.0003
ab_br[32] = 0.0003

#creating wavelength array for HS- and assigning values
wv_hs = array(zeros(33))
wv_hs[0] = 200
wv_hs[1] = 202
wv_hs[2] = 204
wv_hs[3] = 206
wv_hs[4] = 208
wv_hs[5] = 210
wv_hs[6] = 212
wv_hs[7] = 214
wv_hs[8] = 216
wv_hs[9] = 218
wv_hs[10] = 220
wv_hs[11] = 222
wv_hs[12] = 224
wv_hs[13] = 226
wv_hs[14] = 228
wv_hs[15] = 230
wv_hs[16] = 232
wv_hs[17] = 234
wv_hs[18] = 236
wv_hs[19] = 238
wv_hs[20] = 240
wv_hs[21] = 242
wv_hs[22] = 244
wv_hs[23] = 246
wv_hs[24] = 248
wv_hs[25] = 250
wv_hs[26] = 252
wv_hs[27] = 254
wv_hs[28] = 255
wv_hs[29] = 258
wv_hs[30] = 260
wv_hs[31] = 262
wv_hs[32] = 264

#creating absorptivity array for HS- and assigning values
ab_hs = array(zeros(33))
ab_hs[0] = 0.27775
ab_hs[1] = 0.24158
ab_hs[2] = 0.20990
ab_hs[3] = 0.19010
ab_hs[4] = 0.18020
ab_hs[5] = 0.18317
ab_hs[6] = 0.19505
ab_hs[7] = 0.21584
ab_hs[8] = 0.24455
ab_hs[9] = 0.27822
ab_hs[10] = 0.31287
ab_hs[11] = 0.34950
ab_hs[12] = 0.38119
ab_hs[13] = 0.40990
ab_hs[14] = 0.42772
ab_hs[15] = 0.43663
ab_hs[16] = 0.43366
ab_hs[17] = 0.41782
ab_hs[18] = 0.39109
ab_hs[19] = 0.35446
ab_hs[20] = 0.31287
ab_hs[21] = 0.26832
ab_hs[22] = 0.22178
ab_hs[23] = 0.17921
ab_hs[24] = 0.14007
ab_hs[25] = 0.10651
ab_hs[26] = 0.08013
ab_hs[27] = 0.05776
ab_hs[28] = 0.04097
ab_hs[29] = 0.02739
ab_hs[30] = 0.01859
ab_hs[31] = 0.01220
ab_hs[32] = 0.00820

#creating wavelength array for NO3- and assigning values
wv_no3 = array(zeros(33))
wv_no3[0] = 200
wv_no3[1] = 202
wv_no3[2] = 204
wv_no3[3] = 206
wv_no3[4] = 208
wv_no3[5] = 210
wv_no3[6] = 212
wv_no3[7] = 214
wv_no3[8] = 216
wv_no3[9] = 218
wv_no3[10] = 220
wv_no3[11] = 222
wv_no3[12] = 224
wv_no3[13] = 226
wv_no3[14] = 228
wv_no3[15] = 230
wv_no3[16] = 232
wv_no3[17] = 234
wv_no3[18] = 236
wv_no3[19] = 238
wv_no3[20] = 240
wv_no3[21] = 242
wv_no3[22] = 244
wv_no3[23] = 246
wv_no3[24] = 248
wv_no3[25] = 250
wv_no3[26] = 252
wv_no3[27] = 254
wv_no3[28] = 256
wv_no3[29] = 258
wv_no3[30] = 260
wv_no3[31] = 262
wv_no3[32] = 264

#creating absorption array for NO3- and assigning values
ab_no3 = array(zeros(33))
ab_no3[0] = 0.293043
ab_no3[1] = 0.295540
ab_no3[2] = 0.292210
ab_no3[3] = 0.283885
ab_no3[4] = 0.270565
ab_no3[5] = 0.253082
ab_no3[6] = 0.228939
ab_no3[7] = 0.202299
ab_no3[8] = 0.174826
ab_no3[9] = 0.145688
ab_no3[10] = 0.119853
ab_no3[11] = 0.093240
ab_no3[12] = 0.071595
ab_no3[13] = 0.053279
ab_no3[14] = 0.039127
ab_no3[15] = 0.028304
ab_no3[16] = 0.018314
ab_no3[17] = 0.012486
ab_no3[18] = 0.009156
ab_no3[19] = 0.003329
ab_no3[20] = 0.000831
ab_no3[21] = 0.000001
ab_no3[22] = 0.000001
ab_no3[23] = 0.000001
ab_no3[24] = 0.000001
ab_no3[25] = 0.000001
ab_no3[26] = 0.000001
ab_no3[27] = 0.000001
ab_no3[28] = 0.000001
ab_no3[29] = 0.000001
ab_no3[30] = 0.000001
ab_no3[31] = 0.000001
ab_no3[32] = 0.000001


#creating wavelength array for NO2- and assigning values
wv_no2 = array(zeros(33))
wv_no2[0] = 200
wv_no2[1] = 202
wv_no2[2] = 204
wv_no2[3] = 206
wv_no2[4] = 208
wv_no2[5] = 210
wv_no2[6] = 212
wv_no2[7] = 214
wv_no2[8] = 216
wv_no2[9] = 218
wv_no2[10] = 220
wv_no2[11] = 222
wv_no2[12] = 224
wv_no2[13] = 226
wv_no2[14] = 228
wv_no2[15] = 230
wv_no2[16] = 232
wv_no2[17] = 234
wv_no2[18] = 236
wv_no2[19] = 238
wv_no2[20] = 240
wv_no2[21] = 242
wv_no2[22] = 244
wv_no2[23] = 246
wv_no2[24] = 248
wv_no2[25] = 250
wv_no2[26] = 252
wv_no2[27] = 254
wv_no2[28] = 256
wv_no2[29] = 258
wv_no2[30] = 260
wv_no2[31] = 262
wv_no2[32] = 264

#creating absorption array for NO2- and assigning values
ab_no2 = array(zeros(33))
ab_no2[0] = 0.130540
ab_no2[1] = 0.139085
ab_no2[2] = 0.146918
ab_no2[3] = 0.154039
ab_no2[4] = 0.159024
ab_no2[5] = 0.159736
ab_no2[6] = 0.157600
ab_no2[7] = 0.150992
ab_no2[8] = 0.144782
ab_no2[9] = 0.133388
ab_no2[10] = 0.121994
ab_no2[11] = 0.107752
ab_no2[12] = 0.092798
ab_no2[13] = 0.078556
ab_no2[14] = 0.064314
ab_no2[15] = 0.052208
ab_no2[16] = 0.040102
ab_no2[17] = 0.030845
ab_no2[18] = 0.023724
ab_no2[19] = 0.015891
ab_no2[20] = 0.010906
ab_no2[21] = 0.007346
ab_no2[22] = 0.005209
ab_no2[23] = 0.003785
ab_no2[24] = 0.003785
ab_no2[25] = 0.003785
ab_no2[26] = 0.001649
ab_no2[27] = 0.001649
ab_no2[28] = 0.000224
ab_no2[29] = 0.000224
ab_no2[30] = 0.000224
ab_no2[31] = 0.000224
ab_no2[31] = 0.000224

#creating wavelength array for Fe(BF4)2 and assigning values
wv_fe2 = array(zeros(33))
wv_fe2[0] = 200
wv_fe2[1] = 202
wv_fe2[2] = 204
wv_fe2[3] = 206
wv_fe2[4] = 208
wv_fe2[5] = 210
wv_fe2[6] = 212
wv_fe2[7] = 214
wv_fe2[8] = 216
wv_fe2[9] = 218
wv_fe2[10] = 220
wv_fe2[11] = 222
wv_fe2[12] = 224
wv_fe2[13] = 226
wv_fe2[14] = 228
wv_fe2[15] = 230
wv_fe2[16] = 232
wv_fe2[17] = 234
wv_fe2[18] = 236
wv_fe2[19] = 238
wv_fe2[20] = 240
wv_fe2[21] = 242
wv_fe2[22] = 244
wv_fe2[23] = 246
wv_fe2[24] = 248
wv_fe2[25] = 250
wv_fe2[26] = 252
wv_fe2[27] = 254
wv_fe2[28] = 256
wv_fe2[29] = 258
wv_fe2[30] = 260
wv_fe2[31] = 262
wv_fe2[32] = 264

#creating absorbance array for Fe(BF4)2 and assigning values
ab_fe2 = array(zeros(33))
ab_fe2[0] = 242.93
ab_fe2[1] = 275.54
ab_fe2[2] = 334.73
ab_fe2[3] = 359.11
ab_fe2[4] = 373.89
ab_fe2[5] = 374.02
ab_fe2[6] = 350.79
ab_fe2[7] = 317.81
ab_fe2[8] = 278.57
ab_fe2[9] = 241.50
ab_fe2[10] = 217.56
ab_fe2[11] = 169.89
ab_fe2[12] = 140.93
ab_fe2[13] = 128.38
ab_fe2[14] = 111.90
ab_fe2[15] = 100.27
ab_fe2[16] = 91.84
ab_fe2[17] = 84.12
ab_fe2[18] = 78.77
ab_fe2[19] = 74.57
ab_fe2[20] = 69.82
ab_fe2[21] = 65.74
ab_fe2[22] = 59.55
ab_fe2[23] = 56.69
ab_fe2[24] = 52.21
ab_fe2[25] = 48.35
ab_fe2[26] = 43.80
ab_fe2[27] = 39.89
ab_fe2[28] = 35.94
ab_fe2[29] = 31.15
ab_fe2[30] = 26.71
ab_fe2[31] = 24.06
ab_fe2[32] = 19.31

#creating wavelength array for Cl- and assigning values
wv_cl = array(zeros(33))
wv_cl[0] = 200
wv_cl[1] = 202
wv_cl[2] = 204
wv_cl[3] = 206
wv_cl[4] = 208
wv_cl[5] = 210
wv_cl[6] = 212
wv_cl[7] = 214
wv_cl[8] = 216
wv_cl[9] = 218
wv_cl[10] = 220
wv_cl[11] = 222
wv_cl[12] = 224
wv_cl[13] = 226
wv_cl[14] = 228
wv_cl[15] = 230
wv_cl[16] = 232
wv_cl[17] = 234
wv_cl[18] = 236
wv_cl[19] = 238
wv_cl[20] = 240
wv_cl[21] = 242
wv_cl[22] = 244
wv_cl[23] = 246
wv_cl[24] = 248
wv_cl[25] = 250
wv_cl[26] = 252
wv_cl[27] = 254
wv_cl[28] = 256
wv_cl[29] = 258
wv_cl[30] = 260
wv_cl[31] = 262
wv_cl[32] = 264

#creating absorbtion coefficient array for Cl- and assigning values
const_cl = array(zeros(33))
const_cl[0] = 24.4437
const_cl[1] = 19.8930
const_cl[2] = 10.2611
const_cl[3] = 6.3019
const_cl[4] = 4.2305
const_cl[5] = 2.3065
const_cl[6] = 1.6235
const_cl[7] = 1.2420
const_cl[8] = 0.9166
const_cl[9] = 0.6180

#creating wavelength array for fe2+ and assigning values
wv_fe = array(zeros(41))
wv_fe[0] = 200
wv_fe[1] = 205
wv_fe[2] = 210
wv_fe[3] = 215
wv_fe[4] = 220
wv_fe[5] = 225
wv_fe[6] = 230
wv_fe[7] = 235
wv_fe[8] = 240
wv_fe[9] = 245
wv_fe[10] = 250
wv_fe[11] = 255
wv_fe[12] = 260
wv_fe[13] = 265
wv_fe[14] = 270
wv_fe[15] = 275
wv_fe[16] = 280
wv_fe[17] = 285
wv_fe[18] = 290
wv_fe[19] = 295
wv_fe[20] = 300
wv_fe[21] = 305
wv_fe[22] = 310
wv_fe[23] = 315
wv_fe[24] = 320
wv_fe[25] = 325
wv_fe[26] = 330
wv_fe[27] = 335
wv_fe[28] = 340
wv_fe[29] = 345
wv_fe[30] = 350
wv_fe[31] = 355
wv_fe[32] = 360
wv_fe[33] = 365
wv_fe[34] = 370
wv_fe[35] = 375
wv_fe[36] = 380
wv_fe[37] = 385
wv_fe[38] = 390
wv_fe[39] = 395
wv_fe[40] = 400

#creating absorption array for fe2+ and assigning values
ab_fe = array(zeros(41))
ab_fe[0] = 246.1280
ab_fe[1] = 343.2465
ab_fe[2] = 372.2181
ab_fe[3] = 301.1851
ab_fe[4] = 210.4452
ab_fe[5] = 136.6533
ab_fe[6] = 101.9864
ab_fe[7] = 82.5126
ab_fe[8] = 70.2697
ab_fe[9] = 59.8418
ab_fe[10] = 48.7678
ab_fe[11] = 38.5900
ab_fe[12] = 27.1564
ab_fe[13] = 18.6936
ab_fe[14] = 12.0465
ab_fe[15] = 7.0568
ab_fe[16] = 3.1981
ab_fe[17] = 0.8998
ab_fe[18] = 0.5927
ab_fe[19] = 0.3549
ab_fe[20] = 0.2687
ab_fe[21] = 0.2126
ab_fe[22] = 0.1991
ab_fe[23] = 0.1948
ab_fe[24] = 0.1907
ab_fe[25] = 0.1866
ab_fe[26] = 0.1800
ab_fe[27] = 0.1787
ab_fe[28] = 0.1762
ab_fe[29] = 0.1749
ab_fe[30] = 0.1725
ab_fe[31] = 0.1725
ab_fe[32] = 0.1639
ab_fe[33] = 0.1546
ab_fe[34] = 0.1513
ab_fe[35] = 0.1525
ab_fe[36] = 0.1594
ab_fe[37] = 0.1678
ab_fe[38] = 0.1666
ab_fe[39] = 0.1450
ab_fe[40] = 0.1338

#creating wavelength array for fecl2 and assigning values
wv_fecl2 = array(zeros(41))
wv_fecl2[0] = 200
wv_fecl2[1] = 205
wv_fecl2[2] = 210
wv_fecl2[3] = 215
wv_fecl2[4] = 220
wv_fecl2[5] = 225
wv_fecl2[6] = 230
wv_fecl2[7] = 235
wv_fecl2[8] = 240
wv_fecl2[9] = 245
wv_fecl2[10] = 250
wv_fecl2[11] = 255
wv_fecl2[12] = 260
wv_fecl2[13] = 265
wv_fecl2[14] = 270
wv_fecl2[15] = 275
wv_fecl2[16] = 280
wv_fecl2[17] = 285
wv_fecl2[18] = 290
wv_fecl2[19] = 295
wv_fecl2[20] = 300
wv_fecl2[21] = 305
wv_fecl2[22] = 310
wv_fecl2[23] = 315
wv_fecl2[24] = 320
wv_fecl2[25] = 325
wv_fecl2[26] = 330
wv_fecl2[27] = 335
wv_fecl2[28] = 340
wv_fecl2[29] = 345
wv_fecl2[30] = 350
wv_fecl2[31] = 355
wv_fecl2[32] = 360
wv_fecl2[33] = 365
wv_fecl2[34] = 370
wv_fecl2[35] = 375
wv_fecl2[36] = 380
wv_fecl2[37] = 385
wv_fecl2[38] = 390
wv_fecl2[39] = 395
wv_fecl2[40] = 400

#creating absorption array for fecl2 and assigning values
ab_fecl2 = array(zeros(41))
ab_fecl2[0] = 152.1685
ab_fecl2[1] = 133.9050
ab_fecl2[2] = 134.3060
ab_fecl2[3] = 130.1681
ab_fecl2[4] = 128.1980
ab_fecl2[5] = 125.2416
ab_fecl2[6] = 119.4266
ab_fecl2[7] = 113.8783
ab_fecl2[8] = 105.1466
ab_fecl2[9] = 99.4607
ab_fecl2[10] = 91.0874
ab_fecl2[11] = 81.4332
ab_fecl2[12] = 63.4844
ab_fecl2[13] = 51.9381
ab_fecl2[14] = 39.5230
ab_fecl2[15] = 28.6581
ab_fecl2[16] = 21.1167
ab_fecl2[17] = 16.5944
ab_fecl2[18] = 14.0198
ab_fecl2[19] = 12.3315
ab_fecl2[20] = 12.1391
ab_fecl2[21] = 12.5423
ab_fecl2[22] = 13.8202
ab_fecl2[23] = 15.2277
ab_fecl2[24] = 17.3288
ab_fecl2[25] = 18.9412
ab_fecl2[26] = 20.3730
ab_fecl2[27] = 20.5449
ab_fecl2[28] = 20.7195
ab_fecl2[29] = 19.9078
ab_fecl2[30] = 18.5223
ab_fecl2[31] = 16.6872
ab_fecl2[32] = 14.0961
ab_fecl2[33] = 12.1009
ab_fecl2[34] = 10.0914
ab_fecl2[35] = 8.4357
ab_fecl2[36] = 6.6169
ab_fecl2[37] = 5.2808
ab_fecl2[38] = 4.1903
ab_fecl2[39] = 3.0485
ab_fecl2[40] = 2.3364

#creating wavelength array for feso4 and assigning values
wv_feso4 = array(zeros(41))
wv_feso4[0] = 200
wv_feso4[1] = 205
wv_feso4[2] = 210
wv_feso4[3] = 215
wv_feso4[4] = 220
wv_feso4[5] = 225
wv_feso4[6] = 230
wv_feso4[7] = 235
wv_feso4[8] = 240
wv_feso4[9] = 245
wv_feso4[10] = 250
wv_feso4[11] = 255
wv_feso4[12] = 260
wv_feso4[13] = 265
wv_feso4[14] = 270
wv_feso4[15] = 275
wv_feso4[16] = 280
wv_feso4[17] = 285
wv_feso4[18] = 290
wv_feso4[19] = 295
wv_feso4[20] = 300
wv_feso4[21] = 305
wv_feso4[22] = 310
wv_feso4[23] = 315
wv_feso4[24] = 320
wv_feso4[25] = 325
wv_feso4[26] = 330
wv_feso4[27] = 335
wv_feso4[28] = 340
wv_feso4[29] = 345
wv_feso4[30] = 350
wv_feso4[31] = 355
wv_feso4[32] = 360
wv_feso4[33] = 365
wv_feso4[34] = 370
wv_feso4[35] = 375
wv_feso4[36] = 380
wv_feso4[37] = 385
wv_feso4[38] = 390
wv_feso4[39] = 395
wv_feso4[40] = 400

#creating absorption array for feso4 and assigning values
ab_feso4 = array(zeros(41))
ab_feso4[0] = 200.915
ab_feso4[1] = 152.375
ab_feso4[2] = 143.398
ab_feso4[3] = 141.335
ab_feso4[4] = 139.282
ab_feso4[5] = 136.220
ab_feso4[6] = 133.203
ab_feso4[7] = 127.274
ab_feso4[8] = 120.753
ab_feso4[9] = 109.150
ab_feso4[10] = 97.541
ab_feso4[11] = 79.629
ab_feso4[12] = 65.001
ab_feso4[13] = 51.579
ab_feso4[14] = 41.393
ab_feso4[15] = 35.352
ab_feso4[16] = 33.809
ab_feso4[17] = 36.199
ab_feso4[18] = 39.873
ab_feso4[19] = 43.934
ab_feso4[20] = 46.886
ab_feso4[21] = 47.929
ab_feso4[22] = 47.742
ab_feso4[23] = 46.343
ab_feso4[24] = 43.089
ab_feso4[25] = 38.873
ab_feso4[26] = 33.882
ab_feso4[27] = 29.403
ab_feso4[28] = 23.614
ab_feso4[29] = 19.293
ab_feso4[30] = 15.230
ab_feso4[31] = 12.074
ab_feso4[32] = 10.254
ab_feso4[33] = 7.523
ab_feso4[34] = 5.989
ab_feso4[35] = 4.048
ab_feso4[36] = 2.702
ab_feso4[37] = 2.132
ab_feso4[38] = 1.619
ab_feso4[39] = 1.053
ab_feso4[40] = 0.715

#creating wavelength array for so4 and assigning values according to Hayon paper
wv_so4 = array(zeros(41))
wv_so4[0] = 200
wv_so4[1] = 205
wv_so4[2] = 210
wv_so4[3] = 215
wv_so4[4] = 220
wv_so4[5] = 225
wv_so4[6] = 230
wv_so4[7] = 235
wv_so4[8] = 240
wv_so4[9] = 245
wv_so4[10] = 250
wv_so4[11] = 255
wv_so4[12] = 260
wv_so4[13] = 265
wv_so4[14] = 270
wv_so4[15] = 275
wv_so4[16] = 280
wv_so4[17] = 285
wv_so4[18] = 290
wv_so4[19] = 295
wv_so4[20] = 300
wv_so4[21] = 305
wv_so4[22] = 310
wv_so4[23] = 315
wv_so4[24] = 320
wv_so4[25] = 325
wv_so4[26] = 330
wv_so4[27] = 335
wv_so4[28] = 340
wv_so4[29] = 345
wv_so4[30] = 350
wv_so4[31] = 355
wv_so4[32] = 360
wv_so4[33] = 365
wv_so4[34] = 370
wv_so4[35] = 375
wv_so4[36] = 380
wv_so4[37] = 385
wv_so4[38] = 390
wv_so4[39] = 395
wv_so4[40] = 400

#creating absorption/OD array for so4 T 10.4 PH and assigning values according to Hayon paper
ab_so4_b = array(zeros(41))
ab_so4_b[6] = 0.38
ab_so4_b[7] = 0.39
ab_so4_b[8] = 0.40
ab_so4_b[9] = 0.40
ab_so4_b[10] = 0.39
ab_so4_b[11] = 0.37
ab_so4_b[12] = 0.34
ab_so4_b[13] = 0.31
ab_so4_b[14] = 0.26
ab_so4_b[15] = 0.23
ab_so4_b[16] = 0.19
ab_so4_b[17] = 0.15
ab_so4_b[18] = 0.12
ab_so4_b[19] = 0.09
ab_so4_b[20] = 0.06
ab_so4_b[21] = 0.03
ab_so4_b[22] = 0.02
ab_so4_b[23] = 0.02
ab_so4_b[24] = 0.02
ab_so4_b[25] = 0.02
ab_so4_b[26] = 0.03
ab_so4_b[27] = 0.04
ab_so4_b[28] = 0.05
ab_so4_b[29] = 0.07
ab_so4_b[30] = 0.08
ab_so4_b[31] = 0.09
ab_so4_b[32] = 0.10
ab_so4_b[33] = 0.12
ab_so4_b[34] = 0.13
ab_so4_b[35] = 0.14
ab_so4_b[36] = 0.16
ab_so4_b[37] = 0.17
ab_so4_b[38] = 0.18
ab_so4_b[39] = 0.19
ab_so4_b[40] = 0.21

#creating absorption/OD array for so4 T 5.5 PH and assigning values according to Hayon paper
ab_so4_a = array(zeros(41))
ab_so4_a[5] = 0.3179
ab_so4_a[6] = 0.3384
ab_so4_a[7] = 0.3557
ab_so4_a[8] = 0.3628
ab_so4_a[9] = 0.3568
ab_so4_a[10] = 0.3364
ab_so4_a[11] = 0.3101
ab_so4_a[12] = 0.2771
ab_so4_a[13] = 0.2446
ab_so4_a[14] = 0.2098
ab_so4_a[15] = 0.1781
ab_so4_a[16] = 0.1445
ab_so4_a[17] = 0.1200
ab_so4_a[18] = 0.1016
ab_so4_a[19] = 0.0901
ab_so4_a[20] = 0.0836
ab_so4_a[21] = 0.0798
ab_so4_a[22] = 0.0765
ab_so4_a[23] = 0.0747
ab_so4_a[24] = 0.0737
ab_so4_a[25] = 0.0724
ab_so4_a[26] = 0.0721
ab_so4_a[27] = 0.0719
ab_so4_a[28] = 0.0728
ab_so4_a[29] = 0.0738
ab_so4_a[30] = 0.0737
ab_so4_a[31] =0.0742
ab_so4_a[32] =0.0744
ab_so4_a[33] =0.0743
ab_so4_a[34] =0.0753
ab_so4_a[35] =0.0776
ab_so4_a[36] =0.0798
ab_so4_a[37] =0.0836
ab_so4_a[38] =0.0882
ab_so4_a[39] =0.0928
ab_so4_a[40] =0.0987

#importing data
wv_so4, molabs_so4_acid = np.genfromtxt('./Processed-Data/hayon_so4_acid.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1, 
wv_so4, molabs_so4_base = np.genfromtxt('./Processed-Data/hayon_so4_base.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1,
wv_gelbstoff, molabs_gelbstoff = np.genfromtxt('./Processed-Data/cleaves_gelbstoff.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1,
wv_i, molabs_if = np.genfromtxt('./Processed-Data/guenther_i.dat', skip_header=2, unpack=True, usecols=(0,1)) #nm, M^=1 s^-1,

################### calculating molar absorption constants ####################

#calculating molar absorbtion constants for Br-
const_br = array(zeros(33))
for x in range(33):
    const_br[x] = ab_br[x] / M_br_gv

#calculating molar absorbtion constants for HS-
const_hs = array(zeros(33))
for x in range(33):
    const_hs[x] = ab_hs[x] / M_hs_gv
    
#calculating molar absorbtion constants for NO3-
const_no3 = array(zeros(33))
for x in range(33):
    const_no3[x] = ab_no3[x] / M_no3_gv
    
#calculating molar absorbtion constants for NO2-
const_no2 = array(zeros(33))
for x in range(33):
    const_no2[x] = ab_no2[x] / M_no2_gv
    
#calculating molar absorption constants for Fe(BF4)2
const_fe2 = array(zeros(33))
for x in range(33):
    const_fe2[x] = ab_fe2[x] / M_fe2_gv

#calculating molar absorption constants for Fe(BF4)2 (but Fe2+)
const_fe = array(zeros(41))
for x in range(41):
    const_fe[x] = ab_fe[x] / M_fe2_gv
    
#calculating molar absorption constants for FeCl2
const_fecl2 = array(zeros(41))
for x in range(41):
    const_fecl2[x] = ab_fecl2[x] / M_fecl2_gv
    
#calculating molar absorption constants for FeSO4
const_feso4 = array(zeros(41))
for x in range(41):
    const_feso4[x] = ab_feso4[x] / M_feso4_gv
    
#calculating molar absorption constants for SO4 at pH 10.4 according to Haydon paper
const_so4_b = array(zeros(41))
for x in range(41):
    const_so4_b[x] = ab_so4_b[x] / M_so4_gv
    
#calculating molar absorption constants for SO4 at pH 5.5 according to Haydon paper
const_so4_a = array(zeros(41))
for x in range(41):
    const_so4_a[x] = ab_so4_a[x] / M_so4_gv
    
############## calculating absorbtivites for modern ocean #####################

#calculating absorbtivity for Br-
cm_const_br = array(zeros(33))
for x in range(33):
    cm_const_br[x] = const_br[x] * M_br_ex

#calculating absorbtivity for HS-
cm_const_hs = array(zeros(33))
for x in range(33):
    cm_const_hs[x] = const_hs[x] * M_hs_ex
    
#calculating absorptivity for NO3-
cm_const_no3 = array(zeros(33))
for x in range(33):
    cm_const_no3[x] = const_no3[x] * M_no3_ex

#calculating absorptivity for NO2-
cm_const_no2 = array(zeros(33))
for x in range(33):
    cm_const_no2[x] = const_no2[x] * M_no2_ex
    
#calculating total absorptivity
cm_const_tot = array(zeros(33))
for x in range(33):
    cm_const_tot[x] = cm_const_br[x] + cm_const_hs[x] + cm_const_no3[x] + cm_const_no2[x]
    
################### calculating modern ocean absorbances #######################

#calculating absorbance for Br-
ab_mod_br = array(zeros(33))
for x in range(33):
    ab_mod_br[x] = const_br[x] * s * M_br_ex
    
#calculating absorbance for HS-
ab_mod_hs = array(zeros(33))
for x in range(33):
    ab_mod_hs[x] = const_hs[x] * s * M_hs_ex
    
#calculating absorbance for NO3-
ab_mod_no3 = array(zeros(33))
for x in range(33):
    ab_mod_no3[x] = const_no3[x] * s * M_no3_ex
    
#calculating absorbance for NO2-
ab_mod_no2 = array(zeros(33))
for x in range(33):
    ab_mod_no2[x] = const_no2[x] * s * M_no2_ex
    
#calculating total absorbance 
ab_mod_tot = array(zeros(33))
for x in range(33):
    ab_mod_tot[x] = ab_mod_br[x] + ab_mod_hs[x] + ab_mod_no3[x] + ab_mod_no2[x]
    
##############################################################################    

#calculating expected experimental absorbance values for NO3-
ab_ex_no3 = array(zeros(33))
for x in range(33):
    ab_ex_no3[x] = const_no3[x] * s * M_no3_ex
    
#calculating expected experimental absorbance values for HS-
ab_ex_hs = array(zeros(33))
for x in range(33):
    ab_ex_hs[x] = const_hs[x] * s * M_hs_ex

##################### calculating modern transmittances #######################

#calculating modern transmittance for Br-
trans_br = array(zeros(33))
for x in range(33):
    k = const_br[x] * M_br_ex * s * -1
    trans_br[x] = 10 ** k

#calculating modern transmittance for HS-
trans_hs = array(zeros(33))
for x in range(33):
    k = const_hs[x] * M_hs_ex * s * -1
    trans_hs[x] = 10 ** k
    
#calculating modern transmittance for NO3-
trans_no3 = array(zeros(33))
for x in range(33):
    k = const_no3[x] * M_no3_ex * s * -1
    trans_no3[x] = 10 ** k
    
#calculating modern transmittance for NO2-
trans_no2 = array(zeros(33))
for x in range(33):
    k = const_no2[x] * M_no2_ex * s * -1
    trans_no2[x] = 10 ** k
    
#calculating total transmittance in the modern ocean
trans_tot = array(zeros(33))
for x in range(33):
    trans_tot[x] = 10 ** (-1 * ab_mod_tot[x])
    
################### calculating prebiotic absorbtivities ######################
#units cm^-1
    
#calculating prebiotic absorptivity for Br-
cm_const_prebio_br = array(zeros(33))
for x in range(33):
    cm_const_prebio_br[x] = const_br[x] * M_br_prebio
    
#calculating prebiotic absorptivity for NO3-
cm_const_prebio_no3 = array(zeros(33))
for x in range(33):
    cm_const_prebio_no3[x] = const_no3[x] * M_no3_prebio
    
#calculating prebiotic absorptivity for Fe2+
cm_const_prebio_fe = array(zeros(41))
for x in range(41):
    cm_const_prebio_fe[x] = const_fe[x] * M_fe2_prebio
    
#calculating prebiotic absorptivity for FeCl2
cm_const_prebio_fecl2 = array(zeros(41))
for x in range(41):
    cm_const_prebio_fecl2[x] = const_fecl2[x] * M_fecl2_prebio
    
#calculating prebiotic absorptivity for FeSO4
cm_const_prebio_feso4 = array(zeros(41))
for x in range(41):
    cm_const_prebio_feso4[x] = const_feso4[x] * M_feso4_prebio
    
#calculating total prebiotic absorbtivity
cm_const_prebio_tot = array(zeros(33))
for x in range(33):
    cm_const_prebio_tot[x] = cm_const_prebio_br[x] + cm_const_prebio_no3[x] + cm_const_prebio_fe[x] + cm_const_prebio_fecl2[x] + cm_const_prebio_feso4[x]
    
#################### calculating prebiotic absorbances #######################
    
#calculating prebiotic absorbance for Br-
ab_prebio_br = array(zeros(33))
for x in range(33):
    ab_prebio_br[x] = cm_const_prebio_br[x] * s

#calculating prebiotic absorbance for NO3-
ab_prebio_no3 = array(zeros(33))
for x in range(33):
    ab_prebio_no3[x] = cm_const_prebio_no3[x] * s
    
#calculating prebiotic absorbance for Fe2+
ab_prebio_fe = array(zeros(41))
for x in range(41):
    ab_prebio_fe[x] = cm_const_prebio_fe[x] * s
    
#calculating prebiotic absorbance for FeCl2
ab_prebio_fecl2 = array(zeros(41))
for x in range(41):
    ab_prebio_fecl2[x] = cm_const_prebio_fecl2[x] * s
    
#calculating prebiotic absorbance for FeSO4
ab_prebio_feso4 = array(zeros(41))
for x in range(41):
    ab_prebio_feso4[x] = cm_const_prebio_feso4[x] * s

#calculating total prebiotic absorbance 
ab_prebio_tot = array(zeros(33))
for x in range(33):
    ab_prebio_tot[x] = ab_prebio_br[x] + ab_prebio_no3[x] + ab_prebio_fe[x] + ab_prebio_fecl2[x] + ab_prebio_feso4[x]
    
##################### calculating prebiotic transmittances ####################
    
#calculating prebiotic transmittance for Br-
trans_prebio_br = array(zeros(33))
for x in range(33):
    trans_prebio_br[x] = 10 ** (-1 * ab_prebio_br[x])
    
#calculating prebiotic transmittance for NO3-
trans_prebio_no3 = array(zeros(33))
for x in range(33):
    trans_prebio_no3[x] = 10 ** (-1 * ab_prebio_no3[x])
    
#calculating prebiotic transmittance for Fe2+
trans_prebio_fe = array(zeros(41))
for x in range(41):
    trans_prebio_fe[x] = 10 ** (-1 * ab_prebio_fe[x])
    
#calculating prebiotic transmittance for FeCl2
trans_prebio_fecl2 = array(zeros(41))
for x in range(41):
    trans_prebio_fecl2[x] = 10 ** (-1 * ab_prebio_fecl2[x])
    
#calculating prebiotic transmittance for FeSO4
trans_prebio_feso4 = array(zeros(41))
for x in range(41):
    trans_prebio_feso4[x] = 10 ** (-1 * ab_prebio_feso4[x])
    
#calculating total prebiotic transmittance
trans_prebio_tot = array(zeros(33))
for x in range(33):
    trans_prebio_tot[x] = 10 ** (-1 * ab_prebio_tot[x])
    
################## calculating wavenumber for Fe2+ check ######################

#calculating wavenumber for Fe(BF4)2
wn_fe2 = array(zeros(33))
for x in range(33):
    wn_fe2[x] = 1 / wv_fe2[x] * 1e7
    
#calculating wavenumber for Cl
wn_cl = array(zeros(33))
for x in range(33):
    wn_cl[x] = 1 / wv_cl[x] * 1e7
    
#calculating wavenumber for Fe2+
wn_fe = array(zeros(41))
for x in range(41):
    wn_fe[x] = 1 / wv_fe[x] * 1e7
    
#calculating wavenumber for SO4
wn_so4 = array(zeros(41))
for x in range(41):
    wn_so4[x] = 1 / wv_so4[x] * 1e7
    

################### calculating check absorptivities for Fe2+ #################
    
#calculating check absorptivity for Fe2+ to use w/ cl
check_ab_fe2 = array(zeros(33))
for x in range(33):
    check_ab_fe2[x] = const_fe2[x] * M_fe2_check
    
#calculating check absorptivity for Cl
check_ab_cl = array(zeros(33))
for x in range(33):
    check_ab_cl[x] = const_cl[x] * M_fe2_check * 2

#calculating total absorptivity to check FeCl2
check_ab_fecl2 = array(zeros(33))
for x in range(33):
    check_ab_fecl2[x] = check_ab_cl[x] + check_ab_fe2[x]
    
#calculating check absorptivity for Fe2+
check_ab_fe = array(zeros(41))
for x in range(41):
    check_ab_fe[x] = const_fe[x] * M_fe2_check
    
#calculating check absorptivity for SO4 at pH 10.4
check_ab_so4_b = array(zeros(41))
for x in range(41):
    check_ab_so4_b[x] = const_so4_b[x] * M_fe2_check 

#calculating total absorptivity to check FeSO4 at pH 10.4
check_ab_feso4_b = array(zeros(41))
for x in range(41):
    check_ab_feso4_b[x] = check_ab_fe[x] + check_ab_so4_b[x]
    
#calculating check absorptivity for SO4 at pH 5.5
check_ab_so4_a = array(zeros(41))
for x in range(41):
    check_ab_so4_a[x] = const_so4_a[x] * M_fe2_check
    
#calculating total absorptivity to check FeSO4 at pH 10.4
check_ab_feso4_a = array(zeros(41))
for x in range(41):
    check_ab_feso4_a[x] = check_ab_fe[x] + check_ab_so4_a[x]    

##################### plotting Johnson data as check ##########################

#plotting molar absorption coefficients
plt.plot(wv_br, const_br, "go", label="Br-") #plotting Br-
#plt.plot(wv_hs, const_hs, "yo", label="HS-") #plotting HS-
plt.plot(wv_no3, const_no3, "co", label="NO3-") #plotting NO3-
plt.plot(wv_no2, const_no2, "ko", label="NO2-") #plotting NO2-
plt.plot(wv_fe, const_fe, "mo", label="Fe2+") #plotting Fe2+
plt.plot(wv_fe2, const_fe2, "mo") #plotting Fe2+ in the deep UV
plt.plot(wv_fecl2, const_fecl2, "bo", label="FeCl2") #plotting FeCl2
plt.plot(wv_feso4, const_feso4, "ro", label="FeSO4") #plotting FeSO4
plt.plot(wv_gelbstoff, molabs_gelbstoff, "ko", label="gelbstoff") #plotting gelbstoff
plt.plot(wv_i, molabs_i, "yo", label="I-")
#plt.plot(wv_so4, molabs_so4_base, "b*", label="SO4 base" )
#plt.plot(wv_so4, molabs_so4_acid, "r*", label="SO4 acid" )
plt.xlabel("Wavelength (nm)") #titling x axis
plt.ylabel("Molar Absorption Coefficient (cm^-1 M^-1)") #titling y axis
plt.title("Molar Absorption Coefficients") #titling graph
plt.legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
#plt.savefig("Molar Absorption Coefficients of Salts, Johnson paper.pdf") #saving graph as pdf
plt.show() #display graph

#plotting absorption values as given in the Johnson paper
plt.plot(wv_br, ab_br, "go", label="%s M Br-" %(M_br_gv)) #plotting Br-
plt.plot(wv_hs, ab_hs, "yo", label="%s M HS-" %(M_hs_gv)) #plotting HS-
plt.plot(wv_no3, ab_no3, "co", label="%s M NO3-" %(M_no3_gv)) #plotting NO3-
plt.plot(wv_no2, ab_no2, "bo", label="%s M NO2-" %(M_no2_gv)) #plotting NO2-
plt.xlabel("Wavelength (nm)") #titling x axis
plt.ylabel("Absorption") #titling y axis
plt.title("Absorption at 1 cm (from Johnson Paper)") #titling graph
plt.legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
#plt.savefig("Absorption Johnson.pdf") #saving graph as pdf
plt.show() #display graph

###################### plotting Fe2+ check graphs ############################

#fig, axes = plt.subplots(3,figsize=(5.,10.))
#
#axes[0].plot(wn_cl, check_ab_fecl2, "go", label="FeCl2")
#axes[0].set_xlabel("Wavenumber (cm^-1)") #titling x axis
#axes[0].set_ylabel("Molar Extinction (cm^-1)") #titling y axis
#axes[0].set_title("Check FeCl2") #titling graph
#axes[0].legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
#axes[0].set_yscale("log")
#
#axes[1].plot(wn_so4, check_ab_feso4_b, "mo", label="FeSO4 at 10.4 pH")
#axes[1].set_xlabel("Wavenumber (cm^-1)") #titling x axis
#axes[1].set_ylabel("Molar Extinction (cm^-1)") #titling y axis
#axes[1].set_title("Check FeSO4 at 10.4 pH") #titling graph
#axes[1].legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
#axes[1].set_yscale("log")
#
#axes[2].plot(wn_so4, check_ab_feso4_a, "mo", label="FeSO4 at 5.5 pH")
#axes[2].set_xlabel("Wavenumber (cm^-1)") #titling x axis
#axes[2].set_ylabel("Molar Extinction (cm^-1)") #titling y axis
#axes[2].set_title("Check FeSO4 at 5.5 pH") #titling graph
#axes[2].legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
#axes[2].set_yscale("log")
#
#plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
##plt.savefig("Fe2+ check.pdf", orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf
#plt.show() #display graph##
#
#
#
#plt.plot(wv_cl, check_ab_fecl2, "go", label="constructed FeCl2")
#plt.plot(wv_so4, check_ab_feso4_b, "mo", label="constructed FeSO4 at 10.4 pH")
#plt.plot(wv_so4, check_ab_feso4_a, "bo", label="constructed FeSO4 at 5.5 pH")
#plt.plot(wv_fecl2, ab_fecl2, "co", label="Fontana FeCl2")
#plt.plot(wv_feso4, ab_feso4, "yo", label= "Fontana FeSO4")
#plt.plot(wv_fe, ab_fe, "ro", label="Fontana Fe(BF4)2")
#axes[2].set_xlabel("Wavenumber (cm^-1)") #titling x axis
#plt.ylabel("Molar Extinction (cm^-1)") #titling y axis
#plt.title("Check Fe2+") #titling graph
#plt.legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
##plt.yscale("log")
##plt.savefig("Fe2+ check one plot.pdf", orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf
#
#plt.show()
###################### plotting for HS- and NO3- only##########################

#fig, axes = plt.subplots(3,figsize=(8.,10.))

##plotting molar absorbance coefficients
#axes[0].plot(wv_hs, const_hs, "yo", label="HS-") #plotting HS-
#axes[0].plot(wv_no3, const_no3, "co", label="NO3-") #plotting NO3-
#axes[0].set_xlabel("Wavelength (nm)") #titling x axis
#axes[0].set_ylabel("Molar Absorption Coefficient (cm^-1 M^-1)") #titling y axis
#axes[0].set_title("Molar Absorption Coefficients for HS- and NO3-") #titling graph
#axes[0].legend(loc="best", ncol=2,borderaxespad=0, fontsize=10) #creating legend
##plt.savefig("Molar Absorption Coefficients of HS- and NO3-, Johnson paper.pdf") #saving graph as pdf
##plt.show() #display graph
#
##plotting experimental absorbance values
#axes[1].plot(wv_hs, ab_ex_hs, "yo", label="HS- %d \u03BCM" %(M_hs_ex * 1e6)) #plotting HS-
#axes[1].plot(wv_no3, ab_ex_no3, "co", label="NO3- %d \u03BCM" %(M_no3_ex * 1e6)) #plotting NO3-
#axes[1].set_xlabel("Wavelength (nm)") #titling x axis
#axes[1].set_ylabel("Absorbance at %s cm" %(s)) #titling y axis
#axes[1].set_title("Absorbance of HS- and NO3- at %s cm" %(s))#
#axes[1].legend(loc="best", ncol=2,borderaxespad=0, fontsize=10)
#axes[1].axis([190,270,0,1.1]) #setting axis minima and maxima
##plt.savefig("Absorbance of HS- and NO3- at %s cm, Johnson paper.pdf" %(s)) #saving graph as pdf
##plt.show() #display graph
#
##plotting transmittance values
#axes[2].plot(wv_hs, trans_hs, "yo", label="HS- %d \u03BCM" %(M_hs_ex * 1e6)) #plotting HS-
#axes[2].plot(wv_no3, trans_no3, "co", label="NO3- %d \u03BCM" %(M_no3_ex * 1e6)) #plotting NO3-
#axes[2].set_xlabel("Wavelength (nm)") #titling x axis
#axes[2].set_ylabel("Transmittance") #titling y axis
#axes[2].set_title("Transmittance for HS- and NO3- at %s cm" %(s)) #titling graph
#axes[2].legend(loc="best", ncol=2, borderaxespad=0, fontsize=8)
#axes[2].axis([190,270,0,1.1]) #setting axis minima and maxima
##plt.savefig("Transmittance for HS- and NO3- at %s cm.pdf" %(s)) #saving graph as pdf
##plt.show() #display graph
#
#plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
#plt.savefig("HS- and NO3- at %s cm.pdf" %(s), orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf
##plt.show()###############

##################### plottting Fe2+ checks ocean water #########################


######################## plotting modern oceans ###############################

##plotting transmittance for specified path length

fig, axes = plt.subplots(3, figsize=(8.,10,))

axes[0].plot(wv_br, trans_br, "go", label="%s M Br-" %(M_br_ex)) #plotting Br-
#axes[0].plot(wv_hs, trans_hs, "yo", label="%s M HS-" %(M_hs_ex)) #plotting HS-
axes[0].plot(wv_no3, trans_no3, "co", label="%s M NO3-" %(M_no3_ex)) #plotting NO3-
axes[0].plot(wv_no2, trans_no2, "bo", label="%s M NO2-" %(M_no2_ex)) #plotting NO2-
axes[0].plot(wv_no2, trans_tot, "ro", label="total transmittance") #plotting total transmittance
#axes[0].set_yscale("log")
axes[0].set_xlabel("Wavelength (nm)") #titling x axis
axes[0].set_ylabel("Transmittance") #titling y axis
axes[0].set_title("Transmittance in Modern Oceans at %s cm" %(s)) #titling graph
axes[0].legend(loc="best", borderaxespad=0, fontsize=10) #creating legend

#plotting absorbance values for specified path lenght
axes[1].plot(wv_br, ab_mod_br, "go", label="%s M Br-" %(M_br_ex)) #plotting Br-
axes[1].plot(wv_hs, ab_mod_hs, "yo", label="%s M HS-" %(M_hs_ex)) #plotting HS-
axes[1].plot(wv_no3, ab_mod_no3, "co", label="%s M NO3-" %(M_no3_ex)) #plotting NO3-
axes[1].plot(wv_no2, ab_mod_no2, "bo", label="%s M NO2-" %(M_no2_ex)) #plotting NO2-
axes[1].plot(wv_no2, ab_mod_tot, "ro", label="total absorbance") #plotting total absorbance
#axes[1].set_yscale("log")
axes[1].set_xlabel("Wavelength (nm)") #titling x axis
axes[1].set_ylabel("Absorption") #titling y axis
axes[1].set_title("Absorption in Modern Oceans at %s cm" %(s)) #titling graph
axes[1].legend(loc="best", borderaxespad=0, fontsize=10) #creating legend

#plotting absorptivity values for specified molarities
axes[2].plot(wv_br, cm_const_br, "go", label="%s M Br-" %(M_br_ex)) #plotting Br-
axes[2].plot(wv_hs, cm_const_hs, "yo", label="%s M HS-" %(M_hs_ex)) #plotting HS-
axes[2].plot(wv_no3, cm_const_no3, "co", label="%s M NO3-" %(M_no3_ex)) #plotting NO3-
axes[2].plot(wv_no2, cm_const_no2, "bo", label="%s M NO2-" %(M_no2_ex)) #plotting NO2-
axes[2].plot(wv_no2, cm_const_tot, "ro", label="Total absorptivity") #plotting total absorptivity
axes[2].set_xlabel("Wavelength (nm)") #setting x axis title
axes[2].set_ylabel("Absorbtivity (cm^-1)") #setting y axis title
axes[2].set_yscale("log")
axes[2].set_title("Absorvtivity in Modern Ocean Waters") #setting graph title
axes[2].legend(loc="best", borderaxespad=0, fontsize=10) #creating legend

##saving absorbance and transmittance graphs as one figure
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
plt.savefig("Absorbance and Tranmittance in Modern Oceans at %s cm.pdf" %(s), orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf

##saving values for total absorptivity in a file called "constructed_modern_ocean.dat"
#np.savetxt("./Processed-Data/constructed_modern_ocean.dat", np.column_stack((wv_no2, cm_const_tot)), delimiter=",", newline="\n", fmt="%3.1f %1.6e", header="Constructed molar absorbtivity of the modern ocean\nWavelength (nm), Absorptivities (cm^-1)")

##################### plottting prebiotic ocean water #########################

#fig, axes = plt.subplots(3, figsize=(8.,10,))
#
#axes[0].plot(wv_br, trans_prebio_br, "go", label="%s M Br-" %(M_br_prebio)) #plotting Br-
#axes[0].plot(wv_no3, trans_prebio_no3, "co", label="%s M NO3-" %(M_no3_prebio)) #plotting NO3-
#axes[0].plot(wv_fe, trans_prebio_fe, "mo", label="%s M Fe2+" %(M_fe2_prebio)) #plotting Fe2+
#axes[0].plot(wv_fecl2, trans_prebio_fecl2, "bo", label="%s M FeCl2" %(M_fecl2_prebio)) #plotting FeCl2
#axes[0].plot(wv_feso4, trans_prebio_feso4, "yo", label="%s M FeSO4" %(M_feso4_prebio)) #plotting FeSO4
#axes[0].plot(wv_no2, trans_prebio_tot, "ro", label="total transmittance") #plotting total transmittance
##axes[0].set_yscale("log")
#axes[0].set_xlabel("Wavelength (nm)") #titling x axis
#axes[0].set_ylabel("Transmittance") #titling y axis
#axes[0].set_title("Transmittance in Prebiotic Oceans at %s cm" %(s)) #titling graph
#axes[0].legend(loc="best", borderaxespad=0, fontsize=10) #creating legend
#
##plotting absorbance values for specified path lenght
#axes[1].plot(wv_br, ab_prebio_br, "go", label="%s M Br-" %(M_br_prebio)) #plotting Br-
#axes[1].plot(wv_no3, ab_prebio_no3, "co", label="%s M NO3-" %(M_no3_prebio)) #plotting NO3-
#axes[1].plot(wv_fe, ab_prebio_fe, "mo", label="%s M Fe2+" %(M_fe2_prebio)) #plotting Fe2+
#axes[1].plot(wv_no2, ab_prebio_tot, "ro", label="total absorbance") #plotting total absorbance
##axes[1].set_yscale("log")
#axes[1].set_xlabel("Wavelength (nm)") #titling x axis
#axes[1].set_ylabel("Absorption") #titling y axis
#axes[1].set_title("Absorption in Prebiotic Oceans at %s cm" %(s)) #titling graph
#axes[1].legend(loc="best", borderaxespad=0, fontsize=10) #creating legend
#
##plotting absorptivity values for specified molarities
#axes[2].plot(wv_br, cm_const_prebio_br, "go", label="%s M Br-" %(M_br_prebio)) #plotting Br-
#axes[2].plot(wv_no3, cm_const_prebio_no3, "co", label="%s M NO3-" %(M_no3_prebio)) #plotting NO3-
#axes[2].plot(wv_fe, cm_const_prebio_fe, "mo", label="%s M Fe2+" %(M_fe2_prebio)) #plotting Fe2+
#axes[2].plot(wv_no2, cm_const_prebio_tot, "ro", label="Total absorptivity") #plotting total absorptivity
#axes[2].set_xlabel("Wavelength (nm)") #setting x axis title
#axes[2].set_ylabel("Absorbtivity (cm^-1)") #setting y axis title
#axes[2].set_yscale("log")
#axes[2].set_title("Absorvtivity in Prebiotic Ocean Waters") #setting graph title
#axes[2].legend(loc="best", borderaxespad=0, fontsize=10) #creating legend
#
##saving absorbance and transmittance graphs as one figure
#plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.01, hspace=0.4) #adjusting spacing
##plt.savefig("Absorbance and Tranmittance in Prebiotic Oceans at %s cm.pdf" %(s), orientation="portrait", papertype='letter', format="pdf") #saving graph as pdf





