class Solution {
    public void moveZeroes(int[] nums) {

            int index = 0;
            for(int val : nums){
                if(val != 0){
                    nums[index] = val;
                    index++;
                }
            }


            while(index < nums.length){
                nums[index] = 0;
                index++;
            }
        
    }
}