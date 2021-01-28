#!/bin/bash

export SCRAM_ARCH=slc7_amd64_gcc700
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_2_3
eval `scramv1 runtime -sh`
cd -
export LHAPDFPATH=/home/taebh/2021_Research
export PATH=$LHAPDFPATH/bin:$PATH
export PYTHONPATH=$LHAPDFPATH/lib/python2.7/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$LHAPDFPATH/lib/libLHAPDF.so:$LD_LIBRARY_PATH

if [ ! -d condortest ]; then mkdir condortest; fi
mv input.txt histograms.txt fewzw condortest

if [ ! -d condorOut ]; then mkdir condorOut; fi
cd condortest

./fewzw -i ./input.txt -h ./histograms.txt -o output.txt -p . -s $1
mv NNLO.sect$(($1+1)).output.txt ../condorOut/LO.output.${1}.txt
