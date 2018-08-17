from conans import ConanFile, CMake, tools


class MiniupnpcConan(ConanFile):
    name = "miniupnpc"
    version = "2.1"
    license = "Thomas BERNARD All rights reserved"
    url = "https://github.com/rhard/conan-miniupnpc"
    description = "MiniUPnP client - an UPnP IGD control point"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/miniupnp/miniupnp.git")
        self.run("cd miniupnp && git checkout master")
        tools.replace_in_file("miniupnp/miniupnpc/CMakeLists.txt", "project (miniupnpc C)",
                              '''PROJECT(miniupnpc C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["UPNPC_BUILD_TESTS"] = "OFF"
        cmake.definitions["UPNPC_BUILD_SAMPLE"] = "OFF"
        if self.options.shared:
            cmake.definitions["UPNPC_BUILD_STATIC"] = "OFF"
            cmake.definitions["UPNPC_BUILD_SHARED"] = "ON"
        else:
            cmake.definitions["UPNPC_BUILD_STATIC"] = "ON"
            cmake.definitions["UPNPC_BUILD_SHARED"] = "OFF"
        cmake.configure(source_folder="miniupnp/miniupnpc")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="miniupnp/miniupnpc")
        self.copy("*miniupnpc.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = ["libminiupnpc", "ws2_32", "iphlpapi"]
        else:    
            self.cpp_info.libs = ["miniupnpc"]
        if not self.options.shared:
            self.cpp_info.defines.append("MINIUPNP_STATICLIB")


    def configure(self):
        del self.settings.compiler.libcxx
