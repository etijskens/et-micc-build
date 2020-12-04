**********
Change log
**********

v0.10.29
--------
* CMake_ extensions

v0.10.28
--------
* Dependence on a more recent version of pybind11_, v.2.6.1, and, by consequence, on a more
  recent version of CMake_: v3.4 (which is not very stringent, as cmake_'s current version
  is 3.19.

* Folder ``et_micc_build/CMaketools`` is removed. The necessary tools are found in
  ``.venv/lib/pythonX.Y/site-packages/pybind11/share/cmake/pybind11``.

v0.10.27
--------
* installation of C++ binary extensions is effected by CMake_ and has to be specified
  the corresponding ``CMakeLists.txt``. This is automatically assured by the templates.
