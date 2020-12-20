from typing import TypeVar, List, Dict

Rule = TypeVar("Rule", List[List[int]], str)


class RuleMatcher():

    def __init__(self, rules: Dict[int, Rule]):
        self.rules = rules


    def match(self, message: str) -> bool:
        return any(msg == "" for msg in self._match_terminal(self.rules[0], message))


    def _match_terminal(self, rule: Rule, message: str) -> str:
        if type(rule) is list:
            yield from self._match_any(rule, message)
        else:
            if message and message[0] == rule:
                yield message[1:]


    def _match_any(self, rule: Rule, message: str) -> str:
        for branch in rule:
            yield from self._match_all(branch, message)


    def _match_all(self, rule: List[int], message: str) -> str:
        if not rule:
            yield message
        else:
            [rule_ref, *rest] = rule
            for substring in self._match_terminal(self.rules[rule_ref], message):
                yield from self._match_all(rest, substring)

