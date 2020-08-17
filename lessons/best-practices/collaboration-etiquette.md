![ESPIn logo](../../media/ESPIn.png)

# Collaborative projects ("Gitiquette")

This lesson describes a set of best practices
for working on a collaborative project on GitHub.
(Note from MP: Many of these are things I've learned often as the result of mistakes I've made.)

* Workflow: issue, fork, branch, test, PR, merge
* Create a new branch to make any changes to the source code. Avoid working on the master branch.
* Write new tests for any new functionality added by the changes. Don't remove old tests. If necessary, modify them; e.g., in the case that the changes made aren't backward compatible.
* Run the tests. Make any changes needed to have them pass.
* When the changes are complete and tests passing, make a PR from the branch back to master. Only merge the PR when all tests pass. We want the master branch to always be clean and working.

* Writing issues.
* Proper pull requests.
* Don't merge a PR until it has been reviewed.
* Issue first, then PR to fix issue. Use my wget vs curl problem from day 1 of the course.
* Documentation! (Greg: write for your "future self")
* Software isn't finished until it has tests and documentation.
* Eric: Good issue. Minimum working example, reproduce case.
* Check repo state and pull down changes from remote when starting work.



* Make tests as simple as possible. Make tests that cover only the changes made. These can be kind of hard, but the payoff is that you know exactly what the problem is when the test fails.
* We can't have too many tests!
* Consider using public GitHub repo instead of private GitLab repo so we can see the the test results from Travis CI on each PR.

* For every unit (function, subprogram) of software you write, you also write software tests that ensure the software behaves as expected.
* Don't check in code unless it has tests (MP: think of anecdote)
* Don't check in code unless the tests pass.
* Any new code added to existing must also be tested, and can't cause the old tests to fail.
* Writing good tests is a learned skill.


* Use conda environments! I'll usually have several. Switch between them as needed.




*Show a demo of making issue and proper PR.*


## Summary

Concepts table.

This may just be a list?


## Resources

*


___

[Best Practices in Software Development](./index.md) |
Previous: [Continuoues integration with Travis CI](./continuous-integration.md)
