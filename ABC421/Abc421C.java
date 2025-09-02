/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 421-C'
 * 2025/09/02
 */
import java.util.Scanner;

/**
 * @author HirMtsd
 */
public class Abc421C {
	/**
	 * 入出力処理
	 * 標準入力から、題意の入力を受け取る。
	 * 関数func()を呼び出し、結果を標準出力へ出力する。
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を1つの数値として扱う(入力は1～5*10^5に限定されている。)
		int n = s.nextInt();
		// 2行目の入力を1つの文字列として扱う(文字列長はN*2に固定されている。)
		String str = s.next();
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc421C o = new Abc421C();
		System.out.println(String.valueOf(o.func(n, str)));
	}

	/**
	 * 文字'A'がN個、'B'がN個の文字列Sを、同じ文字が隣り合わないように
	 * 隣り合う文字を入れ替える操作を最小何回繰り返す必要があるかを返す
	 * @param n 正整数(1<=x<=5*10^5)
	 * @param s 文字列(文字列長はN*2に固定)
	 * @return long 答え
	 */
	public long func(final int n, final String s) {
		// 文字列の最初の1文字を確認する
		char f = s.charAt(0);
		
		// 1文字目がAなら調査対象文字tを"A",1文字目がBならtを"B"とする。
		char t = f;
		
		// 最終形はtがすべて偶数の位置にあればいい。
		// tの位置を調べて、intの配列に確保する。
		int cnt = 0;
		int[] tmp = new int[n];
		for(int i = 0; i < n * 2; i++){
			if(s.charAt(i) == t){
				tmp[cnt] = i;
				cnt++;
			}
		}
		
		// tmp[]のそれぞれの値が本来あるべき位置からどれくらい離れているか確認し、
		// 答えに足していく
		long ansa = 0;
		for(int i = 0; i < n; i++){
			if(tmp[i] > i*2){
				ansa += tmp[i] - i*2;
			}
			if(tmp[i] < i*2){
				ansa += i*2 - tmp[i];
			}
		}
		
		// tmp[]のそれぞれの値が本来あるべき位置からどれくらい離れているか確認し、
		// 答えに足していく
		long ansb = 0;
		for(int i = 0; i < n; i++){
			if(tmp[i] > i*2 + 1){
				ansb += tmp[i] - (i*2 + 1);
			}
			if(tmp[i] < i*2 + 1){
				ansb += (i*2 + 1) - tmp[i];
			}
		}
		
		// 答えを返す
		return(Math.min(ansa, ansb));
	}
}
