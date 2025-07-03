package Easy;

class Solution {
    public char kthCharacter(int k) {
        return getChar(k, 0);
    }

    private char getChar(int k, int depth) {
        if (k == 1) return 'a';

        int len = 1 << depth; // 2^depth
        while (len < k) {
            depth++;
            len <<= 1;
        }

        int half = len >> 1;
        if (k <= half) {
            return getChar(k, depth - 1);
        } else {
            char ch = getChar(k - half, depth - 1);
            return ch == 'z' ? 'a' : (char)(ch + 1);
        }
    }
}