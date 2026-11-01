{

	"downloads" : [

		"https://github.com/madler/zlib/releases/download/v1.3.1/zlib-1.3.1.tar.gz",

	],

	"url" : "https://zlib.net/",

	"license" : "LICENSE",

	"commands" : [

		"mkdir build",
		"cd build &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_BUILD_TYPE=Release"
			" ..",
		"cd build && cmake --build . --target install --parallel {jobs}",

	],

	"manifest" : [

		"include/zlib.h",
		"include/zconf.h",
		"lib/libz.*{sharedLibraryExtension}*",
		"bin/zlib.dll",
		"lib/zlib.lib",

	],

}
