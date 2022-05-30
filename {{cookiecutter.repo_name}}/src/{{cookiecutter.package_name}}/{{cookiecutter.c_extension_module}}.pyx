# cython: linetrace=True, language_level=3str

def {{ cookiecutter._c_extension_function }}(args):
    return max(args, key=len)
