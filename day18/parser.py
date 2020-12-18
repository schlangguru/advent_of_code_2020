from typing import Tuple, List
import itertools
import re


OPERAND = re.compile(r"\d+")
OPERATOR = re.compile("[+*]")
OPEN_PARAN = re.compile(r"\(")
CLOSE_PARAN = re.compile(r"\)")

def parse_expression(expr: str):
    expr = list(expr.replace(' ', ''))
    tokens = []
    while t := extract_token(expr):
        token = t[0]
        rest = t[1]

        tokens.append(token)
        expr = rest

    return build_ast(tokens)


def extract_token(seq: List[chr]) -> Tuple[str, List[chr]]:
    if not seq:
        return None

    token = ""
    if seq[0].isnumeric():
        token = token.join(itertools.takewhile(str.isnumeric, seq))
        rest = seq[len(token):]
    else:
        token = seq[0]
        rest = seq[1:]

    return (token, rest)


def build_ast(tokens: List[str]) -> List:
    ast = []
    while tokens:
        token = tokens.pop(0)
        if OPEN_PARAN.fullmatch(token):
            ast.append(build_ast(tokens))
        elif CLOSE_PARAN.fullmatch(token):
            return ast
        elif OPERATOR.fullmatch(token):
            ast.append(token)
        elif OPERAND.fullmatch(token):
            ast.append(int(token))
        else:
            raise Exception(f"Invalid token '{token}'")

    return ast
