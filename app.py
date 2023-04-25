import argparse


# Program to display the Fibonacci sequence up to n-th term
def fibonacci(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


if __name__ == '__main__':
    # provide CLI arguments
    #  to function
    parser = argparse.ArgumentParser(description='A test program.')
    parser.add_argument(
        "--terms", help="for how many terms should we calculate ?")
    args = parser.parse_args()
    # convert arg to int and start functions
    fibonacci(int(args.terms))
    print('here your fibonacci numbers')
