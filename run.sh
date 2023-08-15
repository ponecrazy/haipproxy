#!/bin/bash
log_path="./log"
if [ ! -d "$log_path" ]; then
    mkdir "$log_path"
fi

IS_MAC=""
if [ "$(uname)" == "Darwin" ]; then
  IS_MAC="--is_mac"
fi

nohup python crawler_booter.py --usage crawler common > $log_path/crawler.log 2>&1 &
nohup python scheduler_booter.py --usage crawler common > $log_path/crawler_scheduler.log 2>&1 &
nohup python crawler_booter.py --usage validator init > $log_path/init_validator.log 2>&1 &
nohup python crawler_booter.py --usage validator https tgstat > $log_path/spider_validator.log 2>&1&
nohup python scheduler_booter.py --usage validator https tgstat > $log_path/validator_scheduler.log 2>&1 &

nohup python app_booter.py --host 0.0.0.0 --port 8000 > $log_path/app.log 2>&1 &

nohup python squid_update.py --usage https --interval 3 $IS_MAC > $log_path/squid.log 2>&1 &
nohup python squid_update.py --usage tgstat --interval 3 $IS_MAC > $log_path/squid.log 2>&1 &

rm -rf /var/run/squid.pid
squid -N -d1
