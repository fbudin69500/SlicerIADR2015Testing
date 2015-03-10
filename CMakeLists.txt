cmake_minimum_required(VERSION 2.8.9)

project(IADR2015)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://www.example.com/Slicer/Extensions/IADR2015")
set(EXTENSION_CATEGORY "Testing")
set(EXTENSION_CONTRIBUTORS "Francois Budin (UNC)")
set(EXTENSION_DESCRIPTION "This module downloads data for the IADR2015 workshop")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/IADR2015.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/IADR2015/Screenshots/1.png")

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(Download)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
