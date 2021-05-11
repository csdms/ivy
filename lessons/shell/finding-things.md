![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Finding things

The `grep` command is a powerful tool for matching patterns in files.
Let's use it to look for unicorns in our files:
```
$ grep -r unicorn .
./data-shell/creatures/unicorn.dat:1:COMMON NAME: unicorn
Binary file ./data-shell.zip matches
```
The `r` option performs a recursive search,
starting at the current directory,
specified by the dot `.`.
Note that `grep` searched both text and binary files for the matching pattern.
To omit binary files from the search,
use the `I` option:
```
$ grep -rI unicorn .
./data-shell/creatures/unicorn.dat:1:COMMON NAME: unicorn
```

To search only within the current directory,
the syntax of `grep` is slightly different.
Let's find all instances of the word "octane" in the files
in the current directory:
```
$ grep octane *
grep: data-shell: Is a directory
Binary file data-shell.zip matches
molecule_pdb_lengths:4:  30 octane.txt
molecule_pdb_lengths.bak:4:  30 octane.pdb
```
Note that I used the wildcard to denote all files in the current directory.

The `find` command recursively locates all files that match a search pattern.
Let's find all the files with the extension **.txt**:
```
$ find . -iname "*.txt"
./data-shell/data/amino-acids.txt
./data-shell/data/animal-counts/animals.txt
./data-shell/data/animals.txt
./data-shell/data/morse.txt
./data-shell/data/planets.txt
...
```
The search started at the current directory, `.`
The `iname` option directs `find` to ignore case in the search.

In another example,
let's use `find` to recursively locate all the directories
under the current directory:
```
$ find . -type d
.
./data-shell
./data-shell/creatures
./data-shell/data
./data-shell/data/animal-counts
...
```

## Command documentation

In the examples above (and in previous sections),
options for commands are frequently demonstrated.
To view a full list of options for any command,
use the `man` command to pull up its manual page.
For example, to get information about `find`, type:
```
$ man find
```
The `man` command displays documentation for `find`,
including all options and several examples,
in a pager.
The man page for `find` is quite long.
Press `q` in the pager to quit and return to the terminal.


## Command history

Every command you enter is logged.
To see the record of commands,
use `history`:
```
$ history
```
The entire command history is dumped to the terminal.
To view only the last five commands (for example),
pipe the output of `history` through `tail`:
```
$ history | tail -5
  631  find . -type d
  632  man find
  633  man man
  634  man find
  635  history
```

How many times have you referenced `find`?
```
$ history | grep find | wc -l
      32
```

The exclamation point, or bang, `!` can be used to match a command in history.
For example, to execute the last call to `man`, type:
```
$ !man
man find
```

To search history beyond the last instance of a command,
use the `Ctrl-r` keybinding.
At the prompt,
type `Ctrl-r`, then a search term.
Keep hitting `Ctrl-r` to move back through history.



## Summary

The table below summarizes the commands, keyboard shortcuts,
and special characters described in this section.

| Command/Shortcut | Description
| ---------------- | -----------
| grep             | match text in files
| find             | match filenames
| man              | show documentation for command
| history          | record of commands
| !                | repeat command matched from history
| Ctrl-r           | reverse search through history

___

[Introduction to the shell](./index.md) |
Previous: [Pipes and filters](./pipes-and-filters.md)
Next: [Getting things from elsewhere](./getting-things.md)
