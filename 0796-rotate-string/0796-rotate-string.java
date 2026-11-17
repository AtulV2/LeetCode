class Solution {
    public boolean rotateString(String s, String goal) {

        if (s.length() != goal.length()){
            return false;
        }
        String str =  s.concat(s);

        for(int i = 0; i<=s.length(); i++){
            String sub_str = str.substring(i,i+s.length());
            System.out.println(sub_str);
            System.out.println(goal);
            if(sub_str.equals(goal)){
                return true;
            }
        }

        return false;
        
    }
}