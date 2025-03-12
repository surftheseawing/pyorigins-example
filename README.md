# Build Instructions

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
  - Alternatively you can use your favourite Python IDE.
2. Download and install [Git](https://git-scm.com).
  - Alternatively, download the repository as a `.zip` archive and extract it.
3. Download this repository.
    ```
    > git clone https://github.com/surftheseawing/pyorigins-example
    > cd pyorigins-example/
    ```
4. Download and install [Python](https://www.python.org/).
  - Check version.
    ```
    > py -3 --version
    Python 3.9.4
    ```
5. Install [bump](https://github.com/di/bump).
    ```
    > py -3 -m pip install bump
    ```
  - You can use `bump` to increase the version number in `setup.py`.
6. Build the data pack.
    ```
    > py -3 build.py
    ```
  - The `__pycache__` folder contains intermediate binary files used by Python. You can safely ignore them.
  - The `archive` folder contains the built data packs.
  - The `build` folder contains the contents of the latest built data pack.
7. Copy the data pack archive to the `datapacks` folder of a Minecraft world with Origins installed to test it.
  - For example, `E:\curseforge\minecraft\Instances\Test\saves\New World\datapacks\template_v0.1.0.zip`.
