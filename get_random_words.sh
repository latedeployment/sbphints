#!/usr/bin/env bash

shuf -n $1 ./cide_words_4.txt | tr '[:upper:]' '[:lower:]'
