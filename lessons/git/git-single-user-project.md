![ESPIn logo](../../media/ESPIn.png)

# Version control in a single-user project

In this section,
we'll work through an example that broadly demonstrates
how to use version control for a single-user project.
Imagine, for instance,
backing up and tracking
your thesis, a class project, or a journal article<sup>[1](#git-fn1)</sup>.

## Create a repository on GitHub

We'll start by creating a new repository on GitHub.

1. Login to [GitHub](https://github.com).
1. Go to https://github.com/new to set up a new repository.
   (Alternately, select the *New* button from the top left of the
   GitHub main page.)
1. Choose a name for the new repository; please use `espin-example` here.
1. Add a description; e.g., `A sample repository for the ESPIn git lesson`.
1. Make the repository public.
1. Initialize the repository with a README.
1. (Optional, but recommended) Choose an open source license for the
   repository. (CSDMS typically uses the MIT License.)
1. Select the *Create repository* button.

Note the URL of your new repository in the location bar of your web browser.
We'll use it in the next section.


## Clone the repository

The new repository exists on GitHub,
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

The repository is cloned into the directory **espin-example**.
Change to it and view its contents:
```
$ cd espin-example
$ pwd
/Users/mpiper/Desktop/espin-example
$ ls
LICENSE   README.md
```


## Add content to the repository

The repository is empty except for the license and README files.
Let's add some content.

In the shell lesson,
we downloaded the [ESPIn repository](https://github.com/csdms/espin)
as a zip archive and uncompressed it in our **Desktop** directory.
Copy the file **boulder_dem.py** from there to the current directory.
```
$ cp ~/Desktop/espin-main/lessons/best-practices/boulder_dem.py .
```
Alternately,
we could download the file directly from GitHub with `curl`:
```
$ curl https://raw.githububest-practicesrcontent.com/csdms/espin/main/lessons/best-practices/boulder_dem.py > boulder_dem.py 
```
In either case,
check that the file is now present:
```
$ ls
LICENSE        README.md      boulder_dem.py
```

The addition of this file means the repository has changed.
Check the current state of the repository with the `git status` subcommand:
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	boulder_dem.py

nothing added to commit but untracked files present (use "git add" to track)
```
Let's parse this output.
`git` displays helpful information about the state of the repository,
including:

- the current *branch*
- whether the current branch is synchronized with the *origin* repository
- the presence of a file that isn't in the repository
- instruction for how to include this new file in the repository

Two new concepts have been introduced here.
A *branch* is a pointer to a location in the history of the repository.
Think of `git` branches as analogous to alternate history fiction,
like *The Plot Against America* by Philip Roth
or *The Yiddish Policemen's Union* by Michael Chabon:
branches have a common history,
but at one point they diverge and develop their own histories.
The *origin* is the repository from which the current repository was cloned.
The origin is an instance of a *remote* repository,
in contrast the to *local* repository on your computer.
We'll discuss branches and remotes in more detail later.

The file exists in the filesystem of our computer,
but it hasn't been included in the repository.
Doing so is a two-step process.
First,
use `git add`:
```
$ git add boulder_dem.py
```
Check the result of this command with `git status`:
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   boulder_dem.py

```
The repository is now aware of this new file.
It has been placed in the *staging area* of the repository,
a place to gather changes to the repository before finalizing them.

The second step is to *commit* this file to the repository
with `git commit`:
```
$ git commit boulder_dem.py -m "Add example file to the repository"
[master 91695d3] Add example file to the repository
 1 file changed, 35 insertions(+)
 create mode 100644 boulder_dem.py
```
When committing a change to a repository,
it's a best practice to include a message
(here, using the `m` option)
describing why the change is being made.
It's also a convention to use imperative case.
Check the result with `git status`:
```
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```
The file is now a part of this local repository.
The working directory has no unknown files,
and the staging area is empty.
Note that `git` tells us that our local repository
now differs from the remote repository.


## Make changes to the repository

Open the file **boulder_dem.py** in a text editor:
```
$ nano boulder_dem.py
```
Looking over the code,
note that the *jet* colormap is used to visualize the sample topographic data:
```python
elev = ax.imshow(data, cmap="jet")
```
There's a [long](https://aip.scitation.org/doi/abs/10.1063/1.4822401)
[history](https://www.computer.org/csdl/magazine/cg/2007/02/mcg2007020014/13rRUxYrbOE)
of research on how "rainbow" color tables can alter the perception
of scientific visualizations.
Let's exchange this colormap for a more modern
[sequential colormap](https://matplotlib.org/3.3.0/tutorials/colors/colormaps.html#sequential) from matplotlib:
```python
elev = ax.imshow(data, cmap="viridis")
```
Save the file and exit the text editor.

Now that we've changed the file,
check on the state of the repository with `git status`:
```
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   boulder_dem.py

no changes added to commit (use "git add" and/or "git commit -a")
```


View the changes to the file with `git diff`:
```
$ git diff boulder_dem.py
diff --git a/boulder_dem.py b/boulder_dem.py
index 593d344..3bd2294 100644
--- a/boulder_dem.py
+++ b/boulder_dem.py
@@ -18,7 +18,7 @@ def read():

 def display(data, show=False, outfile="boulder_dem.png"):
     fig, ax = plt.subplots()
-    elev = ax.imshow(data, cmap="jet")
+    elev = ax.imshow(data, cmap="viridis")
     fig.colorbar(elev, label="Elevation (m)")
     plt.title("Boulder Topography")

```

Commit the change to the file with `git commit`:
```
$ git commit boulder_dem.py -m "Use viridis colormap for display"
[master 63f3a84] Use viridis colormap for display
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```
Notice here that we bypassed the staging area in favor of committing
directly to the repository.


## Push changes to GitHub

Our local repository now differs from the remote on GitHub.

View the history of revisions to the repository with `git log`:
```
$ git log
commit 63f3a8465cfe77d1880c8d3a739e46a1fee14741 (HEAD -> master)
Author: Mark Piper <mark.piper@colorado.edu>
Date:   Fri Aug 7 16:26:06 2020 -0600

    Use viridis colormap for display

commit 91695d3d9efca80ccc74c838702c276d59f9ef07
Author: Mark Piper <mark.piper@colorado.edu>
Date:   Fri Aug 7 12:37:02 2020 -0600

    Add example file to the repository

commit c04e85cf227e81ce3939da822a2c617e663383b3 (origin/master, origin/HEAD)
Author: Mark Piper <mark.piper@colorado.edu>
Date:   Thu Aug 6 15:34:27 2020 -0600

    Initial commit
```

Let's now transmit the changes from our local repository to the remote.
We do this with the `git push` subcommand,
which has the syntax `git push [remote] [branch]`.
Here,
the remote is `origin`
and the branch is `master`.
Therefore, push the changes with:
```
$ git push origin master
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 998 bytes | 499.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/mdpiper/espin-example
   c04e85c..63f3a84  master -> master
```
Note that in order to push changes to a remote,
you must have write access on the remote.

Go to GitHub to see what your repository looks like now!


## Summary

This example provides about 80 percent of what you need to know
about using `git` and GitHub
(with fewer than 20 percent of the available `git` subcommands,
defying Pareto's principle!).

This table summarizes `git` concepts covered in this section:

| Concept      | Description
| ------------ | -----------
| repository   | a storage area for files where history is tracked by version control
| branch       | a pointer to a timeline of commits to a repository
| origin       | the repository from which your local repository is cloned
| local        | the clone of a repository that resides on your computer
| remote       | a clone of a repository that's not on your computer
| staging area | the gathering place for files to be committed to a repository
| commit       | a change made to the content of a repository under version control


This table summarizes the `git` subcommands used in this section:

| Subcommand | Description
| ---------- | -----------
| clone      | clone a repository into a new directory
| status     | display current state of a repository
| add        | stage a change to a repository
| commit     | finalize a change to a repository
| log        | show commit history in repository
| diff       | show differences between working directory and repository state
| push       | transfer changes from one clone of a repository to another


<a name="git-fn1">1</a>: The catch here is that none of these are necessarily single-user projects;
all could involve collaboration.
In fact,
it may be best to think of any single-user project as a simple case
of a collaborative project.
We'll cover collaborative projects next.

___

[Introduction to version control](./index.md) |
Previous: [Configuring git and GitHub](./configuring-git.md) |
Next: [Version control in a collaborative project](./git-collaborative-project.md)
