#!/bin/bash
nohup python crawler_booter.py --usage crawler common > crawler.log 2>&1 &
nohup python scheduler_booter.py --usage crawler common > crawler_scheduler.log 2>&1 &
nohup python crawler_booter.py --usage validator init > init_validator.log 2>&1 &
nohup python crawler_booter.py --usage validator https tgstat > https_validator.log 2>&1&
nohup python scheduler_booter.py --usage validator https tgstat > validator_scheduler.log 2>&1 &

nohup python app_booter.py --port 6000 > app.log 2>&1 &

nohup python squid_update.py --usage https --interval 3 > squid.log 2>&1 &
rm -rf /var/run/squid.pid
squid -N -d1
