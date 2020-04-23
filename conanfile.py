#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class JsonRpcCxxConan(ConanFile):
    name = "json-rpc-cxx"
    version = "0.1.0"
    license = "MIT"
    author = "Alexander Zaitsev zamazan4ik@tut.by"
    url = "https://github.com/ZaMaZaN4iK/conan-json-rpc-cxx"
    homepage = "https://github.com/jsonrpcx/json-rpc-cxx"
    description = "JSON-RPC for modern C++"
    topics = ("json-rpc", "cpp17")
    no_copy_sources = True
    requires = "jsonformoderncpp/3.7.0"

    _source_subfolder = "source_subfolder"

    def source(self):
        checksum = "e5c9747327d747872b2f3fb787679baccdf8ff5515177b8029310f6c3b89520f"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=checksum)      
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy("*hpp", dst="include", src=os.path.join(self._source_subfolder, "include"))
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)

    def package_info(self):
        self.info.header_only()
