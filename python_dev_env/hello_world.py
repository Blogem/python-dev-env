"""Hello world."""


import logging


def hello_world(world: str = "world") -> str:
    """Welcome someone or something.

    Args:
        world (str, optional): someone or something. Defaults to "world".
    """
    logging.info("saying hello", world=world)
    return f"hello {world}"


if __name__ == "__main__":
    print(hello_world("python user"))
