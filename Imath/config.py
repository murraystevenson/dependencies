{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v3.2.3.tar.gz"

	],

	"url" : "http://www.openexr.com",

	"license" : "LICENSE.md",

	"dependencies" : [ "Python", "Boost" ],

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
			" -D PYTHON=ON"
			" -D BOOST_ROOT={buildDir}"
			" -D Python3_ROOT_DIR={buildDir}"
			" -D Python3_FIND_STRATEGY=LOCATION"
			" -D PYTHON_INSTALL_DIR=python"
			" -D BUILD_TESTING=OFF"
			" {extraArgs}"
			" ."
		,

		"cmake --build . --target install --parallel {jobs} --verbose",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"manifest" : [

		"include/Imath",
		"{sharedLibraryDir}/{libraryPrefix}Imath*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}Imath*.lib",
		"{sharedLibraryDir}/{libraryPrefix}PyImath*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}PyImath*.lib",
		"python/imath{pythonModuleExtension}",

	],

	"platform:windows" : {

		"variables" : {

			"extraArgs" :
				" -D IMATH_LIB_SUFFIX="
			,

		},

	},

}
