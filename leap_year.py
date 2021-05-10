#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program checks if year is a leap year or not


def main():
    # this function checks if year is a leap year or not

    # input
    year_as_string = input("Enter the year: ")
    print("")

    # process & output
    try:
        year_as_number = int(year_as_string)

        if (year_as_number % 4) == 0:
            if (year_as_number % 100) == 0:
                if (year_as_number % 400) == 0:
                    print("{0} is a leap year.".format(year_as_number))
                else:
                    print("{0} is a common year.".format(year_as_number))
            else:
                print("{0} is a leap year.".format(year_as_number))
        else:
            print("{0} is a common year.".format(year_as_number))
    except Exception:
        print("That was not valid input.")


if __name__ == "__main__":
    main()
