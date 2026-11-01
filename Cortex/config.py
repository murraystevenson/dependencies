{

	"downloads" : [

		"https://github.com/ImageEngine/cortex/archive/refs/tags/10.7.4.0.tar.gz"

	],

	"url" : "https://github.com/ImageEngine/cortex",

	"license" : "LICENSE",

	"dependencies" : [
		"Python", "OpenImageIO", "OpenEXR", "Boost", "OpenShadingLanguage",
		"Blosc", "FreeType", "GLEW", "TBB", "OpenVDB", "USD"
	],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		# Build first.
		"scons {args}",
		# Then install separately. This avoids a problem with parallel builds - see
		# https://github.com/ImageEngine/cortex/issues/1308.
		"scons install {args}",

	],

	"variables" : {

		"args" :
			" -j {jobs}"
			" CXXSTD=c++{c++Standard}"
			" INSTALL_PREFIX={buildDir}"
			" INSTALL_DOC_DIR={buildDir}/doc/cortex"
			" INSTALL_PYTHON_DIR={buildDir}/python"
			" INSTALL_IECORE_OPS="
			" PYTHON_CONFIG={buildDir}/bin/python{pythonMajorVersion}-config"
			" PYTHON={buildDir}/bin/python{executableExtension}"
			" BOOST_INCLUDE_PATH={buildDir}/include"
			" LIBPATH={buildDir}/lib"
			" BOOST_LIB_SUFFIX="
			" OPENEXR_INCLUDE_PATH={buildDir}/include"
			" ILMBASE_INCLUDE_PATH={buildDir}/include/Imath"
			" VDB_INCLUDE_PATH={buildDir}/include"
			" TBB_INCLUDE_PATH={buildDir}/include"
			" OIIO_INCLUDE_PATH={buildDir}/include"
			" OSL_INCLUDE_PATH={buildDir}/include"
			" BLOSC_INCLUDE_PATH={buildDir}/include"
			" ALEMBIC_INCLUDE_PATH={buildDir}/include"
			" NANOBIND_INCLUDE_PATH={buildDir}/include"
			" FREETYPE_INCLUDE_PATH={buildDir}/include/freetype2"
			" WITH_GL=1"
			" GLEW_INCLUDE_PATH={buildDir}/include"
			" NUKE_ROOT="
			" USD_LIB_PREFIX=usd_"
			" OPTIONS="
			" {extraArgs}"
			" {pythonArgs}"
			" SAVE_OPTIONS=gaffer.options",

		"extraArgs" :
			" CXX=`which g++`"
			" ENV_VARS_TO_IMPORT='LD_LIBRARY_PATH TERM MACOSX_DEPLOYMENT_TARGET'"
		,
		"pythonArgs" : "",

	},

	"manifest" : [

		"include/IECore*",
		"lib/{libraryPrefix}IECore*{sharedLibraryExtension}",
		"lib/{libraryPrefix}IECore*.lib",
		"python/IECore*",
		"glsl/IECoreGL",
		"glsl/*.frag",
		"glsl/*.vert",
		"resources/IECoreUSD/plugInfo.json",

	],

	"platform:macos" : {

		"variables" : {

			# On Mac, `python3-config --ldflags` is broken, so we specify the flags explicitly.
			"pythonArgs" :
				" PYTHON_LIB_PATH={pythonLibDir}"
				" PYTHON_LINK_FLAGS=-lpython{pythonVersion}"
		},

	},

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}\\bin;%PATH%",

		},

		"variables" : {

			"extraArgs" :
				" USD_INCLUDE_PATH={buildDir}/include"
				" GLEW_LIB_SUFFIX=32"
			,
			# Windows has no `python-config`, so we specify the flags explicitly.
			"pythonArgs" :
				" PYTHON_INCLUDE_PATH={pythonIncludeDir}"
				" PYTHON_LIB_PATH={pythonLibDir}"
				" PYTHON_LINK_FLAGS="
			,

		},

	},

}
