# pyv

On the fly Python virtualenv management for scripts.

## tl;dr

1) Put `pyv` in your `PATH`.

2) Put the requirements for a script `foo.py` in a file `foo.pyv`.

3) Run your script using `pyv` instead of `python`.

## Motivation

Python has a large collection of useful software libraries, via
[pypi][]. For packaging a large application, there
are numerous solutions for dealing with dependencies. But these can be
a bit cumbersome to deal with if all you're trying to do is write a
short script and share it with others.

A common case is [requests][]. If you're not using it for HTTP
requests in Python, you probably should. (Or at least give it a look.)
But it's not in the Python standard library. Which means that if I
have the following in my Python script:

```
import requests
```

Someone running it is likely to get the error:

```
ModuleNotFoundError: No module named 'requests'
```

For a while I dealt with this, for cases in which I didn't want to
deal with real packaging, by just including a comment saying something
like `# use requests virtualenv`. But that's a bit of a barrier,
esp. if I'm sharing it with someone who's not that familiar with
Python, and now I need to go on a tangent explaining virtual
environments.

`pyv` allows you to specify the dependency on requests in a separate
file (which admittedly is similar to what you would do with
`setup.py`), but then the user only needs to execute your script using
`pyv`, rather than `python`, and everything else is automatic. No need
to deal with any packaging, by either the developer or the end user.

Admittedly, this does require a one-time setup of putting `pyv` in
your `PATH`. Which could potentially be a bigger hurdle than trying to
explain virtual environments.

## Prereqs

* [virtualenv][] **is** required

* [virtualenvwrapper][] is **not** required

* Put `pyv` in your `PATH`

## Usage

### Writing a script

Write your script `foo.py`, but you don't have to stick to the Python standard
library. Use any packages available in [pypi][] that you want.

Create a file `foo.pyv` that lists your requirements, and put it in the same
dir as `foo.py`. You can use version [PEP 440][]-compliant version range
specifiers (e.g. `requests>=2.21.0,>2.22`), but you can also just specify the
package name (e.g. `requests`), if you just want the latest. Just as if you
were writing a `setup.py` file and creating a package for your script. But you
don't need to bother with the packaging.

### Running a script

Please the `pyv` script anywhere in your `PATH` (suggestions include `~/bin/`
or `/usr/local/bin`), and make sure it's executable (e.g. `chmod +x pyv` if
necessary on a UNIX-like system).

Run your Python script as you normally would, but instead of `python`, use
`pyv`. For example:

    pyv myscript.py arg1 arg2

This will create a Python virtualenv as needed, with your requirements
installed, in `.pyv/myscript`. Whatever Python executable is valid at the time
you initially create the virtualenv will be respected as long as the
virtualenv exists. This allows you to, for example, use [pyenv][] to change
Python the version to whatever you want, and it will persist for the running
of that script.

To update the dependencies within the virtualenv (e.g. if you change your
requirements file, or if you have an open ended version and want to update to
the latest), use `pyv -u`. (This will **not** change the Python version.)

To completely recreate the virtualenv from scratch, use `pyv -r`. (This
**will** change the Python version if applicable.)

If you need to explicitly point to the Python executable (e.g. if you don't
have [pyenv][] installed and want to explicitly reference `python3`), use `-p`
_`python-exe`_. This can point to either a short name, or a complete name
including full path.

For a complete usage statement, use `pyv -h`.

<!-- links -->

[pypi]: https://pypi.org/
[PEP 440]: https://www.python.org/dev/peps/pep-0440/
[pyenv]: https://github.com/pyenv/pyenv
[requests]: https://pypi.org/project/requests/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/
