import math
import app


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    ################ ACTIVIDAD 2 ####################################
    #Se agregan las funciones de la raíz cuadrada y logaritmo base 10
    def sqrt(self, x):
        self.check_type(x)
        if x < 0:
            raise TypeError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(x)

    def log10(self, x):
        self.check_type(x)
        if x <= 0:
            raise TypeError("El logaritmo en base 10 solo está definido para números positivos")
        return math.log10(x)
    
    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("El parámetro debe ser un número")    
    ####################################################################

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
