from Data import DataClassification
import serial
import random
import time

time.sleep(3)
N_measurements = 10
time_intervals = 1
horizon = N_measurements*time_intervals/60

ser = serial.Serial('COM3',9600, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial communication is set and ready to go!")

#boolean tha decides if we store the data in dictionary form not recommended
#for the actual application
store_as_dict = False
data_class = DataClassification(N_measurements, time_intervals, store_as_dict )

try:
    while True:
        #for i in range(int(horizon*60/time_intervals)):
        time.sleep(time_intervals)

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            instance_meas_list = line.split(' ')
            instance_meas_list = [float(instance_meas_list[0]),float(instance_meas_list[1]),float(instance_meas_list[2])]
            print(instance_meas_list)

            data_class.temperature(instance_meas_list[0])
            #print(data_class.Data_temp)
            data_class.barpressure(instance_meas_list[1])
            #print(data_class.Data_bpress)
            data_class.humidity(instance_meas_list[2])
            #print(data_class.Data_hum)

except KeyboardInterrupt:
    print("Close Serial Communication")
