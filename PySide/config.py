{

	"downloads" : [

		"https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-6.8.5-src/pyside-setup-opensource-src-6.8.5.tar.xz"

	],

	"url" : "http://www.pyside.org",

	"license" : "LICENSES/LGPL-3.0-only.txt",

	# PySide uses clang for parsing headers, hence the LLVM dependency.
	"dependencies" : [ "Python", "Setuptools", "Qt", "LLVM" ],

	"environment" : {

		"PATH" : "{buildDir}/bin{pathListSeparator}$PATH",
		"PYTHONPATH" : "{buildDir}/python",

	},

	"commands" : [

		"python setup.py --parallel {jobs} --qtpaths={buildDir}/bin/qtpaths6{executableExtension} install {extraArgs}",

	],

	"variables" : {

		"extraArgs" : "",

	},

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

		# Shorten overall paths to avoid the Windows command length limit.
		"workingDir" : "p",

		"environment" : {

			"PATH" : "{buildDir}\\bin;{buildDir}\\lib;%PATH%",
			"LLVM_INSTALL_DIR" : "{buildDir}",
			# PySide will pull in VERSION from the environment if it exists, and
			# fail because `--ignore-git` conflicts with it.
			"VERSION" : "",

		},

		"variables" : {

			"extraArgs" : "--ignore-git --openssl={buildDir}\\bin",

		},

	},

}
