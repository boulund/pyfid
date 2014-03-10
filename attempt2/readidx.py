#!/usr/bin/env python
# Read sequences from a previously pickled dictionary of byte positions.
# Fredrik Boulund 2012

from sys import exit,argv
import cPickle

if len(argv)<2:
    print "Usage: script.py fasta.index"

data = cPickle.load(open(argv[1]))
source_fasta, index = data

with open(source_fasta) as seqfile:
    #print "Reading sequences from:",source_fasta
    for seqid in argv[2:]:
        #print "Reading sequence:",seqid
        curseqpos = index[seqid]
        #print curseqpos
        seqfile.seek(curseqpos[0])
        sequence = seqfile.read(curseqpos[1]-curseqpos[0])
        print sequence,

