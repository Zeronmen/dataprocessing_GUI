# These are the files that need to be imported. 

import numpy as np
import string as st
import os.path as path

def createfile( filename ):
    """
        Creates the output file.
        input: filename 
        return: none 
    """
    Data_output = open(filename + '.csv','w')
    Data_output.write('Voc,\t Isc,\t FF,\t RR\n')

    Data_output.close()
    return


def access(batchnumber,device,pixel):
    """
        Checks if the datafile exists. If true imports the data.
        input: batchnumber, devicenumber, pixelnumber
        return: datax, datay
    """
    file = 'PV' + '%d' % batchnumber + '_' + st.ascii_uppercase[device - 1] + '_' + 'P' + '%d' % pixel 
    if path.isfile(file + '.txt'):
        datax,datay = np.loadtxt(file + '.txt',skiprows=1,unpack=True)
    else:
        datax = np.array([0,0])
        datay = datax
    
    return datax,datay

def adddata (voc, isc, FF, RR, filename):
    """
        Adds the input to a file.
        input: voc,isc,FF,RR,filename
        return: none
    """
    Data_output = open(filename + '.csv','a')
    Data_output.write('%f,%1.20f,%f,%f\n' % (voc, isc, FF, RR))

    Data_output.close()
    return

def addline (string,filename):
    """
        Adds a string to a file.
        input: string, filename
        return: none
    """
    Data_output = open(filename + '.csv','a')
    Data_output.write(string  + ', , , ' + '\n')
    
    Data_output.close()
    return

def process (datax, datay):
    """
        Processes data.
        input: datax, datay
        return: (voc,isc,FF,RR) OR string contaning error message 
    """
    Vstep = datax[0]-datax[1]
    if datax[0] == 0:
        return 'NO DATA'
    else:    
        powerdata = datax*np.absolute(datay)
        neg = datay<0
        startq4 = int(np.size(datay) - np.size(datay[neg])) # First index into the 4th Quad
        endq4 = int(datax[0]/Vstep) + 1 # Index for Indi = 0.
        
        if startq4 - endq4 == 1:
            return 0,0,0,0
        else:
        # Calculates the important parameters
    
        # Open Circuit Voltage
            voc = datax[startq4] - datay[startq4]*((datax[startq4 - 1] - datax[startq4])/(datay[startq4 - 1] - datay[startq4]))
        # Short Circuit Current
            isc = datay[endq4]
            
            if   isc >= 0:
                return 'Device failure: Positive Isc'
            elif isc < 0:
                if startq4 == endq4:
                    maxpw = 0.5*voc*np.absolute(isc)
                else:
                    # Measured Max power output. During the 4th quad
                    maxpw = np.amax(powerdata[startq4 : endq4])
                    
                # Fill Factor
                FF = maxpw/(voc*np.absolute(isc))
                # Rectification Ratio
                RR = datay[0]/np.absolute(datay[-1])
                return voc,isc,FF,RR
            else:
                return 'Device failure: randomly variant current'

def process_batch(batchnumber, batchsize):
    """
        Runs the needed function to process all device data.
        input: batchnumber, batchsize
        return: none
    """
    filename = 'PV' + '%d' % batchnumber + '_results'
    createfile(filename)

    for i in range(0,batchsize):
        device = i + 1
        for j in range(0,4):
            pixel = j + 1
            # print('%d, %d' % (device, pixel)) # for troule shooting
            data = access(batchnumber, device, pixel)
            datav = data[0]
            datai = data[1]
            processeddata = process(datav, datai)
            if type(processeddata) == str:
                addline(processeddata,filename)
            else:
                adddata(processeddata[0],processeddata[1],
                        processeddata[2],processeddata[3],
                        filename)
        addline(' ',filename) 
    return
