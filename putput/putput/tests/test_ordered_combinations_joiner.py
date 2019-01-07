import sys
import unittest
from typing import List

from putput.ordered_combinations_joiner import join_ordered_combinations
from putput.types import TokenPattern


class TestOrderedCombinationsJoiner(unittest.TestCase):

    # takes in a token_pattern -> List[List[str]]
    # TODO: Mkae them all call one function instead of repeating constantly

    def _test_join(self,
                   pattern: TokenPattern,
                   max_sample_size: int,
                   max_retry: int,
                   expected_output: List[str]) -> None:
        actual_output = join_ordered_combinations(pattern, max_sample_size, max_retry, 0) # TODO: no hardcoding seed..
        self.assertEqual(len(actual_output), len(expected_output))
        self.assertLessEqual(len(actual_output), max_sample_size)
        for actual in actual_output:
            self.assertIn(actual, expected_output)

    def test_join_same_shape_lists(self) -> None:
        pattern = [["she", "he"], ["wants", "needs"]]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['she needs', 'he wants', 'she wants', 'he needs']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_first_list_shorter_than_second_list(self) -> None:
        pattern = [["he"], ["wants", "needs"]]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['he wants', 'he needs']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_first_list_longer_than_second_list(self) -> None:
        pattern = [["he", "she"], ["wants"]]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['he wants', 'she wants']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_one_list(self) -> None:
        pattern = [["he wants", "she needs"]]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['he wants', 'she needs']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_one_list_one_item(self) -> None:
        pattern = [["he wants"]]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['he wants']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_multiple_lists_same_size(self) -> None:
        pattern = [["he", "she"], ['would', 'will'], ['want', 'need']]
        max_sample_size = max_retry = sys.maxsize
        expected_output = [
            'he would want', 'he would need', 'he will want', 'he will need', 'she would want', 'she would need',
            'she will want', 'she will need'
        ]
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_multiple_lists_first_list_shorter(self) -> None:
        pattern = [["he"], ['would', 'will'], ['want', 'need']]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['he would want', 'he would need', 'he will want', 'he will need']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_multiple_lists_middle_list_shorter(self) -> None:
        pattern = [["he", "she"], ['will'], ['want', 'need']]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['he will want', 'he will need', 'she will want', 'she will need']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_multiple_lists_last_list_shorter(self) -> None:
        pattern = [["he", "she"], ['would', 'will'], ['want']]
        max_sample_size = max_retry = sys.maxsize
        expected_output = ['he would want', 'he will want', 'she would want', 'she will want']
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_multiple_lists_all_different_size(self) -> None:
        pattern = [["he"], ['would', 'will'], ['want', 'have', 'order']]
        max_sample_size = max_retry = sys.maxsize
        expected_output = [
            'he would want', 'he would have', 'he would order', 'he will want', 'he will have', 'he will order'
        ]
        self._test_join(pattern, max_sample_size, max_retry, expected_output)

    def test_max_sample_size_is_larger_than_number_of_permutations(self) -> None:
        pattern = [["he"], ['would', 'will'], ['want', 'have', 'order']]
        max_sample_size = max_retry = sys.maxsize
        actual_output = join_ordered_combinations(pattern, max_sample_size, max_retry, 0) # TODO: no hardcoding seed..
        num_permutations = len(pattern[0]) * len(pattern[1]) * len(pattern[2])
        self.assertEqual(len(actual_output), num_permutations)

    def test_same_seed_same_result(self) -> None:
        pattern = [["1", "2", "3"], ['4'], ['5', '6', '7', '8', '9', '10'], ['11'], ['12']]
        max_sample_size = max_retry = 3
        joined1 = join_ordered_combinations(pattern, max_sample_size, max_retry, 0)
        joined2 = join_ordered_combinations(pattern, max_sample_size, max_retry, 0)
        self.assertEqual(joined1, joined2)

    def test_different_seed_different_result(self) -> None:
        pattern = [["1", "2", "3"], ['4'], ['5', '6', '7', '8', '9', '10'], ['11'], ['12']]
        max_sample_size = max_retry = 3
        joined1 = join_ordered_combinations(pattern, max_sample_size, max_retry, 10)
        joined2 = join_ordered_combinations(pattern, max_sample_size, max_retry, 11)
        self.assertNotEqual(joined1, joined2)


if __name__ == '__main__':
    unittest.main()
