import time
import hashlib
import json
from src.cryptonote_basic.transactions import Transaction  # Ensure this is correctly imported

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0, timestamp=None):
        """Initialize a block."""
        self.index = index
        self.timestamp = timestamp or time.time()
        # Use transactions passed from main.py (already serialized)
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def to_string(self, include_nonce=True):
        """Generate a consistent block string for hashing."""
        block_data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce if include_nonce else 0  # Include nonce only if specified
        }

        return json.dumps(block_data, sort_keys=True)

    def calculate_hash(self):
        """Generate a SHA-256 hash of the block's contents."""
        block_string = self.to_string()  # Use the consistent block string
        return hashlib.sha256(block_string.encode()).hexdigest()

# Test the Block class
if __name__ == "__main__":
    # Create example transactions
    tx1 = Transaction("Alice", "Bob", 50, private=True)
    tx2 = Transaction("Bob", "Charlie", 30, private=False)
    transactions = [tx1.to_dict(), tx2.to_dict()]  # Serialize transactions

    # Create the genesis block
    genesis_block = Block(0, transactions, "0")
    print("Genesis Block Hash:", genesis_block.hash)

    # Create a second block
    new_block = Block(1, transactions, genesis_block.hash, 12345)
    print("New Block Hash:", new_block.hash)
