{

	"downloads" : [

		"https://download.qt.io/archive/qt/6.8/6.8.5/single/qt-everywhere-opensource-src-6.8.5.tar.xz"

	],

	"dependencies" : [ "LibPNG", "LibTIFF", "LibJPEG-Turbo", "FreeType", "LLVM" ],

	"url" : "https://www.qt.io",

	"license" : "LICENSES/LGPL-3.0-only.txt",

	"environment" : {

		"PKG_CONFIG_PATH" : "{buildDir}/lib/pkgconfig",

	},

	"commands" : [

		"{configure}"
			" -prefix {buildDir}"
			" -plugindir {buildDir}/qt/plugins"
			" -release"
			" -opensource -confirm-license"
			" -no-rpath"
			" -no-dbus"
			" -no-egl"
			" -no-gstreamer"
			" -skip qtconnectivity"
			" -skip qtwebengine"
			" -skip qt3d"
			" -skip qtdeclarative"
			" -skip qtgraphs"
			" -skip qtwebchannel"
			" -skip qtnetworkauth"
			" -skip qtwayland"
			" -skip qtdoc"
			" -skip qthttpserver"
			" -skip qtlocation"
			" -skip qtlottie"
			" -skip qtmqtt"
			" -skip qtopcua"
			" -skip qtquick3d"
			" -skip qtquick3dphysics"
			" -skip qtquickeffectmaker"
			" -skip qtquicktimeline"
			" -skip qtvirtualkeyboard"
			" -skip qtwebsockets"
			" -skip qtwebview"
			" -no-libudev"
			" -no-icu"
			" -qt-pcre"
			" -qt-harfbuzz"
			" -nomake examples"
			" -nomake tests"
			" -I {buildDir}/include"
			" -L {buildDir}/lib"
			" {extraArgs}"
			" --"
			" -DCMAKE_OSX_DEPLOYMENT_TARGET={macosDeploymentTarget}"
			" {extraCMakeArgs}"
		,

		"cmake --build . --parallel {jobs} && cmake --install .",
		"{extraCommands}",

	],

	"variables" : {

		"configure" : "./configure",
		"extraCMakeArgs" :
			" -DFREETYPE_LIBRARY_RELEASE={buildDir}/lib/libfreetype{sharedLibraryExtension}"
			" -DPNG_LIBRARY={buildDir}/lib/libpng.a"
		,
		"extraCommands" : "cp {buildDir}/libexec/moc {buildDir}/libexec/rcc {buildDir}/libexec/uic {buildDir}/bin",

	},

	"manifest" : [

		"bin/moc{executableExtension}",
		"bin/qmake{executableExtension}",
		"bin/rcc{executableExtension}",
		"bin/uic{executableExtension}",

		"include/Qt*",

		"bin/Qt*.dll",
		"lib/{libraryPrefix}Qt*",
		"lib/Qt*.framework",

		"mkspecs",
		"qt",
		"lib/cmake",

	],

	"platform:linux" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib",
			"LLVM_INSTALL_DIR" : "{buildDir}",

		},

		"variables" : {

			"extraArgs" : "-xcb -bundled-xcb-xinput -I {buildDir}/include/freetype2",

		},

	},

	"platform:macos" : {

		"environment" : {

			"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",

		},

		"variables" : {

			"extraArgs" : "-no-freetype -I {buildDir}/include/freetype2",

		},

	},

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}/bin;%PATH%",

		},

		"variables" : {

			"configure" : "call configure.bat",
			"extraArgs" :
				" -opengl desktop"
				" -system-zlib"
			,
			"extraCMakeArgs" : "",
			"extraCommands" : "",

		},

	},

}
