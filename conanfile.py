from conan import ConanFile
from conan.tools.files import copy, get
import os

class ArmNoneEabiGccConan(ConanFile):
    name = "arm-none-eabi-gcc"
    version = "15.2"
    package_type = "application"

    settings = "os", "arch"

    exports_sources = "toolchain/*"
    
    def build(self):
        if self.settings.os == "Windows":
            url = ("https://developer.arm.com/-/media/Files/downloads/gnu/"
                   "15.2.rel1/binrel/"
                   "arm-gnu-toolchain-15.2.rel1-mingw-w64-x86_64-arm-none-eabi.zip")
        elif self.settings.os == "Linux":
            url = ("https://developer.arm.com/-/media/Files/downloads/gnu/"
                   "15.2.rel1/binrel/"
                   "arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi.tar.xz")
        else:
            raise Exception("Unsupported OS")

        get(self, url, destination=self.build_folder, strip_root=True)

    def package(self):
        copy(self, "*", src=self.build_folder, dst=self.package_folder)
        
    def package_info(self):
        bin_path = os.path.join(self.package_folder, "bin")
        self.buildenv_info.append_path("PATH", bin_path)
        # Optional environment variables
        self.buildenv_info.define("CC", "arm-none-eabi-gcc")
        self.buildenv_info.define("CXX", "arm-none-eabi-g++")
        self.buildenv_info.define("AR", "arm-none-eabi-ar")
