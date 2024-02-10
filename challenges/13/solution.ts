const mapper = new Map();
mapper
  .set("I", 1)
  .set("V", 5)
  .set("X", 10)
  .set("L", 50)
  .set("C", 100)
  .set("D", 500)
  .set("M", 1000);

function romanToInt(s: string): number {
  let nextChar = "";
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    let curr = mapper.get(s[i]);

    if (i < s.length - 1) {
      nextChar = s[i + 1];
      switch (s[i]) {
        case "I":
          if (nextChar === "V" || nextChar === "X") curr *= -1;
          break;

        case "X":
          if (nextChar === "L" || nextChar === "C") curr *= -1;
          break;

        case "C":
          if (nextChar === "D" || nextChar === "M") curr *= -1;
          break;

        default:
          break;
      }
    }

    if (curr) result += curr;
  }
  return result;
}
