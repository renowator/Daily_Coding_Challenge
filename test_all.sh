#!/bin/bash

for fol in $PWD/*
    do
    [ -d $fol ] &&
    [ -f $fol/run_tests.sh ] &&
    echo $fol problem:  &&
    cd $fol && ./run_tests.sh
done
