import java.util.*;
class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        Map<Character,Character> S_T = new HashMap<>();
        Map<Character,Character> T_S = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            char  s_char = s.charAt(i);
            char  t_char = t.charAt(i);
            Character s_map = S_T.get(s_char);
            Character t_map = T_S.get(t_char);

            if(s_map != null && s_map != t_char ){
                return false;
            }

            if(t_map != null && t_map != s_char){
                return false;
            }


            S_T.put(s_char, t_char);
            T_S.put(t_char, s_char);


        }


        return true;
        
    }
}


