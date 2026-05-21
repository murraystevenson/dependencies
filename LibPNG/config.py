{

	"downloads" : [

		"https://github.com/pnggroup/libpng/archive/refs/tags/v1.6.58.tar.gz"

	],

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
			" -D PNG_EXECUTABLES=OFF"
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
		"lib/libpng*.a",

	],

}
