import time
from src.cryptonote_basic.privacy import Privacy

class Transaction:
    def __init__(self, sender, recipient, amount, private=False):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        self.private = private
        self.privacy = Privacy() if private else None

    def to_dict(self):
        """Convert transaction to dictionary format."""
        if self.private and self.privacy:
            # Ensure private transactions are encrypted before being added to the block
            encrypted_data = self.privacy.encrypt({
                'sender': self.sender,
                'recipient': self.recipient,
                'amount': self.amount,
                'timestamp': self.timestamp
            })
            return {'private_data': encrypted_data.decode()}  # Ensure bytes are decoded to a string
        else:
            return {
                'sender': self.sender,
                'recipient': self.recipient,
                'amount': self.amount,
                'timestamp': self.timestamp
            }

# Test the Transaction class
if __name__ == "__main__":
    tx = Transaction("Alice", "Bob", 10, private=True)
    print("Transaction:", tx.to_dict())

