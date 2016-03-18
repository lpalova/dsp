import csv
import re
import collections

def read_data(myfile):
    dict_list = []
    with open(myfile, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def dict1( dict_list ):
    my_dict = collections.defaultdict(list)
    for d in dict_list:
        last_name = d['name'].strip().split()[-1]
        my_list = [ d[' degree'], " ".join(d[' title'].strip().split()[:-2]),\
                     d[' email'] ]                
        my_dict[last_name].append(my_list)
    return my_dict

def dict2( dict_list ):
    my_dict = {}
    for d in dict_list:
        last = d['name'].strip().split()[-1]
        fm = d['name'].strip().split()[:2]
        if len(fm[0])==2 and fm[0].endswith("."):
            first = fm[1]
        else:
            first = fm[0]
        name_tuple = ( first, last )
        my_list = [ d[' degree'], " ".join(d[' title'].strip().split()[:-2]),\
                     d[' email'] ]   
    #Assuming that the name_tuple keys are unique, or overwriting with a new
    #value             
        my_dict[name_tuple] = my_list
    return my_dict

def sort_dict( my_dict ):
    return collections.OrderedDict(sorted(my_dict.items()))


#Q6. Create a dictionary in the below format:
"""faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }"""
#Print the first 3 key and value pairs of the dictionary:
dict_list = read_data( 'faculty.csv' )
faculty_dict = sort_dict( dict1( dict_list ) )
first3fac = {key: faculty_dict[key] for key in faculty_dict.keys()[:3]}
print first3fac

#Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:
"""professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }"""
#Print the first 3 key and value pairs of the dictionary:
professor_dict = dict2( dict_list ) 
professor_dict_sort = sort_dict( professor_dict )
first3prof = {key: professor_dict_sort[key] for key in professor_dict_sort.keys()[:3]}
print first3prof

#Q8. It looks like the current dictionary is printing by first name. Sort by last name and print the first 3 key and value pairs.
name_tuples = sorted( professor_dict.keys(), key=lambda tup: (tup[1],tup[0]))
count = 0
print "{"
for name in name_tuples:
    print name, ":", professor_dict[name], ",\\"
    count += 1
    if count == 3:
        break
print "}"
