class Solution:
    def deleteDuplicates(self, head):
        current=head
        while current.next != None and current != None:
            if current.next.val==current.val:
                current.next=current.next.next
            else:
                current=current.next
        return head
