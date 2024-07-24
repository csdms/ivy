![Ivy logo](https://raw.githubusercontent.com/csdms/project/main/assets/CSDMS-logo-color-tagline-hor.png)

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

The Ivy repository uses CI: https://github.com/csdms/ivy/actions.
The original Actions configuration file, [test.yml](../../.github/workflows/test.yml),
used for the Ivy repository looks like:
```yaml
name: Test

on: [push, pull_request]

jobs:

  test:
    if:
      github.event_name == 'push' ||
      github.event.pull_request.head.repo.full_name != github.repository

    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ["3.9", "3.10", "3.11", "3.12"]

    runs-on: ${{ matrix.os }}

    defaults:
      run:
        shell: bash -l {0}

    steps:
      - uses: actions/checkout@v4
      - uses: conda-incubator/setup-miniconda@v3
        with:
          python-version: "${{ matrix.python-version }}"
          miniforge-variant: Mambaforge
          miniforge-version: latest

      - name: Install nox
        run: pip install nox

      - name: Test
        run: nox -s test

  test-notebooks:

    if:
      github.event_name == 'push' ||
      github.event.pull_request.head.repo.full_name != github.repository

    name: Test the notebooks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: conda-incubator/setup-miniconda@v3
        with:
          python-version: "3.11"
          miniforge-variant: Mambaforge
          miniforge-version: latest

      - name: Install nox
        run: pip install nox

      - name: Test
        env:
          MPLBACKEND: "Agg"
          OPENTOPOGRAPHY_API_KEY: ${{ secrets.OPENTOPOGRAPHY_API_KEY }}
        run: nox -s test-notebooks --python "3.11"
```

In this configuration file,
we instruct Actions to run the *test* and *test-notebooks* jobs on Linux, macOS, and Windows,
for a set of Python versions,
but only on pushes and external pull requests to the repository.
If anything fails in this process,
Actions stops and issues an error message.

Check the [history of runs](https://github.com/csdms/ivy/actions/workflows/test.yml) of the *test* and *test-notebooks* jobs on the Ivy repository.

For more comprehensive examples of Actions configuration files,
including multiple jobs,
see, e.g., [landlab](https://github.com/landlab/landlab/tree/master/.github/workflows),
[babelizer](https://github.com/csdms/babelizer/tree/develop/.github/workflows), and
[bmi-example-python](https://github.com/csdms/bmi-example-python/tree/master/.github/workflows).


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


___

[Best Practices in Software Development](./index.md) |
Previous: [Unit testing with pytest](./unit-testing.md)
Next: [Collaborative projects ("Gitiquette")](./collaboration-etiquette.md)
