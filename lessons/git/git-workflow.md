![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# A version control workflow

In this section,
we'll work through an example that broadly demonstrates
how to use version control on a project.
Imagine, for instance,
backing up and tracking your thesis, a class project,
or collaborating on a journal article<sup>[1](#git-fn1)</sup>
with a colleague.
This is where GitHub is powerful.

We broadly follow this workflow:

* fork
* clone
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

We'll start by *forking* a repository on GitHub.
A fork is a copy of a repository, a *remote*, placed under your GitHub account.
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


## Branch

## Edit

## Add

## Commit

## Push

## Pull request

## Merge

## Pull
