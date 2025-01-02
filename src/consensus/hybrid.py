from src.mining.miner import Miner
from src.consensus.pos import ProofOfStake
import random

class HybridConsensus:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.pos = ProofOfStake()

    def proof_of_work(self, last_hash):
        """Perform Proof of Work mining."""
        return Miner.proof_of_work(last_hash, self.difficulty)

    def select_validator(self):
        """Select a validator using Proof of Stake."""
        return self.pos.select_validator()

    def decide_next_block_creator(self):
        """Randomly choose between PoW and PoS for the next block."""
        return "PoW" if random.random() > 0.5 else "PoS"

# Test HybridConsensus
if __name__ == "__main__":
    hybrid = HybridConsensus()
    last_hash = "0"  # Simulate the genesis block hash

    next_block_method = hybrid.decide_next_block_creator()
    if next_block_method == "PoW":
        nonce, hash_value = hybrid.proof_of_work(last_hash)
        print(f"Block mined using PoW: Nonce={nonce}, Hash={hash_value}")
    else:
        hybrid.pos.add_stake("Alice", 50)
        hybrid.pos.add_stake("Bob", 30)
        validator = hybrid.select_validator()
        print(f"Block validated using PoS by: {validator}")
