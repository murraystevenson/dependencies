{

	"downloads" : [

		"https://download.osgeo.org/libtiff/tiff-4.1.0.zip",

	],

	"url" : "http://www.libtiff.org",

	"license" : "COPYRIGHT",

	"dependencies" : [ "LibJPEG-Turbo" ],

	"environment" : {

		# Needed to make sure we link against the libjpeg
		# in the Gaffer distribution and not the system
		# libjpeg.
		"CPPFLAGS" : "-I{buildDir}/include",
		"LDFLAGS" : "-L{buildDir}/lib",

	},

	"commands" : [

		"./configure --without-x --prefix={buildDir}",
		"make -j {jobs}",
		"make install"

	],

	"manifest" : [

		"include/tiff*",
		"{sharedLibraryDir}/{libraryPrefix}tiff*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}tiff.lib",

	],

	"platform:windows" : {

		"extraDependencies" : [ "ZLib" ],

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild &&"
				" cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" ..",
			"cd gafferBuild && cmake --build . --target install --parallel {jobs}",

		],

	},

}
