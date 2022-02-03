/*
Author: Kim YeongHwa
Date: 2022-02-03
Title: LeetCode/6. Zigzag Conversion
Language: Java 11
Contents:
    6. Zigzag Conversion
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);


    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

    Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
*/

class Solution {
    public String convert(String s, int numRows) {
        String[] strArr = new String[numRows];
        String[] str = s.split("");
        boolean isUp = false;
        int index = -1;
        for(int i = 0; i < numRows; i++) {
            strArr[i] = "";
        }

        if(numRows == 1 || numRows == s.length()) {
            return s;
        }

        for(String c: str){
            if(isUp) {
                index--;
            } else {
                index++;
            }

            strArr[index] += c;
            if(index == numRows - 1) {
                isUp = true;
            } else if(index == 0){
                isUp = false;
            }
        }
        return String.join("", strArr);
    }
}