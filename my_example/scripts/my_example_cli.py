import multiprocessing
import argparse
import logging

from my_example.my_example_code import my_example_addition_function


def main():

    logger = multiprocessing.log_to_stderr()
    logger.setLevel(level=logging.WARNING)

    parser = argparse.ArgumentParser(
        description="my example adds two numbers!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        usage=argparse.SUPPRESS,
    )

    parser.add_argument("a", type=int, help="value 1")
    parser.add_argument("b", type=int, help="value 2")

    args = parser.parse_args()

    logging.info("calling my super cool library")

    result = my_example_addition_function(args.a, args.b)

    print(f"{args.a} + {args.b} = {result}")
