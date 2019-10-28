import functools

def product(l):
    """Compute the product of all elements of the iterable l."""
    return functools.reduce(times, l)


def times(x, y):
    return x * y

def fib(n):
    """Compute the n-th Fibonacci number.Recursive fib implementations are simpler and simpler code willget you more points. This function does not need to be fast.Note: fib(0) is 0, and fib(1) is 1."""
    raise NotImplementedError()
    
def fac(n):
    """Compute n! (n factorial).Note: fac(0) is 1."""
    raise NotImplementedError()
        
def linear_fib(n):
    """Compute fib(n) in O(n) time using memoization and recursion.Use a global variable and one of the data structures you havelearned about to implement a linear time recursive Fibonacci. Usememoization; it is possible to implement Fibonacci in linear timewithout memoization (using a loop), but that is not theassignment.Remember to look at the Python library documentation for anydata structure needs you have."""
    raise NotImplementedError()