![Ivy logo](https://raw.githubusercontent.com/csdms/project/main/assets/CSDMS-logo-color-tagline-hor.png)

# Collaborative projects ("Gitiquette")

This lesson describes some recommended<sup>[1](#cp-fn1)</sup> best practices
for working on a collaborative project.

## Issues

1. Use issues. A good issue should describe a problem. If an error is thrown,
  the text of the error message should be included. Don't screenshot the
  error--it's not searchable, and the text of the error can't be copy/pasted
  easily.

1. A reproduce case should be provided for the issue, showing the steps
  that lead up to the error.

1. Don't suggest a solution in the issue write-up, but if you have a
  solution in mind, it's helpful to describe it in a comment. The
  repository owner gets to make the final decision on what solution
  should be implemented.

1. Avoid responding to GitHub issues by email--it
  obscures the context of the issue and adds extra
  text to the thread on GitHub.

## Branches

1. Create a new branch to make any changes to source code. Avoid
  working on the default branch, if possible.

1. Before making changes to an existing branch, always check its state
  on your local repository and pull down changes from the remote, if
  necessary.

## Tests

1. Write new tests to address any changes you make. Don't remove old
  tests; if necessary, modify them, e.g., if the changes aren't
  backward compatible. Any new code added shouldn't cause old tests to
  fail.

1. Don't check in code unless it has tests, and the tests pass.

1. Make tests that are as simple as possible, and only cover the
  changes made. This can be difficult, but the payoff is that you
  know exactly what the problem is when the test fails.

1. Writing good tests is a learned skill. It takes time.

## Pull requests

1. When you've finished making changes, and all your tests pass, make
  a pull request back to the
  upstream repository. Be sure to argue your case in your pull
  request! You have to convince the repository owner that your
  proposed changes will improve their code.

1. It's a good idea to request a reviewer on a pull request.

1. It's good to review the the test results from continuous integration on each
  pull request, even when successful.

1. If you're the repository owner, only merge pull requests when all
  tests pass. The default branch of a repository should always be clean and working.

## Python distribution

1. Avoid using the system Python on a computer. It's usually a dependency for other operating system tools, which makes it hard to update. For stability, it's also often a few releases behind the current version.

1. Instead, use a pre-packaged scientific Python distribution with a built-in package manager. We use Anaconda at CSDMS.

1. Further, rather than the full install, use a smaller base install, such as through [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [miniforge](https://github.com/conda-forge/miniforge).

1. Create environments to install custom sets of packages; e.g., for testing. Environments are designed to be ephemeral, trash them when you're done.

1. Don't mix packages from different `conda` channels. They may not be ABI-compatible.

1. Tools installed with the operating system, like `git` or `make`, may also be out of date and hard to update. They can be installed through `conda`.

## General

1. Avoid including data (input or output) in a source code repository. There's some gray area for data
  used in an example, but the data should be small.

1. If a function takes up more than one screen, it may be too long. Consider factoring it into smaller programs.

1. Build scientific visualizations programmatically, ideally using an open source language or, secondarily, a scriptable open source visualization tool.

1. Don't alter a visualization manually (e.g., using commercial software such as Adobe Illustrator) after creating it. This breaks reproducibility.

1. Don't use ChatGPT. It provides answer-shaped objects, not answers. Use collected wisdom sites like Stack Overflow instead.

1. Software isn't finished until it has tests and documentation.

1. Write code for your future self.

If you have a suggestion for a best practice,
please submit it as an [issue](https://github.com/csdms/ivy/issues)
to the Ivy repository!


## Summary

Working on a collaborative project is more complicated
that working alone,
but following a few simple rules can make things go more smoothly.
If all else fails, just remember: be kind.


## Resources

* A [short note](https://github.com/codeforamerica/howto/blob/master/Good-GitHub-Issues.md) on writing a good issue (from [Code for America](https://www.codeforamerica.org/)!)
* A GitHub [blog post](https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/) on writing a good pull request


<a name="cp-fn1">1</a>: Many of these recommendations are
the result of mistakes I've made. *--MP*

___

[Best Practices in Software Development](./index.md) |
Previous: [Continuous integration](./continuous-integration.md)
Next: [FAIR practices for research software](./fair-practices.md)
