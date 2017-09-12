# These are the files that need to be imported. 

import numpy as np
import csv
from matplotlib import pyplot as plt
import process_data as pd
import os.path as path

# Creates data for a RR vs. Voltage graph. not useful.
def RecCur(batchnumber,device,pixel):
    """
        Creates data Voltage, RR data for a plot.
        input: batchnumber, devicenumber, pixel
        return: Vdata,RRdata
    """
    data = pd.access(batchnumber,device,pixel)
    datai = data[1][0 : int(data[0][0]/0.025)]
    dataiin = data[1][::-1][0 : int(data[0][0]/0.025)]
    
    RRdata = np.abs(datai/dataiin)
    Vdata = data[0][0 : int(data[0][0]/0.025)]
    return Vdata,RRdata

# Has method for correctly setting the x and y limits for the whole plots but currently the 4th quad plots
# may need to be adjusted depending on the data. and plot may need further formating to look nice.
def makeplots(batchnumber,firstdevice):
    """
        Creates plots of data.
        input: batchnumber, firstdevice
        return: none
    """

    fig, ax = plt.subplots(2,4,figsize=(15,7))
    fig.subplots_adjust(wspace=0.25)

    start = ord(firstdevice) - 64

    data = np.array([
            [access(batchnumber , i+1 , j+1) for j in range(0,4)]
            for i in range(start - 1,start + 3)])

    fplotx = np.array([data[i][0][0][0] for i in range(0,4)])
    fploty = np.array([data[i][0][1][0] for i in range(0,4)])

    ax[0,0].plot(data[0][0][0], data[0][0][1],
                 data[0][1][0], data[0][1][1],
                 data[0][2][0], data[0][2][1],
                 data[0][3][0], data[0][3][1])

    ax[0,1].plot(data[0][0][0], data[0][0][1],
                 data[0][1][0], data[0][1][1],
                 data[0][2][0], data[0][2][1],
                 data[0][3][0], data[0][3][1])

    ax[0,2].plot(data[1][0][0], data[1][0][1],
                 data[1][1][0], data[1][1][1],
                 data[1][2][0], data[1][2][1],
                 data[1][3][0], data[1][3][1])

    ax[0,3].plot(data[1][0][0], data[1][0][1],
                 data[1][1][0], data[1][1][1],
                 data[1][2][0], data[1][2][1],
                 data[1][3][0], data[1][3][1])

    ax[1,0].plot(data[2][0][0], data[2][0][1],
                 data[2][1][0], data[2][1][1],
                 data[2][2][0], data[2][2][1],
                 data[2][3][0], data[2][3][1])

    ax[1,1].plot(data[2][0][0], data[2][0][1],
                 data[2][1][0], data[2][1][1],
                 data[2][2][0], data[2][2][1],
                 data[2][3][0], data[2][3][1])

    ax[1,2].plot(data[3][0][0], data[3][0][1],
                 data[3][1][0], data[3][1][1],
                 data[3][2][0], data[3][2][1],
                 data[3][3][0], data[3][3][1])

    ax[1,3].plot(data[3][0][0], data[3][0][1],
                 data[3][1][0], data[3][1][1],
                 data[3][2][0], data[3][2][1],
                 data[3][3][0], data[3][3][1])

    ax[0,0].set_xlim(-fplotx[0],fplotx[0])
    ax[0,0].set_ylim(-fploty[0],fploty[0])

    ax[0,2].set_xlim(-fplotx[1],fplotx[1])
    ax[0,2].set_ylim(-fploty[1],fploty[1])

    ax[1,0].set_xlim(-fplotx[2],fplotx[2])
    ax[1,0].set_ylim(-fploty[2],fploty[2])

    ax[1,2].set_xlim(-fplotx[3],fplotx[3])
    ax[1,2].set_ylim(-fploty[3],fploty[3])

    ax[0,1].set_xlim(0,1)
    ax[0,1].set_ylim(-20*10**(-8), 10 ** (-9))

    ax[0,3].set_xlim(0,1)
    ax[0,3].set_ylim(-20*10 ** (-8), 10 ** (-9))

    ax[1,1].set_xlim(0,1)
    ax[1,1].set_ylim(-20*10 ** (-8), 10 ** (-9))

    ax[1,3].set_xlim(0,1)
    ax[1,3].set_ylim(-20*10 ** (-8), 10 ** (-9))

    
    plt.show()
    
    return

# Imports a set of data to be analysized.
def data_import(batchnumber):
    """
        Imports already processed for data for analysis.
        input: batchnumber
        return dataset
    """
    
    Data_input =  open('PV' + '%d' % batchnumber + '_results.csv','r')
    read = csv.reader(Data_input, quotechar='|')

    dataset = []

    for row in read:
        dataset.append(row)
    
    data.close()

    del dataset[0]
    for i in range(len(dataset) - 1 ,0 - 1,-1):
        if dataset[i][3] == ' ': 
            del dataset[i]
        else:
            for j in range(0,4):
                dataset[i][j] = float(dataset[i][j])
    return dataset