# Page loader

[![Maintainability](https://api.codeclimate.com/v1/badges/48644f081f215379ebad/maintainability)](https://codeclimate.com/github/altvec/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/48644f081f215379ebad/test_coverage)](https://codeclimate.com/github/altvec/python-project-lvl3/test_coverage)
[![Build Status](https://travis-ci.org/altvec/python-project-lvl3.svg?branch=master)](https://travis-ci.org/altvec/python-project-lvl3)

This is a CLI utility for downloading the specified webpage from the Internets.

## Installation

``` bash
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ altvec-page-loader
```

## Usage

``` bash
usage: page-loader [-h] [--output OUTPUT] webpage

Page loader

positional arguments:
  webpage

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  set output dir
```

## Downloading simple webpage

``` bash
page-loader --output . http://example.com
```

[![asciicast](https://asciinema.org/a/CNIZ4DO7kT0wNqTcm3QbMybTe.svg)](https://asciinema.org/a/CNIZ4DO7kT0wNqTcm3QbMybTe)
