#!/bin/bash

condorusage(){
echo "Usage: `basename $0` w/z <w'_mass> <charge -:1 +:3> <order 0:LO 1:NLO 2:NNLO> <pdfset ex) NNPDF31_nnlo_as_0118_mc_hessian_pdfas>"
exit 1
}

[ $# -lt 5 ] && condorusage

BOSON=$1
MASS=$2
CHARGE=$3
ORDER=$4
PDFSET=$5
RUNDIR=${1}p_${2}_${3}_${4}_${5}
INFILE=input.txt
OUTFILE=output.txt
HISTFILE=histograms.txt
PDFDIR=.

python makeinput.py $MASS $CHARGE $ORDER $PDFSET $INFILE

RUNDIR=`python scripts/get_relpath.py $RUNDIR ./`
PDFDIR=`python scripts/get_relpath.py $PDFDIR ./`

EXEC=fewz$BOSON

SECTORS=`python scripts/get_sects.py $INFILE $BOSON`

python scripts/create_parallel.py $BOSON $INFILE $RUNDIR

if ! [ -e $RUNDIR/$EXEC ] ; then
   cp $EXEC $RUNDIR/
fi

cp $INFILE $RUNDIR/

if ! [ -e $RUNDIR/$HISTFILE ] ; then
   python scripts/get_bin_files.py $HISTFILE $RUNDIR
fi

python scripts/create_condor_jobs.py $BOSON ${RUNDIR##*/} $INFILE $HISTFILE $OUTFILE $PDFDIR

cd $RUNDIR

mkdir condorLog

cat << EOF > condorRun.sh
#!/bin/bash

export SCRAM_ARCH=slc7_amd64_gcc700
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source \$VO_CMS_SW_DIR/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_2_3
eval \`scramv1 runtime -sh\`
cd -
export LHAPDFPATH=/home/taebh/2021_Research
export PATH=\$LHAPDFPATH/bin:\$PATH
export PYTHONPATH=\$LHAPDFPATH/lib/python2.7/site-packages:\$PYTHONPATH
export LD_LIBRARY_PATH=\$LHAPDFPATH/lib/libLHAPDF.so:\$LD_LIBRARY_PATH

if [ ! -d condorOut ]; then mkdir condorOut; fi
cd condorOut

../$EXEC -i ../$INFILE -h ../$HISTFILE -o $OUTFILE -p $PDFDIR -s \$1
EOF

cat << EOF > job.jdl
executable = condorRun.sh
universe = vanilla
arguments = \$(Process)
output   = condorLog/condor_\$(Cluster).\$(Process).log
error    = condorLog/condor_\$(Cluster).\$(Process).log
log      = /dev/null
should_transfer_files = yes
transfer_input_files = `readlink -f $EXEC`,`readlink -f $INFILE`,`readlink -f $HISTFILE`,`readlink -f bins.txt`
when_to_transfer_output = ON_EXIT
transfer_output_files = condorOut
getenv = True
queue ${SECTORS}
EOF

condor_submit job.jdl
