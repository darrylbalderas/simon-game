# simon-game

Python package for playing the game [Simon](https://en.wikipedia.org/wiki/Simon_(game))

## Table of Contents
1. [Motivation](#motivation)
2. [Installation](#installation)
2. [Create python package](#package)

## Motivation<a name="motivation"></a>


## Installation<a name="installation"></a>

- Create a python3 virtual environment

    `python3 -m venv ./venv`

- Start virtual environment

    `source venv/bin/activate`

- Stop virtual environment

    `deactivate`

- Install project dependencies 

    > (virtual env must be started to install dependencies)
     
    `pip install -r requirements.txt`

## Create python package<a name="package"></a>

* Install twine and create distribution folder

```
pip install twine
python setup.py sdist
```

* Upload to the pypi test repository

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ simon_game
```

* Upload to the pypi repository

```
twine upload dist/*
pip install simon_game
```
