#sudo apt-get -y remove --purge vim vim-runtime vim-gnome vim-tiny vim-common vim-gui-common

#sudo apt-get -y build-dep vim-gnome
 
#sudo apt-get -y install liblua5.1-dev luajit libluajit-5.1 python-dev ruby-dev libperl-dev mercurial libncurses5-dev libgnome2-dev libgnomeui-dev libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libcairo2-dev 
#sudo apt-get -y install libx11-dev libxpm-dev libxt-dev

sudo apt-get -y install liblua5.1-dev luajit libluajit-5.1 mercurial

#sudo rm -rf /usr/local/share/vim

sudo mv /usr/bin/vim /usr/bin/vim.ori
 
sudo mkdir /usr/include/lua5.1/include
sudo mv /usr/include/lua5.1/*.h /usr/include/lua5.1/include/
 
sudo ln -s /usr/bin/luajit-2.0.0-beta9 /usr/bin/luajit
 
mkdir ~/setup/build_vim
cd ~/setup/build_vim
hg clone https://code.google.com/p/vim/
cd vim/src
make distclean
./configure --with-features=huge \
            --enable-rubyinterp \
            --enable-largefile \
            --disable-netbeans \
            --enable-pythoninterp \
            --with-python-config-dir=/usr/lib/python2.7/config \
            --enable-perlinterp \
            --enable-luainterp \
            --with-luajit \
            --enable-gui=auto \
            --enable-fail-if-missing \
            --with-lua-prefix=/usr/include/lua5.1 \
            --enable-cscope 
make 
sudo make install
