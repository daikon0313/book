def is_leap_year(year: int) -> bool:
    """閏年か判定する

    Args:
        year (int): 調べたい年

    Returns:
        bool: 閏年の場合はTrue、そうでない場合はFalse
    """
    if year % 4:
        return False
    # 例外
    if year % 100 == 0 and year % 400 != 0:
        return False

    return True