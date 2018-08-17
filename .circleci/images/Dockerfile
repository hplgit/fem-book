FROM continuumio/miniconda3:latest

USER root

ENV ENV_NAME=fem-book-test

RUN apt update && \
    apt install -y gcc g++ ispell graphicsmagick-imagemagick-compat texlive-extra-utils pdftk ffmpeg

RUN conda config --set always_yes true && \
    conda update -q conda && \
    conda config --add channels conda-forge && \
    conda create -n ${ENV_NAME} doconce fenics matplotlib scipy sympy=1.1 && \
    conda list -n ${ENV_NAME}
