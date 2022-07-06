# mindset-BE

## How to run

## Set up your virtual environment

First set up the virtual environment and activating it by running these two commands in your terminal.

```
python3 -m venv .venv
. .venv/bin/activate
```

NOTE: This project uses Poetry to track dependencies, please have that installed using the follow command:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

After you have set this up in the root of the project, you can run the following command to install the dependencies:

```
poetry install
```

If everything went well, you can start the server by running the following command:

```
flask run
```

Go to http://127.0.0.1:5000/ in your browser to see the results.
