<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
# File handling 2

## 

BB1000 Programming in Python
KTH

---

layout: false

## GUI 'Please think while you run'

Imagine you write a program - and via a pop-up window, you would like to give a message to the user: 'This is a beta version'

We make use of the library `tkinter` and its sublibaries. In the next chapter, we will learn that we load libraries via

```
>>> import tkinter
>>> from tkinter import *

```

The most basic GUI inside tkinter is just a gray box, commonly denoted `root`.

<center>
<img src="{{ base }}/img/root-box_2.png" style="width: 125px;"/>
</center>

---

## GUI 'Please think while you run'

`root` is defined using the `Tk` sublibrary:

```
>>> root= tkinter.Tk()
>>> root

```

Like it is now, the box is open until the end of the program. Since our program only has four lines, the box will close itself immediately and it appears to the human eye that nothing happened. With the option `mainloop`, the box stays visible until we click it to close...

```
>>> root.mainloop()

```

---

## GUI 'Please think while you run'

Using `Label()`, we are able to give the box a message; with `pack()` the size of the box is adapted to the text...

```
>>> root= tkinter.Tk()
>>> w=Label(root,text="This is a beta version. The program comes without guarantee that the results are correct.")
>>> w.pack()
>>> root.mainloop()

```

Remark that `root= tkinter.Tk()` was needed since we killed the `root` on the previous page (we pressed the cross to close it).

<center>
<img src="{{ base }}/img/box_with_text_2.png" style="width: 500px;"/>
</center>


---

## Choose the file

With the `filedialog` module and the `askopenfilename`-function, the user can be asked to select a file.

```
>>> from tkinter.filedialog import askopenfilename
>>> filename = askopenfilename()

```

This file can then be used for further data-mining. 

<center>
<img src="{{ base }}/img/Dialog_choose_file_2.png" style="width: 250px;"/>
</center>

---

## Directories

Via `os` the operating system interfaces can be reached.

```
>>> import os

```

The folder location can be found via

```
>>> cwd = os.getcwd()
>>> print(cwd)
/mnt/disk/python/Filehandling_2

```

An extra folder can be created using `makedirs`.

```
>>> newdir=cwd+'/'+'data'
>>> os.makedirs(newdir)

```

However, an error will appear when the folder already exists.

<!--
>>> os.makedirs(newdir)

FileExistsError                           Traceback (most recent call last)
<ipython-input-10-0698eb90a7e6> in <module>()
      1 os.makedirs(newdir)
	        Cannot rely on checking for EEXIST, since the operating system

FileExistsError: [Errno 17] File exists: '/mnt/disk/AA_PC_Stockholm/Education/Python_programming/2018/lectures/Filehandling_2/data'

-->

We have to check therefore upon its existance:

```
>>> if not os.path.exists(newdir):
...    os.makedirs(newdir)

```

---

## Directories 

After creating the directory, we should make sure we put the data there:

```
>>> os.chdir(newdir)
>>> try1=open("testfile.txt","w")
>>> print('Pierre, Einstein and Planck', file=try1)
>>> try1.close()

```

We can check now what is the content:

```
$ cat testfile.txt
Pierre, Einstein and Planck

```

A word of precaution here: imagine you run the program a second time. The folder 'data' exists already, we do not create a new one and the program continues... and will overwrite the content of 'testfile.txt'. 

```
>>> os.chdir(newdir)
>>> try1=open("testfile.txt","w")
>>> print('Marie, Maria and Dorothy', file=try1)
>>> try1.close()

$ cat testfile.txt
Marie, Maria and Dorothy

```

<!--
Marie Curie, Maria Goppert-Mayer ('nuclear shell structure', TPA), Dorothy Hodgkin (X-ray of biological structures)
-->

---

## Searching information in a file

Imagine we have a file 'Collaborators' with content

```
$ cat Collaborators
Maria has 4 fte collaborators.
Marie has 3.5 fte collaborators.
Dorothy has 2.2 fte collaborators.

```

Please calculate the full amount of fte collaborators for the three Noble prize winners.

It can be noticed that the structure of the three sentences is the same, we should find a way to only take care of the information in between 'has' and 'fte'.  

First, we have to read in all lines.

```
>>> F=open('Collaborators','r')
>>> lines = F.readlines()
>>> F.close()

``` 

---

## Searching information in a file

With the library `re`, regular expressions can be searched - it can be verified whether they match string patterns in a text. And we initialize the final value...

```
>>> import re
>>> tot_value=0

```

We will now search through the content of each of the lines in `lines`. We know `lines` is a list and need therefore to run through the index of it.

`re.search` can scan each line: we search in fact each time three words, of which the middle one is unknown and is replaced by parentheses `()`. It can be any character (`.`) and one or more occurrences of that pattern should be taken into account (`+`).  

```
>>> for i in range(len(lines)):
...     searched_words= re.search('has (.+) fte', lines[i])

```

<!--
The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change.
-->

---

## Searching information in a file

`searched_words` is an object which contains the three words. If there is a problem with the matching words [e.g. 'has (.+) guf'], then `searched_words` is just `None`. 

<!--
print(searched_words)

<_sre.SRE_Match object; span=(6, 15), match='has 4 fte'>
<_sre.SRE_Match object; span=(6, 17), match='has 3.5 fte'>
<_sre.SRE_Match object; span=(8, 19), match='has 2.2 fte'>
-->

It is therefore possible to build in a check:

```
...     if searched_words is None:
...         print('Error in sentence')
...         exit()
	 
```

---

## Searching information in a file

The first word in `searched_words` can be accessed by using `searched_words.group(0)`. We are however interested in the second word, and have to render it to a number.

```
...     svalue = searched_words.group(1)
...     value = float(svalue)

```

We only have to add for each line in `lines` the value to the sum of the previous ones:

```
...     tot_value = tot_value + value

```

And finally the result is

```
>>> print(tot_value)
9.7

```

<!--
>>> for i in range(len(lines)):
...    searched_words = re.search('has (.+) fte', lines[i])
...    if searched_words is None:
...       print('Error in sentence')
...       exit()
...    svalue = searched_words.group(1)
...    value = float(svalue)
...    tot_value = tot_value+value
>>> print(tot_value)
-->

---

## A live example

<center>
<img src="{{ base }}/img/Laurdan.png" style="width: 125px;"/>

<img src="{{ base }}/img/Laurdan_2.png" style="width: 125px;"/>
</center>

This molecule is Laurdan. It is a fluorescent probe - and can therefore be used to investigate lipid bilayers.

By means of quantum chemical software, the evolution of the Gibbs free energy can be calculated in function of e.g. a raising temperature.

<center>
<img src="{{ base }}/img/Gaussian_2.png" style="width: 350px;"/>
</center>

---

## A live example

See file "Laurdan_0_va.log". Browse through the file, search the word 'Temperature' and see that the file contains information about Gibbs free energies ('Sum of electronic and thermal Free Energies') for T=1, 20, 40,..., 500 K. 

Remark that the file is like a film: the sentences are the same, the values change...

<center>
<img src="{{ base }}/img/film_output_log_2.png" style="width: 450px;"/>

<img src="{{ base }}/img/film_output_log_temp_2.png" style="width: 450px;"/>
</center>

We need to make a file, which contains for each temperature the absolute Gibbs free energy in Hartree as well as the relative Gibbs free energy (= the difference with the lowest Gibbs free energy in the table) in kcal/mol. 

---

## Live example: reading in file...

```
>>> import tkinter
>>> from tkinter.filedialog import askopenfilename
>>> filename = askopenfilename()

>>> F=open(filename,'r')
>>> lines = F.readlines()
>>> F.close()

```

Let us make three lists: one for the temperatures, one for the Gibbs free energies and one for the relative Gibbs free energies. Remark that the first (second, third,...) temperature is connected to the first (second, third,...) Gfe and the first relative Gfe.

---

## Live example: making list of the temperatures

We know that `lines` is a list. Let us therefore first be aware of the tools:

```
>>> for i in [2,3,4]:
...     print(i)
2
3
4

```

```
>>> for i in enumerate([2,3,4]):
...     print(i)
(0, 2)
(1, 3)
(2, 4)

```

```
>>> for i,x in enumerate([2,3,4]):
...     print(i)
...     print(x)
0
2
1
3
2
4

```
---

## Live example: making list of the temperatures

```
>>> Tlist=[]

```

We will try to find the numbers of the lines which have the words 'Temperature', 'Kelvin' and 'Pressure', and navigate then back to them to read in the information...

```
>>> location1=[i for i,x in enumerate(lines) if ('Temperature' in x) and \
('Kelvin' in x) and ('Pressure' in x) and ('Atm' in x)]

```

```
>>> for i in location1:
...     foundstring=lines[i]
...     value=float(foundstring.split()[1])
...     Tlist.append(value)

```

Remark that we take the second entry in the string `foundstring`. This could also be obtained by using

```
>>> for i in location1:
...     foundstring=lines[i]
...     searched_words = re.search('Temperature (.+?) Kelvin', foundstring)
...     svalue = searchvalue.group(1)
...     value=float(svalue)
...     Tlist.append(value)

```

---

## Live example: making list of the Gibbs free energies

```
>>> Glist=[]
>>> location2=[i for i,x in enumerate(lines) if ('Sum of electronic and thermal \
Free Energies' in x)]
>>> for i in location2:
...     foundstring=lines[i]
...     value=float(foundstring.split()[7])
...     Glist.append(value)
	
```

---

## Live example: making list of the relative Gibbs free energies

The idea is now that we go through the whole list of Glist... Therefore first a bit of insight:

```
>>> for i in [2,3,4]:
...     print(i)
2
3
4

```

```
>>> for i in len([2,3,4]):
...     print(i)
TypeError: 'int' object is not iterable

```

```
>>> for i in range(len([2,3,4])):
...     print(i)
0
1
2

```

---

## Live example: making list of the relative Gibbs free energies

We would like to make now a list of the Gibbs free energies with respect to the minimal value in the list. We convert the result to kcal/mol. 

```
>>> relativelist=[]
>>> minvalue=min(x for x in Glist)

```

```
>>> for i in range(len(Glist)):
...     j=Glist[i]
...	inkcalmol=(j-minvalue)*627.5095
...	relativelist.append(inkcalmol)

```
---

## Live example: Putting the matrix in the right shape

All data together gives us

```
>>> alldata=[Tlist,Glist,relativelist]

```

The output of the matrix is however not what we want:

```
>>> alldata
[[1.0, 20.0, 40.0,...],[-1065.149362, -1065.151038, -1065.1534,...],
[81.4544981569478, 80.40279223503488,...]]

```

We would prefer a file with the temperatures in the first column, the Hartree-energies in the second and the relative energies in the third one. Therefore, first an exercise:

```
>>> numbers= [1,2,3]
>>> letters= ['a', 'b', 'c']
>>> ziplist=[numbers,letters]
>>> print(ziplist)
[[1, 2, 3], ['a', 'b', 'c']]
>>> print(*ziplist)
[1, 2, 3] ['a', 'b', 'c']
>>> list(zip(*ziplist))
[(1, 'a'), (2, 'b'), (3, 'c')]

```

---

## Live example: Putting the matrix in the right shape

The only thing we need now is to get rid of the tuples, so that we can access the content... The `map` function might be interesting:

```
>>> def qua(x):
...     return x**2
>>> list(map(qua,[4,5,6]))
... [16, 25, 36]

```

However, the content of `map` cannot be written out as such - therefore we have to make a list of it before printing.

<!--
It does not have to be a list, it can also be e.g. a tuple:

tuple(map(qua,[4,5,6]))
(16, 25, 36)
-->

```
>>> list_tup=[(4,5),(6,7)]
>>> list(map(list,list_tup))
[[4, 5], [6, 7]]

```

<!--
>>> tup2=((4,5),(6,7))
>>> list(map(list,tup2))
[[4, 5], [6, 7]]
-->

<!--
Remark that it is logical that the next thing does not work:

>>> list(map(list,(4,5,6,7)))
'int' object is not iterable (number '4' cannot be list)

-->

When we apply all these techniques upon 'alldata', we get

```
>>> ziptransposed=list(map(list,zip(*alldata)))
>>> ziptransposed
[[1.0, -1065.149362, 81.4544981569478],
 [20.0, -1065.151038, 80.40279223503488],
 [40.0, -1065.1534, 78.92061479606737],
 [60.0, -1065.156211, 77.15668559152647],
 ...  

```

---

## Live example: Writing out

We know already

```
>>> import os
>>> cwd=os.getcwd()
>>> newdir=cwd+'/'+'data'
>>> if not os.path.exists(newdir):
...    os.makedirs(newdir)
>>> os.chdir(newdir)

```

```
>>> outfile="data_molecule"
>>> Wf=open(outfile,'w')

```

---

## Live example: Writing out

It is a possibility to print out a string, which is built up by all the elements of the matrix 'ziptransposed'. 

By means of an example, consider

```
>>> matrix_ex=[[1,2,3],[4,5,6]]

```

```
>>> for x in matrix_ex:
...     print(x)
[1, 2, 3]
[4, 5, 6]

```

```
>>> for x in matrix_ex:
...     print(' '.join(str(x) for x in matrix_ex))
[1, 2, 3] [4, 5, 6]
[1, 2, 3] [4, 5, 6]

```

```
>>> for x in matrix_ex:
...     print(' '.join(str(x[i]) for i in range(len(x))))
1 2 3
4 5 6

```

---

## Live example: Writing out

We can now apply the previous to the matrix 'ziptransposed'. However, we should be aware that `print` automatically adds a line break in the end. The function `write` does not do that, therefore we have to add a `write('\n')` extra:

```
>>> for x in ziptransposed:
...   Wf.write(' '.join(str(x[i]) for i in range(len(x))))
...   Wf.write('\n')

```

<!--
To round the numbers:

>>> for x in ziptransposed:
...   Wf.write(' '.join(str(round(x[i],3)) for i in range(len(x))))
...   Wf.write('\n')
-->

```
>>> Wf.close()

```

```
$ cd data
$ cat data_molecule
1.0 -1065.149362 81.4544981569478
20.0 -1065.151038 80.40279223503488
40.0 -1065.1534 78.92061479606737
...

```

---

## References

http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm

"Python for Data Analysis", Wes McKinney, O'Reilly Media, Sebastopol, CA: 2013

"Python for Informatics", Charles Severance, 2013, http://www.pythonlearn.com/book.php#python-for-informatics

http://www.pythonforbeginners.com

