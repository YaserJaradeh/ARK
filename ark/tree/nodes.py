import json
from typing import Dict, Any, Optional, List
from ark.tree import DTCommand, DTChoice, DTCondition, DTExpr, DTChance


class DTNode(object):
    def __init__(self, name: Optional[str], prompt: str):
        self.name: Optional[str] = name
        self.prompt: str = prompt

    @property
    def requires_input(self) -> bool:
        return False

    def validate_node(self):
        pass

    def serialize(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def to_json(self) -> Dict:
        return json.loads(self.serialize())

    def __str__(self):
        return self.serialize()

    def __repr__(self):
        return self.__str__()

    def pre_run(self, env: Dict[str, Any], nodes: Dict[str, 'DTNode']):
        pass

    def run(self, env: Dict[str, Any], nodes: Dict[str, 'DTNode']) -> Optional['DTNode']:
        return None


class GameNode(DTNode):
    def __init__(self, game_title: str, description: str, start_node: str, env: Dict[str, Any],
                 commands: Dict[int, Dict]):
        super().__init__(name=game_title, prompt=description)
        self.start_node = start_node
        self.env = env
        self.commands = DTCommand.dict_to_commands(commands)
        self.validate_node()

    def validate_node(self):
        # validate commands
        pass

    def run(self, env: Dict[str, Any], nodes: Dict[str, DTNode]) -> Optional[DTNode]:
        return nodes[self.start_node]


class ChoiceNode(DTNode):
    def __init__(self, name: Optional[str], prompt: str, set: List[str], choices: Dict[int, Dict]):
        super().__init__(name=name, prompt=prompt)
        self.set = DTExpr.to_expressions(set)
        self.choices = DTChoice.dict_to_choices(choices)
        self.validate_node()

    @property
    def requires_input(self) -> bool:
        return True

    def validate_node(self):
        # validate choices
        pass

    def pre_run(self, env: Dict[str, Any], nodes: Dict[str, DTNode]):
        for exp in self.set:
            exp.apply(env)

    def run(self, env: Dict[str, Any], nodes: Dict[str, DTNode]) -> Optional[DTNode]:
        # Get user input
        print('do something with input')
        # Select branch
        print('move to next node')
        return self


class ConditionNode(DTNode):
    def __init__(self, name: Optional[str], prompt: str, set: List[str], conditions: Dict[int, Dict]):
        super().__init__(name=name, prompt=prompt)
        self.set = DTExpr.to_expressions(set)
        self.conditions = DTCondition.dict_to_conditions(conditions)
        self.validate_node()

    def validate_node(self):
        # validate conditions
        pass

    def pre_run(self, env: Dict[str, Any], nodes: Dict[str, DTNode]):
        for exp in self.set:
            exp.apply(env)

    def run(self, env: Dict[str, Any], nodes: Dict[str, DTNode]) -> Optional[DTNode]:
        # Get user input
        print('do something with input')
        # Select branch
        print('move to next node')
        return self


class ChanceNode(DTNode):
    def __init__(self, name: Optional[str], prompt: str, chances: Dict[float, Dict]):
        super().__init__(name=name, prompt=prompt)
        self.chances = DTChance.dict_to_chances(chances)
        self.validate_node()

    def validate_node(self):
        # validate chances
        pass

    def run(self, env: Dict[str, Any], nodes: Dict[str, DTNode]) -> Optional[DTNode]:
        # Get user input
        print('do something with input')
        # Select branch
        branch = self.chances[0]
        for exp in branch.set:
            exp.apply(env)
        return self
