{

	"downloads" : [

		"https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-1.3.2.tar.gz"

	],

	"url" : "https://chromium.googlesource.com/webm/libwebp",
	"license" : "COPYING",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"include/webp",
		# Note : LibWebP uses the "lib" prefix on Windows too.
		"{sharedLibraryDir}/libwebp*{sharedLibraryExtension}*",
		"{sharedLibraryDir}/libwebpdemux*{sharedLibraryExtension}*",
		"{sharedLibraryDir}/libsharpyuv*{sharedLibraryExtension}*",
		"lib/libwebp*.lib",
		"lib/libsharpyuv*.lib",

	],

	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild &&"
				" cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D BUILD_SHARED_LIBS=1"
				" ..",
			"cd gafferBuild && cmake --build . --target install --parallel {jobs}",

		],

	},

}
