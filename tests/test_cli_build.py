#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `et-micc-build.cli_build ` CLI."""

from click.testing import CliRunner

from et_micc_build.cli_build import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['-vv'])
    print(result.output)
    assert 'running' in result.output

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_main

    print(f"__main__ running {the_test_you_want_to_debug}")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
# eof
