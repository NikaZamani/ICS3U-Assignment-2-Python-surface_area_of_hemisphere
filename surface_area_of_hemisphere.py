#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program calculates the surface area of a hemisphere
#     where the user gets to enter the radius in mm

import math


def main():
    # main function
    print("We will be calculating the surface area of a hemisphere. ")
    # input
    radius = int(input("Enter the radius (mm): "))
    # process
    surface area = 3 * 3.14 * radius * radius
    # output
    print("Surface Area is {} mm²".format(surface area))


if __name__ == "__main__":
    main()
