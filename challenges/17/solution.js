/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  if (!digits || !digits.length) return [];

  const map = new Map([
    ["2", ["a", "b", "c"]],
    ["3", ["d", "e", "f"]],
    ["4", ["g", "h", "i"]],
    ["5", ["j", "k", "l"]],
    ["6", ["m", "n", "o"]],
    ["7", ["p", "q", "r", "s"]],
    ["8", ["t", "u", "v"]],
    ["9", ["w", "x", "y", "z"]],
  ]);

  if (digits.length === 1) return map.get(digits[0]);

  const values = digits.split("").map((x) => +x);

  let output = map.get(digits[0]);
  for (let i = 1; i < digits.length; i++) {
    // i * 4
    output = combineDigits(output, map.get(digits[i]));
  }
  return output;
};

const combineDigits = (a, b) => {
  const response = [];
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < b.length; j++) {
      response.push(a[i] + b[j]);
    }
  }

  return response;
};
