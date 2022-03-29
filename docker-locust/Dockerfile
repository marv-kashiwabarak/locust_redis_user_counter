FROM locustio/locust

ADD source /locust-source

ADD run.sh /home/locust/run.sh

RUN pip3 install redis

EXPOSE 5557 5558 8089

USER root
RUN chown locust:locust /home/locust/run.sh

USER locust
RUN chmod 755 /home/locust/run.sh

ENTRYPOINT ["/home/locust/run.sh"]
