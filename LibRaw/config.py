{

	"downloads" : [

		"https://www.libraw.org/data/LibRaw-0.21.4.tar.gz",

	],

	"url" : "https://www.libraw.org/",

	"license" : "LICENSE.LGPL",

	"commands" : [

		"./configure --disable-examples --prefix={buildDir}",
		"make -j {jobs}",
		"make install"

	],

	"manifest" : [

		"include/libraw",
		# Note : LibRaw uses the "lib" prefix on Windows too.
		"{sharedLibraryDir}/libraw*{sharedLibraryExtension}*",
		"lib/libraw.lib",

	],

	"platform:windows" : {

		"commands" : [

			"msbuild LibRaw.sln -target:libraw /property:Configuration=\"Release\" /property:PlatformToolset={msvcToolset} /property:WindowsTargetPlatformVersion={windowsSDKVersion}",

		],

		"postMovePaths" : {

			"libraw/*.h" : "{buildDir}/include/libraw",
			"buildfiles/release-x86_64/libraw.dll" : "{buildDir}/bin",
			"buildfiles/release-x86_64/libraw.lib" : "{buildDir}/lib",

		},

	},

}
