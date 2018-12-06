#!/bin/bash

for fol in $PWD/*
    do
    [ -d $fol ] && cd $fol && ./run_tests.sh
done
