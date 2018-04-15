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

The most basic GUI inside tkinter is just a gray box, commonly denoted `root`, and is defined using the `Tk` sublibrary:

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
>>> w=Label(root,text="This is a beta version. The program comes without guarantee that the results are correct.")
>>> w.pack()
>>> root.mainloop()

```

---

## Choose the file

With the `filedialog` module and the `askopenfilename`-function, the user can be asked to select a file.

```
>>> from tkinter.filedialog import askopenfilename
>>> filename = askopenfilename()

```

This file can then be used for further data-mining. 

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

## References

http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm

"Python for Data Analysis", Wes McKinney, O'Reilly Media, Sebastopol, CA: 2013

"Python for Informatics", Charles Severance, 2013, http://www.pythonlearn.com/book.php#python-for-informatics

http://www.pythonforbeginners.com

