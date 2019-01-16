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

until curl --connect-timeout 1 -s -u admin:admin --output /dev/null -X POST -f http://sonarqube:9000/api/system/info
do
  echo $? waiting for sonar is ready
  sleep 1
done

curl -u admin:admin -X POST 'http://sonarqube:9000/api/qualityprofiles/create?language=yaml&name=Ansible'
key=$(curl -s -u admin:admin -X POST 'http://sonarqube:9000/api/qualityprofiles/search?qualityProfile=Ansible' | jq -r '.profiles[].key')
curl -u admin:admin -X POST "http://sonarqube:9000/api/qualityprofiles/activate_rules?tags=ansible&targetKey=${key}"
curl -u admin:admin -X POST "http://sonarqube:9000/api/qualityprofiles/set_default?key=${key}"
curl -u admin:admin -X POST 'http://sonarqube:9000/api/qualitygates/create?name=Ansible'