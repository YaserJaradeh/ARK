from typing import Dict, Any, Optional, List
import json
from ark.tree import DTCommand, DTChoice, DTCondition, DTExpr, DTChance


class DTNode(object):
    def __init__(self, name: Optional[str], prompt: str):
        self.name = name
        self.prompt = prompt

    def validate_node(self):
        pass

    def serialize(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def to_json(self) -> Dict:
        return json.loads(self.serialize())


class GameNode(DTNode):
    def __init__(self, game_title: str, description: str, start_node: str, env: Dict[str, Any],
                 commands: Dict[int, Dict]):
        super().__init__(name=game_title, prompt=description)
        self.game_title = game_title
        self.description = description
        self.start_node = start_node
        self.env = env
        self.commands = DTCommand.dict_to_commands(commands)
        self.validate_node()

    def validate_node(self):
        # validate commands
        pass


class ChoiceNode(DTNode):
    def __init__(self, name: Optional[str], prompt: str, set: List[str], choices: Dict[int, Dict]):
        super().__init__(name=name, prompt=prompt)
        self.set = DTExpr.to_expressions(set)
        self.choices = DTChoice.dict_to_choices(choices)
        self.validate_node()

    def validate_node(self):
        # validate choices
        pass


class ConditionNode(DTNode):
    def __init__(self, name: Optional[str], prompt: str, set: List[str], conditions: Dict[int, Dict]):
        super().__init__(name=name, prompt=prompt)
        self.set = DTExpr.to_expressions(set)
        self.conditions = DTCondition.dict_to_conditions(conditions)
        self.validate_node()

    def validate_node(self):
        # validate conditions
        pass


class ChanceNode(DTNode):
    def __init__(self, name: Optional[str], prompt: str, chances: Dict[float, Dict]):
        super().__init__(name=name, prompt=prompt)
        self.chances = DTChance.dict_to_chances(chances)
        self.validate_node()

    def validate_node(self):
        # validate chances
        pass


class BaseDecisionTree(object):

    def parse(self, file):
        pass
