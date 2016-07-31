#!/bin/bash
#Se actualiza todos los paquetes del sistema.
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
sudo dpkg-reconfigure locales

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install zlib1g-dev
sudo apt-get -y install libssl-dev
sudo apt-get -y install libsqlite3-dev
sudo apt-get -y install unzip

#Actualización de dependencias para poder instalar el iPython
sudo apt-get -y install build-essential python-dev

#Estas librerias son para scipy, numpy y matplotlib
sudo apt-get -y install libblas-dev liblapack-dev libatlas-base-dev gfortran

sudo apt-get -y install git

sudo apt-get -y install curl

#Se crea una carpeta para descargar los archivos de instalación.
mkdir instaladores

cd instaladores
#Instalo Python 2.9
sudo curl -O https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
sudo unxz Python-2.7.*
sudo tar xf Python-2.7.*

cd Python-2.7.*
sudo ./configure --with-zlib
sudo make
sudo make install

#Vuelvo a instaladores
cd ..

#Se descarga el PIP y se se actualiza sus dependencias principales.
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
cd ..


sudo pip install -U pip
sudo pip install -U setuptools

sudo pip install --upgrade pip

#---------------Esto se hace para garantizar las dependencias de scipy
#Instalación de Numpy
sudo apt-get -y install python-numpy python-scipy
#Instalación de Matplotlib
sudo apt-get -y build-dep python-matplotlib
#----------------

#Para instalar jjguy heatmap
cd instaladores

cd ../..

#Solo para probar
#Estas librerias son para scipy, numpy y matplotlib
sudo apt-get -y install libblas-dev liblapack-dev libatlas-base-dev gfortran

sudo pip install scipy
sudo pip install matplotlib

#Instalación de Scikit-learn según la pagina
sudo apt-get -y install build-essential python-dev python-setuptools \
                     python-numpy python-scipy \
                     libatlas-dev libatlas3gf-base

sudo pip install -U scikit-learn

#Se instala PIL para heatmap
#heatmap.py: create heatmaps in python
# install libjpeg-dev with apt para pillow
sudo apt-get -y install libjpeg-dev
sudo pip install -U Pillow

#Libreria para hacer web scraping
sudo pip install -U beautifulsoup4
#Requests
sudo pip install -U requests

#Instalación del iPython
#sudo pip install ipython\[all\]
sudo pip install "ipython[notebook]"
sudo pip install "ipython[notebook]" --upgrade

sudo unlink /etc/localtime
sudo ln -s /usr/share/zoneinfo/America/Bogota /etc/localtime

#export LC_ALL=C

#export SECRET_KEY="ivf$x-ssn$%pm%^_75qvu2ml55mkdir data2u*l^y@y2&*n0*ic)^28v+l"

#En un archivo llamado .gitignore, poner vagrant_env/.vagrant
#vagrant up
#vagrant ssh
#cd /vagrant
#ipython notebook --ip=0.0.0.0 --no-browser
