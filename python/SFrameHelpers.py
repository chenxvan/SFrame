# $Id$
###########################################################################
# @Project: SFrame - ROOT-based analysis framework for ATLAS              #
#                                                                         #
# @author Stefan Ask       <Stefan.Ask@cern.ch>           - Manchester    #
# @author David Berge      <David.Berge@cern.ch>          - CERN          #
# @author Johannes Haller  <Johannes.Haller@cern.ch>      - Hamburg       #
# @author A. Krasznahorkay <Attila.Krasznahorkay@cern.ch> - CERN/Debrecen #
#                                                                         #
###########################################################################

## @package SFrameHelpers
#    @short Collection of SFrame related python functions
#
# This package is a collection of python functions useful for SFrame.
# They can either be used from an interactive python session by
# executing
#
# <code>
#  >>> import SFrameHelpers
# </code>
#
# or using the script(s) shipped with SFrame.

# Import base module(s):
import os.path
import time

# Import PyROOT:
import ROOT

##
# @short Function creating <code><In ... /></code> configuration nodes
#
# The function checks the specified input files and writes the XML nodes
# with their information to the specified output file. Their luminosity
# is calculated using the specified cross section.
#
# @param crossSection Cross section of the Monte Carlo
# @param files        List of input files
# @param output       Name of the output file
# @param tree         Name of the main TTree in the files
# @param prefix       Prefix to be put before the file paths. E.g. root://mymachine/
def CreateInput( crossSection, files, output, tree, prefix ):

  # Turn off ROOT error messages:
  oldErrorIgnoreLevel = ROOT.gErrorIgnoreLevel
  ROOT.gErrorIgnoreLevel = ROOT.kSysError

  # Open the output file:
  outfile = open( output, "w" )

  # Print some header in the output text file:
  outfile.write( "<!-- File generated by SFrameHelpers.CreateInput(...) on %s -->\n" % \
                 time.asctime( time.localtime( time.time() ) ) )
  outfile.write( "<!-- The supplied x-section was: %f -->\n\n" % crossSection )

  # Some summary values:
  totEvents = 0
  totLuminosity = 0.0

  # Loop over all the files:
  for file in files:

    # Print some status messages:
    print "Processing file: %s" % os.path.basename( file )

    # Open the AANT file:
    tfile = ROOT.TFile( file, "READ" )
    if not tfile.IsOpen():
      print "*ERROR* File \"" + file + "\" does not exist *ERROR*"
      continue

    # Access a tree in the ntuple:
    collTree = tfile.Get( tree  )
    if( str( collTree ) == 'None' ):
      print "*ERROR* " + tree + "  not found in file: \"" + file + "\" *ERROR*"
      continue

    # Read the number of events in the file:
    events = collTree.GetEntries()
    luminosity = float( events ) / crossSection

    # Increment the summary variables:
    totEvents = totEvents + events
    totLuminosity = totLuminosity + luminosity

    # Compose the XML node. Make sure that the file name has an absolute path
    # (no symbolic link, or relative path) and that the luminosity is printed with
    # a meaningful precision.
    outfile.write( "<In FileName=\"" + prefix + os.path.abspath( os.path.realpath( file ) ) \
                   + ( "\" Lumi=\"%.3g" % luminosity ) + "\" />\n" )

  # Save some summary information:
  outfile.write( "\n<!-- Total number of events processed: %s -->\n" % totEvents )
  outfile.write( "<!-- Representing a total luminosity : %.3g -->" % totLuminosity )

  # Close the output file:
  outfile.close()

  # Print some summary information:
  print "\nTotal number of events processed: %s" % totEvents
  print "Representing a total luminosity : %.3g\n" % totLuminosity

  # Turn back ROOT error messages:
  ROOT.gErrorIgnoreLevel = oldErrorIgnoreLevel

  return

##
# @short Function creating <code><In ... /></code> configuration nodes
#
# The function checks the specified input files and writes the XML nodes
# with their information to the specified output file. It assumes that the
# input files are data files, so it just puts a dummy "1.0" as the
# luminosity for them. (The luminosities are disregarded in the event
# weight calculation when the InputData type is set to "data".)
#
# @param files        List of input files
# @param output       Name of the output file
# @param tree         Name of the main TTree in the files
# @param prefix       Prefix to be put before the file paths. E.g. root://mymachine/
def CreateDataInput( files, output, tree, prefix ):
  
  # Turn off ROOT error messages:
  oldErrorIgnoreLevel = ROOT.gErrorIgnoreLevel
  ROOT.gErrorIgnoreLevel = ROOT.kSysError

  # Open the output file:
  outfile = open( output, "w" )

  # Print some header in the output text file:
  outfile.write( "<!-- File generated by SFrameHelpers.CreateDataInput(...) on %s -->\n\n" % \
                 time.asctime( time.localtime( time.time() ) ) )

  # Some summary values:
  totEvents = 0

  # Loop over all the files:
  for file in files:

    # Print some status messages:
    print "Processing file: %s" % os.path.basename( file )

    # Open the AANT file:
    tfile = ROOT.TFile( file, "READ" )
    if not tfile.IsOpen():
      print "*ERROR* File \"" + file + "\" does not exist *ERROR*"
      continue

    # Access a tree in the ntuple:
    collTree = tfile.Get( tree )
    if( str( collTree ) == 'None' ):
      print "*ERROR* " + tree + " not found in file: \"" + file + "\" *ERROR*"
      continue

    # Read the number of events in the file:
    events = collTree.GetEntries()

    # Increment the summary variables:
    totEvents = totEvents + events

    # Compose the XML node. Make sure that the file name has an absolute path
    # (no symbolic link, or relative path) and that the luminosity is printed with
    # a meaningful precision.
    outfile.write( "<In FileName=\"" + prefix + os.path.abspath( os.path.realpath( file ) ) \
                   + "\" Lumi=\"1.0\" />\n" )

  # Save some summary information:
  outfile.write( "\n<!-- Total number of events processed: %s -->\n" % totEvents )

  # Close the output file:
  outfile.close()

  # Print some summary information:
  print "\nTotal number of events processed: %s" % totEvents

  # Turn back ROOT error messages:
  ROOT.gErrorIgnoreLevel = oldErrorIgnoreLevel

  return
