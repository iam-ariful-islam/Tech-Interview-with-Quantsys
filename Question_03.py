'''Question 03

input:
    read given csv file
output:
    [('Galadriel', 1), ('Gandalf', 3), ('Saruman', 1), ('Bilbo', 3), ....]
'''

import csv
from collections import Counter

# if need then install collections package

li = []
with open('/home/unknown/Desktop/Quantsys_18.01.2023/LOTR.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        li.append(row[0])
        li.append(row[1])
        
# count the words
c = list(Counter(li).items())[2::]
print(c)