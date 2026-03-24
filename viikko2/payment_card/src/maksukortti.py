EDULLINEN = 250
MAUKAS = 400

class Maksukortti:
    def __init__(self, saldo):
        self.saldo = saldo

    def syo_edullisesti(self):
        if self.saldo >= EDULLINEN:
            self.saldo -= EDULLINEN

    def syo_maukkaasti(self):
        if self.saldo >= MAUKAS:
            self.saldo -= MAUKAS

    def lataa_rahaa(self, maara):
        if maara < 0:
            return
        self.saldo += maara
        if self.saldo > 15000:
            self.saldo = 15000

    def __str__(self):
        return f"Kortilla on rahaa {self.saldo / 100:.2f} euroa"
