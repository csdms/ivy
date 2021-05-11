![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Creating things

The filesystem is comprised of directories and files.
Here, we'll see how to make them.

To start, change to the **Desktop** directory:
```
$ cd ~/Desktop
/home/mpiper/Desktop
```
Note that by using the tilde `~`,
we'll get to the Desktop from wherever we are in the filesystem.

Next,
use the `mkdir` command to make a new directory:
```
$ mkdir new
$ ls
data-shell  data-shell.zip  new
```
Change to the new directory and get a listing:
```
$ cd new
$ ls
```
The new directory is empty.

The `touch` command can be used to make a new, empty, file.
```
$ touch haiku
$ ls -l
total 0
-rw-r--r--. 1 mpiper csdms 0 Jul 29 14:23 haiku
```
The `l` option to `ls` forces long output,
which shows, among other things, that the file **haiku** has zero bytes.

Let's add some content to this file.
We'll do so with a *text editor*,
an application that allows us to write in the file.
Note that a text editor is different than a *word processor*
(like Microsoft Word)
which automatically applies markup and formatting to the text.

There are many different text editors available;
e.g., `vi`, `emacs`, `atom`, `sublime`,
but the one we'll use here is called `nano`.
It trades functionality for simplicity.

Open the file **haiku** with `nano`:
```
$ nano haiku
```
The `nano` editor has a simple interface.
Just type text.
I'll enter the following:

> Yesterday it worked  
> Today it is not working  
> Software is like that.

(Funny, but computers are deterministic.
If something's not working,
it's likely because I did something wrong.)

Once you've entered the text,
hit the `Ctrl-x` key combination to save the file and exit.


## Copying, moving, removing

Let's make a copy of our haiku:
```
$ cp haiku haiku-1
$ ls
haiku  haiku-1
```
The `cp` makes a duplicate of a file.

The `mv` command moves a file from one location to another.
Let's move **haiku-1** up to the **Desktop** directory:
```
$ mv haiku-1 ~/Desktop
$ ls
haiku
$ ls ~/Desktop/
data-shell  data-shell.zip  haiku-1  new
```
Note that **haiku-1** has been moved from the **new** directory to **Desktop**.

The `mv` command can also be used to rename a file.
```
$ mv ../haiku-1 haiku.copy
$ ls
haiku  haiku.copy
```
Here, we moved the file back to the **new** directory and renamed it.

Files can be deleted with the `rm` command.
Remove our haiku copy with
```
$ rm haiku.copy
$ ls
haiku
```
There is no concept of a "trash" or "recycle" bin in the shell.
Once a file is removed, it's gone, irrevocably.

As a last step,
let's move our haiku up to the parent directory,
change to the parent directory,
then delete the **new** directory:
```
$ mv haiku ..
$ cd ..
$ rmdir new
$ ls
data-shell  data-shell.zip  haiku
```
As `rm` removes files,
the `rmdir` command removes directories.
However, the directory must be empty before it can be removed.


## Summary

The table below summarizes the commands and keyboard shortcuts
described in this section.

| Command/Shortcut | Description
| ---------------- | -----------
| mkdir            | creates a directory
| touch            | creates an empty file
| nano             | text editor
| cp               | copies a file
| mv               | moves or renames a file
| rm               | deletes a file (permanently)
| rmdir            | deletes a directory (permanently)
| Ctrl-a           | place cursor at start of line
| Ctrl-e           | place cursor at end of line
| Ctrl-k           | clear text to end of line
| Ctrl-l           | clear text in terminal

___

[Introduction to the shell](./index.md) |
Previous: [Files and directories](./files-and-directories.md) |
Next: [Pipes and filters](./pipes-and-filters.md)
