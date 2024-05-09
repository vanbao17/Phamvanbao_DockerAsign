
FROM ubuntu:latest
RUN apt-get update && apt-get install -y cron curl
ENV TZ=Asia/Ho_Chi_Minh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo "42 14 * * * /usr/bin/curl http://crawl_api_container:5555/crawl > /dev/null 2>&1" > /etc/cron.d/my-cron-job
RUN chmod 0644 /etc/cron.d/my-cron-job
RUN crontab /etc/cron.d/my-cron-job
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
