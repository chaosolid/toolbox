# filter a list

lst1 = [1, 'Abc', 'abc', 4, '4cd-ef', 6, 7, '87', 'ADAS-A']

fil_lis = [(s.lower()) for s in lst1 if (type(s) is str) and (not '4' in s)]

print(fil_lis)

# ----------------------------------------------------------------------------------#

a,b = input('enter 2value:').split()
a= int(a)
b = int(b)
print(' what the hell {:d}..how about this..{:d}'.format(a,b))


a = 123
b = "3123"
c = 11
print('{:.5f}......{:d}    {}'.format(a,c,b))

def greeting(greet_message):
    name = input('what is your name? ')
    message = '{0}, {1} !'.format(greet_message, name)
    return print(message)

greeting('hello ')
# ----------------------------------------------------------------------------------#
import pandas as pd

df= pd.DataFrame({'a':['a', ' ', 'c', "e"],2:['d','b','f',2]})
print(df)
print('--------------')
print(df.head())

df= pd.DataFrame({'a':['a', ' ', 'c', "e"],2:['d','b','f',2]})
df

# ----------------------------------------------------------------------------------#