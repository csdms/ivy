![Ivy logo](https://raw.githubusercontent.com/csdms/ivy/main/media/logo.png)

# The shell, in brief

This shortened introduction to the shell
is designed to run on the OpenEarthscape JupyterHub.

## Files and directories

Information on a computer is stored in files and directories.
The part of an operating system that handles this information
is called the *file system*.
Think of the file system as a tree with branches (directories) and leaves (files).

Let's find out where we are in the file system when we start a terminal:
```
$ pwd
/home/jupyter-mpiper
```

The `pwd` command prints the current directory to the terminal.
You can see that I'm in the directory `jupyter-mpiper` under the directory `home`.
The forward slash `/` is used as a delimiter between directory names.

The string "/home/jupyter-mpiper" is called a *path*.
Think of a path as directions used to get to a location on the file system.
This path is an example of an *absolute path*
because it starts at "/", the *root* of the file system.

The directory `/home/jupyter-mpiper` is special--it's the *home directory*
of the user `jupyter-mpiper`.
Every user has a home directory.
It's the default location for you to create and store information.

Note that I executed this command on a JupyterHub running Linux;
the home directory on a macOS or Windows machine will be slightly different.

## Directory listings

Next, let's look at the contents of user `jupyter-mpiper`'s home directory:
```
$ ls
CoCoLessons  bin          bmi-topography  ivy       scratch
README.md    bmi-geotiff  data            projects  tmp
```

The `ls` command provides a directory listing.
This home directory holds a set of files and directories.

We can drill down through directories by providing arguments to `ls`.
For example, to see the contents of the **ivy** directory, type:
```
$ ls ivy
AUTHORS.rst         CONTRIBUTING.rst    README.md           lessons
CITATION.cff        LICENSE.md          data                media
CODE-OF-CONDUCT.rst README.ipynb        environment.yaml
```

You can see that the CSDMS Ivy lesson files
have been added to the JupyterHub.
We can drill further; for example,
to see into the directory containing data files, type:
```
$ ls ivy/data
Europe.csv                 swc_python.zip
EuropePoints_xp25_ym30.csv topo.asc
```

## Changing directories

Although we've peered into the directory of Ivy files,
we remain in the home directory.
To change directories, use the `cd` command:
```
$ cd ivy
$ pwd
/home/jupyter-mpiper/ivy
```

The `pwd` command shows that we've switched to the **ivy** directory.

The `cd` command can take a directory name as an argument.
It can also take no arguments:
```
$ cd
$ pwd
/home/jupyter-mpiper
```

With no arguments, `cd` always returns to your home directory.

The `cd` command can also take a set of special characters as arguments.
To switch to the previous directory, use a dash `-`:
```
$ cd -
/home/jupyter-mpiper/ivy
```

When working with directories, a dot `.` is a shortcut for the current directory,
while two dots `..` are a shortcut for the *parent directory*,
one directory closer to the root of the file system:
```
$ cd .
$ pwd
/home/jupyter-mpiper/ivy
$ cd ..
$ pwd
/home/jupyter-mpiper
```

Likewise, the tilde `~` is a shortcut for the user's home directory:
```
$ cd ~
$ pwd
/home/jupyter-mpiper
```

## Making a directory

From your home directory, use the `mkdir` command to make a new directory:
```
$ mkdir new
$ ls
CoCoLessons  bin          bmi-topography  ivy  projects  tmp
README.md    bmi-geotiff  data            new  scratch
```

Change to the new directory and get a listing:
```
$ cd new
$ ls
```

The new directory is empty.

## Copying, moving, and removing

Let's copy a file from the **ivy** directory to our **new** directory:
```
$ cp ../ivy/README.md .
$ ls
README.md
```

Here, we instructed the `cp` command to go up a directory and over to the
**ivy** directory to get a file and copy it to the current directory.
In this example,
the arguments to `cp` are both *relative paths*
because their starting points are relative
to the current directory on the file system.

Note that the copy and the original both exist, and are the same:
```
$ $ diff -s README.md ../ivy/README.md
Files README.md and ../ivy/README.md are identical
```

The `diff` command compares files and reports how they differ.

The `mv` command can be used to rename a file.
```
$ mv README.md readme.md
$ ls
readme.md
```

The `mv` command can also be used to move a file from one location to another.
Let's move **readme.md** up to the home directory:
```
$ mv readme.md ~
$ ls
$ ls ~
CoCoLessons  bin          bmi-topography  ivy  projects   scratch
README.md    bmi-geotiff  data            new  readme.md  tmp
```

Note that the **new** directory is now empty because **readme.md** has been
moved to the home directory.
Also note that **README.md** and **readme.md** in the home directory are
different files!
The file systems in Linux and macOS are case-sensitive.

Files can be deleted with the `rm` command.
Remove our **readme.md** file with:
```
$ cd
$ rm readme.md
```

There is no concept of a "trash" or "recycle" bin in the shell.
Once a file is removed, it's gone, irrevocably.

## Removing a directory

As a last step, let's delete the **new** directory:
```
$ rmdir new
$ ls
CoCoLessons  bin          bmi-topography  ivy     scratch
README.md    bmi-geotiff  data            projects  tmp
```

As `rm` removes files, the `rmdir` command removes directories.
However, the directory must be empty before it can be removed.

## Summary

The table below summarizes the concepts described in this lesson.

| Concept | Description |
| ------- | ----------- |
| file system       | the part of operating system that organizes how information is stored and accessed |
| path              | a string that gives the location of a file or directory on the file system |
| absolute path     | a path that starts at the root of the file system |
| relative path     | a path that starts at the current directory |
| current directory | the path where the shell process is currently working |
| home directory    | the default path location for a user to store files and directories |
| parent directory  | the path one directory closer to the root |

The table below summarizes the commands and special characters described in this lesson.

| Command | Description |
| ------- | ----------- |
| pwd     | print working directory |
| ls      | directory listing |
| cd      | change directory |
| /       | path delimiter |
| ~       | home directory |
| .       | current directory |
| ..      | parent directory |
| -       | previous directory |
| cp      | copies a file |
| mv      | moves or renames a file |
| diff    | compares contents of files |
| rm      | deletes a file (permanently) |
| mkdir   | creates a directory |
| rmdir   | deletes a directory (permanently) |

___

[Introduction to the shell](./index.md)
