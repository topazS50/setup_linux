cp ./.bashrc_custom ~/

tar -czvf ./bin.tar.gz ./bin
tar -xzvf ./bin.tar.gz -C ~/

echo "source ~/.bashrc_custom" >> ~/.bashrc

./initialize.sh
