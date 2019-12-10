# lsedataset
Spanish Sign Language dataset 

To run this project must install the Python libraries 'pytube' and 'BeautifulSoup'

Instruction to run:
  python crawler urlVideos.txt

## Getting Started

This project will consist of the construction of a video data set, subtitles of sign language people and their corresponding poses

### Prerequisites

To run this project, you need to install some version greater than Python 3 (with pip) and Git.

#### Ubuntu
##### Python

```
Open a Terminal
sudo apt update
sudo apt-get install python3.X 

  X is the number of version
```

##### Pip

```
Open a Terminal
sudo apt update
sudo apt-get install python3-pip
```

##### Git

```
Open a Terminal
sudo apt update
sudo apt-get install git
```

#### Windows

##### Python

```
1. Open a browser window and navigate to the Download page for Windows at python.org.
2. Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x. 
3. Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit. (See below.)
4. Run the installer
```
##### Pip

```
1. Before installing PIP, you’ll need to download get-pip.py: get-pip.py on pypa.io.
2. Open a cmd and navigate to download directory.
3. Run the command:
        python get-pip.py
4. Check the version:
        pip --version
```

##### Git

```
1. To install Git on Windows you will need to download the installer from the Git website:
2. Download the most current version for your operating system by double clicking on the package name:
3. Select Run to begin the installation:
4. Click Yes to continue:
5. Click Next to continue:
```

### Installing

#### Clone or Download the project

```
1. Click to clone or download in the button that it is situated at top of this page.
2. Copy the link if you want clone it and go to 3. or download and unzip the file wherever you want.
3. Go to the directoy you want and execute:
      git clone **link** 
  Where the link is the result of second step
```

#### Install the Requeriments
```
1. Go to the directory 'lsedataset' 
2. Run the command:
      pip install -r Requirements.txt
```

#### Clone or download Openpose

```
1. Go to the directory 'lsedataset' 
  (if you want to go by commmand execute 'cd lsedataset' after clone this project)
2. Go to [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/) and click to clone or download in the button situated at top of that page.
3. Copy the link if you want clone it and go to 3. or download and unzip the file in the new directory.
4. Execute 
      git clone **link** 
  Where the link is the result of second step
```
#### Install Openpose GPU only mode

##### Install Cmake

´´´
**Windows**
1. Install CMake GUI: Download and install the Latest Release of CMake Windows win64-x64 Installer from the CMake download website, called cmake-X.X.X-win64-x64.msi
2. Install Microsoft Visual Studio (VS) 2017 Enterprise with all C++-related flags when selecting the components to install.

**Ubuntu**
1. Run the command:
      sudo apt-get install cmake-qt-gui.
´´´

#### Configure Openpose
´´´

* [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md) - The principal framework to detect the poses
´´´

## Deployment



## Authors

* **Rubén Bernabé Menéndez** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


