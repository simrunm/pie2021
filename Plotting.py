import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d
import pandas as pd

# Calibration Datas
actual_distance = [7,8,9,10,11,12,13,14,15,16,17,18,19,20]
voltage_reading = [500,482,460,443,418,393,370,352,330,312,292,281,276,273]


def find_m_b():
    '''Find a line of best fit for calibration'''
    m, b = np.polyfit(actual_distance, voltage_reading, 1)
    return m,b

def plot_calibration_curve():
    '''Plot distance and calibration'''
    # plot raw data
    plt.plot(actual_distance, voltage_reading, 'ko')
    # find the equation for line of best fit
    m,b = find_m_b()
    y_points = []
    for point in actual_distance:
        y_points.append(point * m + b)
    # plotting the line of best fit
    plt.plot(actual_distance,y_points,'b-')
    plt.xlabel("Actual Distance/ in")
    plt.ylabel("Voltage/ V")
    plt.title('Calibration Plot')
    plt.show()

# Voltage to distance
def voltage_to_distance(voltage,m,b):
    '''Converting voltage to distance based on the calibration'''
    distance = (voltage - b)/m
    return distance

def plot_error_plot():
    ''' Plot error plot for some distances not used while calibrating'''
    m,b = find_m_b()
    # Data from sensor for actual voltage and distance
    extra_distances = [14.5,18.5,23,9.5,11.5,20.5,15.5]
    extra_voltage = [330,256,201,430,386,224,298]
    residuals = []
    # Finding the predicted distance based on calibration function
    for i in range(len(extra_distances)):
        predicted_distance = (extra_voltage[i] - b) / m
        residuals.append(predicted_distance - extra_distances[i])
    # Plotting a stem plot
    plt.stem(extra_distances, residuals)
    plt.xlabel("Actual Distance / in")
    plt.ylabel("Difference between Predicted and Actual Distance / in")
    plt.title('Error Plot')
    plt.show()    

def polar2cart(r, theta, phi):
    ''' Converting spherical coordinates to cartesian coordinates based
    on equations from an online source: 
    https://en.wikipedia.org/wiki/Spherical_coordinate_system
    '''   
    x = r * math.sin(theta*(math.pi/180)) * math.cos(phi*(math.pi/180)), 
    y = r * math.sin(theta*(math.pi/180)) * math.sin(phi*(math.pi/180)),
    z = r * math.cos(theta*(math.pi/180))
    return x,y,z

def polar2cart2d(r, theta):
    ''' Converting polar coordinates to cartesian coordinates'''
    x = r * math.cos(theta*(math.pi/180)),
    y = r * math.sin(theta*(math.pi/180))
    return x,y


def axisEqual3D(ax):
    ''' Helper function taken to set axes equal for 3d graphs taken from here:
    https://newbedev.com/set-matplotlib-3d-plot-aspect-ratio '''
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)

# Make a 3d plot
def plot_3d(xdata,ydata,zdata):
    """ Making a 3d scatter plot based on input data"""
    ax = plt.axes(projection='3d')    
    ax.scatter(xdata, ydata, zdata)    
    axisEqual3D(ax)
    plt.xlabel('X')
    plt.ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Scan of Letter')
    plt.show()

def plot_3d_2(xdata,ydata,zdata,diff_x,diff_y,diff_z):
    ''' Making two 3d scatter plots of different colors'''
    ax = plt.axes(projection='3d')    
    ax.scatter(xdata, ydata, zdata,c='lightblue')
    ax.scatter(diff_x, diff_y, diff_z,c='blue')    
    axisEqual3D(ax)
    plt.xlabel('X')
    plt.ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Scan of Letter')
    plt.show()


def plot_2d(xdata,ydata): 
    """ Making a 2d scatter plot"""   
    ax = plt.axes()    
    ax.scatter(xdata, ydata)
    plt.title('2D Scan of E')
    plt.xlabel('Distance along cross section')
    plt.ylabel('Distance to point / in')

def parse_y_data(xdata,ydata,zdata):
    """ Parsing through y data for points past a certain threshold so that 
        they can be plotted as a different color on the graph to make it easier to see
    """
    diff_x = []
    diff_y = []
    diff_z = []
    # If the y value is beyond 21, then that point is for the wall.
    # This loop is seperating out the poitns that are for the letter and wall 
    # so that they can be plotted seperately.
    for i in range(len(ydata)):
        if ydata[i] > 21:
            diff_x.append(xdata[i])
            diff_y.append(ydata[i])
            diff_z.append(zdata[i])
            xdata[i] = 0
            ydata[i] = 0
            zdata[i] = 0
    xdata = [x for x in xdata if x != 0]
    ydata = [x for x in ydata if x != 0]
    zdata = [x for x in zdata if x != 0]
    return xdata,ydata,zdata,diff_x,diff_y,diff_z


def csv_to_plot():
    distance = []
    xdata = []
    ydata = []
    zdata = []
    m,b = find_m_b()
    df = pd.read_csv (r'full_scan2.csv')
    voltage_list = df['Voltage'].tolist()
    pan_list = df['Pan Angle'].tolist()
    tilt_list = df['Tilt Angle'].tolist()
    for voltage in voltage_list:
        distance.append(voltage_to_distance(voltage,m,b))
    for i in range(len(pan_list)):
       x,y,z =  polar2cart(distance[i], tilt_list[i],pan_list[i])
       xdata.append(x[0])
       ydata.append(y[0])
       zdata.append(z)
    # zdata = [0] * 81
    newx,newy,newz,diff_x,diff_y,diff_z = parse_y_data(xdata,ydata,zdata)
    # plot_3d(xdata,ydata,zdata)
    plot_3d_2(diff_x,diff_y,diff_z,newx,newy,newz)

def csv_to_plot_2d():
    distance = []
    xdata = []
    ydata = []
    m,b = find_m_b()
    df = pd.read_csv (r'single_servo2.csv')
    voltage_list = df['Voltage'].tolist()
    tilt_list = df['Tilt Angle'].tolist()
    # tilt_list = [angle - 50 for angle in tilt_list]
    for voltage in voltage_list:
        distance.append(voltage_to_distance(voltage,m,b))
    for i in range(len(tilt_list)):
       x,y =  polar2cart2d(distance[i], tilt_list[i])
       x = x[0] + 15
       xdata.append(x)
       ydata.append(y)
    plot_2d(xdata,ydata)
    plt.show()


    
csv_to_plot_2d()
csv_to_plot()
# plot_calibration_curve()
# plot_error_plot()

