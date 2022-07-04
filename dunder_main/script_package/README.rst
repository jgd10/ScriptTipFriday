script_package
==============

Package to be run as a cli. Created from https://github.com/pyansys/ansys-templates.
This package exists to demonstrate how ``__main__.py`` can be used to create pip-installable scripts.


How to install
--------------

First install the requirements and build the package by running

.. code-block::
    > python -m pip install -r requirements_build.txt
    > python -m build

Access the tarball and whl files in the newly created dist/ directory.

Use one to locally pip install the package.

.. code-block::
    > python -m pip install dist/script_package-0.1.dev0-py3-none-any.whl

Following this all that needs to be done to run the script is:

.. code-block:: bash
    > python -m script_package

e.g.

.. code-block::
    (venv) PS C:\Users\jderrick\script_package> python -m script_package
    2022-06-29 12:28:43.837231

