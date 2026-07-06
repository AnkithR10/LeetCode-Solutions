char* longestPalindrome(char* s) {
    int n = strlen(s);
    if (n < 1) return "";
    
    int start = 0, maxlen = 0;

    for (int i = 0; i < n; i++) {
        // Case 1: Odd length palindromes (centered at i)
        int l = i, r = i;
        while (l >= 0 && r < n && s[l] == s[r]) {
            if (r - l + 1 > maxlen) {
                start = l;
                maxlen = r - l + 1;
            }
            l--; r++;
        }

        // Case 2: Even length palindromes (centered between i and i+1)
        l = i; r = i + 1;
        while (l >= 0 && r < n && s[l] == s[r]) {
            if (r - l + 1 > maxlen) {
                start = l;
                maxlen = r - l + 1;
            }
            l--; r++;
        }
    }

    char *result = (char*)malloc((maxlen + 1) * sizeof(char));
    strncpy(result, s + start, maxlen);
    result[maxlen] = '\0';
    return result;
}