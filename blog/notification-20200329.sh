#!/bin/bash

set -eu


# �p�C�v�ň������n����Ă��邩�m�F
# �z���g�͗��ĂȂ��ꍇ�̏����������ׂ������ǁC�풓������̂Ń~�X��Ȃ��͂�
if [ -p /dev/stdin ]; then
    mode=`cat -`

    # echo�œn���ꂽ�����ɂ���ĕ���
    if [ ${mode} = "startup" ]; then
        EMOJI=${EMOJI:-':sushi:'}
        HEAD=${HEAD:-"�N��\n"}
    elif [ ${mode} = "uptime" ]; then
        EMOJI=${EMOJI:-':rage:'}
        HEAD=${HEAD:-"�g���ĂȂ��Ȃ�d�����Ƃ���I\n"}
    fi
fi


MESSAGEFILE=$(mktemp -t webhooksXXXX)
trap "rm ${MESSAGEFILE}" 0

# ���ꂪ���s���ă��O�����炤�R�}���h�Ȃ̂ŁCif�����ɓ����Ε����L����
w | tr '\n' '\\' | sed 's/\\/\\n/g' > ${MESSAGEFILE}


URL='���������Ă������'
CHANNEL=${CHANNEL:-'#�����R��'}
BOTNAME=${BOTNAME:-'�����R��'}
MESSAGE='```'`cat ${MESSAGEFILE}`'```'

payload="payload={
    \"channel\": \"${CHANNEL}\",
    \"username\": \"${BOTNAME}\",
    \"icon_emoji\": \"${EMOJI}\",
    \"text\": \"${HEAD}${MESSAGE}\"
}"

curl -s -S -X POST --data-urlencode "${payload}" ${URL} > /dev/null