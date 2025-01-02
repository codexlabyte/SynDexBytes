class ProofOfStake:
    def __init__(self):
        self.stakes = {}  # {address: stake_amount}

    def add_stake(self, address, amount):
        if address not in self.stakes:
            self.stakes[address] = 0
        self.stakes[address] += amount

    def select_validator(self):
        """Select a validator based on stake weight."""
        total_stake = sum(self.stakes.values())
        for address, stake in self.stakes.items():
            if random.uniform(0, total_stake) <= stake:
                return address

# Test PoS
if __name__ == "__main__":
    pos = ProofOfStake()
    pos.add_stake("Alice", 50)
    pos.add_stake("Bob", 30)
    print("Validator:", pos.select_validator())
