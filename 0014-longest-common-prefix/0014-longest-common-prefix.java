class Solution {
    public String longestCommonPrefix(String[] strs) {

        if(strs == null || strs.length == 0){
            return "";
        }

        for(int p = 0 ; p < strs[0].length(); p++){
            char c = strs[0].charAt(p);

            for(int sIndex = 1; sIndex < strs.length ; sIndex++ ){

                if(p >= strs[sIndex].length() || c != strs[sIndex].charAt(p)){
                    return strs[0].substring(0,p);
                }
            }
        }

        return strs[0];
        
    }
}