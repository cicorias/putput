from typing import List, Mapping, Optional, Tuple

import yaml

from putput.input_validator import validate_yml
from putput.types import TokenPattern, UtterancePattern


def _get_static_token_patterns_dict(input_dict: dict) -> dict:
    return {
        token: token_patterns
        for token_type_dict in input_dict['token_patterns']
        for token_type in token_type_dict
        if token_type == 'static'
        for token_patterns_dict in token_type_dict['static']
        for token, token_patterns in token_patterns_dict.items()
    }


def generate_utterance_pattern_and_tokens(input_fname: str,
                                          dynamic_token_patterns_dict: Optional[Mapping[str, List[TokenPattern]]] = None
                                          ) -> List[Tuple[UtterancePattern, List[str]]]:
    with open(input_fname, encoding='utf-8') as f:
        input_dict = yaml.load(f)
    validate_yml(input_dict)
    static_token_patterns_dict = _get_static_token_patterns_dict(input_dict)
    token_patterns_dict = {**static_token_patterns_dict, **(dynamic_token_patterns_dict or {})}
    return [
        ([token_patterns_dict[token] for token in tokens], tokens)
        for tokens in input_dict['utterance_patterns']
    ]
