#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

def read_data(data):
    list = []
    with open(data, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list.append(row)
    return list

def get_min_score_difference(list):
#(self, parsed_data):
    imin = 0
    min = abs( int(list[0]['Goals']) - int(list[0]['Goals Allowed']) )
    for i in range(1, len(list)):
        diff = abs( int(list[i]['Goals']) - int(list[i]['Goals Allowed']) )
        if diff < min:
            imin = i
            min = diff
    return imin

def get_team (list, imin):
#(self, index_value, parsed_data):
    return list[imin]['Team']  

list = read_data( 'football.csv' )
imin = get_min_score_difference( list )
team = get_team( list, imin )
print team
