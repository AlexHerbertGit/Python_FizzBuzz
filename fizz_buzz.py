
def fizz_buzz(up_to_number):
    answer = ""
    i = 0
    while i < up_to_number:
        if i % 3 == 0 and i % 5 == 0 :
            answer = "FizzBuzz"
        elif i % 3 == 0:
            answer = "Fizz"
        elif i % 5 == 0 :
            answer = "Buzz"
        else:
            answer = str(i)
        
        print(i, answer)
        
        i += 1
if __name__ == "__main__":
    fizz_buzz(25)
            