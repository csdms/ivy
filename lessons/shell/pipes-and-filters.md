![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Pipes and filters

The `cat` command dumps the contents of a file to the terminal:
```
$ cat haiku
Yesterday it worked
Today it is not working
Software is like that.
```
This is an easy way of looking at a file--simpler than opening it with
a text editor.

The **haiku** file is short.
For longer files, a *pager* is more appropriate to use.
Let's change to the **data-shell/data** directory
and view the contents of the file **planets.txt**
with the pager `more`:
```
$ cd data-shell/data/
$ ls
amino-acids.txt  animals.txt  morse.txt  planets.txt  sunspot.txt
animal-counts    elements     pdb        salmon.txt
$ more planets.txt
"Planet Name","Pl. Mass","Pl. Radius","Pl. Period",
"55 Cnc e","0.027","0.194","0.7365449",
"CoRoT-1 b","1.03","1.49","1.5089557",
"CoRoT-10 b","2.75","0.97","13.2406",
"CoRoT-11 b","2.33","1.43","2.99433",
"CoRoT-12 b","0.917","1.44","2.828042",
...
```
This text file is quite long,
so `more` pages the output.
You can hit `Enter` or `Spc` to advance through the file,
and `q` to quit back to the command prompt.

The `more` command also has a more advanced sibling, `less`:
```
$ less planets.txt
```

Related to pagers,
the `head` and `tail` commands
dump the first/last (respectively) 10 lines of text from a file.
```
$ head planets.txt
"Planet Name","Pl. Mass","Pl. Radius","Pl. Period",
"55 Cnc e","0.027","0.194","0.7365449",
"CoRoT-1 b","1.03","1.49","1.5089557",
"CoRoT-10 b","2.75","0.97","13.2406",
"CoRoT-11 b","2.33","1.43","2.99433",
"CoRoT-12 b","0.917","1.44","2.828042",
"CoRoT-13 b","1.308","0.885","4.03519",
"CoRoT-14 b","7.6","1.09","1.51214",
"CoRoT-16 b","0.535","1.17","5.35227",
"CoRoT-17 b","2.45","1.02","3.768125",

$ tail planets.txt
"WASP-68 b","0.8","0.9","5.1",
"WASP-69 b","0.3","1","3.9",
"WASP-7 b","0.96","1.33","4.9546416",
"WASP-70 b","0.6","0.8","3.7",
"WASP-8 b","2.244","1.038","8.158715",
"XO-1 b","0.9","1.184","3.9415128",
"XO-2 b","0.62","0.973","2.615838",
"XO-3 b","11.79","1.217","3.1915239",
"XO-4 b","1.72","1.34","4.1250823",
"XO-5 b","1.077","1.03","4.1877537",
```

The `wc` command counts the number of lines, words, and characters in a file.
For example, for our haiku:
```
$ wc haiku
 3 12 67 haiku
```
The file **haiku** has

* 3 lines,
* 12 words, and
* 67 characters.

The vertical bar `|` performs the *pipe* action:
it takes the output from one command
and feeds them as input to another command.
For example,
get the first five lines of the long directory listing
for the **data-shell/data/pdb** directory:
```
$ ls -l data-shell/data/pdb | head -5
total 208
-rw-r--r--. 1 mpiper csdms  1516 Aug  7  2019 aldrin.pdb
-rw-r--r--. 1 mpiper csdms   306 Aug  7  2019 ammonia.pdb
-rw-r--r--. 1 mpiper csdms  1444 Aug  7  2019 ascorbic-acid.pdb
-rw-r--r--. 1 mpiper csdms  1030 Aug  7  2019 benzaldehyde.pdb
```
Actually, how many files are in this directory?
```
$ ls -1 data-shell/data/pdb/ | wc -l
48
```
In this example,
the `1` option forces `ls` to print one file per line,
and the `l` option to `wc` returns only the number of lines.

The greater than symbol `>` performs the *redirect* action:
it takes the output from a command
and redirects it from the terminal to a file.
For example,
there are a set of data files in the **data-shell/molecules** directory:
```
$ ls data-shell/molecules/
cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
```
Let's find the lengths of these files and store them in a new file:
```
$ cd data-shell/molecules/
$ wc -l *.pdb > ~/Desktop/molecule_pdb_lengths
$ cd -
/home/mpiper/Desktop
$ cat molecule_pdb_lengths
  20 cubane.pdb
  12 ethane.pdb
   9 methane.pdb
  30 octane.pdb
  21 pentane.pdb
  15 propane.pdb
 107 total
```
Note that I used the asterisk `*` as a *wildcard* in this example.
The asterisk matches any set of characters;
here, it's used to match any file that ends with **.pdb**.

Related to the asterisk is the question mark `?`,
which is used to match a single character in a filename.
For example,
change to the **data-shell** directory and view its contents:
```
$ cd data-shell/
$ ls
creatures  molecules           notes.txt  solar.pdf
data       north-pacific-gyre  pizza.cfg  writing
```
Now find all files in this directory with five characters in their name
and any extension:
```
$ ls ?????.*
notes.txt  pizza.cfg  solar.pdf
```
Switch back to the previous directory:
```
$ cd -
/home/mpiper/Desktop
```

Finally,
the `sort` command can be used to sort the contents of a file.
Sort the contents of the **molecule_pdb_lengths** file
we created earlier:
```
$ sort -n molecule_pdb_lengths
   9 methane.pdb
  12 ethane.pdb
  15 propane.pdb
  20 cubane.pdb
  21 pentane.pdb
  30 octane.pdb
 107 total
 ```

As a bonus,
the `sed` command is a *stream editor*.
It can programmatically edit files
instead of interactively, like with a text editor.

Use `sed` to programmatically edit the **molecule_pdb_lengths** file,
replacing "pdb" with "txt":
```
$ sed -i.bak s@pdb@txt@g molecule_pdb_lengths
```
The editing is done in-place on the file.
The `i.bak` creates a backup file with the contents of the original file.
View the results:
```
$ cat molecule_pdb_lengths
  20 cubane.txt
  12 ethane.txt
   9 methane.txt
  30 octane.txt
  21 pentane.txt
  15 propane.txt
 107 total

$ cat molecule_pdb_lengths.bak
  20 cubane.pdb
  12 ethane.pdb
   9 methane.pdb
  30 octane.pdb
  21 pentane.pdb
  15 propane.pdb
 107 total
```

Rather than visually inspecting the differences between these files,
use the `diff` command:
```
$ diff molecule_pdb_lengths*
1,6c1,6
<   20 cubane.txt
<   12 ethane.txt
<    9 methane.txt
<   30 octane.txt
<   21 pentane.txt
<   15 propane.txt
---
>   20 cubane.pdb
>   12 ethane.pdb
>    9 methane.pdb
>   30 octane.pdb
>   21 pentane.pdb
>   15 propane.pdb
```


## Summary

The table below summarizes the commands and special characters
described in this section.

| Command/Character | Description
| ----------------- | -----------
| cat               | dump text to terminal
| more              | screen pager
| less              | better screen pager
| head              | print first lines of file
| tail              | print last lines of file
| wc                | count characters, words, lines
| |                 | pipe output of command
| >                 | redirect output of command
| *                 | match all characters
| ?                 | match single characters
| sort              | sorts input
| sed               | stream editor
| diff              | show differences between files

___

[Introduction to the shell](./index.md) |
Previous: [Creating things](./creating-things.md) |
Next: [Finding things](./finding-things.md)
