FROM alpine:3.8

RUN apk add --no-cache curl bash  jq && rm -rf /var/cache/apk/*

COPY sonarqube-init.sh /

ENTRYPOINT ["/bin/bash", "/sonarqube-init.sh"]