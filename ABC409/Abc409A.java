/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 409-A'
 * 2025/07/03
 */
import java.util.Scanner;

/**
 * @author HirMtsd
 */
public class Abc409A {
	/**
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を数値として扱う(入力は1～100の範囲に限定されている。)
		int n = s.nextInt();
		// 2行目の入力を文字列として扱う
		String t = s.next();
		// 3行目の入力を文字列として扱う
		String a = s.next();
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc409A o = new Abc409A();
		System.out.println(o.func(n, t, a));
	}

	/**
	 * t/aの文字列で同じ位置に両方oがある場合Yes、そうでない場合Noを返す。
	 * @param n t/aの個数
	 * @param t 高橋君の要望(oかx、n個の文字列)
	 * @param a 青木君の要望(oかx、n個の文字列)
	 * @return String "Yes" or "No"
	 */
	public String func(final int n, final String t, final String a) {
		// 答は"Yes"か"No"なので、最初に"No"を設定
		String ans = "No";
		
		// n回ループ処理
		for(int i = 0;  i < n; i++){
			// 文字列tと文字列aのi番目を比較し、両方"o"なら、ansを"Yes"にして離脱
			if(t.charAt(i) == 'o' && a.charAt(i) == 'o'){
				ans = "Yes";
				break;
			}
		}
		
		// 答えを返す
		return ans;
	}
}
