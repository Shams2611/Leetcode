// Question: https://leetcode.com/problems/two-sum/


// My approach:
// learning: returning an empty array 
// starting from j = i + 1
// The inner loop starts from i + 1 to ensure each pair is considered only once and to avoid using the same element twice.
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j]; 
            }
        }
    }
    return []; 
};