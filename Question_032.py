'''Question 03

input:
    read given csv file
output:
    [('Galadriel', 1), ('Gandalf', 3), ('Saruman', 1), ('Bilbo', 3), ....]
'''
import csv

# method 1
data_list = []
with open('/home/unknown/Desktop/Quantsys_18.01.2023/LOTR.csv', 'r') as f:
    data = csv.reader(f)
    next(data, None) # skip the headers
    for row in data:
        data_list.append(row[0])
        data_list.append(row[1])
        
com_list = list(set(data_list))

results = []
for x in com_list:
    results.append((x, data_list.count(x)))
print(results)


# method 2
print()

L = []
with open('/home/unknown/Desktop/Quantsys_18.01.2023/LOTR.csv', 'r') as f:
    data = f.readlines()[1:] # skip the headers
    '''
    data = list(csv.reader(f))
    data = data[2::] # skip the headers
    '''
    for x in data:
        L.extend(x.strip().split(','))
        
result = []
for i in L:
    x = (i, L.count(i))
    if x not in result:
        result.append(x)
print(result)
    
    
# method 3
print()

li = []
with open('/home/unknown/Desktop/Quantsys_18.01.2023/LOTR.csv', 'r') as f:
    for line in f:
        li.extend(line.strip().split(','))
    li = li[2::]

results = [(i, li.count(i)) for i in set(li)]
print(results)