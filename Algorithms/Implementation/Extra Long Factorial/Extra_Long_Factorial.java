//Link : https://www.hackerrank.com/challenges/extra-long-factorials/problem
// Name : Extra Long Factorial 
// Level : Medium
// Max Score : 20 

import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        
        BigInteger factorial = new BigInteger("1");
        
        for(int i = 2; i <= N; i++)
        {
            BigInteger multiplier = new BigInteger(String.valueOf(i));
            factorial = factorial.multiply(multiplier);
        }
        
        System.out.println(factorial);
    }
}