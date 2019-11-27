#Exam number: B140990

#an attribute to hold the list of names of fucntions to import as part of the module
__all__ = ['date_time_converter', 'in_out', 'plotter']

#import various libraries for use in the program
import numpy as np
import numpy.ma as ma
from datetime import datetime
from datetime import timedelta
from matplotlib import pyplot as plt

#a function to handle the date-time data in the input file, including handling erroneous data
#a datestring object is returned
def date_time_converter(datestring):
    #if datestring contains an erroneous time value of 24:00, convert it to the correct 00:00
    #convert to datestring and then add a day to compensate for the time change.
    if '24:00' in datestring:
        date=datestring.replace('24:00','00:00')
        date=datetime.strptime(date, '%Y/%m/%d %H:%M')
        date=date+timedelta(days=1)
    #if the datestring does not contain an erroneous value convert to datetime object
    else:
        date=datetime.strptime(datestring, '%Y/%m/%d %H:%M')
    return date

#a function to open the input file, create a list from the headers, add to a dictionary as keys,and
#append the remaining data in the file to the dictionary as values. The function also applies a
#masked array to the dictionary in order to exlude erroneous data in the input file (e.g. -9999). 
#A dictionary is returned from the function.
def in_out(filename):
    with open(filename) as csv_file:
        #read the first line of the input file, strip the '\n', split it on ',' and
        #assign to a new variable. These will be used as the keys in the new dictionary.
        first_line=csv_file.readline()
        first_line=first_line.strip('\n').split(',')
        
        #create a dictionary to hold the data from the input file
        ddict={}
        
        #write the data held in the variable first_line to the dictionary for use as keys
        #in the dictionary
        for element in first_line:
            ddict[element]=[]
        
        #read the remaining lines in the input file, strip the '\n', split it on ',' convert
        #the first row to a datetime object, and the remaining rows to float values and 
        #append to the dictionary.
        for line in csv_file:
            data_row=line.strip('\n').split(',')
            #call the function to convert the date-time string to a datetime object and
            #append the returned value to the dictionary
            ddict[first_line[0]].append(date_time_converter(data_row[0])) 
            for i in range(1,len(data_row)):
                ddict[first_line[i]].append(float(data_row[i]))
                        
        #pass the values in the dictionary to an array based on keys
        for key in ddict:
            ddict[key]=np.array(ddict[key])
               
        #based on keys, excluding the datetime row, check to see if the values in the array
        #are less than -1000. These values are considered erroneous and will be masked.
        for key in ddict:
            if key!='date-time':
                ddict[key]=ma.masked_where(ddict[key] <-1000, ddict[key])
        
        #return the dictionary
        return ddict

#a function to plot data handed to the function, inlcuding the date-time, surface temp, rainfall,
#wind speed, and atmospheric data.  A label for each table is also passed to label the y value 
#for each of the four plots
def plotter(xvalue, column, label):
    
    #plot the data
    plt.plot(xvalue, column)
    
    #format the plot to make it more readable
    plt.ylabel(label)
    plt.xlabel('Date & Time')
    plt.xticks(rotation=45)
    plt.title(label + ' for the year 2011') 
    plt.grid(color = 'gray')

    #show the plot
    plt.show() 


