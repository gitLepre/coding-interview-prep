function searchInsert(nums: number[], target: number): number {
  if (nums.length === 1) {
    if (target > nums[0]) return 1;
    else return 0;
  }

  let index = 0;
  let start = 0;
  let end = nums.length - 1;

  let done = false;
  while (!done) {
    let middle = Math.floor((end + start) / 2);
    if (target == nums[middle]) return middle;
    else if (end - start === 1) {
      if (target < nums[start]) return start;
      else if (target > nums[end]) return end + 1;
      else return end;
    } else if (target < nums[middle]) {
      end = middle;
    } else {
      start = middle;
    }
  }
  return index;
}
