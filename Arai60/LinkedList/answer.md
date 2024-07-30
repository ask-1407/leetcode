# 問題文

# Step1

かかった時間：20min

思考ログ：
- 問題を理解する。
  - 前回とは異なり、重複があるものを”全て”削除する。
  - 入出力：ともに連結リスト
  - 計算量：時間…O(N)　空間…O(1) 
  - ループの中で、2つのポインタの値を比較する。
    - 値が異なる場合は隣にいく。
    - 値が一致した場合は、先頭ノードだけ隣へ更新。再度比較して異なった場合は後方ノードを先頭に、先頭はその隣に移動。
- 解けなかったので解法をみた。最初のノード（head）も重複している場合、それを削除する処理が必要。ダミーを使用することで先頭ノードの削除処理とそれ以外のノードの削除処理を同じ方法で扱える。ダミーを置くことに気づけなかった。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        previous_node = dummy
        current_node = head

        while current_node:
            while current_node.next and current_node.val == current_node.next.val:
                current_node = current_node.next
            if previous_node.next == current_node:
                previous_node = previous_node.next
            else:
                previous_node.next = current_node.next
            current_node = current_node.next
        return dummy.next
```

# Step2
かかった時間：min

思考ログ
- 他の方のコードやコメントを読む
  - [型ヒントでnodeが自明](https://github.com/hrkh/leetcode/pull/5/files#r1676086915)
  - [かといってcurrentという名前は諸説ある](https://github.com/canisterism/leetcode/pull/4#discussion_r1688679810)
  - [マジックナンバー(意味のない数字)は避けるべき](https://github.com/goto-untrapped/Arai60/pull/43#discussion_r1695376875)
- nodeが自明なのはそうだなって思ったので名前からnodeを消して実装をしてみる。こっちのほうが見やすいかも

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        previous = dummy
        current = head

        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            if previous.next == current:
                previous = previous.next
            else:
                previous.next = current.next
            current= current.next
        return dummy.next
```
- 他の解き方がないかを考える。←再帰とか？
  - 深さはheadの長さに依存するのでn
  - 基本：`head`が空ないし要素が単一のときに`head`を返す
  - 再帰：重複があったときの処理
 
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
```

# Step3
かかった時間： 3min

Step2のコードを書き直し⇒Subを何回かした。


# Step 4 
- レビューを持って修正を行う

```python


```