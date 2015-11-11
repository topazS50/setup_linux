DATE=`date '+%Y%m%d%H%M'`
LABEL=$DATE-$1
DST=/media/ogawak/ssd2/bkp/du-sys-$LABEL.log
sudo du --exclude --exclude /media/* --exclude /sys/* --exclude /var/lib/lxc --exclude /proc/kcore --execlude /initrd.img --execlude /initrd.img.old
DST=/media/ogawak/ssd2/bkp/du-home-$LABEL.log
sudo du /home/ogawak > $DST
