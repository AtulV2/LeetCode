class Solution {
    public int reverse(int x) {
        long num = Math.abs((long) x);
        long rev_num = 0;

        while (num > 0) {
            long digit = num % 10;
            rev_num = rev_num * 10 + digit;
            num = num / 10;
        }

        if (x < 0) {
            rev_num = -rev_num;
        }

        if (rev_num > Integer.MAX_VALUE || rev_num < Integer.MIN_VALUE) {
            return 0;
        }

        return (int) rev_num;
    }
}