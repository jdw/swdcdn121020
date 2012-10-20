#!/bin/bash

INIT="nope"
if [ $# -eq 1 ]; then
	if [ $@ == "INIT" ]; then
		INIT="yes"
	fi
fi

if [ $INIT = "yes" ]; then
	echo "Initializing virtual environment..."
	virtualenv .
fi

. bin/activate

if [ $INIT = "yes" ]; then
	echo "Installing packages..."
	easy_install pygame
	easy_install flask
fi

echo "Now run '. bin/activate'"
