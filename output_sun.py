import re
F=open('Collaborators','r')
lines = F.readlines()
F.close()
tot_value=0
for i in range(len(lines)):
    try:
        searched_words = re.search('has (.+) bla', lines[i])
        print(searched_words)
    except:
        print('Error in sentence')
        exit()
    svalue = searched_words.group(1)
    value = float(svalue)
    tot_value = tot_value+value
for i in range(len(lines)):
    searched_words = re.search('has (.+) fte', lines[i])
    svalue = searched_words.group(1)
    value = float(svalue)
    tot_value = tot_value+value
print(tot_value)
for i in range(len(lines)):
    searched_words = re.search('has .+ fte', lines[i])
    svalue = searched_words.group(1)
    value = float(svalue)
    tot_value = tot_value+value
for i in range(len(lines)):
    searched_words = re.search('has (.+) fte', lines[i])
    print(searched_words)
    svalue = searched_words.group(1)
    value = float(svalue)
    tot_value = tot_value+value
for i in range(len(lines)):
    searched_words = re.search('has (.+) fte', lines[i])
    print(searched_words)
    print(searched_words.match)
    svalue = searched_words.group(1)
    value = float(svalue)
    tot_value = tot_value+value
tot_value=0
for i in range(len(lines)):
    searched_words = re.search('has (.+) fte', lines[i])
    print(searched_words)
    svalue = searched_words.group(1)
    value = float(svalue)
    tot_value = tot_value+value
print(tot_value)
location1=[i for i in enumerate([2,3,4])]
location1
location1=[i for i,x in [2,3,4]]
location1=[i for i,x in enumerate(lines)]
location1
location1=[i for i,x in lines]
location1=[i for i,x in [2,3,4]]
location1=[i for i,x in enumerate([2,3,4])]
location1
location1=[i for i,x in enumerate([2,3,4]) if x=3]
location1=[i for i,x in enumerate([2,3,4]) if x==3]
location1
location1=[i for i,x in [2,3,4] if x==3]
location1=[i for i,x in enumerate([2,3,4]) if x==3]
enumerate([2,3,4])
for i in enumerate([2,3,4]):
    print i
for i in enumerate([2,3,4]):
    print(i)
for i,x in enumerate([2,3,4]):
    print(i)
    print(x)
for i in [2,3,4]:
    print(i)
for i,x in [2,3,4]:
    print(i)
    print(x)
import tkinter
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
F=open(filename,'r')
lines=F.readlines()
F.close()
Tlist=[]
location1=[i for i,x in enumerate(lines) if ('Temperature' in x) and ('Kelvin' in x) and ('Pressure' in x) and ('Atm' in x)]
for i in location1:
    foundstring=lines[i]
    value=float(foundstring.split()[1])
    Tlist.append(value)
Glist=[]
location2=[i for i,x in enumerate(lines) if ('Sum of electronic and thermal Free Energies' in x)]
for i in location2:
    foundstring=lines[i]
    value=float(foundstring.split()[7])
    Glist.append(value)
for i in [2,3,4]:
    print(i)
for i in len([2,3,4]):
    print(i)
for i in range(len([2,3,4])):
    print(i)
relativelist=[]
minvalue=min(x for x in Glist)
for i in range(len(Glist)):
    j=Glist[i]
    inkcalmol=(j-minvalue)*627.5095
    relativelist.append(inkcalmol)
 %history -f output_sun.py
