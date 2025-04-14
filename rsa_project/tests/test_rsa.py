import unittest
from src.rsa import generate_keys, encrypt, decrypt


class TestRSA(unittest.TestCase):

    def test_small_message(self):
        public_key, private_key = generate_keys()
        msg = 12345
        cipher = encrypt(msg, public_key)
        decrypted = decrypt(cipher, private_key)
        self.assertEqual(decrypted, msg)

    def test_zero(self):
        public_key, private_key = generate_keys()
        msg = 0
        cipher = encrypt(msg, public_key)
        decrypted = decrypt(cipher, private_key)
        self.assertEqual(decrypted, msg)

    def test_large_message(self):
        public_key, private_key = generate_keys()
        msg = 987654321
        cipher = encrypt(msg, public_key)
        decrypted = decrypt(cipher, private_key)
        self.assertEqual(decrypted, msg)

    def test_invalid_message_too_large(self):
        public_key, _ = generate_keys()
        msg = public_key[1] + 1  # message > n
        with self.assertRaises(ValueError):
            encrypt(msg, public_key)


if __name__ == '__main__':
    unittest.main()
