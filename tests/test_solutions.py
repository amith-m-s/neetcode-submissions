import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "Data Structures & Algorithms"


def load_solution(problem):
    path = SOLUTIONS / problem / "submission-0.py"
    spec = importlib.util.spec_from_file_location(
        f"solution_{problem.replace('-', '_')}", path
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load solution: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution


class SolutionRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.GroupAnagrams = load_solution("anagram-groups")
        cls.HasDuplicate = load_solution("duplicate-integer")
        cls.IsAnagram = load_solution("is-anagram")
        cls.TwoSum = load_solution("two-integer-sum")

    def test_group_anagrams(self):
        actual = self.GroupAnagrams().groupAnagrams(
            ["eat", "tea", "tan", "ate", "nat", "bat"]
        )
        self.assertCountEqual(
            [frozenset(group) for group in actual],
            [
                frozenset({"eat", "tea", "ate"}),
                frozenset({"tan", "nat"}),
                frozenset({"bat"}),
            ],
        )

    def test_group_anagrams_handles_empty_input_and_empty_word(self):
        solution = self.GroupAnagrams()
        self.assertEqual(solution.groupAnagrams([]), [])
        self.assertEqual(solution.groupAnagrams([""]), [[""]])

    def test_duplicate_detection(self):
        solution = self.HasDuplicate()
        self.assertTrue(solution.hasDuplicate([1, 2, 3, 1]))
        self.assertFalse(solution.hasDuplicate([1, 2, 3]))

    def test_duplicate_detection_handles_empty_and_single_item(self):
        solution = self.HasDuplicate()
        self.assertFalse(solution.hasDuplicate([]))
        self.assertFalse(solution.hasDuplicate([42]))

    def test_duplicate_detection_does_not_mutate_input(self):
        values = [3, 1, 2]
        original = values.copy()
        self.HasDuplicate().hasDuplicate(values)
        self.assertEqual(values, original)

    def test_is_anagram(self):
        solution = self.IsAnagram()
        self.assertTrue(solution.isAnagram("anagram", "nagaram"))
        self.assertFalse(solution.isAnagram("rat", "car"))

    def test_is_anagram_handles_empty_and_unicode_strings(self):
        solution = self.IsAnagram()
        self.assertTrue(solution.isAnagram("", ""))
        self.assertTrue(solution.isAnagram("åß", "ßå"))

    def test_two_sum_finds_distinct_indices(self):
        self.assertEqual(self.TwoSum().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.TwoSum().twoSum([3, 3], 6), [0, 1])

    def test_two_sum_handles_negative_values(self):
        self.assertEqual(self.TwoSum().twoSum([0, 4, 3, 0], 0), [0, 3])

    def test_two_sum_returns_empty_when_no_pair_exists(self):
        self.assertEqual(self.TwoSum().twoSum([1, 2, 3], 10), [])
        self.assertEqual(self.TwoSum().twoSum([3], 6), [])

    def test_two_sum_does_not_mutate_input(self):
        values = [3, 2, 4]
        original = values.copy()
        self.TwoSum().twoSum(values, 6)
        self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
