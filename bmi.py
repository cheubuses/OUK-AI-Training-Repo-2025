#!/usr/bin/env python3
"""CLI wrapper for the BMI calculator.

Usage:
  python bmi.py         # prompts for weight and height
  python bmi.py 70 1.75 # use command-line args (weight kg, height m)
"""
import sys
from bmi.bmi_calculator import calculate_bmi, bmi_category


def main(argv=None):
    argv = argv or sys.argv[1:]
    try:
        if len(argv) == 2:
            weight = float(argv[0])
            height = float(argv[1])
        else:
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))

        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi:.2f}")
        print(bmi_category(bmi))
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
