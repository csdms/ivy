![ESPIn logo](../../media/ESPIn.png)

# Version control in a collaborative project

In this section,
we'll work through an example that broadly demonstrates
how to use version control for a collaborative project.
Imagine, for instance,
using version control to back up and track
your thesis, a class project, or a journal article<sup>[1](#git-fn1)</sup>.
This is where GitHub is powerful.


## Fork a repository on GitHub

We'll start by *forking* a repository on GitHub.
A fork is a copy of a repository placed under your GitHub account.
Forks are used for repositories where you don't have write access
(meaning you can view files, but not change them).
Note that forking is a GitHub, not a `git`, concept.

Let's use the ESPIn course repository as an example.
(We've held off on doing this earlier
because this is the proper way to do it.)


1. Go to the [ESPIn repository](https://github.com) on GitHub.
1. From the top right of the repository page, select the *Fork* button--you'll
   be asked where to create the fork; select your GitHub account.

After the fork is created,
the path to the repository on GitHub will read
**[username]/espin** instead of **csdms/espin**,
where **[username]** is your GitHub username,
indicating your ownership of this copy of the repository.


## Clone the repository

The forked repository lives on GitHub.
To work with it,
you have to clone it to your computer.

On your computer, open a terminal and change to your **Desktop** directory:
```
$ cd ~/Desktop
```

Now clone the fork from GitHub.
```
$ git clone https://github.com/[username]/espin
```
where the bracketed text should be replaced with your GitHub username.

The repository is cloned into the directory **espin**.
Change to it and view its contents:
```
$ cd espin
$ pwd
/Users/mpiper/Desktop/espin
$ ls
LICENSE          data             lessons
README.md        environment.yaml media
```


## Make a branch

Next,
to prepare for making changes to the repository,
let's make a new branch.
Recall a branch is an alternate timeline for the history of a repository.
Branches are used in a collaborative project to propose changes.

The syntax for creating a branch is `git branch [branchname]`.
It's a convention to use imperative case for the branch name,
and to prepend your GitHub username.
Looking ahead,
let's name this branch `change-colormap`.
If your GitHub username is `@mdpiper`,
this would be:
```
$ git branch mdpiper/change-colormap
```

Although we've created a new branch,
our *current branch*,
the one accepting changes,
is still the default `main` branch,
as we can see with `git status`:
```
$ $ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Alternately,
we can use the `git branch` command to see the current and available branches:
```
$ git branch
* main
  mdpiper/change-colormap
```
Here, the current branch is marked with an asterisk.

To change the current branch,
use the `git checkout` subcommand
(again, for a hypothetical user `@mdpiper` (red panda)):
```
$ git checkout mdpiper/change-colormap
Switched to branch 'mdpiper/change-colormap'
```
You can verify that the new branch is current with `git status` or `git branch`.


## Modify a file in the repository

As we did in the previous example,
let's change the colormap in the sample Python script;
however, this time we'll do so in your fork of the ESPIn repository.

Use your text editor to open the Python script:
```
$ nano ./lessons/best-practices/boulder_dem.py
```
and recall that we'd like to change the colormap from "jet" to "viridis"
on line 21 of the file, like so:
```python
elev = ax.imshow(data, cmap="viridis")
```
Once you've made the change, save the file and exit the editor.

Using `git status`, we can see that the file has been modified.
```
$ git status
On branch mdpiper/change-colormap
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   lessons/best-practices/boulder_dem.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Commit the change to the branch
(noting that we're again skipping the staging step):
```
$ git commit lessons/best-practices/boulder_dem.py -m "Use viridis colormap for display"
[mdpiper/change-colormap 5b0d87c] Use viridis colormap for display
 1 file changed, 1 insertion(+), 1 deletion(-)
```


## Push changes to GitHub

Now that we've made a change to the local copy of the fork,
let's push the change back to the remote:
```
$ git push origin mdpiper/change-colormap
Counting objects: 10, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 91.63 KiB | 45.81 MiB/s, done.
Total 10 (delta 6), reused 1 (delta 0)
remote: Resolving deltas: 100% (6/6), completed with 4 local objects.
remote:
remote: Create a pull request for 'mdpiper/change-colormap' on GitHub by visiting:
remote:      https://github.com/mdpiper/espin/pull/new/mdpiper/change-colormap
remote:
To https://github.com/mdpiper/espin.git
 * [new branch]      mdpiper/change-colormap -> mdpiper/change-colormap
```
Note that the output from `git push` is more verbose
that in the previous, single-user, example;
it includes a link to create a *pull request* on GitHub.
Copy/paste this link into your browser
and we'll create a pull request next.


## Create a pull request

A *pull request* is a GitHub feature
that allows you to argue why the changes that you've pushed to a repository
deserve to be included in that repository.
In a pull request,
you have to make a case to the owner of the repository
that your code improves on theirs.

A pull request includes a title, a body,
and, optionally, a comment thread.
The title should be as brief, yet descriptive, as possible,
and written as an imperative.
The body is used to explain your changes
and to argue for their inclusion in the repository.
To help make the text more descriptive,
the body is written in [Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax),
a simple markup language.
In the body,
you can also `@` other GitHub users (e.g., `@BCampforts`)
to include them on the pull request.
The comment thread is used to discuss the merits of the pull request.

GitHub provides [much more information](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)
on pull requests.

Argue well, and your contribution may be accepted by the repository owner!


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

| Concept      | Description
| ------------ | -----------
| fork         | a repository copied from elsewhere on GitHub that exists under your GitHub account
| current branch | the active repository branch accepting changes
| pull request | A process for explaining changes pushed to a repository

This table summarizes the `git` subcommands used in this section:

| Subcommand | Description
| ---------- | -----------
| branch     | create a branch of a repository
| checkout   | set a branch as the current branch in a repository


<a name="git-fn1">1</a>: Yes, that was on purpose.

___

[Introduction to version control](./index.md) |
Previous: [Version control in a single-user project](./git-single-user-project.md)
