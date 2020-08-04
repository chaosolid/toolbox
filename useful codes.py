# Some useful codes to familiarize with

# filter a list

lst1 = [1, 'Abc', 'abc', 4, '4cd-ef', 6, 7, '87', 'ADAS-A']

fil_lis = [(s.lower()) for s in lst1 if (type(s) is str) and (not '4' in s)]

print(fil_lis)