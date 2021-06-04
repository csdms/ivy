![ESPIn logo](./media/ESPIn2021.png)

# ESPIn

The Earth Surface Processes Institute (ESPIn),
held 2021 June 8-17,
is an immersive online training experience
for 25 graduate students, postdoctoral fellows, and early career faculty.
ESPIn is designed to help participants make advances
in earth surface processes research
by teaching cyberinfrastructure skills in numerical modeling,
best programming practices, open source software development,
and collaborative coding.


## Topics

The full ESPIn 2021 schedule is [here][espin-schedule].
Topics covered include:

| Topic | Run on...
| ----- | ---------
| [Introduction to the Shell][shell] | local computer
| [Anaconda and conda][conda] | local computer
| [Jupyter Notebook Tutorial][notebook] | [![Run on CSDMS JupyterHub][badge]][gp-notebook]
| [Python Basics][python] | [![Run on CSDMS JupyterHub][badge]][gp-python]
| [Python for ESP Scientists][python] | [![Run on CSDMS JupyterHub][badge]][gp-python]
| [Version Control with git and GitHub][git] | local computer
| [The Basic Model Interface (BMI)][bmi] | [![Run on CSDMS JupyterHub][badge]][gp-bmi]
| [Landlab][landlab] | [![Run on CSDMS JupyterHub][badge]][gp-landlab]
| [The Python Modeling Toolkit (pymt)][pymt] | [![Run on CSDMS JupyterHub][badge]][gp-pymt]
| [Permamodel Toolkit][permamodel] | [![Run on CSDMS JupyterHub][badge]][gp-permamodel]
| [Best Practices in Software Development][best-practices] | local computer


## Requirements

* Laptop
* Web browser
* Internet
* Coffee (optional, but recommended)


## Links

* [Landlab documentation](https://landlab.readthedocs.io)
* [Basic Model Interface (BMI) documentation](https://bmi.readthedocs.io)
* [Babelizer documentation](https://babelizer.readthedocs.io)
* [Python Modeling Toolkit (pymt) documentation](https://pymt.readthedocs.io)
* [Community Surface Dynamics Modeling System (CSDMS)](https://csdms.colorado.edu)


## The ESPIn team

* [Irina Overeem](https://www.colorado.edu/geologicalsciences/irina-overeem)
* [Mark Piper](https://instaar.colorado.edu/people/mark-piper/)
* [Benjamin Campforts](https://instaar.colorado.edu/people/benjamin-campforts/)
* [Nicole Gasparini](https://sse.tulane.edu/eens/faculty/gasparini)
* [Leilani Arthurs](https://www.colorado.edu/geologicalsciences/leilani-arthurs)


ESPIn is a community-focused project;
[contributions](./CONTRIBUTING.rst) that follow
the [contributor code of conduct](./CODE-OF-CONDUCT.rst) are welcomed,
and are [acknowledged](./AUTHORS.rst).
All ESPIn course material is open source,
released under [CC BY 4.0 and MIT licenses](./LICENSE.md).
If you use the ESPIn course material,
please [cite](./CITATION.rst) it.

Portions of the ESPIn shell and Python lessons were derived
from material that is Copyright
[Software Carpentry](http://software-carpentry.org),
and remixed under their [license][swc-license].

ESPIn is supported by the National Science Foundation
under Award Numbers
[1924259](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1924259) and
[1924185](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1924185),
*Cybertraining: Pilot: Collaborative Research:
Cybertraining for Earth Surface Processes Modelers*.


<!-- Links -->

[espin-schedule]: https://docs.google.com/document/d/1fZYIEzfK_MhxnowbXiAVkQG7mUOkwQXaHbUTYAZPuLU/edit?usp=sharing
[badge]: https://img.shields.io/badge/CSDMS-JupyterHub-orange.svg
[shell]: ./lessons/shell/index.md
[conda]: ./lessons/conda/index.md
[notebook]: ./lessons/jupyter/general_jupyter_notebook_tutorial.ipynb
[gp-notebook]: https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=tree%2Fespin%2Flessons%2Fjupyter%2Findex.ipynb&branch=main
[python]: ./lessons/python/index.ipynb
[gp-python]: https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=tree%2Fespin%2Flessons%2Fpython%2Findex.ipynb&branch=main
[git]: ./lessons/git/index.md
[bmi]: ./lessons/bmi/index.ipynb
[gp-bmi]: https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=tree%2Fespin%2Flessons%2Fbmi%2Findex.ipynb&branch=main
[landlab]: ./lessons/landlab/index.ipynb
[gp-landlab]: https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=tree%2Fespin%2Flessons%2Flandlab%2Findex.ipynb&branch=main
[pymt]: ./lessons/pymt/index.ipynb
[gp-pymt]: https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=tree%2Fespin%2Flessons%2Fpymt%2Findex.ipynb&branch=main
[permamodel]: ./lessons/permamodel
[gp-permamodel]: https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=tree%2Fespin%2Flessons%2Fpermamodel&branch=main
[best-practices]: ./lessons/best-practices/index.md
[swc-license]: https://github.com/swcarpentry/python-novice-inflammation/blob/gh-pages/LICENSE.md
