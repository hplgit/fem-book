#!/bin/bash

set -x

encoding="--encoding=utf-8"

name=studyguide

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

rm -f tmp_* *.dolog
