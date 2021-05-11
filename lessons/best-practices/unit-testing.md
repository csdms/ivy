![ESPIn logo](https://github.com/csdms/espin/blob/main/media/ESPIn2021.png)

# Unit testing with pytest

The practice of *unit testing* is this:
when you write code,
for every unit of software
(function, subprogram, class) you create,
you also write tests that ensure the software behaves as expected.
Writing good tests is a learned skill; it takes time.
However, with unit testing
you'll likely save time and energy in the long run
by identifying problems before they become serious.


## Why unit testing?

It takes time to learn how to write unit tests.
It takes time to write the tests themselves.
Why should you,
a busy ESP scientist,
want to use unit testing as a part of your work?
Here are some reasons why:

* Models are software, and every piece of code you write should have
  tests to ensure it produces expected results.
* People may be relying on the software you write. Stop bugs before
  they happen by writing tests.
* You're probably writing code to analyze data for your thesis, or for
  a journal article. Write tests to check that the code is performing
  the analyses correctly.
* Reviews on paper come back with requested revisions. When you modify
  code to make those revisions, testing lets you know if you broke
  anything.
* Testing is a job skill. Not everyone has a job in academia; knowing
  unit testing is a useful skill if you take a job in software or data
  science.
* Testing is a productivity tool! This may seem counterintuitive,
  since there's always additional work in testing, but it also gives
  you the confidence to explore and try things, knowing that your
  tests will let you know if you break anything.
* Testing can make a team more efficient because untested, and
  possibly faulty, code can be caught before it's checked in to a repository.
* Testing can provide metrics of success to a funding agency; e.g.,
  the reliability of code produced on a project as measured through
  coverage statistics.


## The pytest testing framework

There are several unit testing frameworks available in Python;
e.g., `nose`, `pytest`, `unittest`, `lettuce`.
At CSDMS, we use `pytest`.

`pytest` recursively searches a path for Python files
that have "test" in their filename.
It attempts to run any functions in these files that have "test" in their name.
A simple example of using `pytest` is included
in the [lessons/best-practices](./) directory.
The module **examples.py** contains the function *squareit*:
```python
def squareit(number):
    return number*number
```

The module **test_examples.py** includes one function,
*test_squareit*,
that defines a unit test for the example function:
```python
from examples import squareit


def test_squareit():
    assert squareit(5) == 25
```
Note that the *assert* statement evaluates to `True` or `False`.
A `True` result indicates the test passes.

Starting in the **lessons/best-practices** directory,
run `pytest` with:
```
$ pytest -v
=============================== test session starts ================================
platform darwin -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- /Users/mpiper/anaconda3/envs/espin/bin/python
cachedir: .pytest_cache
rootdir: /Users/mpiper/projects/espin/lessons/best-practices
collected 1 item

test_examples.py::test_squareit PASSED                                       [100%]

================================ 1 passed in 0.02s =================================
```
`pytest` generates a report showing that the test passes.

*Code coverage* tools measure how much of a unit of code
is evaluated by its tests.
The coverage is expressed as a fraction of the total amount of code in the unit.
In Python,
the `coverage` package is used for code coverage.
Run `pytest` and `coverage` together to generate coverage statistics:
```
$ coverage run -m pytest
=============================== test session starts ================================
platform darwin -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/mpiper/projects/espin/lessons/best-practices
collected 1 item

test_examples.py .                                                           [100%]

================================ 1 passed in 0.01s =================================
```

Once statistics are generated, `coverage` can display a text report:
```
$ coverage report
Name               Stmts   Miss  Cover
--------------------------------------
examples.py            2      0   100%
test_examples.py       3      0   100%
--------------------------------------
TOTAL                  5      0   100%
```
and also an HTML report:
```
$ coverage html
```
which you can find at [htmlcov/index.html](./htmlcov/index.html).

It's important to note that while
a coverage score of 100% is the goal for any project,
the number itself isn't that important;
it simply gives a developer a guide
for where more testing can be done.


### A question, a challenge

What would happen when a string is passed to `squareit`?
Could you devise a test to catch this,
then use it to suggest an improvement to `squareit`?


## Summary

Every unit of code you write should include a test
to ensure it behaves as expected.
Unit testing may impose a cost in the short run,
but in the long run,
time and effort will likely be saved
by exposing problems in your code before they become serious.

This table summarizes unit testing concepts covered in this section:

| Concept       | Description
| ------------- | -----------
| unit test     | code that checks whether another element of code produces the expected result
| code coverage | the amount of code evaluated by unit tests, expressed as a fraction of the total lines of code in a unit of software

This table summarizes the unit testing subcommands used in this section:

| Command  | Description
| -------- | -----------
| pytest   | runs `pytest` on available unit tests
| coverage | runs `coverage` to generate code coverage stats for unit tests


## Resources

* Software Carpentry Incubator [lesson](http://carpentries-incubator.github.io/python-testing/) on unit testing and continuous integration (in development)
* [*Code Complete*](https://wikipedia.org/wiki/Code_Complete) is a
  comprehensive reference for all aspects of software development;
  it includes a section on unit testing
* `pytest` [documentation](https://docs.pytest.org) 
* [Clune and Rood (2011)](../../media/clune2011software.pdf) provide a case study on how unit testing helped a NASA project
* [Ministry of Testing](https://ministryoftesting.com) is an online
  resource for software test engineers

___

[Best Practices in Software Development](./index.md) |
Previous: [index](./index.md) |
Next: [Continuous integration with Travis CI](./continuous-integration.md)
