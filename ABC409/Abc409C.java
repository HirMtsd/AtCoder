/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 409-C'
 * 2025/07/03
 */
import java.util.Scanner;

/**
 * @author HirMtsd
 */
public class Abc409C {
	/**
	 * @param args 起動時引数(なにも渡さない)
	 */
	public static void main(String[] args) {
		// 標準入力からのデータを関数に渡す
		Scanner s = new Scanner(System.in);
		// 1行目の入力を2つの数値として扱う(入力は3～3*10^5の範囲に限定されている。)
		int n = s.nextInt();
		int l = s.nextInt();
		// 2行目の入力をn個の数値リストとして扱う
		int[] d = new int[n];
		for (int i = 0; i < n - 1; i++){
			d[i] = s.nextInt();
		}
		s.close();
		
		// 処理を呼び出し、結果を出力する
		Abc409C o = new Abc409C();
		System.out.println(o.func(n, l, d));
	}

	/**
	 * 円周の長さl上にあるnこの点で、正三角形ができる個数を求める
	 * (始点には必ず点がある)
	 * @param n 円周上の点の個数(3～3*10^5)
	 * @param l 円周の長さ(3～3*10^5)
	 * @param d 円周上の点間の距離(0～)
	 * @return int 正三角形の個数
	 */
	public long func(final int n, final int l, final int[] d) {
		// Javaのintの最大値は2147483647
		// Javaのlongの最大値は9223372036854775807
		// 答えの最大値は10^5*10^5*10^5=10^15の可能性があるので、longで用意しておく
		// 答えの準備
		long ans = 0;
		
		// 円周上の3点が正三角形であるためには、円周が3の倍数でないと不成立
		// なので、まずlが3の倍数でない場合は除外する。
		if(l % 3 != 0){
			return(ans);
		}
		
		// 円周上の点の位置に点があるか調べるワーク
		int[] w = new int[l];
		
		// 頂点には必ず1つ点がある
		w[0] = 1;
		
		// diは円周の始点からのそれぞれの距離を示すので、
		// 積算してlで割ったあまりが位置を示す
		// 積算用ワーク
		long s = 0;
		
		// lが3の倍数のとき、始点0からl-1までのどこに点が配置されているか調べる
		// n-1回ループ処理
		for(int i=0; i < n-1; i++){
			s += d[i];
			w[(int)(s % l)] += 1;
		}
		
		// 始点0からl/3までの距離についてそこから等距離の点を数える。
		// 0からl/3までループ処理
		for(int j = 0; j < l/3; j++){
			// 掛け算の結果がintにならないように、longにcastしてから掛け算
			ans += (long)w[j] * (long)w[j+l/3] * (long)w[j+l*2/3];
		}
		
		// 答を返す
		return(ans);
	}
}
