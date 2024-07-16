# 問題文
https://leetcode.com/problems/linked-list-cycle-ii/description/
# Step1

かかった時間：10min

思考ログ：
- 問題を理解する。
  - 入出力ともに`Optional[ListNode]`。141との違いはReturnが変わっている
    - 前回は`bool`でよかったが今回はサイクルありならサイクルが始まるListNodeを、そうでないならNoneを返す。
- とりあえずハッシュテーブルを利用する方法でやってみる。空間計算量はO(n)
  - ノードの数がnであるとき、visitedリストも最大でn個の要素を持つため。
  
```python

```
疑問点：
- setでもリストでもとおったが、どっちのほうがよいのだろうか？
- 
参考リンク
- 
# Step2
かかった時間：20min

思考ログ
- まずはハッシュテーブルを再実装し、コードの改良箇所をみつける。

```python

```

- フロイドの循環検出法を実装したがTLE。解法をみた(下記は通らなかった実装)
```python

```

# Step3
かかった時間： 5min
上記を書き直し、実装。

```python

```

# Step 4 
- レビューを持って修正を行う

```python


```