![Ivy logo](./media/logo.png)

# CSDMS Ivy

CSDMS Ivy is a collection of modular lessons on
open source software development
and community cyberinfrastructure
written and maintained by the
[Community Surface Dynamics Modeling System ](https://csdms.colorado.edu)(CSDMS).

CSDMS Ivy grew out of an National Science Foundation Cybertraining pilot program,
*Cybertraining: Pilot: Collaborative Research:
Cybertraining for Earth Surface Processes Modelers*
(award numbers
[1924259](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1924259) and
[1924185](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1924185)),
led by [Irina Overeem](https://www.colorado.edu/geologicalsciences/irina-overeem)
with a project team of
[Leilani Arthurs](https://www.colorado.edu/geologicalsciences/leilani-arthurs),
[Benjamin Campforts](https://instaar.colorado.edu/people/benjamin-campforts/),
[Nicole Gasparini](https://sse.tulane.edu/eens/faculty/gasparini), and
[Mark Piper](https://instaar.colorado.edu/people/mark-piper/).


## Lessons

The lessons in CSDMS Ivy are semi-independent.
They can be run locally on a user's computer,
or on the OpenEarthscape JupyterHub.

| Topic | Run on...
| ----- | ---------
| [Introduction to the Shell][shell] | local computer
| [Anaconda and conda][conda] | local computer
| [Jupyter Notebook Tutorial][notebook] | [![Run on CSDMS JupyterHub][badge]][hub-notebook]
| [Python Basics][python] | [![Run on CSDMS JupyterHub][badge]][hub-python]
| [Python for ESP Scientists][python] | [![Run on CSDMS JupyterHub][badge]][hub-python]
| [Version Control with git and GitHub][git] | local computer
| [The Basic Model Interface (BMI)][bmi] | [![Run on CSDMS JupyterHub][badge]][hub-bmi]
| [Landlab][landlab] | [![Run on CSDMS JupyterHub][badge]][hub-landlab]
| [The Python Modeling Toolkit (pymt)][pymt] | [![Run on CSDMS JupyterHub][badge]][hub-pymt]
| [Permamodel Toolkit][permamodel] | [![Run on CSDMS JupyterHub][badge]][hub-permamodel]
| [Best Practices in Software Development][best-practices] | local computer
| [Introduction to Cluster Computing][hpc] | local computer


CSDMS Ivy is a community-focused project;
[contributions](./CONTRIBUTING.rst) that follow
the [contributor code of conduct](./CODE-OF-CONDUCT.rst) are welcomed,
and are [acknowledged](./AUTHORS.rst).
All CSDMS Ivy course material is open source,
released under [CC BY 4.0 and MIT licenses](./LICENSE.md).
If you use the CSDMS Ivy course material,
please [cite](./CITATION.cff) it.

Portions of the CSDMS Ivy shell and Python lessons were derived
from material that is Copyright
[Software Carpentry](http://software-carpentry.org),
and remixed under their [license][swc-license].

CSDMS Ivy is supported with funding from the National Science Foundation.


<!-- Links -->

[badge]: https://img.shields.io/badge/CSDMS-JupyterHub-orange.svg
[shell]: ./lessons/shell/index.md
[conda]: ./lessons/conda/index.md
[notebook]: ./lessons/jupyter/general_jupyter_notebook_tutorial.ipynb
[hub-notebook]: https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fivy&urlpath=lab%2Ftree%2Fivy%2Flessons%2Fjupyter%2Findex.ipynb%3Fautodecode&branch=main
[python]: ./lessons/python/index.ipynb
[hub-python]: https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fivy&urlpath=lab%2Ftree%2Fivy%2Flessons%2Fpython%2Findex.ipynb%3Fautodecode&branch=main
[git]: ./lessons/git/index.md
[bmi]: ./lessons/bmi/index.ipynb
[hub-bmi]: https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fivy&urlpath=lab%2Ftree%2Fivy%2Flessons%2Fbmi%2Findex.ipynb%3Fautodecode&branch=main
[landlab]: ./lessons/landlab/index.ipynb
[hub-landlab]: https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fivy&urlpath=lab%2Ftree%2Fivy%2Flessons%2Flandlab%2Findex.ipynb%3Fautodecode&branch=main
[pymt]: ./lessons/pymt/index.ipynb
[hub-pymt]: https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fivy&urlpath=lab%2Ftree%2Fivy%2Flessons%2Fpymt%2Findex.ipynb%3Fautodecode&branch=main
[permamodel]: ./lessons/permamodel
[hub-permamodel]: https://lab.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fivy&urlpath=lab%2Ftree%2Fivy%2Flessons%2Fpermamodel%3Fautodecode&branch=main
[best-practices]: ./lessons/best-practices/index.md
[hpc]: ./lessons/hpc/index.md
[swc-license]: https://github.com/swcarpentry/python-novice-inflammation/blob/gh-pages/LICENSE.md
