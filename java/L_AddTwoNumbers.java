/*
Author: Kim YeongHwa
Date: 2022-02-03
Title: LeetCode/2. Add Two Numbers
Language: Java 11
Contents:
    2. Add Two Numbers
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

    Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
 /*
import java.math.*;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        String s1 = "";
        String s2 = "";
        String rs = "";
        String[] result;
        BigInteger i1 = new BigInteger("0");
        BigInteger i2 = new BigInteger("0");
        ListNode cur = l1;

        while(true) {
            if(cur == null) break;
            s1 = Integer.toString(cur.val) + s1;
            cur = cur.next;
        }
        cur = l2;
        while(true) {
            if(cur == null) break;
            s2 = Integer.toString(cur.val) + s2;
            cur = cur.next;
        }

        i1 = new BigInteger(s1);
        i2 = new BigInteger(s2);
        rs = String.valueOf(i1.add(i2));
        result = rs.split("");

        ListNode answer = new ListNode(Integer.parseInt(result[result.length - 1]));
        cur = answer;
        for(int i = result.length - 2; i > -1; i--) {
            ListNode temp = new ListNode(Integer.parseInt(result[i]));
            cur.next = temp;
            cur = cur.next;
        }
        return answer;
    }
} */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode answer = new ListNode();
        ListNode node = answer;
        int carry = 0;

        while(l1 != null || l2 != null) {
            int sum = carry;

            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            carry = sum / 10;
            sum %= 10;

            ListNode temp = new ListNode(sum);
            node.next = temp;
            node = node.next;
        }

        if(carry > 0) {
            ListNode temp = new ListNode(carry);
            node.next = temp;
        }
        return answer.next;
    }
}