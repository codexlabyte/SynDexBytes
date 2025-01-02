import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.tree = self.build_tree()

    def hash(self, data):
        """Generate a SHA-256 hash."""
        return hashlib.sha256(data.encode()).hexdigest()

    def build_tree(self):
        """Build the Merkle Tree from transactions."""
        nodes = [self.hash(tx) for tx in self.transactions]
        while len(nodes) > 1:
            temp = []
            for i in range(0, len(nodes), 2):
                combined = nodes[i]
                if i + 1 < len(nodes):  # Pair with the next node
                    combined += nodes[i + 1]
                temp.append(self.hash(combined))
            nodes = temp
        return nodes[0] if nodes else None  # Root of the Merkle Tree

# Test the MerkleTree
if __name__ == "__main__":
    transactions = ["tx1", "tx2", "tx3", "tx4"]
    merkle = MerkleTree(transactions)
    print("Merkle Root:", merkle.tree)
