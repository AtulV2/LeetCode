class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 0;

        for (int pile : piles) {
            right = Math.max(right, pile);
        }

        while (left < right) {
            int k = left + (right - left) / 2;
            long hoursNeeded = 0;

            for (int pile : piles) {
                hoursNeeded += (pile - 1) / k + 1;
            }

            if (hoursNeeded > h) {
                left = k + 1;
            } else {
                right = k;
            }
        }

        return left;
    }
}