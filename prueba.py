from typing import Optional


def hola(name: str, ne: Optional[str] = None) -> None:
    ne + 2  # type: ignore[operator]
    print('hi ', name)
