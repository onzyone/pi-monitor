#!/usr/bin/env bash

rrdtool xport -s now-3h -e now --step 300 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:temps1:AVERAGE \
XPORT:a:"temperature" > /opt/projects/monitor/data/temperature3h.xml

rrdtool xport -s now-24h -e now --step 900 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:temps1:AVERAGE \
XPORT:a:"temperature" > /opt/projects/monitor/data/temperature24h.xml

rrdtool xport -s now-48h -e now --step 1800 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:temps1:AVERAGE \
XPORT:a:"temperature" > /opt/projects/monitor/data/temperature48h.xml

rrdtool xport -s now-8d -e now --step 7200 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:temps1:AVERAGE \
XPORT:a:"temperature" > /opt/projects/monitor/data/temperature1w.xml

rrdtool xport -s now-1month -e now --step 10800 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:temps1:AVERAGE \
XPORT:a:"temperature" > /opt/projects/monitor/data/temperature1m.xml

rrdtool xport -s now-3month -e now --step 43200 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:temps1:AVERAGE \
XPORT:a:"temperature" > /opt/projects/monitor/data/temperature3m.xml

rrdtool xport -s now-1y -e now --step 86400 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:temps1:AVERAGE \
XPORT:a:"temperature" > /opt/projects/monitor/data/temperature1y.xml

rrdtool xport -s now-3h -e now --step 300 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:hums1:AVERAGE \
XPORT:a:"humidity" > /opt/projects/monitor/data/humid3h.xml

rrdtool xport -s now-24h -e now --step 900 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:hums1:AVERAGE \
XPORT:a:"humidity" > /opt/projects/monitor/data/humid24h.xml

rrdtool xport -s now-48h -e now --step 1800 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:hums1:AVERAGE \
XPORT:a:"humidity" > /opt/projects/monitor/data/humid48h.xml

rrdtool xport -s now-8d -e now --step 7200 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:hums1:AVERAGE \
XPORT:a:"humidity" > /opt/projects/monitor/data/humid1w.xml

rrdtool xport -s now-1month -e now --step 10800 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:hums1:AVERAGE \
XPORT:a:"humidity" > /opt/projects/monitor/data/humid1m.xml

rrdtool xport -s now-3month -e now --step 43200 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:hums1:AVERAGE \
XPORT:a:"humidity" > /opt/projects/monitor/data/humid3m.xml

rrdtool xport -s now-1year -e now --step 86400 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:hums1:AVERAGE \
XPORT:a:"humidity" > /opt/projects/monitor/data/humid1y.xml

rrdtool xport -s now-3h -e now --step 300 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:lux1:AVERAGE \
XPORT:a:"light" > /opt/projects/monitor/data/lux3h.xml

rrdtool xport -s now-24h -e now --step 900 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:lux1:AVERAGE \
XPORT:a:"light" > /opt/projects/monitor/data/lux24h.xml

rrdtool xport -s now-48h -e now --step 1800 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:lux1:AVERAGE \
XPORT:a:"light" > /opt/projects/monitor/data/lux48h.xml

rrdtool xport -s now-8d -e now --step 7200 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:lux1:AVERAGE \
XPORT:a:"light" > /opt/projects/monitor/data/lux1w.xml

rrdtool xport -s now-1month -e now --step 10800 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:lux1:AVERAGE \
XPORT:a:"light" > /opt/projects/monitor/data/lux1m.xml

rrdtool xport -s now-3month -e now --step 43200 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:lux1:AVERAGE \
XPORT:a:"light" > /opt/projects/monitor/data/lux3m.xml

rrdtool xport -s now-1year -e now --step 86400 \
DEF:a=/opt/projects/monitor/db/monitor.rrd:lux1:AVERAGE \
XPORT:a:"light" > /opt/projects/monitor/data/lux1y.xml

chmod 755 /opt/projects/monitor/data/*
