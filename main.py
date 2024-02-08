#REMOVE PASS AND FIX THE FUNCTION

def multiply_and_sum(series1, series2):
    if len(series1) != len(series2):
        return "Error: Lists must be the same length."

    else:
        result = sum(x * y for x, y in zip(series1, series2))
        return result

def main():
    # Input series from the user
    series1 = [int(x) for x in input().strip().split()]
    series2 = [int(x) for x in input().strip().split()]

    # Calculate and display the result
    result = multiply_and_sum(series1, series2)
    print(result)

if __name__ == "__main__":
    #run test LR
    main()
