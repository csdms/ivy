![ESPIn logo](https://raw.githubusercontent.com/csdms/espin/main/media/logo.png)

# Getting things from elsewhere

While it's often straightforward to click to download items from a web browser,
it's also possible to get them with shell commands,
and the shell commands provide more flexibility.

For example,
the URL from which we downloaded the Software Carpentry sample data files is

> https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip

Use the `curl` command to download this file programmatically:
```
$ curl https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip -o shell-lesson-data-1.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  566k  100  566k    0     0  2037k      0 --:--:-- --:--:-- --:--:-- 2045k
```
Here, I used the `o` option to choose a slightly different name
for the downloaded file,
so as not to clobber the existing file.

Verify that the file was downloaded:
```
$ ls -l *.zip
-rw-r--r--  1 mpiper  staff  580102 Jul 30 16:22 shell-lesson-data-1.zip
-rw-r--r--@ 1 mpiper  staff  580102 Jul 28 16:05 shell-lesson-data.zip
```

`curl` can do very cool things with wildcards, as well.
Visit its (lengthy) man page to see all the options.

The `wget` command provides functionality similar to `curl`,
but with a slightly simpler call.
```
$ wget https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip
--2020-07-30 16:36:01--  https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip
Resolving swcarpentry.github.io... 185.199.109.153, 185.199.108.153, 185.199.111.153, ...
Connecting to swcarpentry.github.io|185.199.109.153|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 580102 (567K) [application/zip]
Saving to: ‘shell-lesson-data.zip.1’

shell-lesson-data.zip.1     100%[======================>] 566.51K  --.-KB/s    in 0.09s

2020-07-30 16:36:01 (6.34 MB/s) - ‘shell-lesson-data.zip.1’ saved [580102/580102]
```

Verify that the file was downloaded:
```
$ ll *zip*
-rw-r--r--  1 mpiper  staff  580102 Jul 30 16:22 shell-lesson-data-1.zip
-rw-r--r--@ 1 mpiper  staff  580102 Jul 28 16:05 shell-lesson-data.zip
-rw-r--r--@ 1 mpiper  staff  580102 Jul  1 01:44 shell-lesson-data.zip.1
```


## Unpacking files

Because of their smaller size,
it's more efficient to transfer a compressed file over the internet.

The example files downloaded from Software Carpentry
are compressed into a *zip archive*.
We've already uncompressed these files into the **shell-lesson-data** directory
through the operating system.
Let's remove these files and instead uncompress the zip file using the shell.

First, remove the existing **shell-lesson-data** directory:
```
$ rm -rf shell-lesson-data
```
Then use the `unzip` command to uncompress **shell-lesson-data.zip**:
```
$ unzip shell-lesson-data.zip
Archive:  shell-lesson-data.zip
   creating: shell-lesson-data/
  inflating: shell-lesson-data/pizza.cfg
  inflating: shell-lesson-data/.bash_profile
   creating: shell-lesson-data/molecules/
  inflating: shell-lesson-data/molecules/ethane.pdb
  inflating: shell-lesson-data/molecules/cubane.pdb
  ...
```

While zip files are common on Windows,
*tar* files that use the more efficient gzip and bzip2 compressors
are more common on Unix-based operating systems.

Let's compress the **shell-lesson-data** directory
with `tar` and compare file sizes:
```
$ tar -czf shell-lesson-data.tar.gz shell-lesson-data
$ tar -cjf shell-lesson-data.tar.bz2 shell-lesson-data
```
In these commands,
the `c` option creates an archive file,
the `f` option provides the name of the archive file,
and the `z` and `j` options specify gzip and bzip2 compression, respectively.
The **.tar.gz** and **.tar.bz2** extensions are used by convention.

Check sizes:
```
$ ls -lh shell-lesson-data.*
-rw-r--r--  1 mpiper  staff   393K Jul 31 15:42 shell-lesson-data.tar.bz2
-rw-r--r--  1 mpiper  staff   518K Jul 31 15:41 shell-lesson-data.tar.gz
-rw-r--r--@ 1 mpiper  staff   567K Jul 28 16:05 shell-lesson-data.zip
```
Note that bzip2 < gzip < zip compression.
In the directory listing, recall the `l` option provides a long listing.
The `h` option provides "human readable" output.

Uncompress these tarballs with:
```
tar -xf shell-lesson-data.tar.gz
tar -xf shell-lesson-data.tar.bz2
```
Here, the `x` option is for uncompressing the archive file.
In each case,
the existing **shell-lesson-data** directory was clobbered
when the archive was uncompressed.


## Download the ESPIn repository

The ESPIn repository lives on GitHub at

> https://github.com/csdms/espin

In the lesson on [version control](../git/index.md),
we'll learn how to work with repositories hosted on GitHub,
but for now,
we can download the repository as a zip archive
and uncompress it using the commands we learned above.

Use `curl` to download the zip archive:
```
$ curl https://codeload.github.com/csdms/espin/zip/main -o main.zip
```

The `file` command returns a file's type.
Use it to verify that file downloaded from GitHub
is actually a zip archive:
```
$ file main.zip
main.zip: Zip archive data, at least v1.0 to extract
```

Now use `unzip` to uncompress the file:
```
$ unzip main.zip
```
This creates a new directory, **espin-main**.
View its contents:
```
$ ls espin-main/
LICENSE          data             lessons
README.md        environment.yaml media
```

Note that this is one way of getting files from GitHub.
A better way is to use `git` to retrieve the repository contents
along with their histories.
We'll cover how to do this in the [version control](../git/index.md) lesson.


## Summary

The table below summarizes the commands described in this section.

| Command  | Description
| -------- | -----------
| curl     | get files from an URL
| wget     | get files from an URL (nonstandard)
| zip      | package and compress/uncompress files
| gzip     | package and compress/uncompress files
| tar      | package and compress/uncompress files
| file     | get file type information

___

[Introduction to the shell](./index.md) |
Previous: [Finding things](./finding-things.md)
