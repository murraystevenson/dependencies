{

	"downloads" : [

		"https://github.com/blender/cycles/archive/refs/tags/v5.1.0.tar.gz",

	],

	"url" : "https://www.cycles-renderer.org/",

	"license" : "LICENSE",

	"dependencies" : [ "Boost", "OpenJPEG", "OpenImageIO", "TBB", "Alembic", "Embree", "OpenColorIO", "OpenVDB", "OpenShadingLanguage", "OpenSubdiv", "OpenPGL", "LibWebP", "Zstandard" ],

	"platform:macos" : {

		"extraDependencies" : [ "SSE2NEON" ],

	},

	"platform:windows" : {

		"extraDependencies" : [ "Optix" ],

		"environment" : {

			"PATH" : "{buildDir}/bin;%PATH%",

		},

		"variables" : {

			"extraArgs" :
				" -D CUDA_TOOLKIT_ROOT_DIR=\"%CUDA_TOOLKIT_ROOT_DIR%\""
				" -D PLATFORM_BUNDLED_LIBRARY_DIRS={buildDir}/bin"
				" -D CMAKE_EXE_LINKER_FLAGS=\"/LIBPATH:{buildDir}/lib\""
			,

		},

	},

	"environment" : {

		# Needed because the build process runs oslc.
		"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"mkdir build",
		"cd build &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}/cycles"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D CMAKE_BUILD_TYPE=Release"
			" -D WITH_LIBS_PRECOMPILED=OFF"
			" -D WITH_CYCLES_OPENIMAGEDENOISE=OFF"
			" -D WITH_CYCLES_PATH_GUIDING=ON"
			" -D WITH_CYCLES_CUDA_BINARIES=ON"
			" -D WITH_CYCLES_DEVICE_CUDA=ON"
			" -D WITH_CYCLES_DEVICE_HIP=OFF"
			" -D WITH_CYCLES_DEVICE_OPTIX=ON"
			" -D WITH_CYCLES_HYDRA_RENDER_DELEGATE=OFF"
			" -D CMAKE_POSITION_INDEPENDENT_CODE=ON"
			" -D WITH_CYCLES_USD=OFF"
			" {extraArgs}"
			" ..",
		"cd build && cmake --build . --target install --parallel {jobs} --verbose",

	],

	"postMovePaths" : {

		"src/**/*.h" : "{buildDir}/cycles/include",
		"third_party/atomic/*" : "{buildDir}/cycles/include",
		"{buildDir}/cycles/cycles{executableExtension}" : "{buildDir}/cycles/bin",
		"build/lib" : "{buildDir}/cycles",

	},

	"manifest" : [

		"cycles",

	],

}
