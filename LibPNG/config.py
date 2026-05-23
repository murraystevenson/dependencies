{

	"downloads" : [

		"https://github.com/pnggroup/libpng/archive/refs/tags/v1.6.58.tar.gz"

	],

	"dependencies" : [ "ZLib" ],

	"url" : "http://www.libpng.org",
	"license" : "LICENSE",

	"commands" : [

		"mkdir build",
		"cd build && "
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D PNG_SHARED=OFF"
			" -D PNG_STATIC=ON"
			" -D PNG_TESTS=OFF"
			" -D PNG_TOOLS=OFF"
			" -D PNG_FRAMEWORK=OFF"
			" -D CMAKE_POSITION_INDEPENDENT_CODE=ON"
			" ..",
		"cd build && make -j {jobs} && make install",

	],

	"manifest" : [

		"include/png*",
		"include/libpng*",
		"{sharedLibraryDir}/libpng*{staticLibraryExtension}",	# lib prefix is accurate for all platforms

	],

	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild && "
				" cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D ZLIB_INCLUDE_DIR={buildDir}\\include"
				" -D ZLIB_LIBRARY={buildDir}\\lib\\zlib.lib"
				" -D PNG_SHARED=ON"
				" -D PNG_STATIC=ON"
				" -D PNG_TESTS=OFF"
				" -D PNG_TOOLS=OFF"
				" -D PNG_FRAMEWORK=OFF"
				" -D CMAKE_POSITION_INDEPENDENT_CODE=ON"
				" ..",

			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",

		],

	},

}
