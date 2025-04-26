.. include:: ../README.rst
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.project_short_description }}

Installation
============

Install with pip:

.. code-block:: bash

    pip install {{ cookiecutter.project_slug }}

Or install in editable mode for development:

.. code-block:: bash

    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
    cd {{ cookiecutter.project_slug }}
    pip install -e .

Usage
=====

Import the package:

.. code-block:: python

    import {{ cookiecutter.package_name }}

Then use it!

.. code-block:: python

    result = {{ cookiecutter.package_name }}.your_function()
    print(result)

Examples
========

See the `Notebooks/` folder for Jupyter notebooks demonstrating package usage.

- `Notebooks/example_conversion.ipynb <Notebooks/example_conversion.ipynb>`_

Contributing
============

Contributions are welcome!  
Please read the `CONTRIBUTING.rst <CONTRIBUTING.rst>`_ guide first.

License
=======

This project is licensed under the {{ cookiecutter.open_source_license }} License. See the `LICENSE <LICENSE>`_ file for details.

