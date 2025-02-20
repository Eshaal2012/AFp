class ArithmeticExpression:
    def __init__(self, expression):
        self.expression = expression

    def calculate(self):
        try:
            result = self.evaluate_expression(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"

    def evaluate_expression(self, expr):
        return eval(expr)  

def main():
    expr = input("Enter an arithmetic expression to solve: ")
    solver = ArithmeticExpression(expr)
    result = solver.calculate()
    print(f"The result of the expression '{expr}' is: {result}")

if __name__ == "__main__":
    main()