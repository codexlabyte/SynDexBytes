from src.consensus.merkle import MerkleTree

class CrossChainValidator:
    def __init__(self):
        self.chain_roots = {}  # Stores known Merkle roots for external chains

    def register_chain(self, chain_name, merkle_root):
        """Register an external chain's Merkle root."""
        self.chain_roots[chain_name] = merkle_root

    def validate_transaction(self, chain_name, transaction_hash):
        """Validate a transaction by checking the Merkle root."""
        root = self.chain_roots.get(chain_name)
        if not root:
            raise ValueError("Unknown chain")
        # For simplicity, we assume the transaction hash is part of the root.
        return True if transaction_hash in root else False

# Test CrossChainValidator
if __name__ == "__main__":
    validator = CrossChainValidator()
    merkle = MerkleTree(["tx1", "tx2", "tx3", "tx4"])
    validator.register_chain("Bitcoin", merkle.tree)
    print("Is valid transaction:", validator.validate_transaction("Bitcoin", "tx1"))
