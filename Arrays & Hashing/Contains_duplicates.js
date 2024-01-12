// Question link https://leetcode.com/problems/contains-duplicate
// First solution > this exceeded time limit
var containsDuplicate = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] === nums[j]) {
        return true;
      }
    }
  }
  return false;
};
// Second solution

var containsDuplicate = function (nums) {
  let seen = new Set();
  for (let i = 0; i < nums.length; i++) {
    if (seen.has(nums[i])) {
      return true;
    }
    seen.add(nums[i]);
  }
  return false;
};

// Very efficient method suggested by Ari

var containsDuplicate = function (nums) {
  let newSet = new Set(nums);
  if (newSet.size === nums.length) {
    return false;
  } else {
    return true;
  }
};
