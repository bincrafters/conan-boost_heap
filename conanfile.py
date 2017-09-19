from conans import ConanFile, tools, os

class BoostHeapConan(ConanFile):
    name = "Boost.Heap"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-heap"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["heap"]
    requires =  "Boost.Array/1.65.1@bincrafters/stable", \
                      "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Bind/1.65.1@bincrafters/stable", \
                      "Boost.Concept_Check/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Intrusive/1.65.1@bincrafters/stable", \
                      "Boost.Iterator/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Parameter/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable"

                      #array3 assert1 bind3 concept_check5 config0 intrusive6 iterator5 mpl5 parameter10 static_assert1 throw_exception2 type_traits3
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()