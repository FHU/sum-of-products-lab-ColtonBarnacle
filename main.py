#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def multiply_and_sum(series1, series2):
    if len(series1) != len(series2):
        print('error')

    result = sum(x * y for x, y in zip(series1, series2))
    return result

def main():
    series1_str = input("Enter the first series of integers: ")
    series2_str = input("Enter the second series of integers: ")

    series1 = [int(num) for num in series1_str]
    series2 = [int(num) for num in series2_str]

    result = multiply_and_sum(series1, series2)
    print("The sum of multiplying corresponding items is:", result)
        

if __name__ == '__main__':
    main()