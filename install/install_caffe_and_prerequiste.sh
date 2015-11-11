sudo apt-get update
sudo apt-get -y install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get -y install --no-install-recommends libboost-all-dev
sudo apt-get -y install libatlas-base-dev 
sudo apt-get -y install python-dev
sudo apt-get -y install libgflags-dev libgoogle-glog-dev liblmdb-dev 

sudo apt-get -y install python-numpy
sudo apt-get -y install python-skimage
sudo apt-get -y install python-protobuf

sudo apt-get -y install git

BUILD_CAFFE=$HOME/build_caffe
mkdir $BUILD_CAFFE
cd $BUILD_CAFFE
git clone https://github.com/BVLC/caffe.git
cd $BUILD_CAFFE/caffe
cp ./Makefile.config.example ./Makefile.config

make 2> make.err 1> make.log
make pycaffe 2> pycaffe.err 1> pycaffe.log
make test 2> test.err 1> test.log
make runtest 2> runtest.err 1> runtest.log
