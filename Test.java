import java.util.*;

public class Test{
    public static void main(String[] args){
        System.out.println(solve(Arrays.asList(1,2,1,3,2), 3, 2));
    }

    private static int solve(List<Integer> s, int d, int m){
        int count = 0;
        for(int i=0;i<s.size();i++){
            int sum = 0;
            int barsCount = 0;
            for(int j=i;j<j+m;j++){
                if(j>=s.size() || sum >= d){
                    break;
                }
                barsCount++;
                sum+=s.get(j);
            }
            if(sum == d && barsCount == m){
                count++;
            }
        }
        return count;
    }

}