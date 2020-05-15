# Tests

[Русский](../ru/tests.md) | **English**

### Dependencies

* [pip3](https://github.com/pypa/pip)
* [Python 3.7](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

For testing, the Coverage library is used.  To run the tests, run the command in the [web](../../src/web) folder.

     coverage run --source='.' manage.py test the-app-you-want-to-test

This **command** will fill a **“.coverage”**, located in **COVERAGE_FILE** and then you may see results or report. 
If you need to remove gathered data, execute:

    coverage erase

If you want to show the results in the **command line**, run:

    coverage report

For more readable **reports**:

    coverage html

To know concretely what part of your **code** is covered by **tests**, use:

    coverage annotate -d directory-where-to-put-annotated-files

It will generate same source code file with an additional syntax on it:
* Line with "**>**" means it was **executed**
* Line beginning with "**!**" means it was **not executed**
* Line starting with "**-**" means the line was **excluded** in the **coverage statistics**