/*
Author: Kim YeongHwa
Date: 2022-02-06
Title: LeetCode/9. Palindrome Number
Language: Java 11
Contents:
    9. Palindrome Number
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.

    Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:
    -231 <= x <= 231 - 1

 */

class Solution {
    public boolean isPalindrome(int x) {
        boolean answer = false;
        int origin = x;
        int result = 0;
        if(x < 0) {
            return answer;
        }

        while(x != 0) {
            result *= 10;
            int temp = x % 10;
            result += temp;
            x /= 10;
        }
        if(origin == result) {
            answer = true;
        }
        System.out.println(String.format("%d %d", origin, result));
        return answer;
    }
}