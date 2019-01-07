import os
import sys

from putput.input_processor import generate_utterance_pattern_and_tokens
from putput.utterance_creator import create_utterances_and_tokens


def _wake_handler(tokenized_phrase: str) -> str:
    return "[WAKE(" + tokenized_phrase + ")]"


def _song_handler(tokenized_phrase: str) -> str:
    return "[SONG(" + tokenized_phrase + ")]"


def _action_handler(tokenized_phrase: str) -> str:
    return "[ACTION(" + tokenized_phrase + ")]"


def main() -> None:
    input_fname = os.path.join(os.path.dirname(__file__), "patterns.yml")
    dynamic_token_patterns_dict = {
        "ACTION": [[["tell me the news", "what's the weather"]]]
    }
    token_handlers = {
        "WAKE": _wake_handler,
        "SONG": _song_handler,
        "ACTION": _action_handler
    }
    for utterance_pattern, tokens in generate_utterance_pattern_and_tokens(input_fname, dynamic_token_patterns_dict):
        import pdb; pdb.set_trace()
        utterance, tokens = create_utterances_and_tokens(utterance_pattern,
                                                         tokens,
                                                         sys.maxsize,
                                                         sys.maxsize,
                                                         0,
                                                         token_handlers)
        print("utterance: ", utterance)
        print("tokens: ", tokens)


if __name__ == '__main__':
    main()
