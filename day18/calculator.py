from typing import Tuple, List
from operator import add, mul

from parser import parse_expression


class Calculator():

    OPERATIONS = {
        '+': add,
        '*': mul
    }


    def eval(self, expr: str) -> int:
        return self._calc(parse_expression(expr))


    def _calc(self, ast) -> int:
        if type(ast) is int:
            return ast
        elif type(ast) == list and len(ast) == 1:
            return self._calc(*ast)
        else:
            right = ast.pop()
            operator = ast.pop()
            left = ast

            return self.OPERATIONS[operator](self._calc(left), self._calc(right))


