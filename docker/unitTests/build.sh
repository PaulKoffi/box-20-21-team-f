#!/bin/bash

echo "Building rocket_service docker image"
mkdir resources
cp ../../requirements.txt resources
cp -R ../../tests/unitTests/pollTest.py resources
cp -R ../../tests/unitTests/pollsystemTest.py resources
docker build -t djotiham/unit_tests .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
