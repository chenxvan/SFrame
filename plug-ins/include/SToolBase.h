// Dear emacs, this is -*- c++ -*-
// $Id$
/***************************************************************************
 * @Project: SFrame - ROOT-based analysis framework for ATLAS
 * @Package: Plug-ins
 *
 * @author Stefan Ask       <Stefan.Ask@cern.ch>           - Manchester
 * @author David Berge      <David.Berge@cern.ch>          - CERN
 * @author Johannes Haller  <Johannes.Haller@cern.ch>      - Hamburg
 * @author A. Krasznahorkay <Attila.Krasznahorkay@cern.ch> - CERN/Debrecen
 *
 ***************************************************************************/

#ifndef SFRAME_PLUGINS_SToolBase_H
#define SFRAME_PLUGINS_SToolBase_H

// SFrame include(s):
#include "core/include/SLogger.h"

// Forward declaration(s):
class TH1;
class TObject;
class TBranch;
class SCycleBase;

/**
 *   @short Base class for tools that can be used during the analysis
 *
 *          The idea is that people will probably want to make their analysis
 *          code modular by breaking it into many classes. To make it easy
 *          to do common "SFrame tasks" in these classes (which are not cycles
 *          themselves), one can use this base class. It provides much of the
 *          same convenience functionality that SCycleBase does.
 *
 * @version $Revision$
 */
class SToolBase {

public:
   /// Constructor specifying the parent of the tool
   SToolBase( SCycleBase* parent );

   /// Get a pointer to the parent cycle of this tool
   SCycleBase* GetParent() const;

protected:
   /////////////////////////////////////////////////////////////
   //                                                         //
   //         Functions inherited from SCycleBaseHist         //
   //                                                         //
   /////////////////////////////////////////////////////////////

   /// Function placing a ROOT object in the output file
   template< class T > T* Book( const T& histo,
                                const char* directory = 0 ) throw( SError );
   /// Function searching for a ROOT object in the output file
   template< class T > T* Retrieve( const char* name,
                                    const char* directory = 0 ) throw( SError );
   /// Function for persistifying a ROOT object to the output
   void WriteObj( const TObject& obj,
                  const char* directory = 0 ) throw( SError );
   /// Function searching for 1-dimensional histograms in the output file
   TH1* Hist( const char* name, const char* dir = 0 );

   /////////////////////////////////////////////////////////////
   //                                                         //
   //        Functions inherited from SCycleBaseNTuple        //
   //                                                         //
   /////////////////////////////////////////////////////////////

   /// Connect an input variable
   template< typename T >
   bool ConnectVariable( const char* treeName, const char* branchName,
                         T& variable ) throw ( SError );
   /// Declare an output variable
   template< typename T >
   TBranch* DeclareVariable( T& obj, const char* name,
                             const char* treeName = 0 ) throw( SError );

   /////////////////////////////////////////////////////////////
   //                                                         //
   //        Functions inherited from SCycleBaseConfig        //
   //                                                         //
   /////////////////////////////////////////////////////////////

   /// Declare a property
   template< typename T >
   void DeclareProperty( const std::string& name, T& value );
   /// Add a configuration object that should be available on the PROOF nodes
   void AddConfigObject( TObject* object );
   /// Get a configuration object on the PROOF nodes
   TObject* GetConfigObject( const char* name ) const;

   /////////////////////////////////////////////////////////////
   //                                                         //
   //               The class's own functions                 //
   //                                                         //
   /////////////////////////////////////////////////////////////

   /// Set the name under which the tool's log messages should appear
   void SetLogName( const char* name );

protected:
   mutable SLogger m_logger; ///< Logger object for the tool

private:
   SCycleBase* m_parent; ///< Pointer to the parent cycle of this tool

}; // class SToolBase

// Include the template implementation:
#ifndef __CINT__
#include "SToolBase.icc"
#endif // __CINT__

#endif // SFRAME_PLUGINS_SToolBase_H