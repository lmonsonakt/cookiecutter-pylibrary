{%- if cookiecutter._command_line_interface == 'click' %}
from click.testing import CliRunner
{% endif %}
{%- if cookiecutter._c_extension_support != 'no' %}
from {{ cookiecutter.package_name }} import {{ cookiecutter._c_extension_function }}
{%- endif %}
{%- if cookiecutter._command_line_interface != 'no' %}
from {{ cookiecutter.package_name }}.cli import main
{%- endif %}
{%- if cookiecutter._test_matrix_configurator == 'yes' and cookiecutter._test_matrix_configurator == 'no' or
       cookiecutter._command_line_interface == 'no' %}
from {{ cookiecutter.package_name }} import main
{%- endif %}


def test_main():
{%- if cookiecutter._test_matrix_configurator == 'yes' and cookiecutter._test_matrix_configurator == 'no' %}
    assert 'site-packages' in {{ cookiecutter.package_name }}.__file__
{%- endif %}
{%- if cookiecutter._command_line_interface == 'click' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- elif cookiecutter._command_line_interface == 'argparse' %}
    main([])
{%- elif cookiecutter._command_line_interface == 'plain' %}
    assert main([]) == 0
{%- else %}
    pass
{%- endif %}
{%- if cookiecutter._c_extension_support != 'no' %}


def test_{{ cookiecutter._c_extension_function }}():
    assert {{ cookiecutter._c_extension_function }}([b'a', b'bc', b'abc']) == b'abc'
{%- endif %}
