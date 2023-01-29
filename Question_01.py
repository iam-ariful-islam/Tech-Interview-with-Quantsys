'''
Question 01
input: candy, not candy
ouput: not candy, not candy
'''

# define string or not string toggle function
def not_string(x):
    a = x.split()
    if a[0] == 'not': return x
    else: return 'not ' + x
    
# print not string
print(not_string('candy'))
# print string
print(not_string('not candy'))