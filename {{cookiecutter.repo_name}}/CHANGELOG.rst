
Changelog
=========
{% set datestring -%}
{% if cookiecutter._release_date == 'today' -%}
{% now 'utc', '%Y-%m-%d' %}
{%- else %}{{ cookiecutter._release_date }}{% endif %}
{%- endset %}
{{ cookiecutter._version }} ({{ datestring }})
{% for _ in cookiecutter._version %}-{% endfor %}--{{ '-' * (datestring|length) }}-

* First release on PyPI.
