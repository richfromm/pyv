# pyv

On the fly Python virtualenv management for scripts.

## tl;dr

1) Put `pyv` in your `PATH`.

2) Put the requirements for a script `foo.py` in a file `foo.pyv`.

3) Run your script using `pyv` instead of `python`.

## Motivation

I'll add this later. I promise.

## Usage

### Writing a script

Write your script `foo.py`, but you don't have to stick to the Python standard
library. Use any packages available in [pypi](https://pypi.org/) that you want.

Create a file `foo.pyv` that lists your requirements, and put it in the same
dir as `foo.py`. You can use version
[PEP 440](https://www.python.org/dev/peps/pep-0440/)-compliant version range
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
virtualenv exists. This allows you to, for example, use
[pyenv](https://github.com/pyenv/pyenv) to change Python the version to
whatever you want, and it will persist for the running of that script.

To update the dependencies within the virtualenv (e.g. if you change your
requirements file, or if you have an open ended version and want to update to
the latest), use `pyv -u`. (This will **not** change the Python version.)

To completely recreate the virtualenv from scratch, use `pyv -r`. (This
**will** change the Python version if applicable.)

For a complete usage statement, use `pyv --help`.
