# EECS 4413 Project Frontend

This frontend is made in [Flask](https://flask.palletsprojects.com/en/stable/), though all I really do with it is return the pages in `templates/` with a few value substitutions.

This application works with the backend at [ahopk127/eecs4413-api](https://github.com/ahopk127/eecs4413-api/).

## Set up the Virtual Environment

You only need to do this once.

Run this commands in a terminal inside the same directory as this code.

Windows:
```
python -m venv .venv
.venv\Scripts\activate
pip install Flask
```

Unix:
```
python -m venv .venv
.venv\Scripts\activate
pip install Flask
```

## Executing

Windows:
```
.venv\Scripts\activate
python -m flask run
```

Unix:
```
. .venv/bin/activate
python -m flask run
```

The site will be at http://localhost:5000
