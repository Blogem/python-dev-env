# python-dev-env
This document describes how to setup a up a Python development environment on macOS. The environment can be used to develop most Python projects, including Azure Functions. The instructions should translate fairly straight forward to Windows.

It uses:
- VS Code with extensions as IDE
- pyenv to manage Python versions
- Poetry for package management
- mypy for typechecking
- flake8 for linting
- black as code formatter
- pytest for testing

The document assumes you have Homebrew installed.

## VS Code
Install [VS Code](https://code.visualstudio.com/download).

Install the following extensions:
- Python
- Pylance

Optional:
- A Python docstring generator
- Azure Functions

Enable settings sync (command palette (`shift + command + P`) &#8594; settings sync).

## pyenv
Often it is necessary to use a specific Python version. This can be achieved by using [pyenv](https://github.com/pyenv/pyenv).

### Installation
```
brew update
brew install pyenv
```

### Using pyenv
- Install a specific version: `pyenv install 3.10.3`
- Set as global version: `pyenv global 3.10.3`
- Set shell-specific version: `pyenv shell 3.10.3`
- See available versions: `pyenv versions`
- Help: `pyenv help`

## Poetry
For managing dependent libraries and packaging. More in the [docs](https://python-poetry.org/docs/).

### Installation and configuration
- Install per the instructions in the docs
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
- Updating 
```
poetry self update
```
- Set the .venv to be in the project folder
```
poetry config virtualenvs.in-project true
```
- View the config
```
poetry config --list
```

### Creating a new project
You can now either create a new project folder:
```
poetry new python-dev-env
```

Or initialize an existing directory:
```
cd python-dev-env
poetry init
```

This only creates the `pyproject.toml`, but does not create the directory structure and such. Useful for projects that won't be packaged and only require dependency management.

### Installing packages

- Adding new dependencies can be done by directly editing `pyproject.toml` or with the following command:
```
poetry add [package name]
```
- Removing a package:
```
poetry remove [package name]
```
- Install packages to be used in the development environment only:
```
poetry add [package name] -D
```

## Generating requirements.txt
For compatibility with pip, a `requirements.txt` can be generated with the pinned versions. Azure Functions rely on a `requirements.txt` to be there.
```
poetry export -f requirements.txt --output requirements.txt
```

To automate this process you can create `.git/hooks/pre-commit` with the following contents:
```
#!/bin/sh
#
#  .git/hooks/pre-commit
#

poetry export --without-hashes --output requirements.txt
git add requirements.txt
```

### Create or use the virtual environment
```
poetry shell
```

(You can also use regular `source .venv/bin/activate` if you have an existing `.venv`.)

Install the dependencies: 
```
poetry install
```

This creates or reuses the `poetry.lock` file, that you commit to Git. This file pins the versions of dependencies. If you want to update to the latest versions, run `poetry update`.

### Packaging
Run `poetry build`

## Linting and formatting

Go to the VS code settings (`command + ,`), search for `python.linting` and enable the following linters:
- mypy (typechecking, [cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html))
- flake8 (linting, [docs](https://flake8.pycqa.org/en/latest/user/index.html))
- Optional: pydocstyle (checking docstring)

Search for `python.formatting` and select `black` as the provider. Run `format document` on a script and install when prompted.

## Security

*TODO:* add `bandit` and `safety` for static code scanning

## Testing

Install pytest: 
```
poetry add pytest -D
```

Discover tests via the VS Code command palette, enable the pytest test framework and select the directory containing the tests (`tests`).
