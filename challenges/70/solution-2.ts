function climbStairs2(n: number): number {
  const myTree = new Tree(n);
  return myTree.buildTree();
}

class MyNode {
  left: MyNode; // 1
  right: MyNode; // 2
  value: number = 0;

  constructor(x: number) {
    this.value = x;
  }

  goLeft() {
    this.left = new MyNode(this.value + 1);
  }

  goRight() {
    this.right = new MyNode(this.value + 2);
  }
}

class Tree {
  root: MyNode = new MyNode(0);
  target: number;
  totalCombinations: number = 0;

  constructor(n: number) {
    this.target = n;
  }

  buildTree() {
    if (this.target === 1) return 1; // <3
    this.buildTreeRecursive(this.root);
    return this.totalCombinations;
  }

  buildTreeRecursive(node: MyNode) {
    if (node.value + 1 <= this.target) {
      node.goLeft();
      this.buildTreeRecursive(node.left);
    }
    if (node.value + 2 <= this.target) {
      node.goRight();
      this.buildTreeRecursive(node.right);
    }
    if (!node.left && !node.right) this.totalCombinations++;
  }
}
