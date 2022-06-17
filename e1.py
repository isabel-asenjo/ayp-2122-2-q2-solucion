def reverse(string, new_string):
    if len(string) == 0:
        print(new_string)
    else:
        new_string = new_string + string[-1]
        return reverse(string[:-1], new_string)

def order(numbers, i):
    if i == len(numbers)-1:
        print(numbers)
    elif numbers[i] > numbers[i+1]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        return order(numbers, 0)
    else:
        return order(numbers, i+1)


def main():
    
    order([4,2,8,5,1,3,10], 0)
    print()

    reverse("👍🤠!sotnup 7 ognet aY", "")




main()