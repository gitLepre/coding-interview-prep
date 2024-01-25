function twoSum(nums: number[], target: number): number[] {
  let visited = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const a = nums[i];
    const remainder = target - a;
    const dual = visited.get(remainder);
    visited.set(a, i);
    if (typeof dual === "number") return [dual, i];
  }
  return [];
}
