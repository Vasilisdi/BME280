import serial
import time

ser = serial.Serial('/dev/tyyACM0',9600, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial communication is set and ready to go!")

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

try:
    while True:
        Temperature = []
        BarPressure = []
        Humidity = []
        time.sleep(0.01)
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            #print(line)
            instance_meas_list = line.split(' ')
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
    ser.close()
