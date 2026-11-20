{

	"downloads" : [

		"https://github.com/uclouvain/openjpeg/archive/refs/tags/v2.5.4.tar.gz"

	],

	"url" : "https://www.openjpeg.org/",

	"license" : "LICENSE",

	"commands" : [

		"mkdir build",
		"cd build &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			# OpenJPEG's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" ..",
		"cd build && make install -j {jobs} VERBOSE=1",

	],

	"manifest" : [

		"include/openjpeg-2.5",
		"{sharedLibraryDir}/{libraryPrefix}openjp2*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}openjp2*{staticLibraryExtension}",

	],

	"platform:windows" : {

		"commands" : [

			"mkdir build",
			"cd build &&"
				" cmake"
				" -W-nodev -G {cmakeGenerator}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D BUILD_SHADER_LIBS=on"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" ..",
			"cd build && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",

		]

	}

}
