{

	"downloads" : [

		"https://github.com/pnggroup/libpng/archive/refs/tags/v1.6.59.tar.gz"

	],

	"url" : "http://www.libpng.org",
	"license" : "LICENSE",

	"dependencies" : [ "ZLib" ],

	"commands" : [

		"mkdir build",
		"cd build && "
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D PNG_SHARED={pngShared}"
			" -D PNG_STATIC=ON"
			" -D PNG_TESTS=OFF"
			" -D PNG_TOOLS=OFF"
			" -D PNG_FRAMEWORK=OFF"
			" -D CMAKE_POSITION_INDEPENDENT_CODE=ON"
			" {extraArgs}"
			" ..",
		"cd build && cmake --build . --target install --parallel {jobs}",

	],

	"variables" : {

		"pngShared" : "OFF",
		"extraArgs" : "",

	},

	"platform:windows" : {

		"variables" : {

			"pngShared" : "ON",

		},

		"manifest" : [

			"include/png*",
			"include/libpng*",
			"{sharedLibraryDir}/libpng*{sharedLibraryExtension}*",
			"lib/libpng*.lib",

		],

	},

}
