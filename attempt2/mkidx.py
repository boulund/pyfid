#!/usr/bin/env python
# Make FASTA file index
# Fredrik Boulund 2012


from sys import argv, exit
import cPickle

if len(argv)<2:
    print "Usage: script.py file.fasta"

index={}
bytecounter = 0
prevbytecount = 0

with open(argv[1]) as file:
    line = file.readline()
    while line:
        # See if we have identifier line
        if line.startswith(">"):
            # Extract the unique SeqID
            identifier=line.split()[0][1:]
            bytecounter += len(line) 

            # Read ensuing lines containing sequence
            while line:
                line = file.readline()
                # When we reach a new seqID line, stop
                if line.startswith(">"):
                    # Store the current seqid along with bytepos coordinates
                    if index.has_key(identifier):
                        print "ERROR: Double seq IDs:", identifier
                    else:
                        index[identifier] = (prevbytecount,bytecounter)
                    # Update previous sequence endpos
                    prevbytecount = bytecounter
                    # now fall back to outer loop
                    break 
                # Add the line length to counter
                bytecounter += len(line)

# Store the final seqid along with bytepos coordinates
if index.has_key(identifier):
    print "ERROR: Double seq IDs:", identifier
else:
    index[identifier] = (prevbytecount,bytecounter)

#print index
indexfilename = argv[1]+".idx"
cPickle.dump((argv[1],index),open(indexfilename,'wb'))
print "FASTA index created:", indexfilename 
