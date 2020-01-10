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
usage: page-loader [-h] [--output OUTPUT] [--log-level {INFO,DEBUG}] webpage

Page loader

positional arguments:
  webpage

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT       set output dir
  --log-level {INFO,DEBUG}
```

## Downloading simple webpage

``` bash
page-loader --output . http://example.com
```

[![asciicast](https://asciinema.org/a/CNIZ4DO7kT0wNqTcm3QbMybTe.svg)](https://asciinema.org/a/CNIZ4DO7kT0wNqTcm3QbMybTe)

## Downloading webpage with local resources

``` bash
page-loader --output /tmp/ https://ru.hexlet.io/courses
```

[![asciicast](https://asciinema.org/a/Xk6o4tNfi5VQyLKtpqQzrbzhk.svg)](https://asciinema.org/a/Xk6o4tNfi5VQyLKtpqQzrbzhk)

## Downloadig webpage with local resources and DEBUG mode

``` bash
page-loader --output /tmp/ --log-level DEBUG https://ru.hexlet.io/courses
```

[![asciicast](https://asciinema.org/a/PvfKaog7eyr5dbiEifmdvwLz3.svg)](https://asciinema.org/a/PvfKaog7eyr5dbiEifmdvwLz3)
