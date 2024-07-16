# 問題文
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Step1

かかった時間：10min

思考ログ：
- 問題を理解する。
  - ソートされた連結リストがあり、複製されたものは削除されソートされた連結リストを返す
    - headをsetにあつめたら重複はなくなりそうだが、出力は連結リストなのでNG
    - ソート済みなので現在のノードと次のノードを比較して値が同じなら重複している。このとき更に次を見に行く。
    - そうでないときは隣にいく。
  - 時間計算量：O(N)
  - 
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current_node = head
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:# is でも通るが等価かどうかを判定するので”＝＝”であるべき
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head
```

# Step2
かかった時間：30min

思考ログ
- 他の方のPRを参照にしたり、自分なりにどのようなつっこみを受けるかを考える
  - 冒頭の判定は`head.next`もみたほうがいい
  - `currnet.next.next`とか`currnet.next.val`は視認性がわるい気がするとおもった
    - [こちら](https://github.com/kenta-kk/arai60/pull/3/files#r1677196070)をみるとむしろ逆。余計な変数を定義しないほうがワーキングメモリつかわない
    - 物は試しで書いてみたけど、あんまり変わった印象がない。むしろ余計に行数増えたのでcompare_nopde使わなくていいかなと思った
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        current_node = head
        compare_node = head.next
        while current_node and compare_node:
            if current_node.val == compare_node.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
            compare_node = compare_node.next
        return head
```

  - 他の方法があるか⇒再帰を使った方法
    - よくあるパターンだと階乗の実装でNに対しN-1を引数で関数の出力を返す、みたいなやつ
    - なので`head.next`を`deleteDuplicates`に突っ込む。`head`の移動はこれまでにifと似たような感じでいける。割とすっきりしている印象。
    - 再帰の深さ＝`head`の長さ
  
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        else:
            return head
```

# Step3
かかった時間： min


```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current_node = head
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head
```

# Step 4 
- レビューを持って修正を行う

```python


```