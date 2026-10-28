{

	"downloads" : [

		"https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-6.8.5-src/pyside-setup-opensource-src-6.8.5.tar.xz"

	],

	"url" : "http://www.pyside.org",

	"license" : "LICENSES/LGPL-3.0-only.txt",

	# PySide uses clang for parsing headers, hence the LLVM dependency.
	"dependencies" : [ "Python", "Setuptools", "Qt", "LLVM" ],

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"PYTHONPATH" : "{buildDir}/python",

	},

	"commands" : [

		"python setup.py --parallel {jobs} --qtpaths={buildDir}/bin/qtpaths6 install",

	],

	"manifest" : [

		"include/PySide2",
		"lib/python{pythonVersion}/site-packages/PySide2",
		"lib/python{pythonVersion}/site-packages/pyside2uic",

	],

	"platform:linux" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib",

		},

	},

	"platform:macos" : {

		"environment" : {

			"DYLD_FRAMEWORK_PATH" : "{buildDir}/lib",
			"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",

		},

		"symbolicLinks" : [

			( "{buildDir}/bin/pyside6-uic", "../lib/Python.framework/Versions/Current/bin/pyside6-uic" ),

		]

	},

	"platform:windows" : {

		"workingDir" : "p",    # Shorten overall paths to avoid Windows command character limit

		"manifest" : [

			# PySide is installed to `Lib/site-packages` which is included in Python's manifest.

		],

		"environment" : {

			"PATH" : "{buildDir}\\bin;{buildDir}\\lib;%PATH%",
			"LLVM_INSTALL_DIR" : "{buildDir}",
			"VERSION" : "",	# PySide will pull in VERSION from the environment if it exists and cause a failure because the --ignore-git conflicts with VERSION

		},

		"commands" : [
			"cd ..\\p && python setup.py install"
				" --ignore-git"
				" --openssl={buildDir}\\bin"
				" --parallel {jobs}"
				" --qtpaths={buildDir}/bin/qtpaths6.exe"
				" install",
		],

	},

}
