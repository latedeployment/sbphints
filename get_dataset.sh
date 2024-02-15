#!/usr/bin/env bash

GCIDE_URL="https://ftp.gnu.org/gnu/gcide/gcide-0.53.tar.gz"
GCIDE_BASEFILE=$(basename ${GCIDE_URL})
GCIDE_FOLDER=$(basename -s .tar.gz ${GCIDE_URL})

if [ ! -d ${GCIDE_FOLDER} ]; then
  if ! wget "${GCIDE_URL}"; then
      if ! curl -O "${GCIDE_URL}"; then
        echo "failed to download... install either wget or curl, or test your network..."
        exit 1
      fi
  fi

  if ! tar xvfs ${GCIDE_BASEFILE}; then
    echo "error: unable to extract ${GCIDE_BASEFILE}"
    exit 1
  fi
fi

# remove temp file
#rm ${GCIDE_BASEFILE}

# get dataset by lengths
perl -n -e '/<p><ent>(\w{4,})/ && print("$1\n")' ./${GCIDE_FOLDER}/CIDE.* | sort | uniq > cide_words_4.txt
