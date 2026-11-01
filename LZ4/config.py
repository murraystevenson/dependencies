{

	"downloads" : [

		"https://github.com/lz4/lz4/archive/v1.9.2.tar.gz"

	],

	"url" : "http://www.lz4.org",
	"license" : "lib/LICENSE",

	"commands" : [

		"make install PREFIX={buildDir}",

	],

	"manifest" : [

		# Note : LZ4 uses the "lib" prefix on Windows too.
		"{sharedLibraryDir}/liblz4*{sharedLibraryExtension}*",
		"lib/liblz4*.lib",

	],

	"platform:windows" : {

		"commands" : [

			# From the LZ4 appveyor script
			"msbuild visual\\VS2017\\lz4.sln /m /verbosity:minimal /property:PlatformToolset={msvcToolset} /property:WindowsTargetPlatformVersion={windowsSDKVersion} /t:Clean,Build /p:Platform=x64 /p:Configuration=Release",

		],

		"postMovePaths" : {

			"visual/VS2017/bin/x64_Release/liblz4.dll" : "{buildDir}/bin",
			"visual/VS2017/bin/x64_Release/liblz4.lib" : "{buildDir}/lib",

		},

	},

}
