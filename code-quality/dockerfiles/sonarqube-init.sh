#!/bin/bash
set -e

mkdir -p /opt/sonarqube/extensions/plugins
cd /opt/sonarqube/extensions/plugins

echo Downloading plugins
wget -q -nc https://github.com/sbaudoin/sonar-yaml/releases/download/v1.3.0/sonar-yaml-plugin-1.3.0.jar
stat -c '>> %s (%u:%g) %n' $(pwd)/sonar-yaml-plugin-1.3.0.jar

wget -q -nc https://github.com/sbaudoin/sonar-ansible/releases/download/v2.0.0/sonar-ansible-plugin-2.0.0.jar
stat -c '>> %s (%u:%g) %n' $(pwd)/sonar-ansible-plugin-2.0.0.jar

wget -q -nc https://github.com/sbaudoin/sonar-ansible/releases/download/v2.0.0/sonar-ansible-extras-plugin-2.0.0.jar
stat -c '>> %s (%u:%g) %n' $(pwd)/sonar-ansible-extras-plugin-2.0.0.jar