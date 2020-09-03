FROM ubuntu:18.04
WORKDIR /root
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install \
        sudo make gcc wget apt-utils vim git \
        python3.7 python3.7-dev python3-pip python3.7-venv -y && \
    python3.7 -m pip install -U pip
RUN pip install \
        spacy==2.3.2 \
        ginza==4.0.1 \
        sudachipy==0.4.9 \
        sudachidict_core==20200722 \ 
        sudachidict_small==20200722 \
        sudachidict_full==20200722
ADD ./resources/test.csv /usr/local/lib/python3.7/dist-packages/sudachipy/resources/test.csv
RUN sudachipy ubuild \
        -s /usr/local/lib/python3.7/dist-packages/sudachidict_core/resources/system.dic \
        -o /usr/local/lib/python3.7/dist-packages/sudachipy/resources/test.dic \
        /usr/local/lib/python3.7/dist-packages/sudachipy/resources/test.csv
RUN pip install flask
