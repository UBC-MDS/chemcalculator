# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/UBC-MDS/chemcalculator or email to `kingslin@student.ubc.ca <kingslin@student.ubc.ca>` if you do not have a GitHub account.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

chemcalculator could always use more documentation, whether as part of the
official chemcalculator docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/UBC-MDS/chemcalculator/issues. Otherwise, email to `kingslin@student.ubc.ca <kingslin@student.ubc.ca>` is the alternative. 

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute?

In general, we ask you to follow the GitHub Flow workflow.

Here's how to set up chemcalculator for local development.
1. If you don't have a GitHub, you would need to create one and you would need to install Git for the following steps.
2. Fork the `chemcalculator` repo on GitHub.
3. Clone your fork locally::
```
    $ git clone git@github.com:your_name_here/chemcalculator.git
```
4. Install your local copy (it is recommended to do this with a virtual environment). The method of installation will depend on the packaging library being used.
   For example, if `setuptools` is being used (a setup.py file is present), install chemcalculator with:

```
    $ python setup.py install
```
   If `poetry` is being used (poetry.lock and pyproject.toml files are present), install chemcalculator with:

```
       $ poetry install
```
5. Create a branch for local development and make your changes locally::
```
    $ git checkout -b name-of-your-bugfix-or-feature
```
6. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.
   For example, if the package uses the poetry package management library, black formatting style and pytest for testing::
```
    $ poetry run black chemcalculator
    $ poetry run pytest
```
7. Commit your changes and push your branch to GitHub::
```
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
```
8. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

Code of Conduct
---------------
Please note that the chemcalculator project is released with a Contributor Code of Conduct. By contributing to this project you agree to abide by its terms.
