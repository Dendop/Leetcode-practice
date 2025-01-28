


class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers
        self.sum_of = 0
        self.count = 0
    
    def sum_list(self):
        for i in self.numbers:
            self.count += 1
            self.sum_of += i
        return self.count, self.sum_of
      
    def mean(self):
        if self.count == 0:
            return 0
        return self.sum_of / self.count
        
       
        
def main():
    numbers = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
    stats = Statistics(numbers)
    
    magic_one = stats.sum_list()# magic one will return two variables count and sum_of
    magic_two = stats.mean()

    print(f"{stats.sum_of}")
    print(magic_two)
    
if __name__ == "__main__":
    main()         
        