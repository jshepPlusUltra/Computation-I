# File: oa2801_lab4.py
# Name: LT Jonathan Shepherd
# Email: jonathan.shepherd@nps.edu
#
# OA2801 - Lab 4 (Military Spending)

# import statements first
import sys
import csv
from tabulate import tabulate # Fancy printing 

# function definitions next
def process_data(list_of_lists,start_year,end_year): # New function
#This is for 4.b The total iron and steel was added to this part of the code. 
#I know this code works
#This is for 4.b The total iron and steel was added to this part of the code. 
#I know this code works
    if end_year < start_year:
        print('The start year is greater than end year.')
    else:
        output_list = []
        while start_year <= end_year:  
            expenditure_list = []
            iron_and_steel_list = []
            row = 1 # I had to skip the header row to get actual values
            CINC = 0.0 # I had to make this initialize with everything else so it kepy count

            while row < len(list_of_lists):
                #print(list_of_lists[row][2])
                year = int(list_of_lists[row][2])
                if year == start_year:    
                    #print('This part works and i can see all years %s' %list_of_lists[row][2] ) 

                    if list_of_lists[row][4] != '-9': #Do i want to check all countries later
                        expenditure_list.append(int(list_of_lists[row][4]))
                        iron_and_steel_list.append(int(list_of_lists[row][3]))

                    if float(list_of_lists[row][9]) >  CINC:
                        CINC = float(list_of_lists[row][9])
                        country = list_of_lists[row][0]



                row += 1
            output_list.append([start_year, sum(expenditure_list), sum(iron_and_steel_list), CINC, country])        
            start_year += 1
        title = ['Start Year','Expenditure List', 'Iron and Steel List', 'CINC',  'County']
        return     print(tabulate(output_list, headers = title, tablefmt = 'grid'))


# end of process_data()


#####################################################################
## Note: you should NOT have to modify anything below this point ! ##
#####################################################################

def read_file(infile):
 '''simple function to read in a csv file and return a list-of-lists.'''
    print("Reading file %s..." % infile, end='')
    f = open(infile, 'r', newline='')
    reader = csv.reader(f)
    list_of_lists = list(reader)
    print("done.")
    print("Input list-of-lists contains %d lines." % len(list_of_lists))

    return list_of_lists
# # end of read_file


def write_file(list_of_lists,outfile):
    '''simple function to write a list-of-lists to a csv file.'''

    print("Output list-of-lists has %d lines.  " % len(list_of_lists))
    print("Writing results to %s..." % outfile, end='')
    csvfile = open(outfile, 'w', newline='')
    writer = csv.writer(csvfile)  # pass additional parameters as appropriate
    for row in list_of_lists:
        writer.writerow(row)
    print("done.")
# end of write_file


#
# the main part of the script comes last
#
if __name__ == '__main__':

    # Here we assume that there are exactly three additional arguments...
    if len(sys.argv) != 4:
        sys.stderr.write("\tUsage: this script requires three command line arguments.\n")
        sys.stderr.write("\t arg1: name of csv input file (to be read) \n")
        sys.stderr.write("\t arg2: start year \n")
        sys.stderr.write("\t arg3: end year \n")
        sys.stderr.write("\tAborting.\n")
        sys.exit() # exit the program immediately


    infile = sys.argv[1]
    start_year = int(sys.argv[2])
    end_year = int(sys.argv[3])

    print("\nCommand line arguments read...")
    print("Infile: %s" % infile)
    print("Start Year: %d" % start_year)
    print("End Year: %d" % end_year)

    outfile = "result_" + str(start_year) + "_" + str(end_year) + ".csv"

    print("\nProgram output will be written to: %s\n" % outfile)

    list_of_lists = read_file(infile)

    output_list = process_data(list_of_lists, start_year, end_year)

    write_file(output_list,outfile)

    print("End of script.")
