function climbStairs(n: number): number {
  return fibo(n);
}

function fibo(n) {
  return fiboRecursive(0, 1, n);
}

function fiboRecursive(a: number, b: number, n: number) {
  if (n == 0) return b;
  return fiboRecursive(b, a + b, n - 1);
}
