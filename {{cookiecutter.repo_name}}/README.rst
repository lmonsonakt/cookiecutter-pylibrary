========
Overview
========
{% if cookiecutter._repo_hosting_domain == "github.com" %}
.. start-badges

.. list-table::
    :stub-columns: 1
{% if cookiecutter._sphinx_docs == "yes" %}
    * - docs
      - |docs|
{%- endif %}
    * - tests
      - | {%- if cookiecutter._github_actions == 'yes' %} |github-actions|{% endif -%}
          {%- if cookiecutter._travis == 'yes' %} |travis|{% endif -%}
          {%- if cookiecutter._appveyor == 'yes' %} |appveyor|{% endif -%}
          {%- if cookiecutter._requiresio == 'yes' %} |requires|{% endif -%}
        {{ '' }}
        | {%- if cookiecutter._coveralls == 'yes' %} |coveralls|{% endif -%}
          {%- if cookiecutter._codecov == 'yes' %} |codecov|{% endif -%}
        {{ '' }}
        {%- if cookiecutter._scrutinizer == 'yes' or cookiecutter._codacy == 'yes' or cookiecutter._codeclimate == 'yes' %}
        | {%- if cookiecutter._scrutinizer == 'yes' %} |scrutinizer|{% endif -%}
          {%- if cookiecutter._codacy == 'yes' %} |codacy|{% endif -%}
          {%- if cookiecutter._codeclimate == 'yes' %} |codeclimate|{% endif -%}
        {%- endif -%}
{{ '' }}
{%- if cookiecutter._pypi_badge == "yes" or cookiecutter._repo_hosting_domain == "github.com" %}
    * - package
      - {% if cookiecutter._pypi_badge == "yes" %}| |version| |wheel| |supported-versions| |supported-implementations|
        {{ '' }}{% endif %}
        {%- if cookiecutter._repo_hosting_domain == "github.com" %}| |commits-since|{% endif %}
{%- endif %}
{{ '' }}
{%- if cookiecutter._sphinx_docs == "yes" -%}
{%- if 'readthedocs' in cookiecutter._sphinx_docs_hosting -%}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/
    :alt: Documentation Status
{%- elif 'gitlab' in cookiecutter._sphinx_docs_hosting and 'gitlab' in cookiecutter._repo_hosting_domain -%}
.. |docs| image:: https://{{ cookiecutter._repo_hosting_domain }}/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/badges/{{ cookiecutter._repo_main_branch }}/pipeline.svg
    :target: https://{{ cookiecutter._repo_hosting_domain }}/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name|replace('.', '') }}/commits/{{ cookiecutter._repo_main_branch }}
    :alt: Documentation Status
{% endif %}
{% endif %}
{%- if cookiecutter._travis == 'yes' %}
.. |travis| image:: https://api.travis-ci.com/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}.svg?branch={{ cookiecutter._repo_main_branch }}
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com{% if cookiecutter._repo_hosting == 'github.com' %}/github
                                  {%- elif cookiecutter._repo_hosting == 'gitlab.com' %}/gitlab
                                  {%- endif %}/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter._appveyor == 'yes' %}
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}?branch={{ cookiecutter._repo_main_branch }}&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter._github_actions == 'yes' %}
.. |github-actions| image:: https://github.com/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/actions
{% endif %}
{%- if cookiecutter._requiresio == 'yes' %}
.. |requires| image:: https://requires.io/github/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/requirements.svg?branch={{ cookiecutter._repo_main_branch }}
    :alt: Requirements Status
    :target: https://requires.io/github/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/requirements/?branch={{ cookiecutter._repo_main_branch }}
{% endif %}
{%- if cookiecutter._coveralls == 'yes' %}
.. |coveralls| image:: https://coveralls.io/repos/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch={{ cookiecutter._repo_main_branch }}&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter._codecov == 'yes' %}
.. |codecov| image:: https://codecov.io/gh/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/branch/{{ cookiecutter._repo_main_branch }}/graphs/badge.svg?branch={{ cookiecutter._repo_main_branch }}
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter._codacy == 'yes' %}
.. |codacy| image:: https://img.shields.io/codacy/grade/{{ cookiecutter._codacy_projectid }}.svg
    :target: https://www.codacy.com/app/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}
    :alt: Codacy Code Quality Status
{% endif %}
{%- if cookiecutter._codeclimate == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
   :target: https://codeclimate.com/github/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}
   :alt: CodeClimate Quality Status
{% endif %}
{%- if cookiecutter._pypi_badge == "yes" %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported versions
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
{% endif %}
{%- if cookiecutter._repo_hosting_domain == "github.com" %}
.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter._version }}.svg
    :alt: Commits since latest release
    :target: https://{{ cookiecutter._repo_hosting_domain }}/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter._version }}...{{ cookiecutter._repo_main_branch }}
{% endif %}
{% if cookiecutter._scrutinizer == 'yes' %}
.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/{{ cookiecutter._repo_main_branch }}.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/
{% endif %}

.. end-badges
{% endif %}
{{ cookiecutter.project_short_description|wordwrap(119) }}
{% if cookiecutter._license != "no" %}
* Free software: {{ cookiecutter._license }}
{% endif %}
Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

You can also install the in-development version with::
{% if cookiecutter._repo_hosting_domain == "github.com" %}
    pip install https://github.com/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter._repo_main_branch }}.zip
{% elif cookiecutter._repo_hosting_domain == "gitlab.com" %}
    pip install https://gitlab.com/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}/-/archive/{{ cookiecutter._repo_main_branch }}/{{ cookiecutter.repo_name }}-{{ cookiecutter._repo_main_branch }}.zip
{% else %}
    pip install git+ssh://git@{{ cookiecutter._repo_hosting_domain }}/{{ cookiecutter._repo_username }}/{{ cookiecutter.repo_name }}.git@{{ cookiecutter._repo_main_branch }}
{%- endif %}

Documentation
=============

{% if cookiecutter._sphinx_docs == "yes" %}
{{ cookiecutter._sphinx_docs_hosting }}
{% else %}
To use the project:

.. code-block:: python

    import {{ cookiecutter.package_name }}
    {{ cookiecutter.package_name }}.{{ cookiecutter._c_extension_function }}()
{% endif %}

Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
