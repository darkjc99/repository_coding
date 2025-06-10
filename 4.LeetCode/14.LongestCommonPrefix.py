"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return

    prefix = strs[0]

    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0 : len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
