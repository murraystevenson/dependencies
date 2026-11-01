{

	"downloads" : [

		"http://github.com/zeux/pugixml/releases/download/v1.11/pugixml-1.11.tar.gz"

	],

	"url" : "https://pugixml.org",

	"license" : "LICENSE.md",

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" {extraArgs}"
			" ..",
		"cd gafferBuild && cmake --build . --target install --parallel {jobs} --verbose",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}\\bin;%PATH%"

		},

		"variables" : {

			"extraArgs" : "-D CMAKE_CXX_STANDARD={c++Standard}",

		},

	},

}
