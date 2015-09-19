import unittest

class CeaserCypherDecrypter:
    def decrypt (self, cyphertext):
        result = ""
        for i in cyphertext:
            result = result + chr (ord(i)-3)

        return result



class TestCeaserCypher(unittest.TestCase):
    def decrypt_word(self, word):
        ceaser_cypher_decrypter = CeaserCypherDecrypter()
        return ceaser_cypher_decrypter.decrypt(word)

    def test_zdu_should_decrypt_as_war(self):
        decrypted_value = self.decrypt_word("zdu")

        self.assertEqual(decrypted_value, "war")



if __name__ == '__main__':
    unittest.main()    
