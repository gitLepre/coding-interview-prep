function isValid(s: string): boolean {
  let myStack: string[] = [];
  for (let c of s) {
    if (c === "{" || c === "[" || c === "(") {
      myStack.push(c);
    } else {
      if (myStack.length === 0) return false;
      const popped = myStack.pop();
      if (popped === "[" && c !== "]") return false;
      if (popped === "{" && c !== "}") return false;
      if (popped === "(" && c !== ")") return false;
    }
  }
  return !myStack.length;
}
