/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 413-C'
 * 2025/08/26
 */
import java.util.Scanner;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;

/**
 * @author HirMtsd
 */
public class Abc413C {
	/**
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を数値として扱う(入力は2～2*10^5の範囲に限定されている。)
		int n = s.nextInt();
		// 2行目以降の入力をn個のArrayList<Long>として扱う
		ArrayList<ArrayList<Long>> ql = new ArrayList<ArrayList<Long>>();
		for (int i = 0; i < n; i++){
			long key = s.nextLong();
			ArrayList<Long> val = new ArrayList<Long>();
			if(key == 1){
				val.add(key);
				val.add(s.nextLong());
				val.add(s.nextLong());
			}
			if(key == 2){
				val.add(key);
				val.add(s.nextLong());
			}
			ql.add(val);
		}
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc413C o = new Abc413C();
		long[] a = o.func(n, ql);
		for(int i = 0; i < a.length; i++){
			System.out.println(a[i]);
		}
	}

	/**
	 * クエリを順に処理する
	 * クエリは[1 c x]形式か[2 k]形式のいずれか
	 * 1の場合、整数列Aにxをc個追加する
	 * 2の場合、整数列Aの先頭k個を取り出し、その総和を出力する
	 * クエリ[2 k]の数だけ、総和を出力する。
	 * @param n クエリの数
	 * @param ql クエリのリスト(クエリはArrayList<Long>で保持)
	 * @return long[] クエリ[2 k]毎の総和
	 */
	public long[] func(final int n, final ArrayList<ArrayList<Long>> ql) {
		// クエリを保存するLinkedListを用意する。(リストには[c(繰り返し数),x(値)]のリストを格納する。)
		Deque<ArrayList<Long>> A = new ArrayDeque<ArrayList<Long>>();
		
		// 答のリストを用意しておく
		ArrayList<Long> ans = new ArrayList<Long>();
		
		// クエリをひとつづつ処理していく
		for(int i = 0; i < n; i++){
			// 1文字目が1の場合
			if(ql.get(i).get(0) == 1){
				// クエリの値を追加する
				long c = ql.get(i).get(1);
				long x = ql.get(i).get(2);
				ArrayList<Long> member = new ArrayList<Long>();
				member.add(c);
				member.add(x);
				A.addLast(member);
			}
			// 1文字目が2の場合
			if(ql.get(i).get(0) == 2){
				// 必要な個数を確認する
				long k = ql.get(i).get(1);
				// 部分解を初期化
				long part = 0;
				// ループ処理
				while(true){
					// Aの先頭からcとxを取り出す。
					long c = A.getFirst().get(0);
					long x = A.getFirst().get(1);
					A.removeFirst();
					// cがk以上の場合、部分解にx*kを足し、
					// Aの先頭のcの値をc-kに更新する(ループを終了)
					if(c >= k){
						part += x * k;
						ArrayList<Long> member = new ArrayList<Long>();
						member.add(c - k);
						member.add(x);
						A.addFirst(member);
						break;
					}
					// cがkより小さい場合、部分解にx*cを足し、kをk-cに更新し、Aのクエリカウンタを1つ進める(ループ継続)
					if(c < k){
						part += x * c;
						k = k - c;
					}
				}
				ans.add(part);
			}
		}
		
		// 答を返す
		long[] longAns = new long[ans.size()];
		for(int i = 0; i < ans.size(); i++){
			longAns[i] = ans.get(i);
		}
		return(longAns);
	}
}
