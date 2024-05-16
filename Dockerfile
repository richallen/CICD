FROM ubuntu
RUN apt-get update && \
    apt-get install -y python3 python3-pip
RUN rm /usr/lib/python3.12/EXTERNALLY-MANAGED  
# https://www.makeuseof.com/fix-pip-error-externally-managed-environment-linux/
RUN useradd -m user
#USER user
# For now use root RUN su user && pip3 install flask
RUN pip3 install flask
RUN pip3 install waitress
COPY flask_server.py .
#ENTRYPOINT ["/usr/bin/python3","/home/user/flask_server.py"]
#EXPOSE 9000
ENTRYPOINT ["/usr/bin/python3","flask_server.py"]
