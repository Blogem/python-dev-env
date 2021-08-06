# python-dev-env
This repository contains a description and resources to set up a Python development environment on Mac. It should translate fairly straight forward to Windows.

## VS Code
Install VS Code from https://code.visualstudio.com/download.

Install the following extensions:
- Python
- Pylance

Optional:
- A Python docstring generator

Enable settings sync (command palette (`shift + command + P`) &#8594; settings sync).

## Poetry
For managing dependent libraries and packaging. More in the [docs](https://python-poetry.org/docs/).

### Installation and configuration
Install per the instructions in the docs.

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Updating is also possible:
```
poetry self update
```

Set the .venv to be in the project folder.
```
poetry config virtualenvs.in-project true
```

You can also view the config:
```
poetry config --list
```


### Creating a new project
You can now either create a new project folder:
```
poetry new python-dev-env
```

Or initialize an existing directory (beware: this only creates the `pyproject.toml`, but does not create the directory structure and such):
```
cd python-dev-env
poetry init
```

Adding new dependencies can be done by directly editing `pyproject.toml` or with the following command:
```
poetry add [package name]
```

(Remove them using `poetry remove [package name]`.)

Create or using the virtual environment:
```
poetry shell
```
(You can also use regular `source .venv/bin/activate`.)

You install the dependencies using:
```
poetry install
```

Which creates or reuses the `poetry.lock` file, that you commit to Git. This file pins the versions of dependencies. If you want to update to the latest versions, run `poetry update`.

Running your script is done using:
```
poetry run python python_dev_env/hello_world.py
```

### Packaging
Run
```
poetry build
```

## Linting and formatting

Go to the VS code settings (`command + ,`), search for `python.linting` and enable the following linters:
- mypy (typechecking, [cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html))
- flake8 (linting, [docs](https://flake8.pycqa.org/en/latest/user/index.html))
- pydocstyle (checking docstring)

Search for `python.formatting` and select `black` as the provider. Run `format document` on a script and install when prompted.

## Logging

Add structlog

```
poetry add structlog
poetry install
```

## Testing

Add pytest

```
poetry add pytest
poetry install
```

Discover tests via the command palette, enable the pytest test framework and select the directory containing the tests (`tests`).