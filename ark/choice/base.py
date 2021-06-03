from typing import List, Tuple


class BaseChoiceSelector(object):

    @staticmethod
    def _sort_candidate_choices(ranked_choices: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
        return sorted(ranked_choices, key=lambda c: c[1], reverse=True)

    def _rank_choices(self, text: str, choices: List[str]) -> List[Tuple[str, float]]:
        """
        rank the choices based on the given input text
        (This method should be overridden in each child class)
        :param text: a natural text representing input text
        :param choices: list of choices that text could be assigned to
        :return: a list of the same size as choices but each item is a tuple of the choice and the confidence value
        """
        pass

    def rank_choices(self, text: str, choices: List[str]) -> List[Tuple[str, float]]:
        return self._sort_candidate_choices(self._rank_choices(text, choices))


class DummySelector(BaseChoiceSelector):

    def _rank_choices(self, text: str, choices: List[str]) -> List[Tuple[str, float]]:
        return [(c, 1.0 if c == text else 0.0) for c in choices]
