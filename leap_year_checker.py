#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Oct 2022
# This program checks if the year is a leap year


def main():

    # This function sees if they can date

    # Input
    year_string = input("Please enter a year: ")
    print("")

    # Process and Output
    try:
        year_int = int(year_string)
        if year_int > 0:
            if year_int % 4 == 0:
                if year_int % 100 != 0:
                    print("{0} is a leap year".format(year_string))
                elif year_int % 400 != 0:
                    print("{0} is not a leap year".format(year_string))
                else:
                    print("{0} is a leap year".format(year_string))
            else:
                print("{0} is not a leap year".format(year_string))
        else:
            print("{0} is not a valid year".format(year_string))
    except ValueError:
        print("{0} is not a valid input".format(year_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
