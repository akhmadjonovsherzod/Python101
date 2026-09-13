class Cipher:
    def __init__(self, cypher):

        deduped = ""

        for i in cypher.upper():
            if i not in deduped:
                deduped += i
        self.cypher = deduped
        self.plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.cypher_alphabet = self.cypher.upper() + "".join([i for i in self.plain_alphabet if i not in self.cypher])

    def encode(self, data):
        encoded = ""

        for i in data:
            if i.isupper():
                idx = self.plain_alphabet.find(i)

                if idx != -1:
                    encoded += self.cypher_alphabet[idx]
                else:
                    encoded += i
            else:
                idx = self.plain_alphabet.lower().find(i)
                if idx != -1:
                    encoded += self.cypher_alphabet[idx].lower()
                else:
                    encoded += i
        return encoded

    def decode(self, data):
        decoded = ""

        for i in data:
            if i.isupper():
                idx = self.cypher_alphabet.find(i)

                if idx != -1:
                    decoded += self.plain_alphabet[idx]
                else:
                    decoded += i
            else:
                idx = self.cypher_alphabet.lower().find(i)
                if idx != -1:
                    decoded += self.plain_alphabet[idx].lower()
                else:
                    decoded += i
        return decoded


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))
