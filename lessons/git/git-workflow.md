![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# A version control workflow

In this section,
we'll work through an example that broadly demonstrates
how to use version control on an individual or a group project.
Imagine, for example,
backing up and tracking your thesis,
or collaborating on a journal article
with a colleague.
<!-- This is where GitHub is powerful. -->

We'll broadly follow the series of actions in this workflow:

* fork
* clone
* status
* branch
* edit
* add
* commit
* push
* pull request
* merge
* pull

and we'll frequently refer to this diagram of git remotes:

![git remotes](https://github.com/csdms/espin/blob/main/media/git-remotes-diagram.png "Git remotes")


## Fork

We'll start by forking a repository on GitHub.
A *fork* is a copy of a repository, a *remote*, placed under your GitHub account.
Forks are used for repositories where you don't have write access
(meaning you can view files, but not change them).
Note that forking is a GitHub, not a `git`, concept.

Let's use the repository https://github.com/espin-2021/espin-collaboration as an example.

1. Go to the [repository page](https://github.com/espin-2021/espin-collaboration) on GitHub.
1. From the top right of the repository page, select the *Fork* button--you'll
   be asked where to create the fork; select your GitHub account.

After the fork is created,
the path to the repository on GitHub will read
**[username]/espin-collaboration** instead of **espin-2021/espin-collaboration**,
where **[username]** is your GitHub username,
indicating your ownership of this copy of the repository.


## Clone

The forked repository exists on GitHub,
but to work with it,
we'll need it locally.
We have to *clone* the repository to our computer.
As the name suggests,
a cloned repository is an identical, but separate,
copy of the current state of the original.

On your computer, open a terminal and change to your **Desktop** directory:
```
$ cd ~/Desktop
```

Now clone your repository from GitHub.
The syntax for the `git clone` subcommand is
```
$ git clone [repository-url]
```
where the bracketed text should be replaced with the URL of your new repository.

The repository is cloned into the directory **espin-collaboration**.
Change to it and view its contents:
```
$ cd espin-collaboration
$ pwd
/Users/mpiper/Desktop/espin-collaboration
$ ls
CONTRIBUTORS.md LICENSE   README.md
```


## Status

The next step in the workflow isn't isn't necessary at this point, but it's something we'll return to frequently when working with a repository.

Use the `git status` subcommand to check on the current state of the repository:
```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Let's parse this output.
`git status` displays helpful information about the repository,
including:

- the current *branch*
- whether the current branch is synchronized with the *origin* repository
- whether files are present that aren't in the repository

Branches are covered in the next section.
The *origin* is the repository from which the current repository was cloned.
The origin is an instance of a *remote* repository,
in contrast the to *local* repository on your computer and the *upstream* repository you forked.
(See the diagram above.)


## Branch

To prepare for making changes to the repository,
let's make a new branch.

A *branch* is an alternate timeline for the history of a repository.
Think of `git` branches as analogous to alternate history fiction:
branches have a common history,
but at some point they diverge and develop their own histories.
Branches are used in a collaborative project to propose changes.

The syntax for creating a branch is `git branch [branchname]`.
It's a convention to use imperative case for the branch name,
and to prepend your GitHub username.
Looking ahead,
let's name this branch `update-contributors`.
If your GitHub username is `@mdpiper`,
this would be:
```
$ git branch mdpiper/update-contributors
```

Although we've created a new branch,
our *current branch*,
the one accepting changes,
is still the default `main` branch,
as we can see with `git branch`:
```
$ git branch
* main
  mdpiper/update-contributors
```
The current branch is marked with an asterisk.

To change the current branch,
use the `git checkout` subcommand
(again, for a hypothetical user `@mdpiper`):
```
$ git checkout mdpiper/update-contributors
Switched to branch 'mdpiper/update-contributors
```
You can verify that the new branch is current with `git branch`.


## Edit

Adding or editing content is typically where most of your time is spent
in a project.
In this example, however, it'll be trivial.

Recall that the **espin-collaboration** repository
has a file, **CONTRIBUTORS.md**.
Change to the repository directory and view its contents:
```
$ ls
CONTRIBUTORS.md LICENSE   README.md
```
With your favorite text editor,
open the file **CONTRIBUTORS.md**
add your name to the list of contributors,
along with something interesting.
Save the file.

Now that we've changed a file that's under version control,
view the changes with `git diff`:
```
$ git diff CONTRIBUTORS.md
diff --git a/CONTRIBUTORS.md b/CONTRIBUTORS.md
index 23d368e..41f5c9b 100644
--- a/CONTRIBUTORS.md
+++ b/CONTRIBUTORS.md
@@ -2,4 +2,4 @@

 The following people have contributed to this project.

-* Mark Piper
+* Mark Piper (I like to ride my bike)
```

Then check on the state of the repository with `git status`:
```
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   CONTRIBUTORS.md

no changes added to commit (use "git add" and/or "git commit -a")
```
Note that `git status` gives us a hint at the next step in our workflow.


## Add

## Commit

## Push

## Pull request

## Merge

## Pull

## Summary

The power of GitHub lies in its streamlined support for collaborative development.
GitHub has rewritten the rules for open source software development,
and this has diffused into the modern practice of science,
For example,
all CSDMS products are open source.
If you find a problem in our software, documentation,
Jupyter Notebooks, etc.,
please fix it and send us pull request!
You'll get credit for your contribution.


This table summarizes `git` and GitHub concepts covered in this section:

| Concept        | Description
| ------------   | -----------
| repository     | a storage area for files where history is tracked by version control
| fork           | a repository copied from elsewhere on GitHub that exists under your GitHub account
| branch         | a pointer to a timeline of commits to a repository
| current branch | the active repository branch accepting changes
| origin         | the repository from which your local repository is cloned
| local          | the clone of a repository that resides on your computer
| remote         | a clone of a repository that's not on your computer
| staging area   | the gathering place for files to be committed to a repository
| commit         | a change made to the content of a repository under version control
| push           | a transfer of commits to a remote
| pull request   | a process for explaining changes pushed to a repository

This table summarizes the `git` subcommands used in this section:

| Subcommand | Description
| ---------- | -----------
| clone      | clone a repository into a new directory
| status     | display current state of a repository
| branch     | create a branch of a repository
| checkout   | set a branch as the current branch in a repository
| diff       | show differences between working directory and repository state
| add        | stage a change to a repository
| commit     | finalize a change to a repository
| log        | show commit history in repository
| push       | transfer changes from one clone of a repository to another


___

[Introduction to version control](./index.md) |
Previous: [Version control in a single-user project](./git-single-user-project.md)
