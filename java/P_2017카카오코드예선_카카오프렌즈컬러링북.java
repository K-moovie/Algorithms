class Solution {
    int numberOfArea;
    int maxSizeOfOneArea;
    int sizeOfOneArea;
    boolean[][] check;
    int[] goI;
    int[] goJ;
    public int[] solution(int m, int n, int[][] picture) {
        numberOfArea = 0;
        maxSizeOfOneArea = 0;
        sizeOfOneArea = 0;
        check = new boolean[m][n];
        goI = new int[] {0, 1, -1, 0};
        goJ = new int[] {1, 0, 0, -1};

        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++){
                if (!check[i][j] && picture[i][j] != 0) {
                    numberOfArea++;
                    dfs(i, j, picture);
                }
                if (sizeOfOneArea > maxSizeOfOneArea) {
                    maxSizeOfOneArea = sizeOfOneArea;
                }
                sizeOfOneArea = 0;
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public void dfs(int i, int j, int[][] picture){
        if (check[i][j]) {
            return;
        }
        check[i][j] = true;
        sizeOfOneArea++;
        // System.out.println(Integer.toString(i) + Integer.toString(j));
        int newI = 0, newJ = 0;
        for (int index = 0; index < 4; index++){
            newI = i + goI[index];
            newJ = j + goJ[index];
            if (newI < 0 || newI > picture.length - 1 || newJ < 0 || newJ > picture[0].length - 1) {
                continue;
            }

            if (picture[newI][newJ] == picture[i][j] && !check[newI][newJ]){
                dfs(newI, newJ, picture);
                // System.out.println(Integer.toString(picture[newI][newJ]));
            }
        }
        return;
    }
}