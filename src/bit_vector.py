class BitVector:
    def __init__(self):
        self.bits = 0

    def set(self, index, value):
        self.bits = (self.bits & ~(1 << index)) | (value << index)

    def get(self, index):
        just_that_one = 1 << index
        return (self.bits & just_that_one) != 0

v = BitVector()
print(v.get(5))
v.set(5, 1)
print(v.get(5))
v.set(5, 0)
print(v.get(5))

