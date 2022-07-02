# File: oa2801_lab6.py
# Name: LT Jonathan Shepherd
# Email: jonathan.shepherd@nps.edu
#
# OA2801 - Lab 6 (Humanitarian Relief: Nearrest Airports)

# import statements first
import sys
import csv
import math as m
from operator import itemgetter, attrgetter

# Outside variables 
# infile_targets = "targets2019.csv"
# infile_eastern_Airports = "easternAirports.csv"
# infile_targets
# infile_eastern_Airports

# list_of_lists_targets = oa2801_lab6.read_file(infile_targets)[2:] # This is to make sure that i get the numbers and not the comments
# list_of_lists_eastern_Airports = oa2801_lab6.read_file(infile_eastern_Airports)[20:] # This is to make sure i get the numbers and not the comments

#Functions


print("The script runs at a complexity of 2n + n^3 + Log(n)")
print('')
print('')
print('')  
def dms_to_decimal(a,b,c):
    ans = a + (b/60) + (c/3600)   
    return ans

def rad2nm(distance_radians): # Convert distance in rads to nautical miles 
    distance_nm = ( distance_radians*( (180 * 60)/m.pi) ) 
    #print( str(float(distance_nm)) + ' nm ' ) # How do i get the answer to round to a certain value
    return distance_nm
    
# Your code for Task 4 goes here (you may need to add additional code blocks by using "Insert" on the toolbar)
def calc_distance(lat1, lon1, lat2, lon2): 
    d = rad2nm( m.acos(m.sin(deg2rad(lat1)) * m.sin(deg2rad(lat2))  + m.cos(deg2rad(lat1)) * m.cos(deg2rad(lat2)) * m.cos(deg2rad(lon1)-deg2rad(lon2))) )     #d = 2 * m.asin(m.sqrt((m.sin((lat1-lat2)/2))**2 +  m.cos(lat1) * m.cos(lat2)*(m.sin((lon1-lon2)/2))**2)) #Short Distances
    return d 

def deg2rad(angle_degrees):
    angle_radians = (m.pi/180) * angle_degrees 
    return   angle_radians 


def read_file(infile):
    '''simple function to read in a csv file and return a list-of-lists.'''

    print("Reading file %s..." % infile, end='')
    f = open(infile, 'r', newline='')
    reader = csv.reader(f)
    list_of_lists = list(reader)
    print("done.")
    print("Input list-of-lists contains %d lines." % len(list_of_lists))

    return list_of_lists
# end of read_file

def highest_airports(airport_file, N): #is any= interget
    for elements in range(len(airport_file)): # Big_O ==> N
        #print((((elements))))
        airport_file[elements][13] = int(airport_file[elements][13])
    new_list = sorted(airport_file   , key = itemgetter(-1), reverse = True) 
    #print(new_list[:N])
    
    print('The %d highest airports are:' %N)
    i = 0
    while i < N: #Big_O ==> N # This loop is more for cosmetic reasons. I need this loop to clean up the print statement. There has to be a more efficient way to do this.
        print(new_list[0:N][i]) # This out this print in the loop the format would liik bad. 
        i+=1
    print('')
    print('')    
    return None



def Parse_Disaster_2(list_of_lists_eastern_Airports,list_of_lists_targets, N):
    target_list = []
    eastern_airport_list = []
    for elements_2 in range(len(list_of_lists_eastern_Airports)): # Big_O of n
        #This is to change all of the lat and longs into ints so i can use the numbers for calculations 
        # I have to think of a more efficient way to change a list of strings into ints

        #The next 6 lines of code changes the lat/long from str to in for the airport list data
        list_of_lists_eastern_Airports[elements_2][5] = int(list_of_lists_eastern_Airports[elements_2][5]) #I need to change all of my numbers into ints
        list_of_lists_eastern_Airports[elements_2][6] = int(list_of_lists_eastern_Airports[elements_2][6])
        list_of_lists_eastern_Airports[elements_2][7] = int(list_of_lists_eastern_Airports[elements_2][7])
        list_of_lists_eastern_Airports[elements_2][9] = int(list_of_lists_eastern_Airports[elements_2][9])
        list_of_lists_eastern_Airports[elements_2][10] = int(list_of_lists_eastern_Airports[elements_2][10])
        list_of_lists_eastern_Airports[elements_2][11] = int(list_of_lists_eastern_Airports[elements_2][11])
        #eastern_airport_list.append(list_of_lists_eastern_Airports)
        a = list_of_lists_eastern_Airports[elements_2][5] #I need these variables for my lat/long conversions below
        b = list_of_lists_eastern_Airports[elements_2][6] #I need these variables for my lat/long conversions below
        c = list_of_lists_eastern_Airports[elements_2][7] #I need these variables for my lat/long conversions below
        d = list_of_lists_eastern_Airports[elements_2][9] #I need these variables for my lat/long conversions below
        e = list_of_lists_eastern_Airports[elements_2][10] #I need these variables for my lat/long conversions below
        f = list_of_lists_eastern_Airports[elements_2][11] #I need these variables for my lat/long conversions below
        lat_dec_eastern_Airports = a + (b/60) + (c/3600) #I need these variables for my lat/long conversions below
        long_dec_eastern_Airports = d + (e/60) + (f/3600) #I need these variables for my lat/long conversions below 
    #     print(lat_dec_eastern_Airports)
    #     print(long_dec_eastern_Airports)
        eastern_airport_list.append([list_of_lists_eastern_Airports[elements_2][0],list_of_lists_eastern_Airports[elements_2][1],list_of_lists_eastern_Airports[elements_2][2],list_of_lists_eastern_Airports[elements_2][3],list_of_lists_eastern_Airports[elements_2][4],lat_dec_eastern_Airports, long_dec_eastern_Airports, list_of_lists_eastern_Airports[elements_2][13]]) 

        
    for elements_3 in range(len(list_of_lists_targets)): # Big_O of n      
        #The next 2 lines of code changes the lat/long from str to in for the target list data
        #print(list_of_lists_targets[elements_3][0]) # This is the lat in dec form in int
        #print(list_of_lists_targets[elements_3][1]) # This is the lon in dec form in int
        list_of_lists_targets[elements_3][0] = float(list_of_lists_targets[elements_3][0])
        list_of_lists_targets[elements_3][1] = float(list_of_lists_targets[elements_3][1])
        target_list.append([list_of_lists_targets[elements_3][0],list_of_lists_targets[elements_3][1]]) # all of my values are now ints and appended to an empty list and ready to compare 
    #print(eastern_airport_list[5][5])   
    i = 0
    k = 1
    while i < len(target_list): # The Bog O for this is N squared due to the nested loop. I needed this function to loop through all of my targets per airport.
        target_lat = list_of_lists_targets[i][0]
        target_lon = list_of_lists_targets[i][1]
        temp_list = []
        j = 0
        print('These are the closest airports %d to the target number %d with a latitude: %.3f and longitude: %.3f' % (N,k,target_lat,target_lon))
        while j < len(eastern_airport_list):   
            if list_of_lists_eastern_Airports[j][8] == 'S': # This takes into account the South by placing a negative in front of the lat
                #print(list_of_lists_eastern_Airports[j][8])
                eastern_airport_lat = (-1)*eastern_airport_list[j][5]
            else:
                eastern_airport_lat = eastern_airport_list[j][5]

            if list_of_lists_eastern_Airports[j][8] == 'W':# This takes into account the West by placing a negative in front of the lat
                eastern_airport_lon = (-1)* eastern_airport_list[j][6] 
            else:     
                eastern_airport_lon = eastern_airport_list[j][6] 
            #print(eastern_airport_lon)  


            distance = calc_distance(target_lat, target_lon, eastern_airport_lat, eastern_airport_lon)

            temp_list.append(([distance, eastern_airport_list[j]]))
            #print(eastern_airport_list[j])
            j += 1
          
        sorted_temp_list = sorted(temp_list, key = itemgetter(0), reverse=False) #This is N squared due to the neste # I am using this loop to run through my sorted data. 
        master_list = sorted_temp_list[0:N]
        for index in range(len(master_list)):
            ap = master_list[index]
        
            print("%s %s %s %s %s %.4f %.4f %d %.4f" % (ap[1][0], ap[1][1], ap[1][2],ap[1][3],ap[1][4], ap[1][5],ap[1][6],ap[1][7], ap[0])  )
           
        i+=1  
        k += 1
        print('')
        print('')
   
    return 





#
# the main part of the script comes last
#
if __name__ == '__main__':

    # Here we assume that there are exactly three additional arguments...
    if len(sys.argv) != 4:
        sys.stderr.write("\tUsage: this script requires three command line arguments.\n")
        sys.stderr.write("\t arg1: name of csv input file (to be read) \n")
        sys.stderr.write("\t arg2: name of csv input file (to be read)\n")
        sys.stderr.write("\t arg3: desired number of airports to report (int) \n")
        sys.stderr.write("\tAborting.\n")
        sys.exit() # exit the program immediately


    infile_eastern_Airports= sys.argv[1]
    infile_targets = sys.argv[2]
    N = int(sys.argv[3])
    list_of_lists_targets = read_file(infile_targets)[2:] # This is to make sure that i get the numbers and not the comments
    list_of_lists_eastern_Airports = read_file(infile_eastern_Airports)[20:] # This is to make sure i get the numbers and not the comments    

    highest_airports(list_of_lists_eastern_Airports, N)
    Parse_Disaster_2(list_of_lists_eastern_Airports,list_of_lists_targets, N)


    print("End of script.")










