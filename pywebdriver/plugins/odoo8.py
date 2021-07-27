###############################################################################
#
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
#   @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from flask import jsonify, make_response, request

from pywebdriver import app, drivers


@app.route("/hw_proxy/hello", methods=["GET"])
def hello_http():
    return make_response("ping")


@app.route("/hw_proxy/handshake", methods=["POST", "GET", "PUT"])
def handshake_json():
    return jsonify(jsonrpc="2.0", result=True)


@app.route("/hw_proxy/status_json", methods=["POST", "GET", "PUT"])
def status_json():
    statuses = {}
    params = request.json["params"]
    for driver in drivers:
        statuses[driver] = drivers[driver].get_status(**params)
    return jsonify(jsonrpc="2.0", result=statuses)


@app.route("/hw_proxy/log", methods=["POST", "GET", "PUT"])
def log_json():
    arguments = request.json["params"]["arguments"]
    print(" ".join(str(v) for v in arguments))
    return jsonify(jsonrpc="2.0", result=True)
