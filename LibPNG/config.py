{

	"downloads" : [

		"https://github.com/pnggroup/libpng/archive/refs/tags/v1.6.59.tar.gz"

	],

	"url" : "http://www.libpng.org",
	"license" : "LICENSE",

	"dependencies" : [ "ZLib" ],

	"commands" : [

		# We only build a static library, because a shared `libpng` conflicts
		# with the private copy used by the macOS ImageIO framework, crashing
		# Gaffer when AppKit loads PNG cursors.
		"mkdir build",
		"cd build && "
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
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
