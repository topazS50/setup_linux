if [ -e /dev/sdb1 ]; then
  FLAG=`mount | grep sdb1 | wc -l`
  if [ $FLAG == "0" ]; then
    echo "kpThefc1Vivo" | sudo -S mkdir -p /media/ogawak/ssd2
    echo "kpThefc1Vivo" | sudo -S mount /dev/sdb1 /media/ogawak/ssd2
  fi
fi

export PYTHONPATH=/home/ogawak/build_caffe/caffe/python/
source ~/.bashrc_local
