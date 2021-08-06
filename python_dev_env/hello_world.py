"""Hello world."""


from structlog import get_logger


logger = get_logger(__name__)


def hello_world(world: str = "world") -> str:
    """Welcome someone or something.

    Args:
        world (str, optional): someone or something. Defaults to "world".
    """
    logger.info("saying hello", world=world)
    return f"hello {world}"


if __name__ == "__main__":
    hello_world("python user")
