import java.util.*;

/*
int[] prices = new int[]{32000, 18000, 42500};
int[] discounts = new int[]{50, 20};
*/

public class NaverWebtoon1 {
    public static int solution(int[] prices, int[] discounts) {
        int answer = 0;

        // 내림차순 정렬을 위해 Integer 형식의 배열로 변환
        Integer integersPrices[] = Arrays.stream(prices).boxed().toArray(Integer[]::new);
        Integer integersDiscounts[] = Arrays.stream(discounts).boxed().toArray(Integer[]::new);

        // 내림차순 정렬
        Arrays.sort(integersPrices, Collections.reverseOrder());
        Arrays.sort(integersDiscounts, Collections.reverseOrder());

        // 가격, 할인 배열에서 길이가 긴 배열 사용.
        int length;
        length = (integersPrices.length > integersDiscounts.length) ? integersPrices.length: integersDiscounts.length;
        for (int i = 0;  i < length; i++) {
            if (integersPrices.length - 1 < i ) {
                for (int j = i; j < integersDiscounts.length; j++) {
                    answer += integersDiscounts[j];
                }
                break;
            } else if (integersDiscounts.length  - 1 < i) {
                for (int j = i; j < integersPrices.length; j++) {
                    answer += integersPrices[j];
                }
                break;
            }
            answer += Math.round(integersPrices[i] * ((double)(100 - integersDiscounts[i]) / 100));
        }
        return answer;
    }
}

