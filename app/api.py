import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


########################### ACTIVIDAD 2 ###################################
@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return (f"{CALCULATOR.multiply(num_1, num_2)}", http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return (f"{CALCULATOR.divide(num_1, num_2)}", http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return (f"{CALCULATOR.power(num_1, num_2)}", http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/sqrt/<op>", methods=["GET"])
def sqrt(op):
    try:
        num = util.convert_to_number(op)
        return (str(CALCULATOR.sqrt(num)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/log10/<op>", methods=["GET"])
def log10(op):
    try:
        num = util.convert_to_number(op)
        return (str(CALCULATOR.log10(num)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
    ###################################################################
