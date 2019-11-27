#Exam number: B140990
import IO_CSV
from matplotlib import pyplot as plt

#an attribute to hold a list of names of fucntions to import as part of the module
if __name__=='__main__':
    #assign the input filename to the variable 'filename' which will be handed to the first function
    filename='JCMB_2011.csv'
    
    #call the function in_out and assign the results to variable data
    data=IO_CSV.in_out(filename)
    
    #call the function plotter to plot four graphs using a grid sized 10,6
    #hand the function three variables to be used for plotting and then 
    #show the plot
    plt.figure(figsize=(10,6))
    IO_CSV.plotter(data['date-time'], data['surface temperature (C)'], 'Surface Temperature')
    plt.show()

    plt.figure(figsize=(10,6))
    IO_CSV.plotter(data['date-time'], data['rainfall (mm)'], 'Rainfall')
    plt.show()

    plt.figure(figsize=(10,6))
    IO_CSV.plotter(data['date-time'], data['wind speed (m/s)'], 'Wind Speed')
    plt.show()

    plt.figure(figsize=(10,6))
    IO_CSV.plotter(data['date-time'], data['atmospheric pressure (mBar)'], 'Atmospheric Pressure')
    plt.show()



