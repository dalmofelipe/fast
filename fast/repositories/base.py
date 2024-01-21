from fast.config.database import get_session


class Base:
    def __init__(self) -> None:
        self.get_session = get_session
