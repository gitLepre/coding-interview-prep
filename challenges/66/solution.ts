function plusOne(digits: number[]): number[] {
  let curry = 1;
  for (let j = digits.length - 1; j >= 0; j--) {
    digits[j] = (digits[j] + curry) % 10;
    digits[j] === 0 ? (curry = 1) : (curry = 0);
    if (!curry) return digits;
  }
  if (curry === 1) digits.unshift(curry);
  return digits;
}
