# Solution for Advent of Code 2019

## Installation
I've developed in a `conda` environment. Use `freeze.txt` to recreate that environment.

I've also used the test runners in PyCharm, so `pytest` is nice to use. I've added the `.idea`-folder so 
that test setups has come along. 

## Running tests
simply run 
```
$ pytest --doctest-modules
```
in your terminal, in the root location. Or run in PyCharm.
All test scripts are functions named `test` in some way, so the test runner will find them.
There are some doctests as well, but the flag to `pytest` will make sure it finds them all!
 

## Running solutions
The files called `runner` gives the right answers. Run them.  With 
```
$ python dayXX\runner.py
```
or similar.
