import pysnooper

@pysnooper.snoop()
def test():
    digits = [9]
    plus = True
    new_digits = digits
    l_digits = len(digits) - 1
    for i, x in enumerate(digits): 
        if plus:
            if digits[~i] == 9:
                new_digits.append(0)
                if i == l_digits:
                    new_digits.append(1)
                    break
            else:
                new_digits.append((digits[~i]+1))
                plus = False
            
        else:
            new_digits.append(digits[~i])
    
    new_digits.reverse()
    print(new_digits)

def main():
    test()

if __name__ == '__main__':
    main()