/**
 * @param {string} s
 * @param {number} idx
 * @return {string}
 */
const isInsideBoundaries = (s, idx) => {
  return idx < s.length;
};

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = (s, numRows) => {
  if (s.length <= numRows) return s;
  if (numRows < 2) return s;

  let currIndex = 0;
  let output = "";
  const step = (numRows - 1) * 2;

  for (let i = 0; i < numRows; i++) {
    const rowStepDiagonal = (numRows - 1 - i) * 2;
    const rowStepVertical = step - rowStepDiagonal;
    currIndex = i;
    output += s[currIndex];

    console.log(rowStepDiagonal, rowStepVertical);

    while (isInsideBoundaries(s, currIndex)) {
      currIndex += rowStepDiagonal;
      if (isInsideBoundaries(s, currIndex) && rowStepDiagonal != 0)
        output += s[currIndex];
      currIndex += rowStepVertical;
      if (isInsideBoundaries(s, currIndex) && rowStepVertical != 0)
        output += s[currIndex];
    }
  }

  return output;
};
