#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostHeapConan(base.BoostBaseConan):
    name = "boost_heap"
    url = "https://github.com/bincrafters/conan-boost_heap"
    lib_short_names = ["heap"]
    header_only_libs = ["heap"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_bind",
        "boost_concept_check",
        "boost_config",
        "boost_intrusive",
        "boost_iterator",
        "boost_parameter",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]
