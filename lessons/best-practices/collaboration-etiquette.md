![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Collaborative projects ("Gitiquette")

This lesson describes some best practices
for working on a collaborative project<sup>[1](#cp-fn1)</sup>.

When working on a collaborative project,
the following workflow is recommended:

1. issue
1. fork
1. branch
1. commit
1. test
1. pull request
1. merge

Based on this workflow, some recommendations:

* A good issue should describe the problem. If an error is thrown, the
  text of the error message should be included. Don't screenshot the
  error--it's not searchable, and the text of the error can't be
  copy/pasted easily.
  
* A reproduce case should be provided for the issue, showing the steps
  that lead up to the error.

* Don't suggest a solution in the issue write-up, but if you have a
  solution in mind, it's helpful to describe it in a comment. The
  repository owner gets to make the final decision on what solution
  should be implemented.

* Create a new branch to make any changes to the source code. Avoid
  working on the default branch, if possible.

* Before making changes to an existing branch, always check its state
  on your local repository and pull down changes from the remote, if
  necessary.

* Write new tests to address any changes you make. Don't remove old
  tests; if necessary, modify them, e.g., if the changes aren't
  backward compatible. Any new code added shouldn't cause old tests to
  fail.

* Don't check in code unless it has tests, and the tests pass.

* Make tests that are as simple as possible, and only cover only the
  changes made. This can be difficult, but the payoff is that you
  know exactly what the problem is when the test fails.

* Writing good tests is a learned skill. It takes time.

* When you've finished making changes, and all your tests pass, make
  a pull request from your branch back to the default branch of the
  upstream repository. Be sure to argue your case in your pull
  request! You have to convince the repository owner that your
  proposed changes will improve the repository.

* It's a good idea to request a reviewer on a pull request.

* It's good to review the the test results from Travis CI on each pull
  request, even when successful.

* If you're the repository owner, only merge pull requests when all
  tests pass. The default branch to always be clean and working.

And here are a few recommendations that fall outside the workflow:

* Software isn't finished until it has tests and documentation.
  (Greg Tucker: "Write for your *future self*")

* Avoid including data in a repository. There's some gray area for data
  used in an example, but the data should be small.

* Use conda environments liberally; you can easily set up an
  environment for testing, then discard it when finished

* Avoid responding to GitHub issues and pull requests by email--it
  obscures the context of the issue or pull request, and adds extra
  text to the thread on GitHub.

If you have suggestions for other best practices,
please submit them as an [issue](https://github.com/csdms/espin/issues)
to the ESPIn repository!


## Summary

Working on a collaborative project is more complicated
that working alone,
but following a few simple rules can make things go more smoothly.
If all else fails, just remember: be kind.


## Resources

* A [short note](https://github.com/codeforamerica/howto/blob/master/Good-GitHub-Issues.md) on writing a good issue (from [Code for America](https://www.codeforamerica.org/)!)
* A GitHub [blog post](https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/) on writing a good pull request


<a name="cp-fn1">1</a>: *MP*--Many of these recommended behaviors are
the result of mistakes I've made.

___

[Best Practices in Software Development](./index.md) |
Previous: [Continuous integration with Travis CI](./continuous-integration.md)
