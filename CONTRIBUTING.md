# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

#### Report Bugs

Report bugs at [here](https://github.com/akloster/freecad_jupyter/issues).

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

#### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

#### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

#### Write Documentation

freecad-jupyter could always use more documentation, whether as part of the
official freecad-jupyter docs, in docstrings, or even on the web in blog posts,
articles, and such.

##### Submit Feedback

The best way to send feedback is to file an [issue](https://github.com/akloster/freecad_jupyter/issues).

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `freecad_jupyter` for local development.

1. Fork the `freecad_jupyter` repo on GitHub.
2. Clone your fork locally::

        $ git clone git@github.com:your_name_here/freecad_jupyter.git

3. Install development dependencies:

        $ cd freecad_jupyter/
        $ pipenv install --dev

4. Create a branch for local development::

        $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

        $ flake8 freecad_jupyter tests
        $ python setup.py test or py.test
        $ tox

    To just run test quickly you can run `python tests/test_freecad_jupyter.py`

6. Commit your changes and push your branch to GitHub::

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7, 3.4, 3.5 and 3.6, and for PyPy. Check
   [Travis test](https://travis-ci.org/akloster/freecad_jupyter/pull_requests)
   and make sure that the tests pass for all supported Python versions.


## Tips

To run a subset of tests:

```batch

    $ python -m unittest tests.test_freecad_jupyter
```

## Deploying


A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.md).
Then run:

```batch
$ bumpversion patch # possible: major / minor / patch
$ git push
$ git push --tags
```

Travis will then deploy to PyPI if tests pass.
