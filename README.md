# python-dev-env
This repository contains a description and resources to set up a Python development environment on Mac. It should translate fairly straight forward to Windows.

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

