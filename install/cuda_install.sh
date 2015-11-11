#!/bin/bash

# initialize
#cwd=$(pwd)
#cuda_deb=http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb

# download & install cuda
#wget -O cuda.deb $cuda_deb 
ln -s /media/ogawak/ssd21/cuda_related/cuda-repo-ubuntu1404-7-0-local_7.0-28_amd64.deb  cuda.deb
sudo dpkg -i cuda.deb
#sudo apt-get update
sudo apt-get install -y --force-yes cuda
sudo apt-get install -y --force-yes nvidia-prime

# setup vars
cp ~/.bashrc ~/.bashrc_bak
echo "export CUDA_HOME=/usr/local/cuda" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=\$CUDA_HOME/lib64" >> ~/.bashrc
echo "export PATH=\$CUDA_HOME/bin:\$PATH" >> ~/.bashrc

source ~/.bashrc
