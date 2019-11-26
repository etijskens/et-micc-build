.. highlight:: shell

************
Installation
************

Contrary to `micc <https://github.com/etijskens/et-micc>`_, 
`micc-build <https://github.com/etijskens/et-micc>`_ is automatically a dependency 
of any micc_ project with binary extension modules. So, you just run ``poetry install`` 
in the project's directory to install it in the current Python environment:

.. code-block:: bash

   $ cd path/to/my_micc_project_with_binary_extension_modules
   $ poetry install 
   ... # all dependencies are installed in a virtual environment venv
   $ venv/bin/activate 
   (venv) $ micc-build
   ... # the binary extension modules are built.
   
.. note::

   It is assumed that the Fortran and/or C++ compilers, whichever you need, are 
   just on the system path. They are not a dependency of the project, as users may 
   choose to compile with different compilers, Furthermore, compilers vary between 
   OSes anyway.