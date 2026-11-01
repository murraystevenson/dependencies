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
				" -C ..\\config\\cmake\\cacheinit.cmake"
				" -Wno-dev"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D HDF5_ENABLE_THREADSAFE=ON"
				" -D BUILD_TESTING=OFF"
				" -D HDF5_BUILD_EXAMPLES=OFF"
				" -D HDF5_BUILD_FORTRAN=OFF"
				" -D HDF5_ENABLE_SZIP_SUPPORT=OFF"
				" -D ZLIB_ROOT={buildDir}"
				" -D BUILD_STATIC_LIBS=OFF"
				" ..",
			"cd build && cmake --build . --target install --parallel {jobs}",

		],

	},

}
