import yaml
from typing import Dict
from ark.tree import BaseDecisionTree
from ark.tree import ChoiceNode, ChanceNode, GameNode, DTNode, ConditionNode


class YamlDecisionTree(BaseDecisionTree):

    def parse(self):
        file_content: Dict = {}
        with open(self.path, 'r') as stream:
            try:
                file_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise ValueError(f'Something wrong happened when parsing the file. Error is {exc}')
        if 'game' not in file_content.keys():
            raise ValueError(f'The YAML file should contain a "game" node.')
        for node_key, node in file_content.items():
            if node_key in self.nodes:
                print(f'Be careful some node IDs are duplicates, which means something is going wrong!')
            if node_key == 'game':
                self.game_node = GameNode(**node)
            elif 'choices' in node:
                self.nodes[node_key] = ChoiceNode(**node)
            elif 'conditions' in node:
                self.nodes[node_key] = ConditionNode(**node)
            elif 'chances' in node:
                self.nodes[node_key] = ChanceNode(**node)
            else:
                self.nodes[node_key] = DTNode(**node)
        self.env = self.game_node.env


if __name__ == '__main__':
    dt = YamlDecisionTree(dt_path='C:\\Users\\Yaser\\Downloads\\template.yaml')
    print(dt)
