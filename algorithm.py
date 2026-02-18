from collections import Counter

# Input for number of random numbers to generate
n = int(input("Enter the range: "))

# xorshift128 generator
def xorshift128():
    x = 123456789
    y = 362436069
    z = 521288629
    w = 88675123

    def _random():
        nonlocal x, y, z, w
        t = x ^ ((x << 11) & 0xFFFFFFFF)  # 32-bit 
        x, y, z = y, z, w
        w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))
        return w

    return _random

# Mersenne Twister RNG class
class mersenne_rng:
    def __init__(self, seed=5489):
        self.state = [0] * 624
        self.f = 1812433253
        self.m = 397
        self.u = 11
        self.s = 7
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        self.index = 624
        self.lower_mask = (1 << 31) - 1
        self.upper_mask = 1 << 31

        self.state[0] = seed
        for i in range(1, 624):
            self.state[i] = self.int_32(
                self.f * (self.state[i - 1] ^ (self.state[i - 1] >> 30)) + i)
        self.twist()

    def twist(self):
        for i in range(624):
            temp = self.int_32(
                (self.state[i] & self.upper_mask) + (self.state[(i + 1) % 624] & self.lower_mask))
            temp_shift = temp >> 1
            if temp % 2 != 0:
                temp_shift = temp_shift ^ 0x9908b0df
            self.state[i] = self.state[(i + self.m) % 624] ^ temp_shift
        self.index = 0

    def get_random_number(self):
        if self.index == 624:
            self.twist()
        y = self.state[self.index]
        y = y ^ (y >> self.u)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)
        self.index += 1
        return self.int_32(y)

    def int_32(self, number):
        return int(0xFFFFFFFF & number)

# Print random numbers in columns (terminal)
def print_in_columns(data, columns=6):
    for i, value in enumerate(data, 1):
        print(f"{value:<15}", end=" ")  # Left aligned, width 15
        if i % columns == 0:
            print()
    if len(data) % columns != 0:
        print()

# Print frequencies in columns (terminal)
def print_freq_in_columns(freq_list, columns=6):
    for i, (num, count) in enumerate(freq_list[:100], 1):  # Show first 100 frequencies in terminal
        print(f"{num:>12} : {count:<5}", end=" ")  # Right aligned num, left aligned count
        if i % columns == 0:
            print()
    if len(freq_list[:100]) % columns != 0:
        print()

# Write random numbers in columns (file)
def write_in_columns(f, data, columns=6):
    for i, value in enumerate(data, 1):
        f.write(f"{value:<15} ")  # Left aligned, width 15
        if i % columns == 0:
            f.write("\n")
    if len(data) % columns != 0:
        f.write("\n")

# Write frequencies in columns (file)
def write_freq_in_columns(f, freq_list, columns=6):
    for i, (num, count) in enumerate(freq_list, 1):
        f.write(f"{num:>12} : {count:<5} ")  # Right aligned num, left aligned count
        if i % columns == 0:
            f.write("\n")
    if len(freq_list) % columns != 0:
        f.write("\n")

def main():
    choice = input("Choose RNG (1: xorshift128, 2: mersenne_twister): ")

    if choice == '1':
        r = xorshift128()
        random_numbers = [r() for _ in range(n)]
    elif choice == '2':
        rng = mersenne_rng(1131464071)
        random_numbers = [rng.get_random_number() for _ in range(n)]
    else:
        print("Invalid choice")
        return

    print(f"Sample size: {n}")
    print("Generated random numbers:")
    print_in_columns(random_numbers[:100], columns=6)  # Show first 100 random numbers in terminal

    frequency = Counter(random_numbers)
    sorted_freq = sorted(frequency.items(), key=lambda x: -x[1])

    print("\nFrequency of each number:")
    print_freq_in_columns(sorted_freq, columns=6)  # Show first 100 frequencies in terminal

    with open("random_numbers.txt", "w") as f:
        # Write all random numbers in columns to file
        write_in_columns(f, random_numbers, columns=6)

        f.write("\nFrequency of each number:\n")
        # Write all frequencies in columns to file
        write_freq_in_columns(f, sorted_freq, columns=6)

    print("Random numbers and frequencies saved to random_numbers.txt")

if __name__ == "__main__":
    main()
