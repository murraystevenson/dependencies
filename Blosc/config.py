{

	"downloads" : [

		"https://github.com/Blosc/c-blosc/archive/refs/tags/v1.21.1.tar.gz"

	],

	"url" : "https://blosc.org",

	"license" : "LICENSES",

	"dependencies" : [ "ZLib" ],

	"commands" : [

		"cmake -DCMAKE_INSTALL_PREFIX={buildDir} -DPREFER_EXTERNAL_ZLIB=ON -DCMAKE_PREFIX_PATH={buildDir} {extraArgs} .",
		# Note : Blosc does not declare its build dependencies
		# correctly, so we cannot do a parallel build with `-j`.
		"cmake --build . --target install --verbose",

	],

	"manifest" : [

		"include/blosc*.h",
		"{sharedLibraryDir}/{libraryPrefix}blosc*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}blosc*.lib",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"platform:windows" : {

		"variables" : {

			"extraArgs" : "-DBUILD_TESTS=OFF -DBUILD_BENCHMARKS=OFF -DBUILD_STATIC=OFF",

		},

	},

}
