#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:17:02 2019

@author: s1420671
"""

import numpy as np
from netCDF4 import Dataset
import os
import matplotlib.pyplot as plt



date = ['200401','200402','200403','200404','200405','200406','200407','200408',
        '200409','200410','200411','200412','200501','200502','200503','200504',
        '200505','200506','200507','200508','200509','200510','200511','200512',
        '200601','200602','200603','200604','200605','200606','200607','200608',
        '200609','200610','200611','200612','200701','200702','200703','200704',
        '200705','200706','200707','200708','200709','200710','200711','200712',
        '200801','200802','200803','200804','200805','200806','200807','200808',
        '200809','200810','200811','200812','200901','200902','200903','200904',
        '200905','200906','200907','200908','200909','200910','200911','200912',
        '201001','201002','201003','201004','201005','201006','201007','201008',
        '201009','201010','201011','201012','201101','201102','201103','201104',
        '201105','201106','201107','201108','201109','201110','201111','201112',
        '201201','201202','201203','201204','201205','201206','201207','201208',
        '201209','201210','201211','201212','201301','201302','201303','201304',
        '201305','201306','201307','201308','201309','201310','201311','201312',
        '201401','201402','201403','201404','201405','201406','201407','201408',
        '201409','201410','201411','201412','201501','201502','201503','201504',
        '201505','201506','201507','201508','201509','201510','201611','201512',
        '201601','201602','201603','201604','201605','201606','201607','201608',
        '201609','201610','201611','201612']

nmonths = len(date)

mix13 = []

os.chdir('/geos/d21/s1420671/13CH4/forward/tries/forward')

for n in np.arange(0,len(date)-1,1):
    methane_12c= 'out.{}01.nc'.format((str(date[n])))
    fh = Dataset(methane_12c, mode='r')  
    CH4 = fh.variables['IJ-AVG-S__CH4'][:]
    fh.close()
    MixR =CH4[0,:,:]
    mix13 = np.append(mix13, np.mean(MixR))
    
    
    
mix12 = []

os.chdir('/geos/d21/s1420671/12CH4/prior')
for n in np.arange(1,len(date),1):
    methane_12c= 'out.{}01.nc'.format((str(date[n])))
    #methane_12c= 'GEOSChem_restart.{}010000.nc'.format((str(date[n])))
    fh = Dataset(methane_12c, mode='r')  
    CH4 = fh.variables['IJ-AVG-S__CH4'][:]
    #CH4 = fh.variables['SPC_CH4'][:]
    fh.close()
    MixR =CH4[0,:,:]
    mix12 = np.append(mix12, np.mean(MixR))

tot=[]
    
#os.chdir('/geos/d21/s1420671/jacobian/12CH4/14yr/forward/goodsites')
os.chdir('/geos/d21/s1420671/jacobian/12CH4/14yr/forward/normal')
for n in np.arange(1,len(date),1):
    methane_12c= 'out.{}01.nc'.format((str(date[n])))
    fh = Dataset(methane_12c, mode='r')  
    CH4 = fh.variables['IJ-AVG-S__CH4'][:]
    fh.close()
    MixR =CH4[0,:,:]
    tot = np.append(tot, np.mean(MixR))
    

#mix12=mix12*0.965
#mix13=mix13*1.035
#0.0112372
   
d13 = (((mix13/mix12)/0.0112372)-1)*1000
        

import pandas as pd
x = pd.date_range(start='1/1/2004', end='1/1/2017', periods=nmonths-1)        
     

fig=plt.figure()

fig.set_figheight(10)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)

plt.subplot(4,1,1)
plt.plot(x, tot)
plt.ylabel('total CH4 (ppb)', fontsize=12)
plt.grid()
plt.subplot(4,1,2)
plt.plot(x, mix12)
plt.ylabel('12CH4 (ppb)', fontsize=12)
plt.grid()
plt.subplot(4,1,3)
plt.plot(x,mix13)
plt.ylabel('13CH4 (ppb)', fontsize=12)
plt.grid()
plt.subplot(4,1,4)
plt.plot(x,d13)
plt.ylim(-55,-35)
plt.xlabel('Date')
plt.ylabel('d13C (ppt)', fontsize=12)
plt.grid()





#os.chdir("/home/s1420671/python/Timeseries_Plots/d13_longinv/")
#plt.savefig("d13C_prior_run.jpg")

