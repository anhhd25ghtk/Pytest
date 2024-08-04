def calculate_area_square(length):
    """
    Function  to caculated the area of square
    """

    if not isinstance(length, (int,float)) or length <= 0:
        raise TypeError("Length must be positive non-zero number")
    return length ** 2

