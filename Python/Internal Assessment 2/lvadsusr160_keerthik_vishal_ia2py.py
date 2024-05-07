# -*- coding: utf-8 -*-
"""LVADSUSR160_Keerthik_Vishal_IA2py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_VLByqS-03v79BwvXERFntVv_lH5KaA3
"""

#1.
import numpy as np
arr=np.array([1,2,3,4,5])
min_array = np.min(arr,0)
print("Minimum Array:")
print(min_array)
max_array= np.max(arr,0)
print("Maximum Array:")
print(max_array)
sum_array = sum(arr)
print("Sum:")
print(sum_array)
mean_array = np.mean(arr)
print("Mean:")
print(mean_array)
std_array = np.std(arr)
print("Standard Deviation")
print(std_array)

#2.
import numpy as np
health_data=np.array([[160,70,30],[165,65,35],[170,75,40]])
mean_hd = np.mean(health_data)
print(mean_hd)
std_hd = np.std(health_data)
print(std_hd)

#3.
import numpy as np

#4.
import numpy as np
temperature_readings = np.linspace(15,25,num=24)
print("The temperature readings collected:")
print(temperature_readings)

#5.
import numpy as np
daily_closing_prices = np.array([100,102,98,105,107,110,108,112,115,118,120])
window_size_5 = daily_closing_prices[0:4]
moving_average = np.average(window_size_5)
print("Moving average over a window of five days:")
print(moving_average)

#6.
import numpy as np
a = [0,0]
b = [[1,0.5],[0.5,2]]
arr= np.arange(100)
sample_arr= np.reshape(arr,newshape=(1,100),order='C')
print(sample_arr)

#7.
import numpy as np
properties_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

#8.
import pandas as pd

#9.
import pandas as pd
data={'Name':['Alice','Bob','Charlie','David','Eve','Frank','Grace'],'Age':[25,30,35,40,45,50,55]}

#10.
NA

#11.
NA

#12.
NA

#13
NA

#14
NA

#15
NA