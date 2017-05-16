# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request

blueprint = Blueprint('index', __name__, url_prefix='/api/v1/')


@blueprint.route("ping")
def health_check():
    return jsonify({'ping': 'pong'})


@blueprint.route("solve", methods=['POST'])
def solve():
    solve_request = request.get_json()

    if not solve_request or type(solve_request) is not dict:
        return jsonify({'error': "Bad request"}), 400

    if "array" in solve_request:
        array = solve_request["array"]
        if len(array) != 9:
            return jsonify({'error': "Array is not correctly formatted"}), 400
        for line in array:
            if len(line) != 9:
                return jsonify({'error': "Array is not correctly formatted"}), 400
        from services.puzzle import Puzzle
        puzzle = Puzzle()
        for x in range(0, 9):
            for y in range(0, 9):
                if type(array[x][y]) is int:
                    puzzle.set_value(x, y, array[x][y])
        if puzzle.solve() is True:
            return jsonify({'status': 'OK'})
    return jsonify({'status': 'NOK'})
