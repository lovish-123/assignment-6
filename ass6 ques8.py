class SumToZero:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_triplets(self):
        triplets = []
        self.numbers.sort()
        for i in range(len(self.numbers) - 2):
            if i > 0 and self.numbers[i] == self.numbers[i - 1]:
                continue
            l = i + 1
            r = len(self.numbers) - 1
            while l < r:
                s = self.numbers[i] + self.numbers[l] + self.numbers[r]
                if s == 0:
                    triplets.append([self.numbers[i], self.numbers[l], self.numbers[r]])
                    l += 1
                    r -= 1
                    while l < r and self.numbers[l] == self.numbers[l - 1]:
                        l += 1
                    while l < r and self.numbers[r] == self.numbers[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return triplets

numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
s = SumToZero(numbers)
print(s.find_triplets()) # [[-10, 2, 8], [-7, -3, 10]]