#!/bin/bash

## launch richardcli with docker

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker attach gwynne_dashboard
else
		winpty docker attach gwynne_dashboard
fi

echo "Done"
read -n 1 -s -r -p "Press any key to continue"