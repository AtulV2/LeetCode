class Solution {
    public int removeDuplicates(int[] nums) {

        if (nums.length == 0) {
            return 0;
        }

        int n = 1;

        for(int m = 1; m < nums.length ; m++){
            if(nums[m-1] != nums[m]){
                nums[n] = nums[m];
                n++;
            }
        }


        return n;
        
    }
}