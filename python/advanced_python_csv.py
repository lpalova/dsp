import csv

def read_data(myfile):
    dict_list = []
    with open(myfile, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def get_list(dict_list, name):
    my_list = []
    for d in dict_list:
        my_list.append(d[name])
    return my_list

def write_data(mylist, myfile):
    with open(myfile, 'wb') as csvfile:
#       writer = csv.writer(csvfile)
        for item in mylist:
            csvfile.write("%s\n" % item)
#        Example with writerow(s)
#        writer.writerow(["Name","Address","Telephone","Fax","E-mail","Others"])
#        writer.writerows(mylist) -- separates each char with , ?

# Q5. Write email addresses from Part I to csv file
dict_list = read_data( 'faculty.csv' )
email_list = get_list(dict_list, ' email')
write_data(email_list, 'emails.csv')
