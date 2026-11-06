{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/archive/refs/tags/v1.14.11.0.tar.gz"

	],

	"url" : "https://github.com/imageworks/OpenShadingLanguage",

	"license" : "LICENSE.md",

	"dependencies" : [ "OpenImageIO", "LLVM", "PugiXML", "Python", "Robin-map" ],

	"environment" : {

		# Needed because the build process runs oslc, which
		# needs to link to the OIIO libraries.
		"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"PATH" : "{buildDir}/bin{pathListSeparator}$PATH",
		# We define `OPTIX_ROOT_DIR` in the build container for
		# Cycles to find it, but OSL wants `OPTIX_INSTALL_DIR`.
		"OPTIX_INSTALL_DIR" : "$OPTIX_ROOT_DIR",

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
			" -D STOP_ON_WARNING=0"
			" -D LLVM_STATIC=1"
			" -D USE_BATCHED={useBatched}"
			" -D OSL_SHADER_INSTALL_DIR={buildDir}/shaders"
			" -D OSL_BUILD_PLUGINS=0"
			" -D PYTHON_VERSION={pythonVersion}"
			" -D PYTHON_SITE_DIR={pythonSitePackagesDir}"
			" -D Python3_ROOT_DIR={buildDir}"
			" -D Python3_FIND_STRATEGY=LOCATION"
			" {extraArguments}"
			" ..",
		"cd gafferBuild && cmake --build . --target install --parallel {jobs} --verbose",

	],

	"variables" : {

		"extraArguments" : "",
		"useBatched" : "b8_AVX,b8_AVX2,b8_AVX2_noFMA,b8_AVX512,b8_AVX512_noFMA,b16_AVX512,b16_AVX512_noFMA",

	},

	"manifest" : [

		"bin/oslc{executableExtension}",
		"bin/oslinfo{executableExtension}",
		"bin/testshade{executableExtension}",
		"include/OSL",
		"{sharedLibraryDir}/{libraryPrefix}osl*",
		"{sharedLibraryDir}/{libraryPrefix}*oslexec*",
		"lib/{libraryPrefix}*osl*.lib",
		"doc/osl*",
		"shaders",

	],

	"platform:linux" : {

		"variables" : {

			"extraArguments" : "-D OSL_USE_OPTIX=1",

		},

	},

	"platform:macos" : {

		"variables" : {

			"useBatched" : "0",

		},

	},

	"platform:windows" : {

		"environment" : {

			# The JOM generator was used on the original Windows branch.
			"CMAKE_GENERATOR" : "NMake Makefiles JOM",
			"PATH" : "{buildDir}\\lib;{buildDir}\\bin;%PATH%",
			"CXXFLAGS" : "/utf-8",

		},

		"variables" : {

			"useBatched" : "0",
			"extraArguments" :
				" -D OSL_USE_OPTIX=1"
				" -D USE_LLVM_BITCODE=ON"
				" -D EXTRA_CPP_ARGS=\" /D TINYFORMAT_ALLOW_WCHAR_STRINGS\""
			,

		},

	},

}
