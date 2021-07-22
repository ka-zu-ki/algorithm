'''
片方向連結リスト
'''


from typing import Counter


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # リストの後ろに追加する
    def append(self, data):
        new_node = Node(data)
        # リストになにもない場合
        if self.head is None:
            self.head = new_node
            return

        # リストに値が存在する場合
        last_node = self.head
        # node.nextが存在する限り
        while last_node.next:
            last_node = last_node.next
        # 最後尾まで来たら新しいnodeを追加する
        last_node.next = new_node

    def insert(self, data):
        new_node = Node(data)
        # 追加するnodeのnextを先頭のnodeに指定
        new_node.next = self.head
        # リストの先頭を新しいnodeに指定
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data):
        # 先頭のデータを削除する場合
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        # 戦闘以外のデータを削除する場合
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        # 削除するnodeのnextを一つ前のnodeのnextに置き換える
        previous_node.next = current_node.next
        current_node = None

    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node, previous_node):
            if not current_node:
                return previous_node
            
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node 




l = LinkedList()
l.append(0)
l.append(1)
l.append(2)
l.print()
print('-----------------------------')
l.reverse_iterative()
l.print()
