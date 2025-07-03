/**
 * coding: utf-8
 * Copyright (C) 2025 HirMtsd. All Rights Reserved.
 * Code for 'AtCoder Beginner Contest 409-A Test'
 * 2025/07/03
 */

/* -----
* JUnit5をコマンドラインから使う方法(超簡易版)
 * 1.https://junit.org/等からjunit-platform-console-standalone-1.13.2.jarをダウンロードする
 * 2.ソースコードとテストコード(このファイル)を作成し、同一フォルダに保存
 * 3.コンパイル
 *  javac -cp junit-platform-console-standalone-1.13.2.jar -encoding utf-8 Abc409A.java Abc409ATest.java
 * 4.テスト
 *  java -cp junit-platform-console-standalone-1.13.2.jar org.junit.platform.console.ConsoleLauncher --class-path . --scan-classpath
 */

// unittestの準備
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

/**
 * @author HirMtsd
 */
public class Abc409ATest {
	/**
	 * Abc409A.func()のテスト
	 */
	@Test
	public void testFunc() {
		Abc409A trg = new Abc409A();
		// 課題に記載のケース
		assertEquals("Yes", trg.func( 4, "oxoo", "xoox"));
		assertEquals( "No", trg.func( 5, "xxxxx", "ooooo"));
		assertEquals("Yes", trg.func(10, "xoooxoxxxo", "ooxooooxoo"));
		// N=1のケース
		assertEquals( "No", trg.func( 1, "x", "x"));
		assertEquals( "No", trg.func( 1, "x", "o"));
		assertEquals( "No", trg.func( 1, "o", "x"));
		assertEquals("Yes", trg.func( 1, "o", "o"));
		// N=2のケース
		assertEquals( "No", trg.func( 2, "xx", "xx"));
		assertEquals( "No", trg.func( 2, "xx", "xo"));
		assertEquals( "No", trg.func( 2, "xx", "ox"));
		assertEquals( "No", trg.func( 2, "xx", "oo"));
		assertEquals( "No", trg.func( 2, "xo", "xx"));
		assertEquals( "No", trg.func( 2, "xo", "ox"));
		assertEquals( "No", trg.func( 2, "ox", "xx"));
		assertEquals( "No", trg.func( 2, "ox", "xo"));
		assertEquals( "No", trg.func( 2, "oo", "xx"));
		assertEquals("Yes", trg.func( 2, "xo", "xo"));
		assertEquals("Yes", trg.func( 2, "xo", "oo"));
		assertEquals("Yes", trg.func( 2, "ox", "ox"));
		assertEquals("Yes", trg.func( 2, "ox", "oo"));
		assertEquals("Yes", trg.func( 2, "oo", "ox"));
		assertEquals("Yes", trg.func( 2, "oo", "xo"));
		assertEquals("Yes", trg.func( 2, "oo", "oo"));
		// N=100の最悪ケース
		assertEquals( "No", trg.func(100, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"));
		assertEquals("Yes", trg.func(100, "oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"));
		assertEquals("Yes", trg.func(100, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo"));
	}
}
