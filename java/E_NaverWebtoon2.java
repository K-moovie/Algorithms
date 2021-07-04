import java.util.*;

/*
String s = "abcxyasdfasdfxyabc";
String s = "abcxyqwertyxyabc";
String s = "llttaattll";
String s = "abcabcabcabc";
String s = "abcdef";
*/

public class NaverWebtoon2 {
    public static String[] solution(String s) {
        String[] answer = {};
        List <String> result = new ArrayList<>();
        int lPos = 0;
        int rPos = s.length();
        int count = 1;
        String left;
        String right;
        while (true){
            if (lPos + count > rPos - count) {
                String str = s.substring(lPos, rPos);
                List<String> temp = new ArrayList<>();
                temp.addAll(result);
                Collections.reverse(result);
                temp.addAll(result);
                if (!str.equals("")) {
                    temp.add(temp.size()/2, str);
                }
                answer = temp.toArray(new String[0]);
                break;
            }
            left = s.substring(lPos, lPos + count);
            right = s.substring(rPos - count, rPos);
            if (left.equals(right)) {
                result.add(left);
                lPos += count;
                rPos -= count;
                count = 1;
            }
            else {
                count++;
            }
        }
        return answer;
    }
}