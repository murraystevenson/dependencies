{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v3.4.16.tar.gz"

	],

	"url" : "http://www.openexr.com",

	"license" : "LICENSE.md",

	"dependencies" : [ "Python", "Boost", "Imath" ],

	"environment" : {

		"PATH" : "{buildDir}/bin{pathListSeparator}$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			# OpenEXR's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" {extraArgs}"
			" ."
		,

		"cmake --build . --target install --parallel {jobs} --verbose",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"manifest" : [

		"bin/exrheader{executableExtension}",
		"include/OpenEXR",
		"{sharedLibraryDir}/{libraryPrefix}Iex*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}Iex*.lib",
		"{sharedLibraryDir}/{libraryPrefix}IlmThread*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}IlmThread*.lib",
		"{sharedLibraryDir}/{libraryPrefix}OpenEXR*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}OpenEXR*.lib",

	],

	"platform:windows" : {

		"variables" : {

			"extraArgs" :
				# Windows has no unversioned symlinks, so we build
				# unversioned libraries instead.
				" -D OPENEXR_LIB_SUFFIX="
				" -D Python3_ROOT_DIR={buildDir}"
				" -D Python3_FIND_STRATEGY=LOCATION"
			,

		},

	},

}
