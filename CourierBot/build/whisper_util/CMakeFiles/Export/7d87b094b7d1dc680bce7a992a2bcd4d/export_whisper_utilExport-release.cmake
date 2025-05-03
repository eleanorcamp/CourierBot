#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "whisper_util::whisper_util" for configuration "Release"
set_property(TARGET whisper_util::whisper_util APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(whisper_util::whisper_util PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libwhisper_util.so"
  IMPORTED_SONAME_RELEASE "libwhisper_util.so"
  )

list(APPEND _cmake_import_check_targets whisper_util::whisper_util )
list(APPEND _cmake_import_check_files_for_whisper_util::whisper_util "${_IMPORT_PREFIX}/lib/libwhisper_util.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
