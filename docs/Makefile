# Minimal makefile for Sphinx documentation
# Execute this file as from the project`s directory as:
#  > cd path/to/project/docs        # where the Makefile is located
#  > source ../.venv/bin/activate   # activate the project's virtual environment
#  (.venv) > make                   # to generate help
#  (.venv) > make html              # to generate documentation in html format
#  (.venv) > make latexpdf          # to generate documentation in pfd format

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = micc
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile venv deps

# Verify that the right virtual environment is activated
venv:
	@if [ "$$VIRTUAL_ENV" == "" ]; then echo "ERROR: .venv not activated: expecting '`realpath ../.venv`' to be activated."; exit 1; fi
	@if [ "$$VIRTUAL_ENV" -ef "../.venv/" ]; then : ; else echo "ERROR: wrong .venv: expecting '`realpath ../.venv`'"; exit 1; fi

# Install the necessary dependendies for documenting the project.
deps:
	@pip show click            >/dev/null && if [ $$? -eq 0 ]; then echo "Installed: click"           ; else pip install click           ; fi
	@pip show sphinx-click     >/dev/null && if [ $$? -eq 0 ]; then echo "Installed: sphinx-click"    ; else pip install sphinx-click    ; fi
	@pip show sphinx           >/dev/null && if [ $$? -eq 0 ]; then echo "Installed: sphinx"          ; else pip install sphinx          ; fi
	@pip show sphinx-rtd-theme >/dev/null && if [ $$? -eq 0 ]; then echo "Installed: sphinx-rtd-theme"; else pip install sphinx-rtd-theme; fi

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile deps
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
