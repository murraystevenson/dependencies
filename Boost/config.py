{

	"downloads" : [

		"https://archives.boost.io/release/1.80.0/source/boost_1_80_0.tar.gz"

	],

	"license" : "LICENSE_1_0.txt",

	"url" : "http://www.boost.org",

	"dependencies" : [ "Python" ],

	"environment" : {

		# Without this, boost build will still pick up the system python framework,
		# even though we tell it quite explicitly to use the one in {buildDir}.
		"DYLD_FALLBACK_FRAMEWORK_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"MACOSX_DEPLOYMENT_TARGET" : "10.9",
		# Give a helping hand to find the python headers, since the bootstrap
		# below doesn't always seem to get it right.
		"CPLUS_INCLUDE_PATH" : "{pythonIncludeDir}",

	},

	"commands" : [

		"./bootstrap.sh --prefix={buildDir} --with-python={buildDir}/bin/python --with-python-root={buildDir} --without-libraries=log --without-icu",
		"./b2 -d+2 -j {jobs} --disable-icu cxxflags='-std=c++{c++Standard} {extraCXXFlags}' cxxstd={c++Standard} variant=release link=shared threading=multi install",

	],

	"variables" : {

		"extraCXXFlags" : "",
	},

	"manifest" : [

		"include/boost",
		"lib/libboost_*{sharedLibraryExtension}*",
		"lib/libboost_test_exec_monitor.a",

	],

	"platform:macos" : {

		"variables" : {

			"extraCXXFlags" : "-DBOOST_NO_CXX98_FUNCTION_BASE -D_HAS_AUTO_PTR_ETC=0 -Wno-deprecated-builtins -Wno-deprecated-declarations -Wno-enum-constexpr-conversion"

		},

	},

}
