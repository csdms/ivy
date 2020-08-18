![ESPIn logo](../../media/ESPIn.png)

# Continuous integration with Travis CI

*Continuous integration* (CI) is a software engineering practice
where people working together on a project frequently merge their work.
An automated system then builds and tests the changes,
ensuring that they work together.

CSDMS uses the continuous integration service Travis CI (https://travis-ci.org).
What this means in practice is that 
every time a pull request is submitted to a repository,
the actions designated in the Travis CI configuration file are performed.
While this varies from project to project,
it typically includes building and testing the software in the pull request
on Linux, macOS, and Windows.

The ESPIn repository is under CI: https://travis-ci.org/github/csdms/espin.
The Travis CI configuration file ([.travis.yml](../../.travis.yml))
used for the ESPIn repository is:
```yaml
language: python

os:
  - linux

install:
  - pip install pytest coverage

before_script:
  - test -d ./lessons/best-practices
  - test -f ./lessons/best-practices/examples.py
  - test -f ./lessons/best-practices/test_examples.py

script:
  - coverage run -m pytest

after_success:
  - coverage report
```
In this configuration file,
we instruct Travis to perform the build on Linux
(it's easy and quick)
using its default Python distribution.
We have very little code to test in the ESPIn repository<sup>[1](#ci-fn1)</sup>,
but we do have the unit testing example from the previous section.
Use `pip` to install the *pytest* and *coverage* packages
into the default Python installation.
Run `pytest` and `coverage` from the root of the repository,
checking beforehand that the sample files exist.
Afterward,
view the coverage report.
If anything fails in this process,
Travis CI stops and issues an error message.

The first build of the ESPIn repository is available
on [Travis CI](https://travis-ci.org/github/csdms/espin/builds/718488184).
Success!

For more comprehensive examples of Travis CI configuration files,
see, e.g., [pymt](https://github.com/csdms/pymt/blob/master/.travis.yml),
[babelizer](https://github.com/csdms/babelizer/blob/develop/.travis.yml), and
[bmi-example-c](https://github.com/csdms/bmi-example-c/blob/master/.travis.yml).


## Summary

Continuous integration is used in team projects
to help keep local repositories synchronized across the team.
It's useful even in individual projects, though,
because it can be configured to build, test, and run a project
on each push or pull request to a repository,
alerting a developer when a build or a test fails.


## Resources

* A (long, detailed) [blog post](https://martinfowler.com/articles/continuousIntegration.html) on CI by Martin Fowler (father of "refactoring")
* Travis CI [documentation](https://docs.travis-ci.com/)


<a name="ci-fn1">1</a>: There's code in the Jupyter Notebooks that can
be tested, but this hasn't been set up yet.

___

[Best Practices in Software Development](./index.md) |
Previous: [Unit testing with pytest](./unit-testing.md)
Next: [Collaborative projects ("Gitiquette")](./collaboration-etiquette.md)
