DATE=`date '+%Y%m%d%H%M'`
LABEL=$DATE-$1
DST=/media/ogawak/ssd2/bkp/bkp-varliblxc-$LABEL.tar.gz
sudo tar -czvf $DST /var/lib/lxc
