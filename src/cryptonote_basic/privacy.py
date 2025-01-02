from cryptography.fernet import Fernet

class Privacy:
    def __init__(self):
        # Generate a symmetric key for encryption/decryption
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """Encrypt data (convert dictionary to bytes before encryption)."""
        data_bytes = str(data).encode()
        return self.cipher.encrypt(data_bytes)

    def decrypt(self, encrypted_data):
        """Decrypt data and convert bytes back to dictionary."""
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return eval(decrypted_data.decode())

# Test the privacy module
if __name__ == "__main__":
    privacy = Privacy()
    transaction = {"sender": "Alice", "recipient": "Bob", "amount": 50}
    encrypted = privacy.encrypt(transaction)
    print("Encrypted:", encrypted)
    decrypted = privacy.decrypt(encrypted)
    print("Decrypted:", decrypted)
