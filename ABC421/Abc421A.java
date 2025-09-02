/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 421-A'
 * 2025/09/02
 */
import java.util.Scanner;

/**
 * @author HirMtsd
 */
public class Abc421A {
	/**
	 * 入出力処理
	 * 標準入力から、題意の入力を受け取る。
	 * 関数func()を呼び出し、結果を標準出力へ出力する。
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を1つの数値として扱う(入力は1～100に限定されている。)
		int n = s.nextInt();
		// 2～n+1行目の入力をn個の文字列リストとして扱う
		String[] str = new String[n];
		for (int i = 0; i < n; i++){
			str[i] = s.next();
		}
		// n+2行目の入力を1個の数値と1つの文字列として扱う
		int x = s.nextInt();
		String y = s.next();
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc421A o = new Abc421A();
		System.out.println(o.func(n, str, x, y));
	}

	/**
	 * n室の部屋の住人のうち、X号室のYさん宛の荷物の宛先が正しい場合Yes、そうでない場合Noを返す。
	 * @param n 部屋の数
	 * @param s 住人の名前の配列
	 * @param x 荷物の宛先号室
	 * @param y 荷物の宛先名前
	 * @return String "Yes" or "No"
	 */
	public String func(final int n, final String[] s, final int x, String y) {
		// 答は"Yes"か"No"なので、最初に"No"を設定
		String ans = "No";
		
		// s[x-1]とyを比較
		if(s[x-1].equals(y)) {
			ans = "Yes";
		}
		
		// 答えを返す
		return ans;
	}
}
