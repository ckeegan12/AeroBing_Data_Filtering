import numpy as np
import pandas as pd
import plotly as py
import plotly.graph_objs as go

# Import Data SETS
SENSOR_DATA = pd.read_csv("/workspaces/AeroBing_Data_Filtering/Flight_Data/SHART_SENSOR_DATA_copy.csv")
GPS_DATA = pd.read_csv("/workspaces/AeroBing_Data_Filtering/Flight_Data/SHART_GPS_DATA_copy.csv")

def Get_Variables(File, Variable_Name):
    return pd.read_csv(File, usecols=Variable_Name)

##### TEST CODE ######
# print(GPS_DATA.columns)
# print(SENSOR_DATA.columns)
##### TEST END #####

# GPS DATA VARIABLES
GPS_File = "/workspaces/AeroBing_Data_Filtering/Flight_Data/SHART_GPS_DATA_copy.csv"  
GPS_Variable_Name = GPS_DATA.columns

df_GPS = Get_Variables(GPS_File, GPS_Variable_Name)
GPS_time = df_GPS['time']

# SENSOR DATA VARIABLES
SENSOR_File = "/workspaces/AeroBing_Data_Filtering/Flight_Data/SHART_SENSOR_DATA_copy.csv" 
SENSOR_Variable_Name = SENSOR_DATA.columns

df_SENSOR = Get_Variables(SENSOR_File, SENSOR_Variable_Name)
SENSOR_time = df_SENSOR['time']

# VISUALIZATION OF DATA
def Plot_Var(inputx, inputy):
    trace = go.Scatter(x=inputx, y=inputy, mode='lines+markers')
    return py.iplot([trace])

# Plot GPS variables
for i in range(len(GPS_Variable_Name) - 1):
    if GPS_Variable_Name[i + 1] != 'time':  
        Plot_Var(GPS_time, df_GPS[GPS_Variable_Name[i + 1]])

# Plot SENSOR variables
for i in range(len(SENSOR_Variable_Name) - 1):
    if SENSOR_Variable_Name[i + 1] != 'time':  
        Plot_Var(SENSOR_time, df_SENSOR[SENSOR_Variable_Name[i + 1]])