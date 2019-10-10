#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:59:24 2018

@author: s1420671
"""

from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import os



lati=[42,33,31,28,27,21,12, 9, 0]
loni=[38,15,23,37, 5,47,71,22,48]

nsites = len(loni)


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
nmonths=len(date)

mix = []

os.chdir('/geos/d21/s1420671/jacobian/12CH4/14yr/forward/normal')

for lcount in np.arange(nsites):
    lat = lati[lcount]
    lon = loni[lcount]
    
    for n in np.arange(0,len(date),1):
        methane_12c= 'out.{}01.nc'.format((str(date[n])))
        fh = Dataset(methane_12c, mode='r')  
        CH4 = fh.variables['IJ-AVG-S__CH4'][:]
        fh.close()
        MixR =CH4[0,lat,lon]
        mix = np.append(mix, MixR)


site = ['zep','nwr','bmw','ask','kum','sey','bhd','ush','spo']
mx=[]
y=[]

m=0
mx=[]
y=[]
      
for siten in np.arange(len(site)):
    #print(len(mx))
    si = site[siten]
    os.chdir('/home/s1420671/Downloads/12CH4_NOAA_observations')
    f = open("ch4_"+si+"_surface-flask_1_ccgg_month.txt", "r")
    for line in f:
        if '2004' in line:
           mx = np.append(mx,line)
        if '2005' in line:
           mx = np.append(mx,line)
        if '2006' in line:
           mx = np.append(mx,line)
        if '2007 ' in line:
           mx = np.append(mx,line)
        if '2008' in line:
           mx = np.append(mx,line)
        if '2009' in line:
           mx = np.append(mx,line)
        if '2010' in line:
           mx = np.append(mx,line)
        if '2011' in line:
           mx = np.append(mx,line)
        if '2012' in line:
           mx = np.append(mx,line)
        if '2013' in line:
           mx = np.append(mx,line)
        if '2014' in line:
           mx = np.append(mx,line)
        if '2015' in line:
            mx=np.append(mx,line)
        if '2016' in line:
           mx=np.append(mx,line)

        
            
    f.close


for line in mx:
    spl = line.split()
    y = np.append(y, float(spl[3]))
    
 
#y=y*0.988
import pandas as pd
x = pd.date_range(start='1/1/2004', end='1/1/2017', periods=nmonths)

scale=[]
pl=0

fig=plt.figure()
fig.set_figheight(15)
fig.set_figwidth(40)


for plot in np.arange(len(site)):
    s = site[plot]

    plt.subplot(3,4,plot+1)  

    plt.plot(x,mix[pl:pl+156], x,y[pl:pl+156])

    plt.title(s,fontsize=25)
    
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.legend(('GEOS-Chem', 'NOAA'),prop={'size':20})
    
    pl=pl+156
    

    if plot == 4:
        plt.ylabel('CH4 mixing ratio (ppb)',fontsize=30)

    if plot == 11:
        plt.xlabel('Month',fontsize=25)
    if plot == 8:
        plt.xlabel('Month',fontsize=25)
    if plot == 10:
        plt.xlabel('Month',fontsize=25)
    if plot == 9:
        plt.xlabel('Month',fontsize=25)

plt.subplots_adjust(hspace=0.4)


#os.chdir("/home/s1420671/python/Timeseries_Plots/")
#plt.savefig("12c_timeseries_.jpg")
