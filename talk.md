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

The operating system interfaces can be reached via the `os` module.

```python
import os
```

---

## Directories

The operating system interfaces can be reached via the `os` module.

```python
import os
```

The location of the current working directory can be found via

```python
workdir = os.getcwd()
print(workdir)
```
<pre>
/mnt/disk/python/Filehandling_2
</pre>

---

## Directories

The operating system interfaces can be reached via the `os` module.

```python
import os
```

The location of the current working directory can be found via

```python
workdir = os.getcwd()
print(workdir)
```
<pre>
/mnt/disk/python/Filehandling_2
</pre>

An extra directory (folder) can be created using `makedirs`.

```python
datadir = workdir + '/' + 'data'
os.makedirs(datadir)
```

---

## Directories

The operating system interfaces can be reached via the `os` module.

```python
import os
```

The location of the current working directory can be found via

```python
workdir = os.getcwd()
print(workdir)
```
<pre>
/mnt/disk/python/Filehandling_2
</pre>

An extra directory (folder) can be created using `makedirs`.

```python
datadir = workdir + '/' + 'data'
os.makedirs(datadir)
```

However, an error will appear if the directory already exists. We have to check
the existance of the directory:

```
if not os.path.exists(datadir):
    os.makedirs(datadir)
```

---

## Directories 

After creating the directory, we write to file `testfile.txt` therein:

```python
os.chdir(datadir)
f_test = open('testfile.txt', 'w')
print('Marie, Maria and Dorothy', file=f_test)
f_test.close()
```

---

## Directories 

After creating the directory, we write to file `testfile.txt` therein:

```python
os.chdir(datadir)
f_test = open('testfile.txt', 'w')
print('Marie, Maria and Dorothy', file=f_test)
f_test.close()
```

We can check now what is the content:

```
$ cat testfile.txt
Marie, Maria and Dorothy
```

---

## Directories 

After creating the directory, we write to file `testfile.txt` therein:

```python
os.chdir(datadir)
f_test = open('testfile.txt', 'w')
print('Marie, Maria and Dorothy', file=f_test)
f_test.close()
```

We can check now what is the content:

```
$ cat testfile.txt
Marie, Maria and Dorothy
```

[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie)

[Maria Goppert-Mayer](https://en.wikipedia.org/wiki/Maria_Goeppert_Mayer)

[Dorothy Hodgkin](https://en.wikipedia.org/wiki/Dorothy_Hodgkin)

---

## Searching information in a file

Imagine we have a file 'Collaborators' with content

```
$ cat Collaborators
Maria has 4 FTE collaborators.
Marie has 3.5 FTE collaborators.
Dorothy has 2.2 FTE collaborators.
```

Our task is to calculate the full amount of FTE collaborators for the three
Nobel Laureates.

---

## Searching information in a file

Imagine we have a file 'Collaborators' with content

```
$ cat Collaborators
Maria has 4 FTE collaborators.
Marie has 3.5 FTE collaborators.
Dorothy has 2.2 FTE collaborators.
```

Our task is to calculate the full amount of FTE collaborators for the three
Nobel Laureates.

Note that the three sentences have the same structures. We should find a way to
retrieve the information between 'has' and 'FTE'.  

First, we read in all lines.

```python
f_dat = open('Collaborators', 'r')
lines = f_dat.readlines()
f_dat.close()
``` 

---

## Searching information in a file

Regular expressions are available via the `re` module. They are very useful for
matching string patterns in a text.

```python
import re
```

---

## Searching information in a file

Regular expressions are available via the `re` module. They are very useful for
matching string patterns in a text.

```python
import re
```

With `re.search`, the following code searches three words, of
which the middle one is unknown.

+ `.` matches any character
+ `+` matches one or more occurrences of the pattern before it
+ `()` indicates the start and end of a group

```python
total_amount = 0.0

for line in lines:
    match = re.search(r'has (.+) FTE', line)
```

---

## Searching information in a file

Regular expressions are available via the `re` module. They are very useful for
matching string patterns in a text.

```python
import re
```

With `re.search`, the following code searches three words, of
which the middle one is unknown.

+ `.` matches any character
+ `+` matches one or more occurrences of the pattern before it
+ `()` indicates the start and end of a group

```python
total_amount = 0.0

for line in lines:
    match = re.search(r'has (.+) FTE', line)
```

The 'r' at the start of the pattern string designates a raw string that treats
backslashes as literal characters.

---

## Searching information in a file

If the string pattern was successfully found, `re.search` returns an object
that contains the three words. Otherwise `None` will be returned.

It is therefore possible to check the result of the search:

```python
    if match is None:
        print('String pattern not found in line: ' + line)
```

---

## Searching information in a file

If the string pattern was successfully found, `re.search` returns an object
that contains the three words. Otherwise `None` will be returned.

It is therefore possible to check the result of the search:

```python
    if match is None:
        print('String pattern not found in line: ' + line)
```

The matched group in `match` is accessible via `match.group(1)`. We need to
turn it into a floating point number and then add it to `total_amount`.

```python
    string_value = match.group(1)
    total_amount += float(string_value)
```

---

## Searching information in a file

Putting together, the code looks like

```python
import re

total_amount = 0.0

for line in lines:
    match = re.search(r'has (.+) FTE', line)

    if match is None:
        print('Information not found!')

    string_value = match.group(1)
    total_amount += float(string_value)

print(total_amount)
```

---

## Searching information in a file

Putting together, the code looks like

```python
import re

total_amount = 0.0

for line in lines:
    match = re.search(r'has (.+) FTE', line)

    if match is None:
        print('Information not found!')

    string_value = match.group(1)
    total_amount += float(string_value)

print(total_amount)
```

And the result is

<pre>
9.7
</pre>

---

## A live example

<center>
<img src="{{ base }}/img/Laurdan.png" style="width: 200px;"/>

<img src="{{ base }}/img/Laurdan_2.png" style="width: 200px;"/>
</center>

This molecule is Laurdan. It is a fluorescent probe - and can therefore be used
to investigate lipid bilayers.

By means of quantum chemical software, the evolution of the Gibbs free energy
can be calculated as a function of e.g. a raising temperature.

<center>
<img src="{{ base }}/img/Gaussian_2.png" style="width: 400px;"/>
</center>

---

## A live example

See file "Laurdan\_0\_va.log". We need to

+ extract the temperatures from the following lines

<img src="{{ base }}/img/film_output_log_temp_2.png" style="width: 450px;"/>

+ and extract the total free energies from the following lines

<img src="{{ base }}/img/film_output_log_2.png" style="width: 550px;"/>

---

## Live example: reading in file...

The following code reads the temperatures into a list

```python
import re

temperatures = []

f_log = open('Laurdan_0_va.log', 'r')

for line in f_log:
    match = re.search(r'Temperature(.+)Kelvin\.', line)
    if match is not None:
        temp = float(match.group(1).strip())
        temperatures.append(temp)

f_log.close()

print(temperatures)
```

---

## Live example: reading in file...

The following code reads both the temperatures and the free energies

```python
import re

temperatures = []
free_energies = []

f_log = open('Laurdan_0_va.log', 'r')

for line in f_log:

    match = re.search(r'Temperature(.+)Kelvin\.', line)
    if match is not None:
        temp = float(match.group(1).strip())
        temperatures.append(temp)

    match = re.search(r'Sum of electronic and thermal Free Energies=(.+)', line)
    if match is not None:
        free_e = float(match.group(1).strip())
        free_energies.append(free_e)

f_log.close()

print(temperatures)
print(free_energies)
```

---

## Live example: relative Gibbs free energies

In the log file, the default unit for energy is atomic unit, which is
equivalanet to 2625.5 kJ/mol.

It makes sense to convert the absolute free energies into relative free
energies (with respect to the minimal value in the list).

```python
minimal_free_e = min(free_energies)

relative_free_energies = []
for free_e in free_energies:
    relative_free_energies.append(2625.5 * (free_e - minimal_free_e))

print(relative_free_energies)
```

---

## Live example: relative Gibbs free energies

In the log file, the default unit for energy is atomic unit, which is
equivalanet to 2625.5 kJ/mol.

It makes sense to convert the absolute free energies into relative free
energies (with respect to the minimal value in the list).

```python
minimal_free_e = min(free_energies)

relative_free_energies = []
for free_e in free_energies:
    relative_free_energies.append(2625.5 * (free_e - minimal_free_e))

print(relative_free_energies)
```

It is convenient to plot the temperature - free energy curve in Jupyter
notebook

```python
%matplotlib inline

import matplotlib.pyplot as plt
plt.plot(temperatures, relative_free_energies, marker='o')
plt.xlabel('Temperature / [K]')
plt.ylabel('Relative free energy [kJ/mol]')
```

---

## Live example: writing to file

We can save the data in a file for future use

```python
import os

datadir = os.getcwd() + '/' + 'data'
if not os.path.exists(datadir):
    os.makedirs(datadir)

datafile = datadir + '/' + 'data_molecule'
f_dat = open(datafile, 'w')

for T, E, rel_E in zip(temperatures, free_energies, relative_free_energies):
    f_dat.write("{} {} {}\n".format(T, E, rel_E))

f_dat.close()
```

---

## Live example: writing to file

We can save the data in a file for future use

```python
import os

datadir = os.getcwd() + '/' + 'data'
if not os.path.exists(datadir):
    os.makedirs(datadir)

datafile = datadir + '/' + 'data_molecule'
f_dat = open(datafile, 'w')

for T, E, rel_E in zip(temperatures, free_energies, relative_free_energies):
    f_dat.write("{} {} {}\n".format(T, E, rel_E))

f_dat.close()
```

After writing, the content of the file is

```
$ cat data/data_molecule
1.0 -1065.149362 340.8056529997816
20.0 -1065.151038 336.40531500014595
40.0 -1065.1534 330.20388400028185
...
```

---

## Live example: numpy array

We can also play with the data using [numpy](http://www.numpy.org/) array.

```python
import numpy as np

mydata = [temperatures, free_energies, relative_free_energies]
myarray = np.array(mydata)
print(myarray.T)
```

---

## Live example: numpy array

We can also play with the data using [numpy](http://www.numpy.org/) array.

```python
import numpy as np

mydata = [temperatures, free_energies, relative_free_energies]
myarray = np.array(mydata)
print(myarray.T)
```

<pre>
[[ 1.00000000e+00 -1.06514936e+03  3.40805653e+02]
 [ 2.00000000e+01 -1.06515104e+03  3.36405315e+02]
 [ 4.00000000e+01 -1.06515340e+03  3.30203884e+02]
 ...
 [ 4.80000000e+02 -1.06527917e+03  0.00000000e+00]]
</pre>

---

## References

http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm

"Python for Data Analysis", Wes McKinney, O'Reilly Media, Sebastopol, CA: 2013

"Python for Informatics", Charles Severance, 2013, http://www.pythonlearn.com/book.php#python-for-informatics

http://www.pythonforbeginners.com
