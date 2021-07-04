import java.util.*;
import java.util.regex.Pattern;

/*
String s = "aaaaabbbbb";
String t = "ab";
*/

public class NaverWebtoon3 {
    public static int solution(String s, String t) {
        int result = 0;
        String pattern = ".*" + t + ".*";
        while (true){
            if (!Pattern.matches(pattern, s)) {
                break;
            }
            s = s.replaceFirst(t,"");
            result++;
        }
        return result;
    }
}