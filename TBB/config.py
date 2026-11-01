{

	"downloads" : [

		"https://github.com/uxlfoundation/oneTBB/archive/refs/tags/v2022.3.0.tar.gz"

	],

	"url" : "http://threadingbuildingblocks.org/",

	"license" : "LICENSE.txt",

	"commands" : [

		"mkdir build",
		"cd build &&"
			" cmake"
			" -D CMAKE_CXX_STANDARD={c++Standard}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D TBB_TEST=OFF"
			" ..",
		"cd build && cmake --build . --target install --parallel {jobs} --verbose",
	],

	"manifest" : [

		"include/tbb",
		"include/oneapi",
		"{sharedLibraryDir}/{libraryPrefix}tbb*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}tbb*.lib",

	],

}
