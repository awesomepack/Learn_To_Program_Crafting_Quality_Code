def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    
    >>> num_buses(75)
    2

    >>> num_buses(0)
    0

    >>> num_buses(999999)
    20000
    """
    return round(n / 50)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)

    >>> stock_price_summary([0.01 , 0.03 , 0.02 , 0.25])
    (0.31, 0)

    >>> stock_price_summary([-.01 , -.03 , -.02 , -.25])
    (0, -0.31)

    >>> stock_price_summary([])
    (0, 0)

    >>> stock_price_summary([.09])
    (0.09, 0)

    >>> stock_price_summary([-.09])
    (0, -0.09)
    """
  # Group values of the same sign into lists
    pos = [price for price in price_changes if price >= 0]
    neg = [price for price in price_changes if price < 0]

    return (sum(pos),sum(neg))


    


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> swap_k([1, 2, 3, 4, 5, 6], 2)
    [5, 6, 3, 4, 1, 2]

    >>> swap_k([] , 0)
    []

    >>> swap_k([-1,2,3,-4] , 2)
    [3, -4, -1, 2]

    >>> swap_k([1,2,3,4,5,6,7,8,9,10,11] , 5)
    [7, 8, 9, 10, 11, 6, 1, 2, 3, 4, 5]

    >>> swap_k([1,2,3] , 1)
    [3, 2, 1]

    
    """

    L_F = [L[x] for x in range(-k , 0)]
    F_L = [L[x] for x in range(0 , k)]
    m = L[k:-k]

    return L_F + m + F_L


if __name__ == '__main__':
    import doctest
    doctest.testmod()