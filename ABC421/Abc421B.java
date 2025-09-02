/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 421-B'
 * 2025/09/02
 */
import java.util.Scanner;

/**
 * @author HirMtsd
 */
public class Abc421B {
	/**
	 * 入出力処理
	 * 標準入力から、題意の入力を受け取る。
	 * 関数func()を呼び出し、結果を標準出力へ出力する。
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を2つの数値として扱う(入力は1～10^5に限定されている。)
		int x = s.nextInt();
		int y = s.nextInt();
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc421B o = new Abc421B();
		System.out.println(String.valueOf(o.func(x, y)));
	}

	/**
	 * 題意のrev関数
	 * 引数xを10進表記して、得られる文字列を反転したものを整数とした値を返す
	 * @param x 整数値
	 * @return long 答え
	 */
	public long rev(final long x) {
		// xを文字列に変換
		String xs = String.valueOf(x);
		
		// xsを反転
		StringBuilder sb = new StringBuilder(xs);
		String xsr = sb.reverse().toString();
		
		// 反転文字列を数値に変換
		long xr = Long.parseLong(xsr);
		
		// 答えを返す
		return(xr);
	}

	/**
	 * 正整数列Aを以下のように定義し、a10の値を返す
	 * A=(a1, a2, ... an)
	 * a1=x
	 * a2=y
	 * ai=rev(ai-1 + ai-2)
	 * @param x 正整数(1<=x<=10^5)
	 * @param y 正整数(1<=x<=10^5)
	 * @return long 答え
	 */
	public long func(final long x, final long y) {
		// 正整数列の準備
		long[] ans = new long[10];
		
		// 順に足していく
		ans[0] = x;
		ans[1] = y;
		for(int i = 2; i < 10; i++) {
			ans[i] = rev(ans[i-1] + ans[i-2]);
		}
		
		// 答えを返す
		return ans[9];
	}
}
