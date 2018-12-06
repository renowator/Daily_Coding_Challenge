#!/bin/bash

for fol in $PWD/*
    do
    [ -d $fol ] && echo $fol problem: && cd $fol && ./run_tests.sh
done
