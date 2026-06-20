#!/usr/bin/env python3
"""
TRIZ Contradiction Matrix lookup helper.

Usage:
    python3 lookup.py <improving_param_number> <worsening_param_number>
    python3 lookup.py 14 1
    -> Strength (improve) vs Weight of moving object (worsen): principles [1, 8, 40, 15]

    python3 lookup.py --list-params
    -> prints all 39 parameters with numbers

    python3 lookup.py --principle 35
    -> prints the name of inventive principle 35

Run from the references/ directory, or pass an explicit --data path.
"""
import json
import sys
import os
import argparse


def load_data(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contradiction_matrix.json")
    with open(path) as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="TRIZ Contradiction Matrix lookup")
    parser.add_argument("improving", nargs="?", type=int, help="Improving parameter number (1-39)")
    parser.add_argument("worsening", nargs="?", type=int, help="Worsening parameter number (1-39)")
    parser.add_argument("--list-params", action="store_true", help="List all 39 parameters")
    parser.add_argument("--list-principles", action="store_true", help="List all 40 principles")
    parser.add_argument("--principle", type=int, help="Look up a single principle's name by number")
    parser.add_argument("--data", type=str, default=None, help="Path to contradiction_matrix.json")
    args = parser.parse_args()

    data = load_data(args.data)
    params = {int(k): v for k, v in data["parameters"].items()}
    principles = {int(k): v for k, v in data["principles"].items()}
    matrix = data["matrix"]

    if args.list_params:
        for i in range(1, 40):
            print(f"{i:2d}. {params[i]}")
        return

    if args.list_principles:
        for i in range(1, 41):
            print(f"{i:2d}. {principles[i]}")
        return

    if args.principle:
        print(f"{args.principle}. {principles.get(args.principle, 'unknown')}")
        return

    if args.improving is None or args.worsening is None:
        parser.print_help()
        sys.exit(1)

    i, j = args.improving, args.worsening
    if i == j:
        print("Improving and worsening parameters must differ.")
        sys.exit(1)
    if not (1 <= i <= 39 and 1 <= j <= 39):
        print("Parameters must be in range 1-39. Use --list-params to see the list.")
        sys.exit(1)

    key = f"{i}-{j}"
    result = matrix.get(key)

    print(f"Improving: {i}. {params[i]}")
    print(f"Worsening: {j}. {params[j]}")
    print()
    if not result:
        print("No dominant principle recorded for this pairing in Altshuller's original matrix.")
        print("Try reformulating the contradiction with different parameters, or consider all 40 principles.")
    else:
        print("Suggested Inventive Principles (in Altshuller's frequency order):")
        for p in result:
            print(f"  {p}. {principles[p]}")


if __name__ == "__main__":
    main()
