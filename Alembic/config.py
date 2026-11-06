{

	"downloads" : [

		"https://github.com/alembic/alembic/archive/refs/tags/1.8.3.tar.gz"

	],

	"url" : "http://www.alembic.io",

	"license" : "LICENSE.txt",

	"dependencies" : [ "Python", "OpenEXR", "Boost", "HDF5" ],

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D HDF5_ROOT={buildDir}"
			" -D USE_HDF5=TRUE"
			" -D USE_TESTS=FALSE"
			" -D USE_ARNOLD=FALSE"
			" -D USE_PRMAN=FALSE"
			" -D USE_MAYA=FALSE"
			" {extraArgs}"
			" ."
		,

		"cmake --build . --target install --parallel {jobs} --verbose",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"manifest" : [

		"bin/abcconvert{executableExtension}",
		"bin/abcecho{executableExtension}",
		"bin/abcechobounds{executableExtension}",
		"bin/abcls{executableExtension}",
		"bin/abcstitcher{executableExtension}",
		"bin/abctree{executableExtension}",

		"include/Alembic",

		"{sharedLibraryDir}/{libraryPrefix}Alembic*",
		"lib/{libraryPrefix}Alembic*.lib",

		"python/alembic*",

	],

	"platform:windows" : {

		"variables" : {

			"extraArgs" :
				" -D USE_STATIC_HDF5=ON"
			,

		},

		"postMovePaths" : {

			"{buildDir}/lib/Alembic.dll" : "{buildDir}/bin",

		},

	},

}
