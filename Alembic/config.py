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
			" ."
		,

		"make VERBOSE=1 -j {jobs}",
		"make install",

	],

	"manifest" : [

		"bin/abcconvert",
		"bin/abcecho",
		"bin/abcechobounds",
		"bin/abcls",
		"bin/abcstitcher",
		"bin/abctree",

		"include/Alembic",

		"lib/libAlembic*",

		"python/alembic*",

	],

}
