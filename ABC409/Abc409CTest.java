/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 409-C Test'
 * 2025/07/03
 */

/* -----
* JUnit5をコマンドラインから使う方法(超簡易版)
 * 1.https://junit.org/等からjunit-platform-console-standalone-1.13.2.jarをダウンロードする
 * 2.ソースコードとテストコード(このファイル)を作成し、同一フォルダに保存
 * 3.コンパイル
 *  javac -cp junit-platform-console-standalone-1.13.2.jar -encoding utf-8 Abc409C.java Abc409CTest.java
 * 4.テスト
 *  java -cp junit-platform-console-standalone-1.13.2.jar org.junit.platform.console.ConsoleLauncher --class-path . --scan-classpath
 */

// unittestの準備
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

/**
 * @author HirMtsd
 */
public class Abc409CTest {
	/**
	 * Abc409C.func()のテスト
	 */
	@Test
	public void testFunc() {
		Abc409C trg = new Abc409C();
		// int配列の準備(中身がすべて1で300000個)
		int[] int30000 = new int[300000];
		for(int i = 0; i < int30000.length; i++){
			int30000[i] = 1;
		}
		// 課題に記載のケース
		assertEquals(  2, trg.func( 5,  6, new int[]{4, 3, 1, 2}));
		assertEquals(  0, trg.func( 4,  4, new int[]{1, 1, 1}));
		assertEquals( 13, trg.func(10, 12, new int[]{4, 4, 5, 7, 1, 7, 0, 8, 5}));
		// L=3のケース
		assertEquals(  0, trg.func( 3,  3, new int[]{0, 0}));
		assertEquals(  0, trg.func( 3,  3, new int[]{0, 1}));
		assertEquals(  1, trg.func( 3,  3, new int[]{1, 1}));
		assertEquals(  8, trg.func( 6,  3, new int[]{1, 1, 1, 1, 1}));
		assertEquals( 27, trg.func( 9,  3, new int[]{1, 1, 1, 1, 1, 1, 1, 1}));
		assertEquals(1000000000000000L, trg.func(300000,  3, int30000));
		// L=4のケース
		assertEquals(  0, trg.func( 3,  4, new int[]{1, 1, 1}));
		assertEquals(  0, trg.func(300000, 4, int30000));
		// L=5のケース
		assertEquals(  0, trg.func( 3,  5, new int[]{1, 1, 1}));
		assertEquals(  0, trg.func(300000, 5, int30000));
		// L=3*10**5のケース
		assertEquals(100000, trg.func(300000, 300000, int30000));
	}
}
