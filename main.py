import time
from src.cryptonote_basic.block import Block
from src.cryptonote_basic.transactions import Transaction
from src.mining.miner import Miner

class Blockchain:
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain = []
        self.difficulty = 1  # Initial difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain."""
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        """Get the most recent block."""
        return self.chain[-1]

    def adjust_difficulty(self, last_block_time, target_time=10):
        """Dynamically adjust difficulty based on mining time."""
        if last_block_time < target_time:
            return self.difficulty + 1
        elif last_block_time > target_time:
            return max(1, self.difficulty - 1)  # Ensure difficulty doesn't go below 1
        return self.difficulty

    def add_block(self, transactions):
        """Add a new block to the blockchain with PoW."""
        last_block = self.get_last_block()
        serialized_transactions = [tx.to_dict() for tx in transactions]
        timestamp = time.time()  # Generate a single timestamp

        # Adjust difficulty based on time taken to mine the last block
        last_block_time = timestamp - last_block.timestamp
        self.difficulty = self.adjust_difficulty(last_block_time)

        # Create a temporary block to generate the block string
        temp_block = Block(len(self.chain), serialized_transactions, last_block.hash, nonce=0, timestamp=timestamp)
        block_string = temp_block.to_string(include_nonce=False)

        # Perform Proof of Work
        nonce, hash_value = Miner.proof_of_work(block_string, self.difficulty)

        # Create and append the new block
        new_block = Block(len(self.chain), serialized_transactions, last_block.hash, nonce, timestamp)

        # Debugging: Print PoW and calculated hashes
        print("PoW Hash:", hash_value)
        print("Block Hash:", new_block.hash)

        if new_block.hash == hash_value:  # Verify the PoW result
            self.chain.append(new_block)
        else:
            raise ValueError("Invalid block hash!")

# Test the Blockchain
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Print the genesis block
    print("Genesis Block:", blockchain.chain[0].hash)

    for i in range(5):
        print(f"\nMining Block {i + 1}...")

        # Create encrypted and plaintext transactions
        tx1 = Transaction("Alice", "Bob", 50, private=True)
        tx2 = Transaction("Bob", "Charlie", 30, private=False)

        start_time = time.time()

        # Add a new block with Proof of Work
        blockchain.add_block([tx1, tx2])

        # Record the end time and calculate elapsed time
        elapsed_time = time.time() - start_time
        print(f"Block {i + 1} mined in {elapsed_time:.2f} seconds")

        # Print the length of the blockchain
        print("Blockchain Length:", len(blockchain.chain))

        # Print the latest block
        latest_block = blockchain.get_last_block()
        print("Latest Block:")
        print(f"  Index: {latest_block.index}")
        print(f"  Transactions: {latest_block.transactions}")
        print(f"  Previous Hash: {latest_block.previous_hash}")
        print(f"  Nonce: {latest_block.nonce}")
        print(f"  Hash: {latest_block.hash}")

        # Print current difficulty
        print("Current Difficulty:", blockchain.difficulty)
