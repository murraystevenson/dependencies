{

	"downloads" : [

		"https://github.com/github/cmark-gfm/archive/refs/tags/0.29.0.gfm.2.tar.gz",

	],

	"url" : "https://github.com/github/cmark",

	"license" : "COPYING",

	"commands" : [

		"mkdir build",
		"cd build && cmake -D CMAKE_INSTALL_PREFIX={buildDir} ..",
		"cd build && cmake --build . --target install --parallel {jobs}",

	],

	"manifest" : [

		"{sharedLibraryDir}/{libraryPrefix}cmark*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}cmark*.lib",

	],

}
