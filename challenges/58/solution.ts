var lengthOfLastWord = function (s) {
  let idx = s.length - 1;
  let len = 0;
  while (idx >= 0) {
    if (s[idx] === " ") {
      idx--;
      continue;
    } else break;
  }
  while (idx >= 0) {
    if (s[idx] !== " ") {
      idx--;
      len++;
    } else break;
  }
  return len;
};
