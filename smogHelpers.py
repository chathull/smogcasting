import pandas as pd
import numpy as np

# Format dates
def formatDates(df) :
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%y%m%d %H%M')
    df = df.drop(columns=['date', 'time'])    
    return df

# Calculate AQI value from concentration
def calcAQI(concentration) :    
    if concentration <= 12.0 :
        BP_hi = 12
        BP_lo = 0
        I_hi = 50
        I_lo = 0
    elif 12.0 < concentration <= 35.4 :
        BP_hi = 35.4
        BP_lo = 12.1
        I_hi = 100
        I_lo = 51
    elif 35.4 < concentration <= 55.4 :
        BP_hi = 55.4
        BP_lo = 35.5
        I_hi = 150
        I_lo = 101
    elif 55.4 < concentration <= 150.4 :
        BP_hi = 150.4
        BP_lo = 55.5
        I_hi = 200
        I_lo = 151
    elif 150.4 < concentration <= 250.4 :
        BP_hi = 250.4
        BP_lo = 150.5
        I_hi = 300
        I_lo = 201
    elif 250.4 < concentration <= 350.4 :
        BP_hi = 350.4
        BP_lo = 250.5
        I_hi = 400
        I_lo = 301
    elif 350.4 < concentration <= 500.4 :
        BP_hi = 500.4
        BP_lo = 350.5
        I_hi = 500
        I_lo = 401
    
    return (I_hi-I_lo)/(BP_hi-BP_lo)*(concentration - BP_lo) + I_lo
