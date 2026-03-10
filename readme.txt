conan create . -s os=Linux -s arch=x86_64
conan create . -s os=Linux -s arch=x86_64 --build=never #if cache has downloaded toolchain, then do not download
