![ESPIn logo](../../media/ESPIn.png)

# Collaborative projects ("Gitiquette")

This lesson describes a set of best practices
for working on a collaborative project<sup>[1](#cp-fn1)</sup>.

First, a generic workflow for contributing to a collaborative project:

1. issue
1. fork
1. branch
1. test
1. pull request
1. merge

Next, a list of suggested best practices:

* A good issue should describe the problem. If an error is thrown, the
  text of the error message should be included. A reproduce case
  should also be provided, showing the steps that lead up to the
  error.  Don't suggest a solution in the issue write-up. This can be
  done as a suggestion in a comment, if desired.

* Create a new branch to make any changes to the source code. Avoid
  working on the default branch, if possible.
* Before making changes to an existing branch, always check its state
  on your local repository and pull down changes from the remote, if
  necessary.

* Write new tests to address any changes you make. Don't remove old
  tests. If necessary, modify them; e.g., in the case that the changes
  made aren't backward compatible. Any new code added can't cause old
  tests to fail.
* Don't check in code unless it has tests. Don't check in code unless
  the tests pass.
* Make tests as simple as possible. Make tests that cover only the
  changes made. These can be kind of hard, but the payoff is that you
  know exactly what the problem is when the test fails.
* Writing good tests is a learned skill. It takes time!
* We can't have too many tests!


* When the changes are complete and tests passing, make a PR from the branch back to the default branch. (Proper pull requests.) Only merge the PR when all tests pass. We want the default branch to always be clean and working.
* Don't merge a PR until it has been reviewed.

* See the the test results from Travis CI on each PR.

* Use conda environments! I'll usually have several. Switch between them as needed.
* Software isn't finished until it has tests and documentation. (Greg: write for your "future self")

Last, a demonstration of performing this workflow.

Use my `wget` vs `curl` problem from day 1 of the course.
Make an issue and create a PR.


## Summary



## Resources

* Writing a good issue: https://github.com/codeforamerica/howto/blob/master/Good-GitHub-Issues.md
* Writing a good PR: https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/


<a name="cp-fn1">1</a>: *MP:* Many of these recommended behaviors are
things I've learned as the result of mistakes I've made.

___

[Best Practices in Software Development](./index.md) |
Previous: [Continuoues integration with Travis CI](./continuous-integration.md)
