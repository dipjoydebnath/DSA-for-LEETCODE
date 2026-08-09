class Solution {
    public ListNode deleteDuplicates(ListNode head) {

        // if the list is empty
        if (head == null) {
            return head;
        }

        // start from head
        ListNode current = head;

        // traverse the list
        while (current.next != null) {

            if (current.val == current.next.val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return head;
    }
}