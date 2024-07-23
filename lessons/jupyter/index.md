![Ivy logo](https://raw.githubusercontent.com/csdms/ivy/main/media/logo.png)

# Project Jupyter

<img align="right" width="150" height="150" src="https://jupyter.org/assets/homepage/main-logo.svg">

[Project Jupyter][jupyter] is a non-profit, open-source, community-driven
organization that oversees the development of a software ecosystem
for interactive scientific coding, learning, and discovery.
Project Jupyter grew out of the [IPython project][ipython]
started by Fernando P&eacute;rez as a graduate student in physics
at the University of Colorado Boulder.

In CSDMS Ivy, we'll use three tools from the Project Jupyter ecosystem:
JupyterHub, JupyterLab, and Jupyter Notebook.

## JupyterHub

A [JupyterHub](https://jupyter.org/hub) is a server system
that allows multiple users access to a computational resource,
where each user can run Jupyter Notebook and other software
in their own workspace.
A JupyterHub can be installed in the cloud, on a server, or locally.

Through the NSF-funded [OpenEarthscape][oes] project,
CSDMS provides a [JupyterHub][jhub]
where Ivy course material can be viewed and run.
Click this button:

[![Run on EarthscapeHub][badge]][jhub-link]

to open the lessons directly on the EarthscapeHub *explore* instance!

> **Note:** The EarthscapeHub *explore* instance is password-protected.
  Please contact your instructor about obtaining a login,
  or visit [this][jhub-info] CSDMS wiki page for more information.

## JupyterLab

JupyterLab is a browser-based interactive development environment.
It provides tools for writing code and creating notebooks, including:

- a file browser,
- launchers for notebooks, data files, and images,
- terminal, text editor, and code console applications, and
- keyboard shortcuts to speed your work.

JupyterLab is the default user interface for JupyterHub.
Like JupyterHub, JupyterLab can be installed
in the cloud, on a server, or locally.

Take a few minutes to familiarize yourself with the JupyterLab interface
on EarthscapeHub.

## Jupyter Notebook

A Jupyter Notebook is an interactive document
for writing, explaining, and running code, and for communicating results.

Notebooks are live documents,
with the ability to display tabular data and graphics,
as well as interactive displays with widgets.
A notebook is made of cells.
Each cell can hold code, formatted text (using Markdown), equations,
or visualizations.

To get a sense of their popularity,
by [one estimate](https://github.com/parente/nbestimate/blob/master/estimate.ipynb),
there are currently over 7.5 million notebooks hosted on GitHub.
The estimate is presented, of course, in a notebook.

The majority of the CSDMS Ivy course material is built as notebooks.

## Resources

- [Project Jupyter][jupyter] home
- JupyterHub [documentation][jupyterhub-docs]
- JupyterLab [documentation][jupyterlab-docs] and
  [an entertaining demonstration](https://youtu.be/A5YyoCKxEOU) on YouTube
- Jupyter Notebook [documentation][jupyter-notebook-docs]
- The [first section][swc-ppp-1] of the Software Carpentry
  [Plotting and Programming in Python][swc-ppp] lesson has a great section on
  JupyterLab and Jupyter Notebook
- A collection of [notable Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki)
  and a comprehensive [tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)


<!-- Links, by alpha -->

[badge]: https://img.shields.io/badge/Run%20on-EarthscapeHub-orange
[jhub]: https://explore.openearthscape.org
[jhub-link]: https://explore.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fivy&urlpath=lab%2Ftree%2Fivy%2FREADME.ipynb%3Fautodecode&branch=main
[jhub-info]: https://csdms.colorado.edu/wiki/JupyterHub
[ipython]: https://ipython.org/
[jupyter]: https://jupyter.org/
[jupyterhub-docs]: https://jupyterhub.readthedocs.io
[jupyterlab-docs]: https://jupyterlab.readthedocs.io
[jupyter-notebook-docs]: https://jupyter-notebook.readthedocs.io
[oes]: https://openearthscape.org/
[swc-ppp]: https://swcarpentry.github.io/python-novice-gapminder/
[swc-ppp-1]: https://swcarpentry.github.io/python-novice-gapminder/01-run-quit/index.html
