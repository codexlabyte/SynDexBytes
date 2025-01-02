class StateChannel:
    def __init__(self, participants):
        self.participants = participants  # List of participants' public keys
        self.balance = {p: 0 for p in participants}  # Off-chain balances
        self.transactions = []  # List of off-chain transactions

    def add_transaction(self, sender, recipient, amount):
        """Add an off-chain transaction."""
        if self.balance[sender] < amount:
            raise ValueError("Insufficient balance")
        self.transactions.append({"sender": sender, "recipient": recipient, "amount": amount})
        self.balance[sender] -= amount
        self.balance[recipient] += amount

    def close_channel(self):
        """Finalize the state channel and broadcast transactions to the main chain."""
        return self.transactions

# Test StateChannel
if __name__ == "__main__":
    channel = StateChannel(["Alice", "Bob"])
    channel.balance["Alice"] = 100
    channel.add_transaction("Alice", "Bob", 30)
    print("Channel Transactions:", channel.close_channel())
