![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Files and directories

Information on a computer is stored in files and directories.
The part of an operating system that handles this information
is called the *filesystem*.
Think of the filesystem as a tree with branches (directories)
and leaves (files).

Let's find out where we are in the filesystem when we start a terminal.
```
$ pwd
/home/mpiper
```
The `pwd` command prints the current directory to the terminal.
You can see that I'm in the directory `mpiper` under the directory `home`.
The forward slash `/` is used as a delimiter between directory names.

This directory, `/home/mpiper`, is special--it's the *home directory*
for the user `mpiper`.
Every user has a home directory.
It's the default location for you to create and store information.

Note that I executed this command on a Linux machine;
the home directory on a macOS or Windows machine will be slightly different.


## Directory listings

Next, let's look at the contents of this directory.
```
$ ls
anaconda3  build  Desktop  local  packages  scratch  tmp
bin        data   dist     nb     projects  testing
```
The `ls` command provides a directory listing.
This home directory holds a set of subdirectories.

We can drill down through directories by providing arguments to `ls`.
For example, to see the contents of the **Desktop** directory, type:
```
$ ls Desktop
data-shell  data-shell.zip
```
You can see the sample files we downloaded earlier.
We can drill further; for example, to see into the directory containing
the sample files:
```
$ ls Desktop/data-shell
creatures  molecules           notes.txt  solar.pdf
data       north-pacific-gyre  pizza.cfg  writing
```


## Changing directories

Although we've peered into the directory of sample files,
we remain in the home directory.
To change directories,
use the `cd` command:
```
$ cd Desktop
$ pwd
/home/mpiper/Desktop
```
The `pwd` command shows that we've switched to the **Desktop** directory.

The `cd` command can take a directory name as an argument.
It can also take no arguments:
```
$ cd
$ pwd
/home/mpiper
```
With no arguments, `cd` always returns to your home directory.

The `cd` command can also take a set of special characters.
To switch to the previous directory,
use a dash `-`:
```
$ cd -
$ pwd
/home/mpiper/Desktop
```

When working with directories,
a dot `.` is a shortcut for the current directory,
while dot dot `..` is a shortcut for the parent directory:
```
$ cd .
$ pwd
/home/mpiper/Desktop
$ cd ..
$ pwd
/home/mpiper
```
Likewise,
the tilde `~` is a shortcut for the user's home directory:
```
$ cd ~
$ pwd
/home/mpiper
```

## Directory queues

Directories can be stacked in a queue.
This can be really helpful when you're frequently moving between
a set of directories.

The `pushd` command pushes a directory onto the stack:
```
$ pushd Desktop/
~/Desktop ~
```
There are now two directories on the stack:
the home directory `~`, where we started,
and `~/Desktop`.
A nice way to view the stack is with the `dirs` command;
in particular,
with the `v` option (for verbose):
```
$ dirs -v
 0  ~/Desktop
 1  ~
```
To switch to another directory on the stack,
use the `pushd` command again,
but this time with an argument,
the index in the stack.
For example, to switch to the home directory:
```
$ pushd +1
~ ~/Desktop
$ dirs -v
 0  ~
 1  ~/Desktop
```
The current directory is now the home directory.

To remove a directory from the stack,
use the `popd` command.
For example, pop the home directory off the stack with:
```
$ popd
~/Desktop
```
The current directory is now **Desktop**.


## Handy things

I'm not the best typist.
The shell saves me time, though, with *tab completion*.
Anytime you're in the process of entering a command in a terminal,
hit the `Tab` key,
and the shell will attempt to complete the command.
For example,
from the **Desktop** directory,
try listing the contents of **data-shell**
by typing the first few characters, then hitting the `Tab` key:
```
$ ls da
```
Tab completion is wonderful.

The `tree` command is nonstandard,
but it can be installed into a shell.
It acts like an ASCII-art Finder,
printing to the terminal the branch-leaf structure from a point
in the filesystem.
For example,
from the **Desktop** directory,
view the contents of the **data-shell/writing** directory 
with `tree`:
```
$ tree data-shell/writing
data-shell/writing/
|-- data
|   |-- LittleWomen.txt
|   |-- one.txt
|   `-- two.txt
|-- haiku.txt
|-- thesis
|   `-- empty-draft.md
`-- tools
    |-- format
    |-- old
    |   `-- oldtool
    `-- stats

4 directories, 8 files
```


## Summary

The table below summarizes the commands and special characters
described in this section.

| Command/Character | Description
| ----------------- | -----------
| pwd               | print working directory
| ls                | directory listing
| cd                | change directory
| /                 | path delimiter
| ~                 | home directory
| .                 | current directory
| ..                | one directory up
| -                 | previous directory
| pushd             | push directory on stack
| popd              | pop directory off stack
| dirs              | print directory stack
| tree              | view directory tree *(nonstandard)*
| tab               | complete command

___

[Introduction to the shell](./index.md) |
Previous: [index](./index.md) |
Next: [Creating things](./creating-things.md)
