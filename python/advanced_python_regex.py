import csv
import re

def read_data(data):
    dict_list = []
    with open(data, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(row)
    return dict_list

def freq(dict_list, name, num = 0):
    my_dict = {}
    for d in dict_list:
        if num == 0:
            name_list = d[name].strip().split()
        else:
            name_list = [" ".join(d[name].strip().split()[:num])]
        for item in name_list:
            item = re.sub("\.","",item)
            if item in my_dict:
                my_dict[item] += 1
            else:
                my_dict[item] = 1
    return my_dict

def get_list(dict_list, name):
    my_list = []
    for d in dict_list:
        my_list.append(d[name])
    return my_list

def get_domain_set(l, c):
    my_set = set()
    for item in l:
        domain = item.strip().split(c)[-1]
        if domain not in my_set:
            my_set.add(domain)
    return my_set


dict_list = read_data( 'faculty.csv' )

# Q1: Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
degree_dict = freq(dict_list, ' degree')
print degree_dict
# {'MD': 1, 'MA': 1, 'ScD': 6, 'BSEd': 1, 'PhD': 31, '0': 1, 'MPH': 2, 'MS': 2, 'JD': 1}

#Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
title_dict = freq(dict_list, ' title', num = -2)
print title_dict
# {'Assistant Professor': 12, 'Professor': 13, 'Associate Professor': 12}

#Q3. Search for email addresses and put them in a list. Print the list of email addresses.
email_list = get_list(dict_list, ' email')
print email_list
# ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']

#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.
domain_set = get_domain_set(email_list, '@')
print list(domain_set)
# ['email.chop.edu', 'upenn.edu', 'cceb.med.upenn.edu', 'mail.med.upenn.edu']
