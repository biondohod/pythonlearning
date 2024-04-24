def  meow(n: int) -> str:
    """
    Meows n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows on 1 line
    :rtype: str
    """
    return "meow " * n

    

number: int = int(input("Number: "))

meows: str = meow(number)
print(meows)
