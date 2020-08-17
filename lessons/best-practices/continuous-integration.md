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

First build here: https://travis-ci.org/github/csdms/espin/builds/718488184.
Success!


For more comprehensive examples of Travis CI configuration files,
see, e.g., pymt, babelizer, bmi-example-python, bmi-example-c,
and bmi-example-fortran.


## Summary

Concepts table.

* continuous integration


## Resources

* A (long, detailed) [blog post](https://martinfowler.com/articles/continuousIntegration.html) on CI by Martin Fowler (father of "refactoring")
* Travis CI [documentation](https://docs.travis-ci.com/)


___

[Best Practices in Software Development](./index.md) |
Previous: [Unit testing with pytest](./unit-testing.md)
Next: [Collaborative projects ("Gitiquette")](./collaboration-etiquette.md)
