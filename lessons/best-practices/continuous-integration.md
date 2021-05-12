![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Continuous integration with GitHub Actions

*Continuous integration* (CI) is a software engineering practice often used
where people working together on a project frequently merge their work.
An automated system then builds and tests the changes,
ensuring that they work together.

CSDMS uses the continuous integration service [GitHub Actions](https://docs.github.com/en/actions).
What this means in practice is that 
every time a pull request is submitted to a repository,
the jobs designated in the GitHub Actions configuration file(s) are performed.
While this varies from project to project,
it typically includes building and testing the software in the pull request
on Linux, macOS, and Windows.

The ESPIn repository is under CI: https://github.com/csdms/espin/actions.
The Actions configuration file ([test.yml](../../.github/workflows/test.yml))
used for the ESPIn repository is:
```yaml
name: Test

on: [push, pull_request]

jobs:

  test:
    # We want to run on external PRs, but not on our own internal PRs as they'll be run
    # by the push to the branch. Without this if check, checks are duplicated since
    # internal PRs match both the push and pull_request events.
    if:
      github.event_name == 'push' ||
      github.event.pull_request.head.repo.full_name != github.repository

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2

      - name: Install dependencies
        run: pip install pytest coverage

      - name: Test for files
        run: |
          test -d ./lessons/best-practices
          test -f ./lessons/best-practices/examples.py
          test -f ./lessons/best-practices/test_examples.py

      - name: Run pytest and coverage
        run: coverage run -m pytest

      - name: Show coverage report
        run: coverage report
```
In this configuration file,
we instruct Actions to run the "test" job on Linux,
only on pushes and external pull requests to the repository,
using a default Python distribution.
We have very little code to test in the ESPIn repository<sup>[1](#ci-fn1)</sup>,
but we do have the unit testing example from the previous section.
Use `pip` to install the *pytest* and *coverage* packages
into the default Python distribution.
Run `pytest` and `coverage` from the root of the repository,
checking beforehand that the sample files exist.
Afterward,
view the coverage report.
If anything fails in this process,
Actions stops and issues an error message.

The first run of the "test" job on the ESPIn repository
is [available](https://github.com/csdms/espin/runs/2558250304?check_suite_focus=true)
on GitHub.
Success!

For more comprehensive examples of Actions configuration files,
including multiple jobs,
see, e.g., [pymt](https://github.com/csdms/pymt/tree/master/.github/workflows),
[babelizer](https://github.com/csdms/babelizer/tree/develop/.github/workflows), and
[bmi-example-c](https://github.com/csdms/bmi-example-c/blob/master/.github/workflows/conda-and-cmake.yml).


## Summary

Continuous integration is used in team projects
to help keep local repositories synchronized across the team.
It's useful even in individual projects, though,
because it can be configured to build, test, and run a project
on each push or pull request to a repository,
alerting a developer when a build or a test fails.


## Resources

* A (long, detailed) [blog post](https://martinfowler.com/articles/continuousIntegration.html) on CI by Martin Fowler (father of "refactoring")
* GitHub Actions [documentation](https://docs.github.com/en/actions)


<a name="ci-fn1">1</a>: There's code in the Jupyter Notebooks that can
be tested, but this hasn't been set up yet.

___

[Best Practices in Software Development](./index.md) |
Previous: [Unit testing with pytest](./unit-testing.md)
Next: [Collaborative projects ("Gitiquette")](./collaboration-etiquette.md)
