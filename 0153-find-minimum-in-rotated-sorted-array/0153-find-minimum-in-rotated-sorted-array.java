class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) { // in binary search <= tha yha nhi hai
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) { // the this part (left part is unsorted and here our answer exist)
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
}