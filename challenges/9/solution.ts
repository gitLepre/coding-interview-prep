function isPalindrome(x: number): boolean {
  if (x < 0) return false;
  const castedValue = "" + x;
  for (let j = 0; j < castedValue.length / 2; j++) {
    if (castedValue[j] != castedValue[castedValue.length - 1 - j]) return false;
  }
  return true;
}
