# Python package plot weather data stored in a csv file.

The input data file (JCMB_2011.zip) contains minute by minute weather measurements (atmospheric pressure (mBar), wind speed (m/s), relative humidity (%), etc.) covering January to October 2001. The code also contains a date-time field. Some fields contain erroneous data, which needs to be identified and handled.

This python package completes a number of tasks. First it opens the csv file and passes the data stored in the file to a dictionary - the first line of the dictionary is used as keys, while the data stored in the remaining corresponding fields are split, stripped and assigned to the dictionary as values. A check is made for erroneous data before adding to the dictionary.

A seperate function handles the date-time field, first checking for and handling invalid entries and then stripping the date and time to create a datetime object.

A final function is then used to plot the different weather measurements, including labels, titles, etc. using matplotlib.
