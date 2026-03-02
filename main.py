"""Simple script for Fibonacci calculation."""

def fib(n: int) -> int:
    """Return the n-th Fibonacci number using recursion.

    The sequence is defined as::

        fib(0) == 0
        fib(1) == 1
        fib(n) == fib(n-1) + fib(n-2) for n > 1

    This implementation is intentionally naive and exponential in
    time to demonstrate recursion.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # simple command-line interaction
    import sys

    try:
        n = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: python main.py <non-negative-integer>")
        sys.exit(1)

    print(f"fib({n}) = {fib(n)}")
