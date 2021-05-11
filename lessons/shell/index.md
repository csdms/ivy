![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Introduction to the shell

In this lesson we'll learn about the *shell*,
a command-based interface for interacting
with the operating system of a computer.

*Learning objectives:*

* Locate and open the terminal application on your computer
* Know what a file system is
* Understand basic shell commands for manipulating files
* Get exposure to some intermediate/advanced commands
* Know where to get help, or more information


## Get the lesson data

This lesson uses a set of sample files
from [Software Carpentry](https://software-carpentry.org/).
which you'll need to follow the lesson.

Please:

1. Download [data-shell.zip](https://swcarpentry.github.io/shell-novice/data/data-shell.zip) and move the file to your Desktop.
1. Unzip/extract the file (ask your instructor if you need help with this step).

You should end up with a new folder called **data-shell** on your Desktop.


## Open a terminal

A *terminal* is an application that allows a user to communicate
with the operating system of a computer
through terse text commands.

* Linux: terminal or xterm
* macOS: Terminal.app (built-in) or [iTerm.app](https://www.iterm2.com/) (better)
* Windows: Git Bash Shell in [Git for Windows](https://gitforwindows.org/)

At this time,
if you haven't already done so,
open a terminal on your computer.


## Why are we using a terminal?

Because it works. Really well.

When you develop skill with shell commands in a terminal,
you can do filesystem-specific tasks--moving, copying, renaming, deleting
files and directories--much faster than with a graphical application.

By analogy, think of keyboard shortcuts on your computer:
if you want to change from one application to another,
it's much faster to hit `Cmd-Tab` (on macOS; `Alt-Tab` on Linux and Windows)
than it is to use a mouse to go find the other application window.

Commands tend to be terse to the point of being cryptic,
not that different from texting shorthand:
instead of brb, it's `cd`;
instead of ttyl, it's `rm`, etc.
And it's done for the same reason: speed.

Commands can also be gathered into *scripts* that can be executed as a single unit.
With a script, you can automate a repetitive task.
Scripts are marvelous for data processing pipelines,
and can improve reproducibility.
We won't cover scripting here,
but there's more information in Software Carpentry's
[The Unix Shell](https://swcarpentry.github.io/shell-novice/) lesson,
on which this lesson is based.


## Enter commands, get results

The command prompt (or shell prompt) is where we enter commands into a terminal.
It's typically denoted with a dollar sign `$`.

We use a terminal in a **read-evaluate-print loop (REPL)**;
that is, when we enter a command at the prompt, the shell

1. reads the command
1. evaluates the command
1. prints output to the terminal

This process is repeated every time we enter a command.


## Topics

This lesson on the shell continues in the following sections.

1. [Files and directories](./files-and-directories.md)
1. [Creating things](./creating-things.md)
1. [Pipes and filters](./pipes-and-filters.md)
1. [Finding things](./finding-things.md)
1. [Getting things from elsewhere](./getting-things.md)


## Resources

* This lesson is loosely based on the Software Carpentry [shell lesson](https://swcarpentry.github.io/shell-novice/)
* The [Bash Guide for Beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/) from the Linux Documentation Project
* The [GNU Bash Manual](https://www.gnu.org/software/bash/manual/) in various formats
