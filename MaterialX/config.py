{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/MaterialX/archive/refs/tags/v1.39.4.tar.gz",

	],

	"url" : "http://www.materialx.org/",

	"license" : "LICENSE",

	"dependencies" : [ "Python", "OpenImageIO", "OpenShadingLanguage" ],

	"environment" : {

		"PATH" : "{buildDir}/bin{pathListSeparator}$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",

	},

	"commands" : [

		"mkdir build",
		"cd build && cmake"
			" -D CMAKE_CXX_STANDARD={c++Standard}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D MATERIALX_BUILD_SHARED_LIBS=ON"
			" -D MATERIALX_BUILD_PYTHON=ON"
			" -D MATERIALX_BUILD_OIIO=ON"
			" -D MATERIALX_BUILD_TESTS=OFF"
			" -D MATERIALX_INSTALL_LIB_PATH={buildDir}/lib"
			" -D MATERIALX_INSTALL_STDLIB_PATH={buildDir}/materialX/libraries"
			" -D MATERIALX_PYTHON_EXECUTABLE={buildDir}/bin/python"
			" {extraArgs}"
			" ..",

		"cd build && cmake --build . --clean-first --target install --parallel {jobs} --verbose",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"manifest" : [

		"include/MaterialX*",
		"{sharedLibraryDir}/{libraryPrefix}MaterialX*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}MaterialX*.lib",
		"materialX",
		"python/MaterialX",

	],

	"platform:windows" : {

		"variables" : {

			"extraArgs" : "-D CMAKE_PREFIX_PATH={buildDir}",

		},

	},

}
