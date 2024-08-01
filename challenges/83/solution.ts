/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

// empty list
// can be negative, between -100 and 100
// ascending

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  if (!head) return head;

  let currentNode = head;

  while (!!currentNode?.next) {
    while (currentNode.val === currentNode.next?.val || null) {
      currentNode.next = currentNode.next.next;
    }
    currentNode = currentNode.next;
  }
  return head;
};
