/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 413-B'
 * 2025/08/14
 */
import java.util.Scanner;
import java.util.HashSet;

/**
 * @author HirMtsd
 */
public class Abc413B {
	/**
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を数値として扱う(入力は2～100の範囲に限定されている。)
		int n = s.nextInt();
		// 2行目の入力をn個の文字列リストとして扱う
		String[] str = new String[n];
		for (int i = 0; i < n; i++){
			str[i] = s.next();
		}
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc413B o = new Abc413B();
		System.out.println(o.func(n, str));
	}

	/**
	 * 文字列リストの中から2つ取り出して連結した文字列の重複を除いた個数を求める
	 * @param n sの要素数
	 * @param s 文字列リスト
	 * @return int 個数
	 */
	public int func(final int n, final String[] s) {
		// Setの準備
		HashSet<String> cset = new HashSet<String>();
		
		// n*n回ループ処理
		for(int i=0; i < n; i++){
			for(int j=0; j < n; j++){
				if(i == j){
					continue;
				}
				cset.add(s[i]+s[j]);
			}
		}
		
		// 要素数を返す
		return(cset.size());
	}
}
