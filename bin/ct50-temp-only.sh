#!/usr/bin/env bash

THERMOSTAT_IP=${1}
THERMOSTAT_HOSTNAME=RT
ZABBIX_SENDER="zabbix_sender -z 127.0.0.1 --host ${THERMOSTAT_HOSTNAME} --input-file -"

if [ -z "${THERMOSTAT_IP}" ]; then
  THERMOSTAT_IP=$(ping -c 1 ${THERMOSTAT_HOSTNAME} >/dev/null 2>&1 && echo ${THERMOSTAT_HOSTNAME})
  if [ -z "${THERMOSTAT_IP}" ]; then
    echo 0
    exit
  fi
fi

DATA_URLS=(\
 '/tstat/temp'
# '/tstat {"temp":72.50,"tmode":1,"fmode":0,"override":0,"hold":0,"t_heat":62.00,"tstate":0,"fstate":0,"time":{"day":4,"hour":23,"minute":20},"t_type_post":0}' \
# '/tstat/ttemp {"t_heat":62.00,"t_cool":82.00}'
# '/tstat/model {"model":"CT50 V1.09"}' \
# '/tstat/errstatus {"errstatus":0}' \
# '/tstat/power {"power":350}' \
# '/tstat/version {"version":100}' \
)
#
# Thermostat Programs for Heating and Cooling, Mon = 0, Sun = 6
# '/tstat/program/heat {"0":[360,70,480,62,1080,70,1320,62],"1":[360,70,480,62,1080,70,1320,62],"2":[360,70,480,62,1080,70,1320,62],"3":[360,70,480,62,1080,70,1320,62],"4":[360,70,480,62,1080,70,1320,62],"5":[360,70,480,62,1080,70,1320,62],"6":[360,70,480,62,1080,70,1320,62]}' \
# '/tstat/program/cool {"0":[360,78,480,85,1080,78,1320,82],"1":[360,78,480,85,1080,78,1320,82],"2":[360,78,480,85,1080,78,1320,82],"3":[360,78,480,85,1080,78,1320,82],"4":[360,78,480,85,1080,78,1320,82],"5":[360,78,480,85,1080,78,1320,82],"6":[360,78,480,85,1080,78,1320,82]}' \

for u in $(seq 0 $((${#DATA_URLS[*]} - 1))); do
  URL=$(echo ${DATA_URLS[${u}]}|cut -d" " -f1)
  DATA=$(curl -s http://${THERMOSTAT_IP}${URL})
  if [ -z "$DATA" ]; then
     exit
  fi

  FIELD_COUNT=$(( $(echo ${DATA}| sed -e 's/[^,]//g' |wc -c) + 0 ))

  for n in $(seq 1 ${FIELD_COUNT}); do
    # echo -n "${n}. "
    FIELD=$(echo ${DATA} | cut -d, -f${n})

    FIELD_NAME=$(echo ${FIELD}| sed -e 's/[^:]*:\([^:]*\):.*/\1/' -e 's/[^"]*"\([^"]*\)".*/\1/' )
    FIELD_DATA=$(echo ${FIELD}| sed -e 's/.*:\([^},]*\).*/\1/' -e 's/\s*//g')

    FIELD_DATA=$(echo $(( $(( $(( $(echo ${FIELD_DATA}| tr -d .) - 3200 ))  * 5 )) / 9 )) | rev | sed -e 's/\(..\)/\1./' | rev )
# <hostname> <key> <timestamp> <value
    # echo "${FIELD_NAME}=${FIELD_DATA}" >> /tmp/values.txt
    if [ "${FIELD_DATA}" != "-1" ] && [ "${FIELD_DATA}" != "-1.00" ]; then # -1 indicates an error retrieving the value
      # echo ${THERMOSTAT_HOSTNAME} ct50.${FIELD_NAME} ${FIELD_DATA}
      echo ${THERMOSTAT_HOSTNAME} ct50.${FIELD_NAME} $(date +%s) ${FIELD_DATA}
    fi
  done
done | sort -u # | ${ZABBIX_SENDER}

# echo 1





