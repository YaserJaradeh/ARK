from typing import Dict, Any
from ark.tree import DTNode, GameNode


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

    def run_through(self):
        while self.cursor is not None:
            # Check commands
            print('Should check input as well')  # TODO: something here
            # Apply actions of nodes
            self.cursor.pre_run()
            # Get user input
            if self.cursor.requires_input:
                print('requires')
            # Move node to new node
            self.cursor = self.cursor.run(self.env, self.nodes)

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
