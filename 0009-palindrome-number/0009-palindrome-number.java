class Solution {
    public boolean isPalindrome(int x) {

        // Negative numbers cannot be palindrome
        if (x < 0) {
            return false;
        }

        int num = x;
        int rev_num = 0;

        while (num > 0) {
            int digit = num % 10;
            rev_num = rev_num * 10 + digit;
            num = num / 10;
        }

        return x == rev_num;
    }
}