import itertools
from typing import Callable, List, Mapping, Optional, Tuple

from putput.ordered_combinations_joiner import join_ordered_combinations
from putput.types import UtterancePattern


def _get_token_handler(token: str,
                       token_handlers: Optional[Mapping[str, Callable[[str], str]]] = None
                       ) -> Callable[[str], str]:
    if token_handlers:
        token_handler = token_handlers.get(token) or token_handlers.get("DEFAULT")
    return token_handler or (lambda _: "[" + token + "]")


def create_utterances_and_tokens(utterance_pattern: UtterancePattern,
                                 tokens: List[str],
                                 max_sample_size: int,
                                 max_retries: int,
                                 seed: int = 0,
                                 token_handlers: Optional[Mapping[str, Callable[[str], str]]] = None
                                 ) -> Tuple[List[str], List[str]]:
    # pylint: disable=too-many-arguments
    # TODO: the first join_ordered_combinations should always be sys.maxsize..., max retries....
    utterance_combinations = [
        list(itertools.chain.from_iterable(
            join_ordered_combinations(token_pattern, max_sample_size, max_retries, seed)
            for token_pattern in token_patterns))
        for token_patterns in utterance_pattern
    ]
    token_combinations = [[_get_token_handler(token, token_handlers)(word) for word in words]
                          for words, token in zip(utterance_combinations, tokens)]
    utterances = join_ordered_combinations(utterance_combinations, max_sample_size, max_retries, seed)
    tokens = join_ordered_combinations(token_combinations, max_sample_size, max_retries, seed)
    return utterances, tokens
