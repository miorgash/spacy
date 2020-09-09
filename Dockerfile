FROM ubuntu:18.04
RUN : "essential tools" && \
    apt-get update -y && apt-get upgrade -y && \
    apt-get install \
        sudo make gcc wget apt-utils vim git \
        python3.7 python3.7-dev python3-pip python3.7-venv -y && \
    python3.7 -m pip install -U pip
RUN : "for web app" && \
    pip install flask
RUN : "for tokenize and dependency analysis" && \
    pip install \
        spacy==2.3.2 \
        ginza==4.0.1 \
        sudachipy==0.4.9 \
        sudachidict_core==20200722 \ 
        sudachidict_small==20200722 \
        sudachidict_full==20200722
RUN sudachipy link -t core
RUN SUDACHIPATH=`python3.7 -c "import sudachipy as _; print(_.__path__[0])"` && \
    mv ${SUDACHIPATH}/resources/sudachi.json ${SUDACHIPATH}/resources/sudachi.json.bak
RUN echo "v.0.6.0"
ADD spacy/ /spacy
ENTRYPOINT ["python3.7", "/spacy/app.py"]
