from typing import NoReturn


def check_not_negative(
    height : float
) -> NoReturn:
    """
    Description
    -----------
    Check Height value is greater than 0
    Parameters
    ----------
    height : float
        height in m
    """

    if height < 0 :
        raise ValueError("height should be grater than zero")



def check_greater_than(
    a: float,
    a_name: str,
    b: float,
    b_name: str,
) -> NoReturn:
    if a > b:
        raise ValueError(f"{a_name} is greater than {b_name}!")



def check_Value_p(
    p : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check p value is greater than 1
    Parameters
    ----------
    p : float
       a constant parameter
    """
    
    if not 1 < p :
        raise ValueError(
            f'p value must be greater than 1: {p}'
        )



def check_Value_a(
    a : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check a value is greater than 0
    Parameters
    ----------
    a : float
        a constant parameter
    """
    
    if not 0 < a :
        raise ValueError(
            f'a value must be greater than 0: {a}'
        )

