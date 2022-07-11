# Testing in Python

_Python Bootcamp for Data week 3: Testing in Python with Pytest_

This is week 3 (out of 4) of the Python Bootcamp for Data. The whole course has four weeks:

- [Week 1: Introduction to Python](https://github.com/alfredodeza/introduction-to-python)
- [Week 2: Python Functions and Classes](https://github.com/alfredodeza/python-functions-and-classes)
- [Week 3: Testing In Python](https://github.com/alfredodeza/python-testing/)
- [Week 4: Introduction to Pandas and Numpy](https://github.com/alfredodeza/pandas-and-numpy)

# Table of Contents

- [📚 Course Content](#week-3-content)
- [🎯Learning Objectives](#learning-objectives)
- [💡 Useful Resources](#useful-resources)

# Week 3 Content

1. [Testing Conventions](./notebooks/lesson1/testing-conventions.ipynb)
1. [Testing with Python](./notebooks/lesson1/testing-with-pytest.ipynb)
1. [Test Classes and parametrizing](./notebooks/lesson2/)
1. [Failure output and Fixtures](./notebooks/lesson3/)

## Learning Objectives

In this week you will learn to:

- Understand the basics of testing and its importance
- Write and run tests with functions and classes
- Use Pytest for running and creating tests

## Excuses

If you are wondering about why test at all, first you should know about some common excuses:


<details>
  <summary>It takes too much time</summary>

  It isn't that it takes _too much time_, but it does take time. What takes more time than testing is debugging what went wrong
  and ensuring nothing broke with the latest change.
</details>

<details>
  <summary>It is too difficult</summary>

  Like almost anything, it takes practice to make progress. Take the time to understand what makes a good test, and why slow tests aren't that good. It is better to know that a window in your house is broken than a test that tells you that your house has some undefined problem somehwere.
</details>

<details>
  <summary>We don't have bugs</summary>

  Eventually, all software has bugs. And it is better to fix a bug once, not twice. A test will help you understand what and how it broke, and give you confidence on the fix.
</details>


## Why test at all

If it doesn't work, who do we blame? The customer?

If you are releasing software, do you wait until a user finds a problem? The idea of testing is primarily to increase _confidence_.

Software tends to grow, dependencies change, and almost all engineers will forget about some crucial part of their software at some point. If you are making sure that a change is doing what is supposed to be doing, imagine having 30 steps to verify it all works.

You will miss a step if you need 30 steps to verify everything works.

# Useful Resources

- [Week 1: Introduction to Python](https://github.com/alfredodeza/introduction-to-python)
- [Week 2: Python Functions and Classes](https://github.com/alfredodeza/python-functions-and-classes)
- [Week 3: Testing In Python](https://github.com/alfredodeza/python-testing/)
- [Week 4: Introduction to Pandas and Numpy](https://github.com/alfredodeza/pandas-and-numpy)
- [Python dictionaries Learn Module](https://docs.microsoft.com/learn/modules/python-dictionaries/?WT.mc_id=academic-0000-alfredodeza)
- [Testing In Python book](https://learning.oreilly.com/library/view/testing-in-python/97986PAIML/)
- [Minimal Python book](https://www.amazon.com/Minimal-Python-efficient-programmer-onemillion2021-ebook/dp/B0855NSRR7)
- [Free Azure Certification for Students](https://docs.microsoft.com/learn/certifications/student-training-and-certification?WT.mc_id=academic-0000-alfredodeza)
- [Python for Beginners Learn Path](https://docs.microsoft.com/learn/paths/beginner-python/?WT.mc_id=academic-0000-alfredodeza)
