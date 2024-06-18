# 問題文
https://leetcode.com/problems/linked-list-cycle/description/

# Step1

かかった時間：30min

思考ログ：
- 問題をよむ：
  - 入力は連結リスト。出力はBool.　
  - 入力がループしている場合にTrueを、そうでないならFalseを返す
- 連結リストに関して調査
  - 連結リストは、各要素が一つ前あるいは後ろの要素へのリンクを持つリスト。
  - そのため、同じ要素数を持つ配列よりも多くのメモリを消費する。
  - ただし、要素を挿入あるい削除するとき、配列では後ろの要素を全てずらす必要があるのに対して、連結リストはその箇所のリンクを繋ぎ変えるだけになるので、計算時間が短くなる。
- posを理解
  - 末尾の次のポインタが接続されているノードのインデックスを示す
  - パラメータとして渡されない。
- 計算量がどれくらいでいけるのだろうか
  - ぐぐってたらフロイドの循環検出アルゴリズムにたどり着いた
    - 一方のポインタslowはL上を1ノードずつ進め、他方のポインタfastはL上を2ノードずつ進める。サイクル（循環）が存在しない場合、 fast がリストの末尾に達して終了。サイクルが存在する場合、サイクル内で fast が slow に追いつくことでサイクルを検出

以下を実装しとりあえずとおった。
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: #headが空のときの挙動
            return False 
        fast=head.next
        slow=head

        while fast is not None and fast.next is not None:
            if fast == slow:
                return True                
            fast = fast.next.next
            slow = slow.next
        return False
```

参考リンク
- https://astrostory.hatenablog.com/entry/2020/02/24/070213
- https://note.com/rhayahi/n/n7fc11c09fec6

# Step2
かかった時間：5min

思考ログ
- 上記を消してもう一回実装。滞りなくかけたので素直かも
- ちょっとwhileが気に食わないのでドモルガンで下記なおしてみた。ぱっと見やすい説

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False 
        fast = head.next 
        slow = head

        while not (fast is None or fast.next is None):
            if fast == slow:
                return True
            
            fast = fast.next.next
            slow = slow.next
        return False
```

# Step3
かかった時間：3min

3回トライしていずれも1分程度、問題なくAcceptできた。