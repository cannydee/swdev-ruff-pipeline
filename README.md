GitHub repository with ruff linting pipeline

For this exercise I created a new local git repository with a minimal Python package. The structure of the repository is:

swdev-ruff-pipeline/
- src/mypkg/__init__.py
- src/mypkg/example.py
- requirements.txt
- .github/workflows/lint.yml

The package consists of a single module src/mypkg/example.py that defines a simple add(a, b) function. This is enough to give ruff some code to inspect.

I added a requirements.txt file that contains only one dependency: ruff. In the GitHub Actions workflow lint.yml I set up a job that runs on every push and on every pull request. The job checks out the code, installs Python, installs the dependencies from requirements.txt, and then runs two commands:

1. ruff format --check .     (formatting check)
2. ruff check .              (lint check)

The --check option for ruff format is important, because in a CI pipeline we do not want to modify files automatically. Instead, the command exits with a nonzero status code when formatting is not correct, which makes the pipeline fail. The same is true for ruff check when linting errors are present.

To test that the pipeline really fails on bad code, I first pushed a clean version of example.py and confirmed that the workflow passed. Afterwards, I made a second commit where I intentionally added style problems, an unused import, bad spacing, and removed type hints in example.py. After pushing this commit, the GitHub Actions run failed because ruff format --check and ruff check reported errors.

This shows that the repository now has an automated linting pipeline that enforces ruff formatting and linting rules and rejects commits with bad code.
