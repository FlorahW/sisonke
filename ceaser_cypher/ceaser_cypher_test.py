import unittest

class CeaserCypherEncrypter:
    def encrypt(self, plain_text):
        result = ""
        for i in plain_text:
            result = result + chr(ord(i) + 3)
        #result = chr(ord(plain_text[0]) + 3) + chr(ord(plain_text[1]) + 3) + chr(ord(plain_text[2]) + 3)
        return result

class TestCeaserCypher(unittest.TestCase):
    def encrypt_word(self, word):
        ceasercypherencrypter = CeaserCypherEncrypter()
        return ceasercypherencrypter.encrypt(word)

    def test_war_should_encrypt_as_zdu(self):
        encrypted_value = self.encrypt_word("war")

        self.assertEqual(encrypted_value, "zdu")

    def test_warrior_should_encrypt_as_zduulru(self):
        encrypted_value = self.encrypt_word("warrior")
        self.assertEqual(encrypted_value, "zduulru")

    def test_me_should_encrypt_as_ph(self):
        encrypted_value = self.encrypt_word("me")
        self.assertEqual(encrypted_value, "ph")





# class TestStringMethods(unittest.TestCase):

#       def test_upper(self):
#           self.assertEqual('foo'.upper(), 'FOO')

#       def test_isupper(self):
#               self.assertTrue('FOO'.isupper())
#               self.assertFalse('Foo'.isupper())

#       def test_split(self):
#           s = 'hello world'
#           self.assertEqual(s.split(), ['hello', 'world'])
#                   # check that s.split fails when the separator is not a string
#           with self.assertRaises(TypeError):
#               s.split(2)

if __name__ == '__main__':
    unittest.main()
