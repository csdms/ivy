![Ivy logo](https://raw.githubusercontent.com/csdms/project/main/assets/CSDMS-logo-color-tagline-hor.png)

# Anaconda and conda

One feature of Python that makes it a great language for science
is its abundance of packages (numpy! scipy! pandas! xarray! landlab!).
Package management can be difficult, though,
especially when a typical Python installation may contain dozens of packages.

This is where the `conda` *package manager* is handy,
and a primary reason why CSDMS uses (and we recommend)
the [Anaconda Distribution](https://www.anaconda.com/products/distribution).

*Learning objectives:*

* Learn what a package manager is, and why it's useful
* Understand what a virtual environment is
* Execute basic `conda` commands to set up a vitual environment

## Conda

With `conda`, you can:

* install
* list
* update
* remove

packages from a Python installation.
`conda` ensures that the packages work together without conflict.

Because much of our work with Ivy takes place
on [EarthscapeHub](https://csdms.colorado.edu/wiki/JupyterHub),
we don't spend much time on `conda` here;
however,
we recommend installing Anaconda on your computer
so that you can use all of the CSDMS Ivy course material locally.

Further,
to ensure you have all the correct packages needed to use the course material,
we ask that you set up a *virtual environment*,
an independent, isolated, Python installation managed by `conda`.
To do so,
we'll need an *environment file* from the Ivy repository.

In a terminal,
change to the Ivy repository directory and view the file **environment.yaml** with `cat`:
```
# A conda environment file for the CSDMS Ivy lessons.
#
# This file is used to create the `ivy` environment on Linux, macOS, and
# Windows. See "environment.unix.yaml" for additional packages that aren't
# available on Windows.
#
# Usage:
#   $ conda env create --file environment.yaml
#   $ conda activate ivy

name: ivy
channels:
  - conda-forge
dependencies:
  - python >=3.9
  - bmi-topography
  - bmipy
  - imageio
  - landlab >=2.5
  - matplotlib
  - notebook
  - numpy
  - pandas
  - pip
  - pymt >=1.3
  - pymt_child
  - pymt_hydrotrend
  - rasterio
  - scipy
  - terrainbento
  - tqdm
  - nox
  - pip:
    - git+https://github.com/csdms/bmi-example-python.git
```

The environment file lists the packages needed to run the course material.
If a package has a dependency not explicitly listed
(e.g., `pymt` is built on `xarray`),
`conda` finds a compatible package version for you.

To create the environment, type:
```
$ conda env create --file environment.yaml
```

Once the environment has been created, type
```
$ conda activate ivy
```
to make this environment current.
(Note on Linux and macOS,
you may have to use `source` instead of `conda` to activate the environment.)

Some packages used in Ivy aren't built for Windows.
These packages have been listed in a second environment file,
**environment.unix.yaml**.
To update the `ivy` environment on Linux or macOS
with these packages, type:
```
$ conda env update --name ivy --file environment.unix.yaml --prune
```

Later,
when finished using the environment, type
```
$ conda deactivate
```
to return to the base environment,
and
```
$ conda remove -n ivy --all
```
to fully remove the environment and all its packages from your Anaconda installation.

### Mamba

`mamba` is a drop-in replacement for `conda`.
It supports most `conda` commands,
and it's typically faster,
since it reimplements the slower parts of `conda` in C++.
Learn more about `mamba`
at its [GitHub repository](https://github.com/mamba-org/mamba)
and through its [documentation](https://mamba.readthedocs.io).

## Summary

While Python is installed with most operating systems,
or can be downloaded and installed from source,
CSDMS recommends the use of Anaconda
because of its `conda` package management system.

This table summarizes `conda` concepts covered in this section:

| Concept      | Description
| ------------ | -----------
| package manager | a tool for managing Python packages, ensuring compatibility
| environment  | an independent, isolated Python installation managed by `conda`
| environment file | a file specifying the packages that make a `conda` environment

This table summarizes the `conda` subcommands used in this section:

| Subcommand | Description
| ---------- | -----------
| list       | lists all packages installed in an environment
| create     | make a new environment from a file
| install    | adds a new package into an environment
| remove     | uninstalls a package from an environment
| update     | gets newer versions of packages in an environment

This table summarizes shell commands used in this section:

| Command      | Description
| ------------ | -----------
| source       | runs a script on a Unix-based operating system


## Resources

* The `conda` [User guide](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html); in particular, the section on [managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* A `conda` command [cheatsheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf) from Anaconda
