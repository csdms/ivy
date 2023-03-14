![Ivy logo](https://raw.githubusercontent.com/csdms/ivy/main/media/logo.png)

# GitHub authentication

GitHub allows users to connect to remote repositories
through two protocols, HTTPS and SSH.

When using HTTPS,
a user must supply a personal access token (PAT)--a long string of characters--on
every connection attempt.

When using SSH,
GitHub looks for an SSH key cached locally.
An SSH key is a little harder to set up than a PAT,
but easier to use over time.

In this lesson,
we'll cover how to create an SSH key
and add it to your GitHub profile.

## Check for an existing SSH key

Before we create a new SSH key,
let's check if you already have one on your system.
Open a terminal and type
```
$ ls ~/.ssh
```

GitHub supports three types of keys.
If you have a **.ssh** directory with one of these files:

* **id_rsa.pub**
* **id_ecdsa.pub**
* **id_ed25519.pub**

you can skip ahead to the [Add an SSH key to GitHub](./github-authentication.md#add-an-ssh-key-to-github) section.

If you don't have a **.ssh** directory
or one of the three supported key types,
proceed to the next section.

## Create an SSH key

To create a new SSH key,
type the following into a terminal:
```
$ ssh-keygen -t ed25519 -C "YOUR EMAIL"
```
The `-t` flag specifies the type of key to create;
in this case,
using the [ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519) algorithm.
Use the email address associated with your GitHub account,
keeping the quote marks.
Follow the prompts and enter a passphrase for the key.

Check the contents of your **.ssh** directory (which will now exist if it didn't before):
```
$ ls ~/.ssh
id_ed25519      id_ed25519.pub
```
You now have an SSH key pair (private, public).

Remember your passphrase!
You'll have to enter it when connecting to GitHub.
Optionally,
you can use the `ssh-agent` service on your computer to store the password;
GitHub provides [documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent) for doing so.

## Add an SSH key to GitHub

Now that we have an SSH key pair,
we need to add the public key to GitHub.

Start by copying the public key.
Print the key to the terminal with `cat`:
```
$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AA4WC3NzqC45ZD81NTR5AQAAIBbFO9USDsVFLRIiBJ9Y6wJil4AFrW5ysRrGNCd5wDvy mark.piper@colorado.edu
```
then select the text and copy it.

Next, go to https://github.com/settings/keys.
(If you aren't signed in to GitHub,
you'll be prompted to do so.)

In the "SSH keys" section,
click the *New SSH key* button.
In the resulting form,
you can name your key
and paste in the key text.

That's it!

## Test your SSH key

To check that GitHub has your SSH key, type the following in a terminal:
```
$ ssh -T git@github.com
```
You'll be prompted to enter the passphrase for your key.

If you get a return like
```
Hi mdpiper! You've successfully authenticated, but GitHub does not provide shell access.
```
you're all set!

## Summary

Github requires either a personal access token (PAT)
or an SSH key
to connect to remote repositories.
Here,
we describe how to create and add an SSH key to GitHub.

___

[Introduction to version control](./index.md) |
Previous: [Configuring git](./configuring-git.md)
Next: [A version control workflow](./git-workflow.md)
