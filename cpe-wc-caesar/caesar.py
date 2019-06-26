#Author : Ilham HaX0r
#Name   : Caesar Chiper Python
class CaesarCipher(object):
    def __init__(self):
        self.L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
        self.I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def encrypt(self, text, key):
        result = ""
        for i in text.upper():
            if i.isalpha(): result += self.I2L[ (self.L2I[i] + key)%26 ]
            else: result += i
        return result

    def decrypt(self, text, key):
        result = ""
        for i in text.upper():
            if i.isalpha(): result += self.I2L[ (self.L2I[i] - key)%26 ]
            else: result += i
        return result

    def brute(self, text):
        for key in range(1, 26):
            result = ""
            for i in text.upper():
                if i.isalpha(): result += self.I2L[ (self.L2I[i] - key)%26 ]
                else: result += i
            print(key, ":", result)
        
tes = CaesarCipher()
print(tes.encrypt("YOU", 5))
print(tes.decrypt("DTZ", 5))
print(tes.brute("DTZ"))
