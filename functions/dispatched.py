"""Example for single dispatch
"""

from functools import singledispatch


def show_object_undispatch(obj):
    """Show information about an object
    """
    print(f'Type: {type(obj).__name__}')
    print(f'Value: {obj}')


@singledispatch
def show_object(obj):
    """Show information about an object
    """
    print(f'Type: {type(obj).__name__}')
    print(f'Value: {obj}')


@show_object.register(list)
def _show_object_list(obj):
    """Show information about a list
    """
    print(f'Type: {type(obj).__name__}')
    if len(obj) > 10:
        print(f'Value: {repr(obj[:3])[:-1]} ... {repr(obj[-3:])[1:]}')
    else:
        print(f'Value: {obj}')
    print(f'Length: {len(obj)}')


@show_object.register(tuple)
@show_object.register(list)
def _show_object_sequence(obj):
    """Show information about a list, tuple, and set
    """
    print(f'Type: {type(obj).__name__}')
    if len(obj) > 10:
        print(f'Value: {repr(obj[:3])[:-1]} ... {repr(obj[-3:])[1:]}')
    else:
        print(f'Value: {obj}')
    print(f'Length: {len(obj)}')


def show_string(obj):
    """Show information about a string
    """
    print('String')
    print('======')
    print(f'Type: {type(obj).__name__}')
    if len(obj) > 10:
        print(f'Value: {repr(obj[:3])[:-1]} ... {repr(obj[-3:])[1:]}')
    else:
        print(f'Value: {obj}')
    print(f'Length: {len(obj)}')


show_object.register(str)(show_string)
