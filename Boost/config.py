{

	"downloads" : [

		"https://archives.boost.io/release/1.88.0/source/boost_1_88_0.tar.gz"

	],

	"license" : "LICENSE_1_0.txt",

	"url" : "http://www.boost.org",

	"dependencies" : [ "Python" ],

	"environment" : {

		# Without this, boost build will still pick up the system python framework,
		# even though we tell it quite explicitly to use the one in {buildDir}.
		"DYLD_FALLBACK_FRAMEWORK_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		# Give a helping hand to find the python headers, since the bootstrap
		# below doesn't always seem to get it right.
		"CPLUS_INCLUDE_PATH" : "{pythonIncludeDir}",

	},

	"commands" : [

		"{bootstrap}",
		"{b2} -d+2 -j {jobs} --prefix={buildDir} --without-log --disable-icu cxxstd={c++Standard} variant=release link=shared threading=multi {extraArgs} install",

	],

	"variables" : {

		"bootstrap" : "./bootstrap.sh --with-python={buildDir}/bin/python --with-python-root={buildDir} --without-icu",
		"b2" : "./b2",
		"extraArgs" : "",

	},

	"manifest" : [

		"include/boost",
		"{sharedLibraryDir}/{libraryPrefix}boost_*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}boost_*.lib",
		# Note : this has the "lib" prefix on all platforms.
		"lib/libboost_test_exec_monitor{staticLibraryExtension}",

	],

	"platform:windows" : {

		"extraDependencies" : [ "ZLib" ],

		"environment" : {

			# Boost needs help finding Python
			"PATH" : "{buildDir}\\bin;%PATH%",
			"PYTHONPATH" : "{buildDir};{buildDir}\\bin;{buildDir}\\lib\\python{pythonVersion};{buildDir}\\lib"

		},

		"variables" : {

			# `bootstrap.bat` accepts only a toolset, so we configure everything
			# else via `b2`, and tell it where to find ZLib with a `user-config.jam`.
			"bootstrap" : "bootstrap.bat && echo using zlib : : ^<include^>\"{buildDir}/include\" ^<search^>\"{buildDir}/lib\" ; > user-config.jam",
			"b2" : "b2",
			"extraArgs" : "--layout=system --toolset=msvc architecture=x86 address-model=64 --user-config=user-config.jam",

		},

		"postMovePaths" : {

			"{buildDir}/lib/*.dll" : "{buildDir}/bin",

		},

	},

}
