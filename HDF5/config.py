{

	"downloads" : [

		"https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.12/hdf5-1.12.0/src/hdf5-1.12.0.tar.gz"

	],

	"url" : "http://www.hdfgroup.org",

	"license" : "COPYING",

	"commands" : [

		"./configure --prefix={buildDir} --enable-threadsafe --disable-hl --with-pthread=/usr/include",

		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"{sharedLibraryDir}/{libraryPrefix}hdf5*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}hdf5*.lib",

	],

	"platform:windows" : {

		"commands" : [

			"mkdir build",
			"cd build &&"
				" cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D HDF5_ENABLE_THREADSAFE=ON"
				" -D HDF5_ENABLE_Z_LIB_SUPPORT=ON"
				" -D ZLIB_ROOT={buildDir}"
				" -D HDF5_BUILD_HL_LIB=OFF"
				" -D HDF5_BUILD_CPP_LIB=OFF"
				" -D HDF5_BUILD_TOOLS=OFF"
				" -D HDF5_BUILD_EXAMPLES=OFF"
				" -D BUILD_TESTING=OFF"
				" ..",
			"cd build && cmake --build . --target install --parallel {jobs}",

		],

	},

}
