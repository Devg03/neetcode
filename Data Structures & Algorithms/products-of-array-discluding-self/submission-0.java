class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prefixProduct = 1;
        int suffixProduct = 1;
        int[] answer = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            answer[i] = prefixProduct;
            prefixProduct *= nums[i];
        }
        System.out.println(Arrays.toString(answer));
        for (int j = nums.length - 1; j >= 0; j--) {
            answer[j] *= suffixProduct;
            suffixProduct *= nums[j];
        }
        return answer;
    }
}