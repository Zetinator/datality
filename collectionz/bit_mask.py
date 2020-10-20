class BitMask:
    """implements some useful bitwise operations

    https://visualgo.net/en/bitmask
    """

    @staticmethod
    def set(number: int, index: int) -> int:
        """sets a 1 at the bit positioned at `index`

        Args:
            number (int): number to toggle bits on
            index (int): position

        Returns:
            int: integer after bitwise operation
        """
        return number | (1 << index)

    @staticmethod
    def toggle(number: int, index: int) -> int:
        """toggle the bit at the given `index`

        Args:
            number (int): number to toggle bits on
            index (int): position

        Returns:
            int: integer after bitwise operation
        """
        return number ^ (1 << index)

    @staticmethod
    def reset(number: int, index: int) -> int:
        """resets the bit at the given `index`

        Args:
            number (int): number to toggle bits on
            index (int): position

        Returns:
            int: integer after bitwise operation
        """
        number = number | (1 << index)
        return number ^ (1 << index)

    @staticmethod
    def check(number: int, index: int) -> bool:
        """check the bit at the given `index` if it's a 1

        Args:
            number (int): number to toggle bits on
            index (int): position

        Returns:
            int: integer after bitwise operation
        """
        return bool(number & (1 << index))

    @staticmethod
    def clear(number: int) -> int:
        """resets all the bits

        Args:
            number (int): number to toggle bits on

        Returns:
            int: integer after bitwise operation
        """
        return number & 0
