class Solution {
    public String reverseVowels(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        int low = 0;
        int high = n-1;
        String vowel = "aeiou";
        while(low<high){

            while(low<high && vowel.indexOf(Character.toLowerCase(arr[low])) == -1){
                low++;
            }

            while(low<high && vowel.indexOf(Character.toLowerCase(arr[high])) == -1){
                high--;
            }

            if(vowel.indexOf(Character.toLowerCase(arr[low])) != -1 && vowel.indexOf(Character.toLowerCase(arr[high])) != -1){
                char temp = arr[low];
                arr[low] = arr[high];
                arr[high] = temp;
            }
            low++;
            high--;
        }

        return String.valueOf(arr);
    }
}