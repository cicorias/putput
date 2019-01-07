import sys
import unittest

from putput.utterance_creator import create_utterances_and_tokens


class TestUtteranceCreator(unittest.TestCase):
    def setUp(self) -> None:
        self._token_handlers = {"SPEAKER": lambda token_val: f"[{token_val.upper()}(id=1)]"}
        self._max_sample_size = self._max_retries = sys.maxsize
        self._seed = 0

    def test_solo_static_without_combinations(self) -> None:
        utterance_pattern = [[[['kanye west', 'the beatles']]]]
        utterance_pattern_tokens = ['ARTIST']
        actual_utterances, actual_tokens = create_utterances_and_tokens(utterance_pattern,
                                                                        utterance_pattern_tokens,
                                                                        self._max_sample_size,
                                                                        self._max_retries,
                                                                        self._seed,
                                                                        self._token_handlers)
        expected_utterances = ['kanye west', 'the beatles']
        expected_tokens = ['[ARTIST]'] * 2
        for utterance, tokens in zip(expected_utterances, expected_tokens):
            self.assertIn(utterance, actual_utterances)
            self.assertIn(tokens, actual_tokens)
        self.assertEqual(len(expected_tokens), len(actual_tokens))
        self.assertEqual(len(expected_utterances), len(actual_utterances))

    def test_solo_static_with_combinations(self) -> None:
        play_token_patterns = [[['i', 'he'], ['will', 'would'], ['play', 'listen to']], [['play', 'start playing']]]
        playlist_token_patterns = [[['slow', 'fast'], ['songs', 'jams']]]
        utterance_pattern = [play_token_patterns, playlist_token_patterns]
        utterance_pattern_tokens = ['PLAY', 'PLAYLIST']
        actual_utterances, actual_tokens = create_utterances_and_tokens(utterance_pattern,
                                                                        utterance_pattern_tokens,
                                                                        self._max_sample_size,
                                                                        self._max_retries,
                                                                        self._seed,
                                                                        self._token_handlers)
        expected_utterances = [
            'he would listen to fast jams', 'i would listen to fast jams', 'start playing fast songs',
            'he will play slow jams', 'play slow jams', 'i would play fast songs', 'i will play slow songs',
            'he will listen to fast songs', 'he would play fast jams', 'he would listen to slow songs',
            'i will listen to slow jams', 'i would listen to slow songs', 'start playing slow jams',
            'he will play fast jams', 'play fast songs', 'i will play fast jams', 'he will listen to slow jams',
            'i would play slow songs', 'i will listen to fast songs', 'i would listen to fast songs',
            'he will play slow songs', 'he would play slow jams', 'play slow songs', 'he would listen to fast songs',
            'start playing fast jams', 'i will play slow jams', 'i would play fast jams', 'i will listen to slow songs',
            'i would listen to slow jams', 'he will listen to fast jams', 'he would play fast songs', 'play fast jams',
            'he would listen to slow jams', 'start playing slow songs', 'i will play fast songs',
            'he will play fast songs', 'i would play slow jams', 'i will listen to fast jams',
            'he will listen to slow songs', 'he would play slow songs'
        ]
        expected_tokens = ['[PLAY] [PLAYLIST]'] * (2 * 2 * 2 + 2 * 1) * (2 * 2)
        for utterance, tokens in zip(expected_utterances, expected_tokens):
            self.assertIn(utterance, actual_utterances)
            self.assertIn(tokens, actual_tokens)
        self.assertEqual(len(expected_tokens), len(actual_tokens))
        self.assertEqual(len(expected_utterances), len(actual_utterances))

    def test_solo_dynamic_without_combinations(self) -> None:
        utterance_pattern = [[[['bose', 'jambox', 'echo']]]]
        utterance_pattern_tokens = ['SPEAKER']
        actual_utterances, actual_tokens = create_utterances_and_tokens(utterance_pattern,
                                                                        utterance_pattern_tokens,
                                                                        self._max_sample_size,
                                                                        self._max_retries,
                                                                        self._seed,
                                                                        self._token_handlers)
        expected_utterances = ['bose', 'jambox', 'echo']
        expected_tokens = ['[BOSE(id=1)]', '[JAMBOX(id=1)]', '[ECHO(id=1)]']
        for utterance, tokens in zip(expected_utterances, expected_tokens):
            self.assertIn(utterance, actual_utterances)
            self.assertIn(tokens, actual_tokens)
        self.assertEqual(len(expected_tokens), len(actual_tokens))
        self.assertEqual(len(expected_utterances), len(actual_utterances))

    def test_solo_dynamic_with_combinations(self) -> None:
        pass

    def test_static_and_dynamic(self) -> None:
        pass

    def test_max_sample_size(self) -> None:
        pass

    def test_max_retries(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
