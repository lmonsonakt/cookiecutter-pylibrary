__version__ = '{{ cookiecutter._version }}'
{%- if cookiecutter._c_extension_support == 'cffi' %}

from .{{ cookiecutter.__c_extension_module }} import ffi as _ffi
from .{{ cookiecutter.c_extension_module }} import lib as _lib


def {{ cookiecutter._c_extension_function }}(args):
    args = [_ffi.new('char[]', arg) for arg in args]
    result = _lib.{{ cookiecutter._c_extension_function }}(len(args), _ffi.new('char *[]', args))
    if result == _ffi.NULL:
        return ''
    else:
        return _ffi.string(result)
{%- elif cookiecutter._c_extension_support != 'no' %}
{%- if cookiecutter._c_extension_optional == 'yes' %}
try:
    from .{{ cookiecutter.c_extension_module }} import {{ cookiecutter._c_extension_function }}  # noqa
except ImportError:
    def {{ cookiecutter._c_extension_function }}(args):
        return max(args, key=len)
{%- else %}
from .{{ cookiecutter.c_extension_module }} import {{ cookiecutter._c_extension_function }}  # noqa
{%- endif %}
{%- endif %}
