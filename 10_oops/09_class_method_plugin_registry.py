"""
The Statement:
Build a base class BaseParser that maintains a class-level dictionary registry _registry = {}.
Implement a class method @classmethod def register(cls, format_name: str) 
acting as a decorator to register subclasses, 
and another class method @classmethod def get_parser(cls, format_name: str) 
that instantiates and returns the correct registered subclass parser.
"""