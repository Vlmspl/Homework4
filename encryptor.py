import random


class Encryption:
    def __init__(self):
        self.encryption_table = {}
        self.retrieved_key = ""

    def __random_number_string(self):
        randstring = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        while randstring in self.encryption_table.values():
            randstring = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        return randstring

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char in self.encryption_table:
                encrypted_text += self.encryption_table[char][0] + " "
            else:
                self.encryption_table[char] = [self.__random_number_string(), char]
                encrypted_text += self.encryption_table[char][0] + " "
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = ""
        table_of_values = encrypted_text.split(" ")
        for num in table_of_values:
            for key, value in self.encryption_table.items():
                if value[0] == num:
                    decrypted_text += value[1]
                    break
        return decrypted_text


Encryptor = Encryption()
EncryptedText = Encryptor.encrypt("the roses are red, the violets are blue")
print(EncryptedText)
DecryptedText = Encryptor.decrypt(EncryptedText)
print(DecryptedText)
