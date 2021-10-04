package licensechecker;

public class Cryptor {

    private final byte[] HASH_PATTERN = {0x09, 0x43, 0x17, 0x53, 0x10, 0x46, 0x1c};
    private final String FLAG = "oren_ctf_z3r0d4y!";

    public String decrypt(byte[] encrypted) {
        StringBuilder msg = new StringBuilder();

        msg.append(FLAG.substring(0, 9));
        for (int i = 0; i < 7; i++) {
            char ch = (char) (FLAG.charAt(i + 9) ^ HASH_PATTERN[i]);
            msg.append(ch);
        }
        msg.append(FLAG.charAt(16));

        return msg.toString();
    }

    public boolean hash(byte[] encryptedLicense) {
        if (encryptedLicense.length != 17) {
            return false;
        }

        int offset = encryptedLicense.length;
        int last = encryptedLicense.length + 1;
        if (encryptedLicense.length % 2 != 0) {
            offset += 1;
            last -= 2;
        }
        offset /= 2;

        for (int i = offset; i < last; i++) {
            if (encryptedLicense[i] != HASH_PATTERN[i - offset]) {
                return false;
            }
        }

        return true;
    }
}
