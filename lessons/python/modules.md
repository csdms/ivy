<a href="https://csdms.colorado.edu"><img style="float: center; width: 75%" src="https://raw.githubusercontent.com/csdms/ivy/main/media/logo.png"></a>

# Modules, scripts, and the basics of packaging

Jupyter Notebooks can get you a long way,
but to really advance your Python (and scientific programming) skills,
you'll need to write source code in modules.
A *module* is a file containing Python statements and definitions.
It uses the `.py` extension.
The module name is the filename.

Code from a module can be imported
into an interactive Python session, a notebook, or even other modules,
just as we have with NumPy or Matplotlib functions.
Code in a module can be executed from a shell prompt as a *script*.

A group of modules can be bound together as a *package*.
Packages are the most effective way to share Python code.

Because packages can be installed into an environment,
path considerations aren't an issue.
(More on this below.)
Code from an installed package can be run at any location on a filesystem.
The NumPy and Matplotlib libraries are packages.

Let's start by creating a module
from the diffusion code we set up in the [functions](./functions.ipynb) lesson.

## Modules

Modules are defined as files on the filesystem,
not in notebooks.

Start by opening a terminal and making a new directory `ivy_diffusion`,
in your home directory.
```
$ mkdir ~/ivy_diffusion
```

Change info this directory
and start a new module file `solver.py`.
```
$ cd ~/ivy_diffusion
$ touch solver.py
```

Your directory structure should look like this:
```
ivy_diffusion
└── solver.py
```

Next,
open `solver.py` in a text editor.
Copy all of the imports and functions from the [functions](./functions.ipynb) notebook
into `solver.py`.

It should look like this:

~~~
"""A solver for the one-dimensional diffusion equation."""
import numpy as np

np.set_printoptions(precision=1, floatmode="fixed")


def calculate_time_step(grid_spacing, diffusivity):
    return grid_spacing**2 / diffusivity / 2.1


def set_initial_profile(domain_size=100, boundary_left=500, boundary_right=0):
    concentration = np.empty(domain_size)
    concentration[: int(domain_size / 2)] = boundary_left
    concentration[int(domain_size / 2) :] = boundary_right
    return concentration


def solve1d(concentration, grid_spacing=1.0, time_step=1.0, diffusivity=1.0):
    """Solve the one-dimensional diffusion equation with fixed boundary conditions.

    Parameters
    ----------
    concentration : ndarray
        The quantity being diffused.
    grid_spacing : float (optional)
        Distance between grid nodes.
    time_step : float (optional)
        Time step.
    diffusivity : float (optional)
        Diffusivity.

    Returns
    -------
    result : ndarray
        The concentration after a time step.

    Examples
    --------
    >>> import numpy as np
    >>> from solver import solve1d
    >>> z = np.zeros(5)
    >>> z[2] = 5
    >>> solve1d(z, diffusivity=0.25)
    array([   0.0,    1.2,    2.5,    1.2,    0.0])
    """
    flux = -diffusivity * np.diff(concentration) / grid_spacing
    concentration[1:-1] -= time_step * np.diff(flux) / grid_spacing


def diffusion_example():
    """An example of using `solve1d` in a diffusion problem."""
    print(diffusion_example.__doc__)
    D = 100  # diffusivity
    Lx = 10  # domain length
    dx = 0.5  # grid spacing

    dt = calculate_time_step(dx, D)
    C = set_initial_profile(Lx)

    print("Time = 0\n", C)
    for t in range(1, 5):
        solve1d(C, dx, dt, D)
        print(f"Time = {t*dt:.4f}\n", C)
~~~

(You can instead copy/paste the above, if you wish.)

By convention,
imports are listed at the beginning of the module,
and there are two blank lines between definitions.
One extra decoration--a module docstring--has been added at the top of the file.

Before continuing,
be sure to save the file `solver.py` in your text editor.


### Scripts

With a text editor,
add the following code to the bottom of module file `solver.py`.
~~~
if __name__ == "__main__":
    diffusion_example()
~~~
This is an example of a main program.

Calling the `solver` module as a script
executes the main program.
```
$ python solver.py
An example of using `solve1d` in a diffusion problem.
Time = 0
 [500.0 500.0 500.0 500.0 500.0   0.0   0.0   0.0   0.0   0.0]
Time = 0.0012
 [500.0 500.0 500.0 500.0 261.9 238.1   0.0   0.0   0.0   0.0]
Time = 0.0024
 [500.0 500.0 500.0 386.6 363.9 136.1 113.4   0.0   0.0   0.0]
Time = 0.0036
 [500.0 500.0 446.0 429.8 266.2 233.8  70.2  54.0   0.0   0.0]
Time = 0.0048
 [500.0 474.3 464.0 359.6 328.7 171.3 140.4  36.0  25.7   0.0]
```

Scripts are handy!

Typically used to run an example that demonstrates the code in a module.

### Importing code from a module

We can now import code from `solver.py` into a Python session.

First, because we'll need NumPy, make sure you're in the `ivy` environment.
```
$ source activate ivy
```

Now,
from your `ivy_diffusion` directory,
start a Python session
and attempt to import the `solve1d` function from the `solver` module.
```
>>> from solver import solve1d
>>> solve1d
<function solve1d at 0x105845300>
```
We successfully imported the function.
Exit the Python session (`Ctrl-D` or `exit()`),

Next,
change to your home directory
and start another Python session.
Again,
try to import the `solve1d` function.
```
>>> from ivy_diffusion.solver import solve1d
>>> solve1d
<function solve1d at 0x103495300>
```
This also works.
Exit the Python session (`Ctrl-D` or `exit()`),

Last,
change to an arbitrary location on your filesystem;
e.g.,
```
mkdir -p ~/tmp && cd ~/tmp
```
Start a Python session and try to import the `solve1d` function.
```
>>> from ..ivy_diffusion.solver import solve1d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: attempted relative import with no known parent package
```
Look at the error message:
because of the change in path,
there's no way to get to the `solver` module.

One way to address this is by modifying Python's path,
but this isn't a good idea because it's not portable and doesn't scale well.

A better solution is packaging.

## Packaging

What is a package?

Configure a directory structure for the package.
```
$ mkdir ~/ivy-diffusion && cd ~/ivy-diffusion
$ mv ivy_diffusion .
$ touch pyproject.toml
```
Note the hyphen in the top directory.

Your directory structure should look like this:
```
ivy-diffusion
├── pyproject.toml
└── ivy_diffusion
    └── solver.py
```
(This directory structure is ready to become a `git` repository.)

A bare minimum `pyproject.toml` file.
~~~
[build-system]
requires = [
    "setuptools",
    "wheel",
    ]
build-backend = "setuptools.build_meta"

[project]
name = "ivy-diffusion"
version = "0.1"
~~~


Install the `ivy-diffusion` package into the `ivy` environment with:
```
pip install -e .
```

Once the package is installed,
you can start a Python interpreter from anywhere on your file system
and import definitions from the packaged `solver` module.
```
>>> from ivy_diffusion.solver import solve1d, diffusion_example
```


## Summary

The [Modules](https://docs.python.org/3/tutorial/modules.html) section
of the Python documentation was used to write this lesson.

While this lesson introduces the basics of packaging,
there's much more to learn,
and the best place to look for more information
is the [Python Packaging User Guide](https://packaging.python.org/).

Build and upload packaged code to PyPI for others to use.
