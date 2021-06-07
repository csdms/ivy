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
* sync

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
On branch mdpiper/update-contributors
Your branch is up-to-date with 'origin/main'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   CONTRIBUTORS.md

no changes added to commit (use "git add" and/or "git commit -a")
```
Note that `git status` gives us a hint at the next step in our workflow.


## Add

At this point, `git` is aware that a file has changed in the repository.

The next step is to call `git add` on this file
so that `git` knows that its changes are intended to be included in the repository.
```
$ git add CONTRIBUTORS.md
```

Check the result of this command with `git status`:
```
$ git status
On branch mdpiper/update-contributors
Your branch is up-to-date with 'origin/main'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   CONTRIBUTORS.md

```
The file has now been placed in the *staging area* of the repository,
a place to gather changes to the repository before finalizing them.

While this step is needed to add new files to a repository,
it's not technically needed in the context of this example.
However, it's often useful, for example when working with a number of files,
to stage a subset of related changes to be grouped into a single commit.


## Commit

To finalize the changes to the repository,
we *commit* them with `git commit`:
```
$ git commit -m "Add an interesting fact to contributor list"
[mdpiper/update-contributors 4c9565b] Add an interesting fact to contributor list
 1 file changed, 1 insertion(+), 1 deletion(-)
```

When committing a change to a repository,
it's a good practice to include a message
(here, using the `m` option)
describing why the change is being made.
It's also a convention to use imperative case.
Check the result with `git status`:
```
$ git status
On branch mdpiper/update-contributors
nothing to commit, working directory clean
```

The file is now a part of the local repository.
The working directory has no unknown files,
and the staging area is empty.


## Push

Our local repository now differs from its remotes.

View the history of revisions to the repository with `git log`:
```
$ git log
commit 4c9565be25ca5c91d66867631112c68301250991
Author: Mark Piper <mark.piper@colorado.edu>
Date:   Mon Jun 7 15:19:32 2021 -0600

    Add an interesting fact to contributor list

commit 966dab15533e3a975ebc9bb0a8ca9b5a9f05bf09
Author: Mark Piper <mark.piper@colorado.edu>
Date:   Fri Jun 4 12:11:41 2021 -0600

    Add contributors document

commit 97fb4755d5f469ae32fff99864eb49e8ab193457
Author: Mark Piper <mark.piper@colorado.edu>
Date:   Fri Jun 4 12:05:49 2021 -0600

    Initial commit
```

Let's now transmit the changes from our local repository to the *origin* remote.
We do this with the `git push` subcommand,
which has the syntax `git push [remote] [branch]`.
Here,
the remote is `origin`
and the branch is `mdpiper/update-contributors`.
Note that in order to push changes to a remote,
you must have write access on the remote.
Therefore, push the changes with:
```
$ git push origin mdpiper/update-contributors
Counting objects: 3, done.
Delta compression using up to 16 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 387 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'mdpiper/update-contributors' on GitHub by visiting:
remote:      https://github.com/mdpiper/espin-collaboration/pull/new/mdpiper/update-contributors
remote:
To https://github.com/mdpiper/espin-collaboration
 * [new branch]      mdpiper/update-contributors -> mdpiper/update-contributors
```

Note that the output from `git push`
includes a link to create a *pull request* on GitHub.
Copy/paste this link into your browser
and we'll create a pull request next.


## Pull request

A *pull request* is a GitHub feature
that allows you to argue why the changes that you've pushed to a remote
deserve to be included in that repository.
In a pull request,
you have to make a case to the owner of the repository
that your code improves on theirs.

A pull request includes a title, a body,
and, optionally, a comment thread.
The title should be brief, yet descriptive,
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


## Merge

A *merge* occurs after a pull request has been approved.
Merging joins two or more branches together in the *upstream* remote.
Anyone who has push access to this remote can perform a merge.

A *merge conflict* occurs when a line or section of code has been modified
in more than one branch,
preventing the histories from being joined.
Merge conflicts have to be resolved before a pull request can be merged.
A repository owner can keep changes from one of the branches,
or make a new change that incorporates changes from both branches.


## Pull and sync

After a pull request has been merged,
the *upstream* remote includes history not present in the *local* or *origin* remotes.
We can *sync* these repositories in a few steps.

First,
use the `git remote` subcommand to view what remotes are being tracked on your local machine:
```
origin	https://github.com/mdpiper/espin-collaboration (fetch)
origin	https://github.com/mdpiper/espin-collaboration (push)
```

By default,
the only remote tracked is *origin*.
We can track the *upstream* remote, as well, with:
```
$ git remote add upstream https://github.com/espin-2021/espin-collaboration
```

Check the result with another call to `git remote`:
```
$ git remote -v
origin	https://github.com/csdms/espin-collaboration (fetch)
origin	https://github.com/csdms/espin-collaboration (push)
upstream	https://github.com/espin-2021/espin-collaboration (fetch)
upstream	https://github.com/espin-2021/espin-collaboration (push)
```

Next, switch back to the *main* branch in your local repository.
This is the branch into which the pull request was merged.
```
$ git checkout main
Switched to branch 'main'
Your branch is up-to-date with 'origin/main'.
```

Now *pull* the changes from the *upstream* remote into you local repository
with the `git pull` subcommand:
```
$ git pull upstream main
```

Your local repository is now in sync with the *upstream* remote.

Finally, sync the *origin* remote by pushing the changes from your local repository:
```
$ git push origin main
```


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
| merge          | joins the history of one branch to another
| merge conflict | competing line changes in one or branches to be merged
| sync           | set all remotes to a common point in their histories


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
| push       | transfer changes from a local repository to a remote
| pull       | transfer changes from a remote to a local repository
| remote     | add, remove, or update remote repositories


___

[Introduction to version control](./index.md) |
Previous: [Version control in a single-user project](./git-single-user-project.md)
