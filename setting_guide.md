- Openpilot commit hash value: `c9679222aebfcbf0dcce7ac00d2e03d19101a81f`
- Enviroment: Ubuntu 20.04.1 LTS

## Download Submodule
```
git submodule init
git submodule update --recursive
```

## Install QT5
- The version of QT should be bigger than `5.10`
```
sudo apt install qt5-default qtmultimedia5-dev
```

## Set Enviroment
- Install dependencies
```
cd openpilot
cd tools
./ubuntu_setup.sh
```

- Set pyenv enviroment: Add below context in .bashrc or .zshrc
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

## Add openpilot's path in sys.path
```
python -c 'import sys; print(sys.path)'
```

1. Find the path of the folder which is like `.../site-packages`
2. Create a new file `openpilot.pth` in the folder.
3. Add the path of openpilot folder in the file(like: `/home/.../openpilot`).


## Compile via scons
```
cd openpilot
scons
```

## Install Carla
```
cd openpilot/tools/sim
./install_carla.sh
```
- [Linux Build](https://carla.readthedocs.io/en/latest/build_linux/)

### Trouble Shoot
- Cannot install llvm8 because of dependencies issue
    - [Remove `deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main` from /etc/apt/sources.list](https://github.com/carla-simulator/carla/issues/3441)
