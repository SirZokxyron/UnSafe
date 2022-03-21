from hashing import UnSafeHash, UnSafeUnHash

VAULT_FILE = "vault.db"

class Database(object):
    def __init__(self) -> None:
        self.Hashed = True
        self.Key = None
        with open(VAULT_FILE, "a"): pass
        self.Load()

    def __str__(self): 
        return str(self.Data)

    def Hash(self) -> bool:
        if self.Hashed:
            return False
        for i in range(len(self.Data)):
            self.Data[i][2] = UnSafeHash(self.Key, self.Data[i][2])
        return True

    def UnHash(self):
        if not self.Hashed or self.Key == None:
            return False
        for i in range(len(self.Data)):
            self.Data[i][2] = UnSafeUnHash(self.Key, self.Data[i][2])
        return True

    def Add(self, NewCombo) -> bool:
        if NewCombo not in self.Data:
            self.Data.append(NewCombo)
            return True
        return False

    def Sub(self, Index) -> bool:
        if NewCombo in self.Data:
            del self.Data[Index]
            return True
        return False

    def Save(self):
        with open(VAULT_FILE, "w") as file:
            file.writelines([" ".join(combo)+'\n' for combo in self.Data])

    def Load(self):
        with open(VAULT_FILE, "r") as file:
            self.Data = [combo.split() for combo in file.readlines()]
