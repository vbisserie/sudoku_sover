Sudoku Solver
==============

This project create an endpoint that solve sudoku. In this first version, input is an array 9*9 and number to discover are just empty.
In a second version this endpoint will be able to receive a photo.

Getting started:

    - docker-compose build api
    - docker-compose up api
    
There is at least one endpoint by default: `http://localhost:5000/api/v1/ping`

To run tests:

    - docker-compose run --rm shell "pytest /srv/app/tests"
