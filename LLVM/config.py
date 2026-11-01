{

	"downloads" : [

		"https://github.com/llvm/llvm-project/releases/download/llvmorg-{llvmVersion}/llvm-{llvmVersion}.src.tar.xz",
		"https://github.com/llvm/llvm-project/releases/download/llvmorg-{llvmVersion}/clang-{llvmVersion}.src.tar.xz",
		"https://github.com/llvm/llvm-project/releases/download/llvmorg-{llvmVersion}/cmake-{llvmVersion}.src.tar.xz"

	],

	"url" : "https://llvm.org",

	"license" : "LICENSE.TXT",

	"commands" : [

		"cmake -E rename ../clang-{llvmVersion}.src tools/clang",
		"{extraCommands}",
		"cmake -E rename ../cmake-{llvmVersion}.src ../cmake",
		"mkdir build",
		"cd build &&"
			" cmake"
			" -D CMAKE_CXX_STANDARD={c++Standard}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_BUILD_TYPE=Release"
			" -D LLVM_ENABLE_RTTI=ON"
			" -D LLVM_ENABLE_LIBXML2=OFF"
			" -D LLVM_ENABLE_ZSTD=OFF"
			" -D LLVM_INCLUDE_BENCHMARKS=OFF"
			" -D LLVM_INCLUDE_EXAMPLES=OFF"
			" -D LLVM_INCLUDE_TESTS=OFF"
			" -D LLVM_INCLUDE_UTILS=OFF"
			" -D CLANG_ENABLE_STATIC_ANALYZER=OFF"
			" -D CLANG_ENABLE_ARCMT=OFF"
			" -D LLVM_TARGETS_TO_BUILD={buildTargets}"
			" {extraArgs}"
			" ..",
		"cd build && cmake --build . --target install --parallel {jobs}",

	],

	"variables" : {

		"llvmVersion" : "20.1.8",
		"buildTargets" : "\"Native\"",
		"extraArgs" :
			" -D GCC_INSTALL_PREFIX={compilerRoot}"
			" -D USE_DEPRECATED_GCC_INSTALL_PREFIX=ON"
		,
		"extraCommands" : "",

	},

	"platform:linux" : {

		"variables" : {

			"buildTargets" : "\"Native;NVPTX\"",

		},

	},

	"platform:windows" : {

		"variables" : {

			"buildTargets" : "\"Native;NVPTX\"",
			"extraArgs" :
				" -D LLVM_BUILD_LLVM_C_DYLIB=OFF"
				" -D LLVM_ENABLE_ZLIB=OFF"
			,
			# Must be applied after Clang has been moved into place, so we
			# can't use the standard `patches/windows` mechanism.
			"extraCommands" : "patch -p1 < ..\\..\\patches\\windows\\clang_fma.patch.txt",

		},

	},

}
