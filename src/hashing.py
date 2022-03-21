HASH_SIZE = 30

def UnSafeHash(Master: str, Password: str) -> str:
    LongMaster = (Master * (HASH_SIZE//len(Master)+1))[:HASH_SIZE]
    LongPassword = (Password * (HASH_SIZE//len(Password)+1))[:HASH_SIZE]
    Hash = [ord(LongMaster[i]) + ord(LongPassword[i]) - len(Master) for i in range(HASH_SIZE)]
    Hash = '$'.join(map(str, Hash))
    Hash = f"{len(Master) + len(Password)}@" + Hash
    return Hash

def UnSafeUnHash(Master: str, Hash: str) -> str:
    LongMaster = (Master * (HASH_SIZE//len(Master)+1))[:HASH_SIZE]
    Size, Hash = Hash.split('@')
    Size = int(Size) - len(Master)
    Hash = list(map(int, Hash.split('$')))
    LongUnHash = [Hash[i] + len(Master) - ord(LongMaster[i]) for i in range(HASH_SIZE)]
    Password = ''.join(map(chr, LongUnHash))
    return Password[:Size]
