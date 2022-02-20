import random
import time
import numpy as np

time.sleep(3)
time_intervals = 1
horizon = 0.2
meanT_over_Horizon = []
meanP_over_Horizon = []
meanH_over_Horizon = []
medianT_over_Horizon = []
medianP_over_Horizon = []
medianH_over_Horizon = []
ID = []
Iteration_val = 1


print("Serial communication is set and ready to go!")

try:
    while True:
        Temperature = []
        BarPressure = []
        Humidity = []
        for i in range(int(horizon*60/time_intervals)):
            time.sleep(time_intervals)
            instance_meas_list = random.sample(range(15, 20), 3)
            print(instance_meas_list)
            Temperature.append(instance_meas_list[0])
            BarPressure.append(instance_meas_list[1])
            Humidity.append(instance_meas_list[2])
        #print(np.array([Temperature,BarPressure,Humidity]))
        meanT_over_Horizon.append(np.mean(Temperature))
        meanP_over_Horizon.append(np.mean(BarPressure))
        meanH_over_Horizon.append(np.mean(Humidity))
        medianT_over_Horizon.append(np.median(Temperature))
        medianP_over_Horizon.append(np.median(BarPressure))
        medianH_over_Horizon.append(np.median(Humidity))
        ID.append(Iteration_val)
        print(ID)
        Iteration_val += 1
        print(np.transpose(np.array([ID,meanT_over_Horizon,meanP_over_Horizon,meanH_over_Horizon])))
        print(np.transpose(np.array([ID,medianT_over_Horizon,medianP_over_Horizon,medianH_over_Horizon])))

except KeyboardInterrupt:
    print("Close Serial Communication")
