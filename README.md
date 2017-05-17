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


## Solve a sudoku
### As an array
To solve a sudoku as an array, send a POST request to `http://localhost:5000/api/v1/solve`.
Request shall have following header:

    - Content-Type: application/json

Request shall have following parameter:

    - "array": a 9x9 array of integers except for unknown values (use 'null' for them). Exemple :
                    "array": [
                        [2, null, 7, null, null, 5, null, 6, null],
                        [null, null, null, 6, null, null, null, 1, 2],
                        [null, null, 6, null, 1, null, null, null, null],
                        [7, null, null, null, null, 2, null, null, null],
                        [4, 8, null, null, null, null, null, 9, 1],
                        [null, null, null, 8, null, null, null, null, 5],
                        [null, null, null, null, 3, null, 8, null, null],
                        [8, 7, null, null, null, 9, null, null, null],
                        [null, 9, null, 5, null, null, 3, null, 4]
                    ]