"""Example plugin that reverses a string after a discord command."""

from .__about__ import (__author__, __copyright__, __email__, __license__,
                        __summary__, __title__, __uri__, __version__)
from .commands import on_reverse

__all__ = [
    '__author__',
    '__copyright__',
    '__email__',
    '__license__',
    '__summary__',
    '__title__',
    '__uri__',
    '__version__',
]

commands = {
    'reverse': [on_reverse]
}
