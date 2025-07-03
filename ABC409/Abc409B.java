/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 409-B'
 * 2025/07/03
 */
import java.util.Scanner;

/**
 * @author HirMtsd
 */
public class Abc409B {
	/**
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を数値として扱う(入力は1～100の範囲に限定されている。)
		int n = s.nextInt();
		// 2行目の入力をn個の数値リストとして扱う(数値は0～10^9の範囲)
		// Javaのintの最大値は2147483647なので、かろうじて収容可能
		int[] a = new int[n];
		for (int i = 0; i < n; i++){
			a[i] = s.nextInt();
		}
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc409B o = new Abc409B();
		System.out.println(o.func(n, a));
	}

	/**
	 * 次の条件を満たす最大のxを求める「aに、x以上の要素が重複を含めてx回以上現れる」
	 * @param n aの要素数
	 * @param a 非負整数列
	 * @return int 条件を満たすx
	 */
	public int func(final int n, final int[] a) {
		// 数列aの値が0～nのどれに当たるか調べるためのワーク
		int[] c = new int[n+1];
		
		//  n回ループ処理
		for(int i=0; i < n; i++){
			// 数列aの値をワークにセット
			// (数列aの値が0ならc[0]の個数を+1する。)
			// ただし数列aの値がn以上の場合はc[n]にセット
			if(a[i] > n){
				c[n] += 1;
			} else {
				c[a[i]] += 1;
			}
		}
		
		// 要素数の積算個数
		int s = 0;
		// n～0までループ処理
		for(int j = n; j >= 0; j--){
			// 積算個数に要素の個数を加算
			s += c[j];
			// 積算個数がj以上の場合、jを返す
			if(s >= j){
				return(j);
			}
		}
		
		// 最後まで離脱しなかった場合0を返す
		return(0);
	}
}
