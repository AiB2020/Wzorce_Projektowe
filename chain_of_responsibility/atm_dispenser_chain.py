"The ATM Dispenser Chain"
from dispenser10 import Dispenser10
from dispenser20 import Dispenser20
from dispenser50 import Dispenser50


class ATMDispenserChain: 
    "The Chain Client"

    def __init__(self):
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)