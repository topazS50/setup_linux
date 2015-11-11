DATE=`date '+%Y%m%d%H%M'`
LABEL=$DATE-$1
DST=/media/ogawak/ssd2/bkp/bkp-sys-$LABEL.tar.gz
sudo tar -czvf $DST / --exclude /media/* --exclude /home/* --exclude /var/lib/lxc --exclude /proc/kcore
#sudo tar -czvf $DST / --exclude /media/* --exclude /home/* --exclude *lxc* --exclude /proc/kcore
sudo du / > /media/ogawak/ssd2/bkp/du-$LABEL.log
