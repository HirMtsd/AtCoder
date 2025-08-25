/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 413-A'
 * 2025/08/14
 */
import java.util.Scanner;

/**
 * @author HirMtsd
 */
public class Abc413A {
	/**
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を2つの数値として扱う(入力は3～3*10^5の範囲に限定されている。)
		int n = s.nextInt();
		int m = s.nextInt();
		// 2行目の入力をn個の数値リストとして扱う
		int[] a = new int[n];
		for (int i = 0; i < n; i++){
			a[i] = s.nextInt();
		}
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc413A o = new Abc413A();
		System.out.println(o.func(n, m, a));
	}

	/**
	 * n個の品物の大きさの総和がかばんの大きさm以下の場合Yes、そうでない場合Noを返す。
	 * @param n 品物の個数
	 * @param m かばんの大きさ
	 * @param a 品物の大きさのリスト
	 * @return String "Yes" or "No"
	 */
	public String func(final int n, final int m, final int[] a) {
		// 答は"Yes"か"No"なので、最初に"No"を設定
		String ans = "No";
		
		// 品物の大きさの総和
		int all = 0;
		
		// n回ループ処理
		for(int i = 0;  i < n; i++){
			// 数値リストの中身を全部足す
			all += a[i];
		}
		
		// mと比較
		if(all <= m) {
			ans = "Yes";
		}
		
		// 答えを返す
		return ans;
	}
}
