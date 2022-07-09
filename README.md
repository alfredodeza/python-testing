# Testing in Python

_Python Bootcamp for Data week 3: Testing in Python with Pytest_

This is week 3 of the Python Bootcamp for Data.


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
