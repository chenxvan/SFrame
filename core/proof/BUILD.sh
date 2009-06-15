# $Id: BUILD.sh,v 1.1.2.2 2009-01-08 16:09:32 krasznaa Exp $
#***************************************************************************
#* @Project: SFrame - ROOT-based analysis framework for ATLAS
#* @Package: Core
#*
#* @author Stefan Ask       <Stefan.Ask@cern.ch>           - Manchester
#* @author David Berge      <David.Berge@cern.ch>          - CERN
#* @author Johannes Haller  <Johannes.Haller@cern.ch>      - Hamburg
#* @author A. Krasznahorkay <Attila.Krasznahorkay@cern.ch> - CERN/Debrecen
#*
#***************************************************************************

#
# This script builds the SFrameCore package on the PROOF worker and master
# nodes.
#

if [ "$1" = "clean" ]; then
    make distclean
    exit 0
fi

make default