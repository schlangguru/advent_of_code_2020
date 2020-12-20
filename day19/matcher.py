from typing import TypeVar, List, Dict

Rule = TypeVar("Rule", List[List[int]], str)


class RuleMatcher():

    def __init__(self, rules: Dict[int, Rule]):
        self.rules = rules


    def matches_rule(self, message: str) -> bool:
        msg = list(message)
        result = self._matches_rule(self.rules[0], msg)
        return result and len(msg) == 0


    def _matches_rule(self, rule: Rule, message: List[chr]) -> bool:
        if type(rule) is str:
            c = message.pop(0)
            return c == rule
        else:
            result = False
            match_count = 0
            for sub_rules in rule:
                msg = message.copy()
                and_result = True
                for sub_rule in sub_rules:
                    and_result = and_result and self._matches_rule(self.rules[sub_rule], msg)
                result = result or and_result
                match_count = max(match_count, len(message) - len(msg))

            if result:
                for _ in range(match_count):
                    message.pop(0)

            return result


