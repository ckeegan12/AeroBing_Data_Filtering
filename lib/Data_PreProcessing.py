import numpy as np
import pandas as pd

# Import Data SETS
SENSOR_DATA = pd.read_csv("ckeegan12/AeroBing_Data_Filtering/Flight_Data/SHART_SENSOR_DATA_copy.csv")
GPS_DATA = pd.read_csv("ckeegan12/AeroBing_Data_Filtering/Flight_Data/SHART_GPS_DATA_copy.csv")

def Get_Variables(File,Variable_Name):
  return pd.read_csv(File,usecols=Variable_Name)

# GPS DATA VARIABLES
GPS_File = 'ckeegan12/AeroBing_Data_Filtering/Flight_Data/SHART_GPS_DATA_copy.csv'
GPS_Variable_Name = ['time','latitude','longitude','altitude','vel_n','vel_e','vel_d','eph','epv','sacc','gspeed','pdop','nsats','fix_type','valid','flags']

df_GPS = Get_Variables(GPS_File,GPS_Variable_Name)
GPS_time = df_GPS['time']

# SENSOR DATA VARIABLES
SENSOR_File = 'ckeegan12/AeroBing_Data_Filtering/Flight_Data/SHART_SENSOR_DATA_copy.csv'
SENSOR_Variable_Name = ['time','acc_x','acc_y','acc_z','gyr_x','gyr_y','gyr_z','mag_x','mag_y','mag_z','temp','pressure','acc_x_adxl','acc_y_adxl','acc_y_adxl','status','sd_file']

df_SENSOR = Get_Variables(SENSOR_File,SENSOR_Variable_Name)
SENSOR_time = df_SENSOR['time']
