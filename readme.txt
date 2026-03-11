
install python
[Linux] sudo apt update
[Linux] sudo apt python3 python3-venv python3-pip
[Windows] install https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe

Create a virtual enviornment
python -m venv conan-venv
 [Linux] source conan-venv/bin/activate
 [Windows-cmd] conan-venv/Scripts/activate.bat
 [Windows-PowerShell] conan-venv/Scripts/Activate.ps1

 python -m pip install conan
 python -m pip install cmake

For Windows
Install https://github.com/msys2/msys2-installer/releases/download/2025-12-13/msys2-x86_64-20251213.exe

Open MSYS2 UCRT64 APP (Terminal)
$ pacman -S mingw-w64-ucrt-x86_64-gcc
$ pacman -S mingw-w64-ucrt-x86_64-make

In sytem envionment variable update path variable with C:\msys64\ucrt64\bin

For Linux
sudo apt install build-essentials

conan create . -s os=Linux -s arch=x86_64
conan create . -s os=Windows -s arch=x86_64
conan create . -s os=Linux -s arch=x86_64 --build=never #if cache has downloaded toolchain, then do not download


