class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> counts = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char s_char = s.charAt(i);
            char t_char = t.charAt(i);

            counts.put(s_char, counts.getOrDefault(s_char, 0) + 1);
            counts.put(t_char, counts.getOrDefault(t_char, 0) - 1);
        }

        for (int count : counts.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
        
    }
}