"""코딩테스트 기본 패턴 독립 연습용. 프로그래머스 제출 답안이 아닙니다."""

from __future__ import annotations

import unittest


def has_pair_sum(numbers: list[int], target: int) -> bool:
    """합이 target인 서로 다른 두 인덱스의 값이 있는지 확인한다."""
    seen: set[int] = set()
    for value in numbers:
        if target - value in seen:
            return True
        seen.add(value)
    return False


def lower_bound(sorted_numbers: list[int], target: int) -> int:
    """정렬된 배열에서 target 이상 값이 처음 등장하는 위치를 반환한다."""
    left, right = 0, len(sorted_numbers)
    while left < right:
        mid = (left + right) // 2
        if sorted_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def longest_unique_substring(text: str) -> int:
    """중복 문자가 없는 가장 긴 연속 부분 문자열의 길이를 구한다."""
    last_seen: dict[str, int] = {}
    left = 0
    longest = 0
    for right, char in enumerate(text):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        longest = max(longest, right - left + 1)
    return longest


class PatternTests(unittest.TestCase):
    def test_pair_sum(self) -> None:
        self.assertTrue(has_pair_sum([2, 7, 11, 15], 9))
        self.assertTrue(has_pair_sum([3, 3], 6))
        self.assertFalse(has_pair_sum([3], 6))
        self.assertFalse(has_pair_sum([], 0))

    def test_lower_bound(self) -> None:
        self.assertEqual(lower_bound([1, 2, 2, 4], 2), 1)
        self.assertEqual(lower_bound([1, 2, 2, 4], 3), 3)
        self.assertEqual(lower_bound([1, 2, 2, 4], 5), 4)
        self.assertEqual(lower_bound([], 2), 0)

    def test_unique_window(self) -> None:
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(longest_unique_substring("abba"), 2)
        self.assertEqual(longest_unique_substring("aaaa"), 1)
        self.assertEqual(longest_unique_substring(""), 0)


if __name__ == "__main__":
    unittest.main()
