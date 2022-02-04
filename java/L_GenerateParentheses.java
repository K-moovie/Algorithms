/*
Author: Kim YeongHwa
Date: 2022-02-04
Title: LeetCode/22. Generate Parentheses
Language: Java 11
Contents:
    22. Generate Parentheses
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]

    Constraints:
    1 <= n <= 8
*/

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> answer = new ArrayList<>();
        backtracking("", n, 0, 0, answer);
        return answer;
    }

    public void backtracking(String curStr, int n, int open, int close, List<String> answer) {
        if(curStr.length() == n * 2) {
            answer.add(curStr);
            return;
        }
        System.out.println(curStr);

        if (open < n) {
            backtracking(curStr+"(", n, open + 1, close, answer);
        }
        if(open > close) {
            backtracking(curStr+")", n, open, close + 1, answer);
        }
    }
}