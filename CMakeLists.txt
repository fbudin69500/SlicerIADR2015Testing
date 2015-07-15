cmake_minimum_required(VERSION 2.8.9)

project(SlicerIADR2015Testing)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/fbudin69500/SlicerIADR2015Testing")
set(EXTENSION_CATEGORY "Testing")
set(EXTENSION_CONTRIBUTORS "Francois Budin (UNC)")
set(EXTENSION_DESCRIPTION "This module downloads data for the IADR2015 workshop")
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/fbudin69500/SlicerIADR2015Testing/master/IADR2015.png")
set(EXTENSION_SCREENSHOTURLS "https://sites.google.com/a/umich.edu/dentistry-image-computing/_/rsrc/1367306451665/Gallery/Cristianotestfrontal.png?height=200&width=150")

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(SlicerIADR2015Testing)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
