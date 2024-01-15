// Question link: https://leetcode.com/problems/valid-anagram/description/
// My initial aapproach

var containsDuplicate = function (nums) {
  let newSet = new Set(nums);
  if (newSet.size === nums.length) {
    return false;
  } else {
    return true;
  }
};

//One line approach

var isAnagram = (s, t) =>
  s.split("").sort().join("") === t.split("").sort().join("");
