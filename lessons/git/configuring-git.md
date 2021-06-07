![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Configuring git

When using `git` for the first time on a computer,
some setup is required.
Start by opening a terminal
(your preferred terminal app on Linux or macOS;
the Git Bash Shell on Windows).

Make sure `git` is installed and in the application search path:
```
$ git --version
```

Configure `git` on your machine with the following commands:
```
$ git config --global user.name "[your name]"
$ git config --global user.email "[your email address]"
```
Substitute your name and email address in the brackets above.
This information is used by `git`,
as well as GitHub and other `git`-based services.
(A quick reminder,
if you haven't already done so,
please [sign up](https://github.com/signup) for an account on GitHub.)

You can also set the default editor used with `git`:
```
$ git config --global core.editor "nano -w"
```
We'll use `nano` by default,
but if you prefer a different editor,
the Software Carpentry [lesson](https://swcarpentry.github.io/git-novice/02-setup/index.html)
on version control has a summary table
with configuration commands for various editors.

Check the configuration you set:
```
$ git config --list
```


## Command structure

Note that the syntax for using `git` is slightly different than what we saw
for the commands in the [shell lesson](../shell/index.md).
`git` uses *subcommands*.
All calls to `git` look like `git [subcommand] [options]`.
This is a not uncommon syntax for shell commands.
We'll see other software (e.g., `conda`) that uses a similar subcommand syntax.


## Getting help with git

`git` provides several ways to get help.
Get help on the `git` command itself:
```
$ git --help
```
The output from this command shows the most common subcommands.
Get help on a specific subcommand with:
```
git [subcommand] --help
```
replacing the brackets with the subcommand;
e.g., `git config --help` will provide detailed information
on all of the options for the `config` subcommand.

To see a list of all subcommands, try:
```
$ git --help -a
```

`git` also has a (very long) `man` page:
```
man git 
```

Finally,
the full [git documentation](https://git-scm.com/docs) is available online.


## Summary

`git`:

* needs to be configured on a computer before it's used
* uses subcommands
* provides several ways to get help

___

[Introduction to version control](./index.md) |
Previous: [index](./index.md) |
Next: [A version control workflow](./git-workflow.md)
