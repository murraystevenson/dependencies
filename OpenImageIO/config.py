{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/OpenImageIO/releases/download/v3.0.6.1/OpenImageIO-3.0.6.1.tar.gz",

	],

	"url" : "http://www.openimageio.org",

	"license" : "LICENSE.md",

	"dependencies" : [ "Boost", "Python", "PyBind11", "OpenEXR", "LibTIFF", "LibPNG", "OpenJPEG", "LibJPEG-Turbo", "OpenColorIO", "LibRaw", "PugiXML", "Fmt", "LibWebP", "TBB", "FreeType", "Robin-map" ],

	"environment" : {

		"PATH" : "{buildDir}/bin{pathListSeparator}$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",

	},

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_CXX_STANDARD={c++Standard}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D CMAKE_FIND_FRAMEWORK=LAST"
			" -D USE_FFMPEG=NO"
			" -D USE_GIF=0"
			" -D USE_OPENVDB=NO"
			" -D USE_PYTHON=YES"
			" -D USE_EXTERNAL_PUGIXML=YES"
			" -D OIIO_BUILD_TESTS=NO"
			" -D OIIO_DOWNLOAD_MISSING_TESTDATA=NO"
			" -D PYTHON_VERSION={pythonVersion}"
			" -D PYTHON_SITE_DIR={pythonSitePackagesDir}/OpenImageIO"
			" -D Python3_ROOT_DIR={buildDir}"
			" -D Python3_FIND_STRATEGY=LOCATION"
			# This disables `iv`, which fails to build on Mac
			# due to OpenGL deprecations, and which we've never
			# packaged anyway.
			" -D USE_QT=NO"
			" {extraArgs}"
			" ..",
		"cd gafferBuild && cmake --build . --target install --parallel {jobs} --verbose",

	],

	"variables" : {

		"extraArgs" : "",

	},

	"manifest" : [

		"bin/maketx{executableExtension}",
		"bin/oiiotool{executableExtension}",

		"include/OpenImageIO",
		"{sharedLibraryDir}/{libraryPrefix}OpenImageIO*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}OpenImageIO*.lib",

		"doc/openimageio.pdf",

	],

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}/bin;{buildDir}/lib;%PATH%",
			"CXXFLAGS" : "/utf-8",

		},

		"variables" : {

			"extraArgs" : " -D USE_SIMD=sse4.2",

		},

	},

}
