class Solution {
    public String frequencySort(String s) {

        Map<Character, Integer> f = new HashMap<>();

        for(char ch : s.toCharArray()){
            f.put(ch,f.getOrDefault(ch,0) + 1);
        }

        List<Character> l =  new ArrayList<>(f.keySet());

        l.sort((a,b)-> Integer.compare(f.get(b), f.get(a)));

        StringBuilder result = new StringBuilder();

        for(char ch : l ){
            int cout = f.get(ch);
            for(int i = 0; i<cout; i++){
                result.append(ch);
            }
        }

        return result.toString();
        
        
    }
}