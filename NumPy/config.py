{

	"downloads" : [

		"https://files.pythonhosted.org/packages/source/n/numpy/numpy-2.3.5.tar.gz"

	],

	"url" : "https://numpy.org",

	"license" : "LICENSE.txt",

	"dependencies" : [ "Python" ],

	"environment" : {

		"DYLD_FRAMEWORK_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		# We install the official binary wheel. The source archive
		# above is only used for the license.
		"{buildDir}/bin/python3 -m pip install numpy==2.3.5",

	],

}
