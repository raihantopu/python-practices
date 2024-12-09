import java.util.*;

public class Test{
    public static void main(String[] args){

        String s = "07:05:45PM";
        System.out.println(solve(s));
    }

    private static String solve(String s){
        if(s.contains("- 12:00:00AM")){
            return "00:00:00";
        }
        if(s.contains("- 12:00:00PM")){
            return "12:00:00";
        }
        if(s.contains("PM")){
            String subString = s.substring(0, s.length() - 2);
            String[] splitedString = subString.split(":");
            if(Integer.valueOf(splitedString[0]) == 12){
                return splitedString[0] + ":" + splitedString[1] + ":" + splitedString[2];
            }else{
               int hour = Integer.valueOf(splitedString[0]) + 12;
                return hour + ":" + splitedString[1] + ":" + splitedString[2]; 
            }
        }else{
            String subString = s.substring(0, s.length() - 2);
            String[] splitedString = subString.split(":");
            if(Integer.valueOf(splitedString[0]) == 12){
                return "00:" + splitedString[1] + ":" + splitedString[2]; 
            }else{
                return s.substring(0, s.length() - 2);
            }
           
        }
    }
}