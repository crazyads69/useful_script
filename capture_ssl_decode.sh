#!/bin/bash

echo "Capturing ssl log";
export SSLKEYLOGFILE=$HOME/sslkeylog.log;

echo "Start Chrome to capture:";
open /Applications/Google\ Chrome.app;
