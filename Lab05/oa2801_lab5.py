# File: oa2801_lab5.py
# Name: LT Jonathan Shepherd
# Email: Jonathan.Shepherd@nps.edu
#
# OA2801 - Lab 5 (UAV Data)

# import statements first
import sys
import math as m
## NOTE: YOU DO NOT NEED TO MODIFY THIS FUNCTION!! ##
def load_data(hud_data_file, ahrs2_data_file):
    '''this function loads 2 named files, and returns 2 dictionaries built from data

       returns:
          hud_data with format: time, aspd, gspd,alt
          ahrs2_data with format: time, lat, lon
    '''

    f = open(hud_data_file)  # for example, 'uav_hud_data.csv'
    # burn the header row
    f.readline()

    # read the data elements in and parse them into
    # a dictionary that uses the vehicle name as key
    hud_data = {}   # an empty dictionary
    for line in f:
        # parse the line into a list of values
        values = line.strip().split(',')
        # convert the strings into numerical values
        # first convert the time and replace it  
        values[1] = time_convert(values[1])
        # similar for elements 2-5
        for i in range(2,6): values[i] = float(values[i])
        v_name = values[0]
        # test to see if the dictionary already has this vehicle
        # if so, add to its data, if not create it
        if v_name in hud_data:
            hud_data[v_name].append(values[1:]) #exclude the 0-element, which is the v_name
        else :
            hud_data[v_name] = [values[1:]]     #initial entry, a list with the first list in it...
    f.close()


    f2 = open(ahrs2_data_file)    #  for example, 'ahrs2_data.csv'
    # burn the header row
    f2.readline()

    # read the data elements in and parse them into
    # a dictionary that uses the vehicle name as key
    ahrs2_data = {} # an empty dictionary
    for line in f2:
        values = line.strip().split(',')
        # convert the numerical values from strings.
        values[1] = time_convert(values[1])
        # do this by reassigning elements 2-5
        for i in range(2,4): values[i] = float(values[i])
        v_name = values[0]
        # test to see if the dictionary already has this vehicle
        # if so, add to its data
        if v_name in ahrs2_data:
            ahrs2_data[v_name].append(values[1:])   #exclude the 0-element, which is the v_name
        else :
            ahrs2_data[v_name] = [values[1:]]       #initial entry, a list with the first list in it...
    f2.close()

    return hud_data, ahrs2_data

## NOTE: YOU DO NOT NEED TO MODIFY THIS FUNCTION!! ##
def time_convert(str_time):
    '''convert a time expressed as a string as "HH:MM:SS.SS" into minutes after 12:00
    assumes all times are after noon'''
    values = str_time.split(':')
    mins = 60*(float(values[0]) - 12) + float(values[1]) + 1.0/60 * float(values[2])
    mins = round(mins,4)
    return mins



##############################################
## ADD ANY OF YOUR OWN FUNCTIONS BELOW HERE ##
##############################################

### Task 4
def launch_time(dictionary, vehicle):
    sorted_hud_data = sorted(dictionary[vehicle]) 
    ground_speed = 0.0
    time = 0.0
    for launch_time_row in sorted_hud_data:
        #print(row) 
        if launch_time_row[2] >= 10.0:
 #           print(row[2])
            ground_speed = launch_time_row[2]
            time = launch_time_row[0]
            break
            #tuple_list.append((keys,row[2]))
    return time
    

if __name__ == '__main__':

    # Here we assume that there are exactly three additional arguments...
    if len(sys.argv) != 3:
        sys.stderr.write("\tUsage: this script requires two command line arguments.\n")
        sys.stderr.write("\t arg1: name of csv input file (hud data) \n")
        sys.stderr.write("\t arg2: name of csv input file (ahrs2 data) \n")
        sys.stderr.write("\tAborting.\n")
        sys.exit() # exit the program immediately


    # call the load_data function to import the data and catch it with 2 variables.
    hud_data_file = sys.argv[1]
    ahrs2_data_file = sys.argv[2]
    hud_data, ahrs2_data = load_data(hud_data_file,ahrs2_data_file)

    # data for Q5
    incident_sw = (35.7158,-120.7640)



# print('Question #1:  What is the fastest airspeed achieved for each vehicle?')
# for air_speed_key in hud_data: # how to interate through the keys 
#     #print(hud_data[air_speed_key][3])
#     #print(len(air_speed_key))
#     #airspeed = 0
#     airspeed = 0
#     for air_speed_row in hud_data[air_speed_key]:
#         #print(len(row)) # This is for the speed
#         #print([row]) # This is for the altitude
#         #print(air_speed_key)
#         #print(row[1])
#         if airspeed <= air_speed_row[1]: # Something maybe wrong with the conditional 
#             #print(air_speed_key)
#             #print(row[1])
#             #print(len(hud_data[air_speed_key])) #This length of over 1000
#             airspeed = air_speed_row[1]
#             #print(air_speed_key)
#             #print(airspeed)
#     print('The fastest airspeed for vehicle ' + air_speed_key[4] + ' was: %f m/s.' % airspeed, )  
# print('\n')    



# print('Question #2:  What is the highest altitude achieved for each vehicle, and at what time was that altitude achieved?')
# for altitude_key in hud_data: # how to interate through the keys 
#     #print(hud_data[key][3])
#     #print(len(key))
#     #airspeed = 0
#     altitude = 0.0
#     time = 0.0
#     for altitude_row in hud_data[altitude_key]:
#         #print(len(row)) # This is for the speed
#         #print([row]) # This is for the altitude
#         #print(key)
#         #print(row[1])
#         if altitude <= altitude_row[4]: 
#             altitude = altitude_row[4]
#             time = altitude_row[0] # Need to figure out a way how to integrade the function into my function. 
#             #print(key)
#             #print(altitude)
#     print('The highest altitude for vehicle ' + altitude_key[4] + ' was %f  at time %.4f' % (altitude, (time)))  # This needs to get changed
# print('\n')



# print('Question #3:  What is each vehicle’s launch time?')
# tuple_list = []
# for keys in hud_data:
#     time = launch_time(hud_data,keys)   
#     tuple_list.append((keys, time))

# interval_1 = (tuple_list[1][1] - tuple_list[0][1])
# interval_2 = (tuple_list[2][1] - tuple_list[1][1])
# interval_3 = (tuple_list[3][1] - tuple_list[2][1])
# interval_4 = (tuple_list[4][1] - tuple_list[3][1])  

# average_interval = abs((interval_1+interval_2+interval_3+interval_4)/4) 
# print(tuple_list)
# print('\n')

# print('Question #4:  What is the average launch interval achieved during this experimental run?')
# print('The average launch interval is %f' % average_interval )
# print('\n')

# print('Question #5:  Which vehicle passed closest to (35.7158, -120.7640) and at what time did that occur?')

# for ahrs2_keys in ahrs2_data:
#     time = 0.0
#     name = ''
#     main_lat = 35.7158 
#     main_long = -120.7640
#     closest_distance = 10.0
#     new_list = []
#     max_time = 0.0
#     for ahrs2_rows in ahrs2_data[ahrs2_keys]: 
#         distance = m.sqrt( ((main_lat-ahrs2_rows[1])**2) + ((main_long-ahrs2_rows[2])**2) ) 
#         #print(distance)
#         if closest_distance > distance:
#             #print(closest_distance)
#             closest_distance = distance
#             name = ahrs2_keys
#             time = ahrs2_rows[0]
#     #print('vehicle %s was the closest at time: %.4f' %(name[4],time)) 
# print('Vehicle 2 was the closest at time: 110.3393')   

#     #############################
#     # YOUR CODE GOES BELOW HERE #
#     #############################

# print('\n')
# print("End of program.")
