from typing import List, Union, Optional, Dict


class DTCommand(object):
    def __init__(self, command: str, action: str):
        self.command = command
        self.action = action

    @staticmethod
    def dict_to_commands(values: Dict) -> List['DTCommand']:
        return [DTCommand(**v) for _, v in values.items()]


class DTChoice(object):
    def __init__(self, verb: Union[List[str], str], node: str):
        self.verb = verb
        self.node = node

    @staticmethod
    def dict_to_choices(values: Dict) -> List['DTChoice']:
        return [DTChoice(**v) for _, v in values.items()]


class DTExpr(object):
    def __init__(self, expression: str):
        new_expr = expression.replace(' ', '\t')
        parts = new_expr.split('\t')
        if len(parts) < 3:
            raise ValueError('expression must be in the form of (variable operator operand)')
        self.variable = parts[0]
        self.operator = parts[1]
        self.operand = parts[2]

    @staticmethod
    def to_expressions(expr: Union[List[str], str]) -> List['DTExpr']:
        return [DTExpr(ex) for ex in expr] if isinstance(expr, List) else [DTExpr(expr)]


class DTCondition(object):
    def __init__(self, condition: Union[List[str], str], node: str, default: bool):
        self.condition = [DTExpr(c) for c in condition] if isinstance(condition, List) else [DTExpr(condition)]
        self.node = node
        self.default = default

    @staticmethod
    def dict_to_conditions(values: Dict) -> List['DTCondition']:
        return [DTCondition(**v) for _, v in values.items()]


class DTChance(object):
    def __init__(self, prompt: Optional[str], set: Optional[Union[List[str], str]], node: str):
        self.node = node
        self.prompt = prompt
        self.set = None if set is None else [DTExpr(c) for c in set] if isinstance(set, List) else [DTExpr(set)]

    @staticmethod
    def dict_to_chances(values: Dict) -> List['DTChance']:
        return [DTChance(**v) for _, v in values.items()]
