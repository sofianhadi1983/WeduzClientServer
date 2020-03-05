#!/usr/bin/env bash

SERVER_NAME="node$NODE_NAME"

while inotifywait -q -e modify /var/log/messages > /dev/null
do
    NUM_ATTEMPTS=$(grep -r "Accepted\|Failed" /var/log/messages | wc -l)
    REQUEST=$(jq -n \
            --arg name "$SERVER_NAME" \
            --arg cnt "$NUM_ATTEMPTS" \
            '{server_name: $name, total_login_attempts: $cnt}')

    echo $REQUEST
done