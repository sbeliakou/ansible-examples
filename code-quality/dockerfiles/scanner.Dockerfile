FROM python:2.7

RUN pip install ansible-lint==3.4.15

RUN apt-get update && \
    apt install -y default-jre && \
    java -version

RUN apt-get install -y unzip && \
    wget -q -nc http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/2.4/sonar-runner-dist-2.4.zip && \
    unzip sonar-runner-dist-2.4.zip && \
    chmod a+x /sonar-runner-2.4/bin/* && \
    rm -f sonar-runner-dist-2.4.zip

ENV PATH PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sonar-runner-2.4/bin

ENTRYPOINT /sonar-runner-2.4/bin/sonar-runner