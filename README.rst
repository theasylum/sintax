sintax
------

sintax provides a small library and utility for converting Criterion.rs CSV
files into Google's Benchmark JSON format. It also allows you to read in Google
JSON formatted files, and iterate over the list of results, for further
post-processing.

Python versions supported: 3.6, 3.7

Usage
~~~~~

Install the library, and then import sintax.

.. code:: python

    import sintax


If you want to use the command line utility you may do so easily:

.. code:: bash

    sintax.convert -i raw.csv -o benchmark.json


Installation
~~~~~~~~~~~~

.. code:: bash

    pip install sintax

Development
~~~~~~~~~~~

This project uses ``pre-commit`` to automatically verify code style and linting
using ``black`` the Python code formatter.

.. code:: bash

    pre-commit install

Then everytime you run ``git commit`` the code will be verified to match our
style.

You may also run ``black`` directly using ``tox``

.. code:: bash

    tox -e run-black

For running tests and verifying everything continues to work, please run:

.. code:: bash

    tox
