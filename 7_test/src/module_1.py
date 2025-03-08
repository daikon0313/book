def add_numbers(a, b):
    """add

    Args:
        a (int): 数値1
        b (int): 数値2

    Returns:
        int: 数値3
    """
    return a + b

def all_books(con):
    books = con.execute("SELECT * FROM books").fetchall()
    return books