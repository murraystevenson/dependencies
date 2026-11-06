{

	"downloads" : [

		"https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v26.05.tar.gz"

	],

	"url" : "https://openusd.org",

	"license" : "LICENSE.txt",

	"dependencies" : [ "Boost", "Python", "OpenImageIO", "TBB", "Alembic", "OpenSubdiv", "OpenVDB", "OpenShadingLanguage", "PyOpenGL", "GLEW", "PySide", "Embree", "MaterialX", "Jinja2" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",
		"PYTHONPATH" : "{buildDir}/python",

	},

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D Boost_NO_SYSTEM_PATHS=TRUE"
			" -D Boost_NO_BOOST_CMAKE=TRUE"
			" -D PXR_ENABLE_OPENVDB_SUPPORT=TRUE"
			" -D PXR_ENABLE_OSL_SUPPORT=TRUE"
			" -D PXR_ENABLE_PTEX_SUPPORT=FALSE"
			" -D PXR_BUILD_TESTS=FALSE"
			" -D PXR_BUILD_OPENIMAGEIO_PLUGIN=TRUE"
			" -D PXR_BUILD_ALEMBIC_PLUGIN=TRUE"
			" -D PXR_BUILD_EMBREE_PLUGIN=FALSE"
			" -D PXR_ENABLE_HDF5_SUPPORT=FALSE"
			" -D PXR_ENABLE_MATERIALX_SUPPORT=TRUE"
			" -D MATERIALX_STDLIB_DIR={buildDir}/materialX"
			" -D PXR_PYTHON_SHEBANG=\"/usr/bin/env python\""
			" -D Python3_ROOT_DIR={buildDir}"
			" -D Python3_FIND_STRATEGY=LOCATION"
			" -D ALEMBIC_DIR={buildDir}/lib"
			# Needed to prevent CMake picking up system python libraries on Mac.
			" -D CMAKE_FRAMEWORK_PATH={pythonLibDir}"
			" {extraArgs}"
			" ."
		,

		"cmake --build . --target install --parallel {jobs} --verbose",

		"cmake -E rm -rf {buildDir}/python/pxr",

	],

	"postMovePaths" : {

		"{buildDir}/lib/python/pxr" : "{buildDir}/python",

	},

	"variables" : {

		"extraArgs" : "",

	},

	"manifest" : [

		"bin/usd*",
		"bin/sdfdump{executableExtension}",

		"include/pxr",

		"lib/{libraryPrefix}usd*{sharedLibraryExtension}",
		"lib/{libraryPrefix}usd*.lib",
		"lib/usd",

		"python/pxr",

		"plugin/usd",
		"share/usd",

	],

	"platform:windows" : {

		"environment" : {

			"PXR_PLUGINPATH_NAME" : "{buildDir}/bin/usd",
			"CXXFLAGS" : "/utf-8",

		},

		"variables" : {

			"extraArgs" :
				" -D PXR_INSTALL_LOCATION={buildDir}/bin/usd"
				" -D PXR_ENABLE_PRECOMPILED_HEADERS=0"
				" -D PYSIDEUICBINARY={buildDir}/bin/uic.exe"
			,

		},

	},

}
