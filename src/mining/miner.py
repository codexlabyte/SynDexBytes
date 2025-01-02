import hashlib
import json
import time

class Miner:
    @staticmethod
    def proof_of_work(block_string, difficulty=1):
        """Perform Proof of Work to find a valid nonce."""
        prefix = '0' * difficulty
        nonce = 0
        while True:
            hash_attempt = hashlib.sha256(block_string.encode()).hexdigest()
            if hash_attempt.startswith(prefix):
                return nonce, hash_attempt
            nonce += 1

# Test the miner
if __name__ == "__main__":
    # Test with a simulated block string
    block_string = "0[{'sender': 'Alice', 'recipient': 'Bob', 'amount': 50}]previous_hash"
    difficulty = 1
    nonce, hash_value = Miner.proof_of_work(block_string, difficulty)
    print(f"Nonce: {nonce}, Hash: {hash_value}")

