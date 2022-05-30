from __future__ import print_function

import datetime
import os
import shutil
import subprocess
import sys
from os.path import join

try:
    from click.termui import secho
except ImportError:
    warn = note = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)


def unlink_if_exists(path):
    if os.path.exists(path):
        os.unlink(path)

if __name__ == "__main__":
{%- if cookiecutter._c_extension_test_pypi == 'yes' %}
{%- if cookiecutter._test_matrix_separate_coverage == 'no' %}
    warn("TODO: c_extension_test_pypi=yes will not work with _test_matrix_separate_coverage=no for now.")
    sys.exit(1)
{%- endif %}
{%- if cookiecutter._c_extension_support == 'no' %}
    warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!      ERROR:                                                                !!
!!                                                                            !!
!!          c_extension_test_pypi=yes is designed to build and publish        !!
!!          platform-specific wheels.                                         !!
!!                                                                            !!
!!          You have set c_extension_support=no, and that will make every     !!
!!          test environment publish duplicated universal wheels.             !!
!!                                                                            !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""")
    sys.exit(1)
{%- endif %}
{%- endif %}

{% if cookiecutter._sphinx_docs == "no" %}
    shutil.rmtree('docs')
    os.unlink('.readthedocs.yml')
{%- elif 'readthedocs' not in cookiecutter._sphinx_docs_hosting %}
    os.unlink('.readthedocs.yml')
{% endif %}

{%- if cookiecutter._command_line_interface == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '__main__.py'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', 'cli.py'))
{% endif %}

{%- if cookiecutter._test_matrix_configurator == 'no' %}
    os.unlink(join('ci', 'templates', 'tox.ini'))
{% endif %}
{%- if cookiecutter._allow_tests_inside_package == 'no' %}
    shutil.rmtree(join('src', '{{ cookiecutter.package_name }}', 'tests'))
{% endif %}
{%- if cookiecutter._c_extension_support == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.c'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py'))
{%- elif cookiecutter._c_extension_support == 'cffi' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx'))
{%- elif cookiecutter._c_extension_support == 'cython' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.c'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py'))
    try:
        subprocess.check_call(['tox', '-e', 'cythonize'])
    except Exception:
        subprocess.check_call([sys.executable, '-mtox', '-e', 'cythonize'])
{%- else %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.pyx'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py'))
{%- endif %}

    unlink_if_exists(join('ci', 'appveyor-with-compiler.cmd'))
{%- if cookiecutter._appveyor == 'no' %}
    os.unlink(join('ci', 'templates', '.appveyor.yml'))
    unlink_if_exists('.appveyor.yml')
{% endif %}
    unlink_if_exists(join('ci', 'templates', 'appveyor.yml'))
    unlink_if_exists('appveyor.yml')
    unlink_if_exists(join('ci', 'appveyor-bootstrap.py'))

{%- if cookiecutter._travis == 'no' %}
    os.unlink(join('ci', 'templates', '.travis.yml'))
    unlink_if_exists('.travis.yml')
{% endif %}

{%- if cookiecutter._github_actions == 'no' %}
    os.unlink(join('ci', 'templates', '.github', 'workflows', 'github-actions.yml'))
    unlink_if_exists(join('.github', 'workflows', 'github-actions.yml'))
{% endif %}

{%- if cookiecutter._repo_hosting == 'no' %}
    os.unlink('CONTRIBUTING.rst')
{% endif %}

{%- if cookiecutter._setup_py_uses_setuptools_scm == 'yes' %}
    os.unlink('MANIFEST.in')
{% endif %}

{%- if cookiecutter._pre_commit == 'no' %}
    os.unlink('.pre-commit-config.yaml')
{% endif %}

{%- if cookiecutter._version_manager == 'bump2version' %}
    os.unlink('tbump.toml')
{%- elif cookiecutter._version_manager == 'tbump' %}
    os.unlink('.bumpversion.cfg')
{% endif %}

{%- if cookiecutter._license == "no" %}
    os.unlink('LICENSE')
{% endif %}

    print("""
################################################################################

    Generating CI configuration ...
""")
    try:
        subprocess.check_call(['tox', '-e', 'bootstrap', '--sitepackages'])
    except Exception:
        try:
            subprocess.check_call([sys.executable, '-mtox', '-e', 'bootstrap', '--sitepackages'])
        except Exception:
            subprocess.check_call([sys.executable, join('ci', 'bootstrap.py')])

    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

    See .cookiecutterrc for instructions on regenerating the project.

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git tag v{{ cookiecutter._version }}
        git remote add origin git@{{ cookiecutter._repo_hosting_domain }}:{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin {{ cookiecutter._repo_main_branch }} v{{ cookiecutter._version }}

{% if cookiecutter._test_matrix_configurator == "yes" %}
    To regenerate your tox.ini, .travis.yml or .appveyor.yml run:
{% else %}
    To regenerate your .travis.yml or .appveyor.yml run:
{% endif %}

        tox -e bootstrap

    You can also run:

        ./ci/bootstrap.py

""")

{%- if cookiecutter._c_extension_test_pypi == 'yes' %}
    note("""
NOTE:

    You are using the c_extension_test_pypi option.

    Make sure you are setting TWINE_PASSWORD as a secret env variable in CI settings:
    - https://ci.appveyor.com/project/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/settings/environment
    - https://travis-ci.com{% if cookiecutter._repo_hosting == 'github.com' %}/github
                           {%- elif cookiecutter._repo_hosting == 'gitlab.com' %}/gitlab
                           {%- endif %}/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/settings
""")
{%- endif %}

    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    while command_line_interface_bin_name.endswith('.py'):
        command_line_interface_bin_name = command_line_interface_bin_name[:-3]

        if command_line_interface_bin_name == '{{ cookiecutter.package_name }}':
            warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!      ERROR:                                                                !!
!!                                                                            !!
!!          Your result package is broken. Your bin script named              !!
!!          {0} !!
!!                                                                            !!
!!          Python automatically adds the location of scripts to              !!
!!          `sys.path`. Because of that, the bin script will fail             !!
!!          to import your package because it has the same name               !!
!!          (it will try to import itself as a module).                       !!
!!                                                                            !!
!!          To avoid this problem you have two options:                       !!
!!                                                                            !!
!!          * Remove the ".py" suffix from the `command_line_interface_bin_name`.                    !!
!!                                                                            !!
!!          * Use a different `__package_name` {1} !!
!!                                                                            !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""".format(
                '"{{ cookiecutter.command_line_interface_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(command_line_interface_bin_name).ljust(32)))
            sys.exit(1)
        break
