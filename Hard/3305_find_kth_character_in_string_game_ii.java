package Hard;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public char kthCharacter(long k, int[] operations) {
        int shift = 0;
        long len = 1;
        List<Long> lengths = new ArrayList<>();

        for (int i = 0; i < operations.length; i++) {
            len *= 2;
            lengths.add(len);
            if (len >= k) break;
        }

        for (int i = lengths.size() - 1; i >= 0; i--) {
            long half = lengths.get(i) / 2;
            if (k > half) {
                k -= half;
                if (operations[i] == 1) shift++;
            }
        }

        return (char) ((shift % 26) + 'a');
    }
}
