from ark.choice import BaseChoiceSelector
from typing import List, Tuple
from transformers import pipeline


class ZeroShotSelector(BaseChoiceSelector):

    def __init__(self, multi_label: bool = False):
        self.classifier = pipeline("zero-shot-classification")
        self.multi_label = multi_label

    def _rank_choices(self, text: str, choices: List[str]) -> List[Tuple[str, float]]:
        response = self.classifier(text, choices, multi_label=self.multi_label)
        return [(c, response['scores'][i]) for i, c in enumerate(response['labels'])]


if __name__ == '__main__':
    cls = ZeroShotSelector()
    print(cls.rank_choices(text='let\'s head 45 degrees west', choices=['turn left', 'turn right', 'stop and rest', 'fight enemy']))
