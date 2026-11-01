{

	"downloads" : [

		"https://github.com/NVIDIA/optix-dev/archive/refs/tags/v8.0.0.zip",

	],

	"url" : "https://developer.nvidia.com/rtx/ray-tracing/optix",

	"license" : "LICENSE.txt",

	"commands" : [],

	"postMovePaths" : {

		"include/*" : "{buildDir}/include",

	},

	# The headers are only needed at build time, so we don't
	# package anything.
	"manifest" : [],

	# On Linux, Optix is provided by the build container.
	"enabled" : False,

	"platform:windows" : {

		"enabled" : True,

	},

}
