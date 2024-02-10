function lengthOfLongestSubstring(s: string): number {
  let maxLength = 0;
  let currLength = 0;
  let lastSubstringInitialIndex = 0;
  let visited = new Map<string, number>();
  for (let i = 0; i < s.length; i++) {
    if (
      typeof visited.get(s[i]) !== "undefined" &&
      lastSubstringInitialIndex <= (visited.get(s[i]) || 0)
    ) {
      lastSubstringInitialIndex = (visited.get(s[i]) || 0) + 1;
    }
    visited.set(s[i], i);
    currLength = i - lastSubstringInitialIndex + 1;
    if (maxLength < currLength) maxLength = currLength;
  }
  return maxLength;
}

lengthOfLongestSubstring("abba");
