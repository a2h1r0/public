#!/bin/bash

set -eu


# パイプで引数が渡されているか確認
# ホントは来てない場合の処理も書くべきだけど，常駐させるのでミスらないはず
if [ -p /dev/stdin ]; then
    mode=`cat -`

    # echoで渡された引数によって分岐
    if [ ${mode} = "startup" ]; then
        EMOJI=${EMOJI:-':sushi:'}
        HEAD=${HEAD:-"起床\n"}
    elif [ ${mode} = "uptime" ]; then
        EMOJI=${EMOJI:-':rage:'}
        HEAD=${HEAD:-"使ってないなら電源落とせよ！\n"}
    fi
fi


MESSAGEFILE=$(mktemp -t webhooksXXXX)
trap "rm ${MESSAGEFILE}" 0

# これが実行してログをもらうコマンドなので，if文内に入れれば幅が広がる
w | tr '\n' '\\' | sed 's/\\/\\n/g' > ${MESSAGEFILE}


URL='引っ張ってきたやつ'
CHANNEL=${CHANNEL:-'#ご自由に'}
BOTNAME=${BOTNAME:-'ご自由に'}
MESSAGE='```'`cat ${MESSAGEFILE}`'```'

payload="payload={
    \"channel\": \"${CHANNEL}\",
    \"username\": \"${BOTNAME}\",
    \"icon_emoji\": \"${EMOJI}\",
    \"text\": \"${HEAD}${MESSAGE}\"
}"

curl -s -S -X POST --data-urlencode "${payload}" ${URL} > /dev/null