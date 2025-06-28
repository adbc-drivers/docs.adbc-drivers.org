# docs.adbc-drivers.org

This site is built using [Sphinx](https://sphinx-doc.org).

## Building

## Pre-requisites

- Python

## Steps

```sh
# optionally, create a venv first
python -m pip install -r requirements.txt
make html
```

To view the output, you can run,

```sh
python -m http.server -d _build/html
```

and open your web browser to <https://localhost:8000>.
