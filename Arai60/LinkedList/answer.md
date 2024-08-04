# 問題文
https://leetcode.com/problems/add-two-numbers/description/

# Step1
かかった時間：min

思考ログ：
- 問題を理解する。
  - リストを逆順に高い桁の数値に格納し、それらの合計をとる。
  - 桁の繰り上げ…ノードの和に対して10で割ったときの商を値として保持し、次の計算時に足す。
  - 計算量
    - 時間計算量：O(n)←入力リストの各ノードを一度だけ訪問する。
    - 時間計算量：O(n)←l1とl2の数に由来
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0 #l1に値ありならx=l1.val, そうでないならx=0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = sum // 10 #切り捨て除算
            current.next = ListNode(sum % 10) #剰余
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:#最後の加算で桁上がりがある場合ノードを追加
            current.next = ListNode(carry)
        
        return dummyHead.next
```
 
# Step2
かかった時間：min

思考ログ
- Step1の改修できる箇所をさがす
  - x、y⇒l1_val、l2_valとか？　関数化も視野かなと思ったが、これくらいならむしろしなくていいんじゃないかという気もする
  - sumは予約語になってるケースもあるので名前変える
  - l1, l2の判定は1行で書ける
  - carryは0か1しかない　Ifかかなくても` total // 10`でいけてそう

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = carry + l1_val + l2_val
            carry = total // 10
            current.next = ListNode(total % 10) 
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry != 0: current.next = ListNode(carry)
        return dummyHead.next

```

- 再帰による解法
  - l1、l2、carrtすべてNoneならNoneを返す
  - 基本の和や繰り上げは同じ
  - 最後に次のノードへの代入として再帰で呼び出す
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],carry = 0) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None

        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        total = carry + l1_val + l2_val
        carry = total // 10
        current_node = ListNode(total % 10)

        l1_next = l1.next if l1 else None
        l2_next = l2.next if l2 else None
        current_node.next = self.addTwoNumbers(l1_next, l2_next, carry)

        return current_node
```

# Step3
かかった時間：5min

step2(iterative)を何回か書き直してSubした
# Step 4 
- レビューを持って修正を行う
- while に`carry`を追加
- 変数名変更(`l1_val` -> `v1` ,`l2_val` -> `v2`, `sum_node` -> `total`)

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = carry + v1 + v2
            carry = total // 10
            current.next = ListNode(total % 10) 
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummyHead.next
```