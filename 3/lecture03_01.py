from FizzBuzzBase import FizzBuzzBase

class FizzBuzz(FizzBuzzBase):

    __DEFAULT_LOOP_TIME = 20

    def __init__(self, max_count=__DEFAULT_LOOP_TIME):
        super().__init__(max_count)

    def __convert(self,input : int) -> str:
        if input%3 == 0:
            if input%5 == 0:
                result_str = "FizzBuzz"
            else: result_str = "Fizz"
        elif input%5 == 0:
            result_str = "Buzz"
        else: result_str = str(input)
        return result_str

    def print_fizzbuzz(self,max_count : int) -> None:
        for i in range(max_count):
            print(self.__convert(i+1))

if __name__ == '__main__':
    test = FizzBuzz(10)
    print("-----------------------")
    test = FizzBuzz()
    print("-----------------------")
    test = FizzBuzz(30)