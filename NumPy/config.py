{

	"downloads" : [

		"https://files.pythonhosted.org/packages/source/n/numpy/numpy-2.3.5.tar.gz"

	],

	"url" : "https://numpy.org",

	"license" : "LICENSE.txt",

	"dependencies" : [ "Python" ],

	"environment" : {

		"PATH" : "{buildDir}\\bin;%PATH%",

	},

	"commands" : [

		# We install the official binary wheel. The source archive
		# above is only used for the license.
		"{buildDir}\\python.exe -m pip install numpy==2.3.5",

	],

}
