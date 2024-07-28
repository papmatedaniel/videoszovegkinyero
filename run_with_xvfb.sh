#!/bin/bash

# Ellenőrizd, hogy az Xvfb már fut-e, és ha igen, állítsd le
if pgrep -x "Xvfb" > /dev/null
then
    echo "Xvfb is already running. Stopping it..."
    pkill -x "Xvfb"
fi

# Indítsd el az Xvfb-t
Xvfb :99 -screen 0 1024x768x16 &

# Állítsd be a DISPLAY változót
export DISPLAY=:99

# Várj egy kicsit, hogy az Xvfb elinduljon
sleep 2

# Futtasd a Python szkriptet
python3 /workspaces/videoszovegkinyero/main.py
