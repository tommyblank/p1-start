import matplotlib.pyplot as plt
import numpy as np
import sys

tungsten_raw="raw-data/Sp15_245L_sec-001_group-01_bendtest-tungsten.raw"
tungsten2_raw="raw-data/Sp15_245L_sec-001_group-01_bendtest-tungsten2.raw"
tungsten3_raw="raw-data/Sp15_245L_sec-001_group-01_bendtest-tungsten3.raw"
glass_raw="raw-data/Sp15_245L_sect-001_group-1_glass.raw"
ultem_raw="raw-data/Sp15_245L_sect-001_group-1_ultem.raw"
steel_raw="raw-data/Sp15_245L_sect-001_group-2-4_bendtest-steel.raw"
aluminum_raw="raw-data/Sp15_245L_sec-001_group-01_bendtest-aluminum.raw"
aluminum2_raw="raw-data/Sp15_245L_sec-001_group-01_bendtest-aluminum2.raw"
aluminum3_raw="raw-data/Sp15_245L_sec-001_group-01_bendtest-aluminum3.raw"

filename = aluminum_raw        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
#Plotting Stress vs Strain
data = np.loadtxt(filename,skiprows=32,delimiter=',')
range=(len(data))
stress=abs(data[0:, 3])
strain=abs(data[0:, 7])
plt.plot(strain, stress,'k-', linestyle='solid', label='Stress vs. Strain')

#Plotting Linear fit
m1,b1=np.polyfit(strain,stress,1)
plt.plot(strain,strain*m1+b1,'g--',linestyle='dashed',label='Linear Fit')

#Labeling graph
plt.title(filename, loc='center')
plt.grid(True)
plt.xlabel('Strain (Ext %)')
plt.ylabel('Stress (MPa)')

#Saving Graph
plt.savefig(filename+'.pdf')

#Printing Graph
plt.legend(loc='best')
plt.show()   # Attempts to load filename into local variable data.

#Printing Young's Modulus
print("The Young's Modulus of ")
print(filename)
print('=')
print(m1)
print('MPa')

## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.


#Well I tried my very best, and that's all anyone can really ask for.
#I just wish I could figure out how to get the linear fit to be over the right area.
#I was looking through everyone files, and out of the ones I could understand,
#No one could figure it out. But I just may be dumb and did not read any of them right.
