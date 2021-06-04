from typing import Dict, Any, Optional, List
import json
from ark.tree import DTCommand, DTChoice, DTCondition, DTExpr, DTChance


class DTNode(object):
    def __init__(self, name: Optional[str], prompt: str):
        self.name: Optional[str] = name
        self.prompt: str = prompt

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

    def run(self) -> Optional['DTNode']:
        pass


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

    def __init__(self, dt_path: str):
        self.path = dt_path
        self.game_node: DTNode = None
        self.nodes: Dict[str, DTNode] = {}
        self.cursor: DTNode = None
        self.env: Dict[str, Any] = {}
        self.parse()

    def parse(self):
        pass

    def __str__(self):
        return f'DT loaded from "{self.path}"\nGame node: {self.game_node}\n' \
               f'Current position in the tree: {self.cursor}\nTree has the following nodes:\n{self.nodes}'


class DummyDecisionTree(BaseDecisionTree):

    def parse(self):
        self.game_node = GameNode(
            game_title='Dummy game', description='None for now!',
            start_node='first-node', env={'budget': 30000, 'age': 31},
            commands={0: {'command': 'status', 'action': 'print env'}, 1: {'command': 'die', 'action': 'die'}}
        )
        self.cursor = DTNode(name='Wowza!', prompt='This is the final node.')


if __name__ == '__main__':
    dt = DummyDecisionTree(dt_path='')
    print(dt)
