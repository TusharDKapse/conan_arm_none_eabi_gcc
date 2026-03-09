from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.env import VirtualBuildEnv
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch"
    test_type = "explicit"
    #generators = "VirtualBuildEnv"
    
    def requirements(self):
        self.requires(self.tested_reference_str)

    def test(self):
        if can_run(self):
            src = os.path.join(self.source_folder, "test.c")
            obj = os.path.join(self.build_folder, "test.o")

            # Compile only (no linking, avoids _start warnings)
            self.run(f"arm-none-eabi-gcc -c {src} -o {obj}")

            # Optional: check that compiler runs
            self.run("arm-none-eabi-gcc --version")

            # Optional: check other tools from toolchain
            for tool in ["arm-none-eabi-objcopy", "arm-none-eabi-size"]:
                self.run(f"{tool} --version")
