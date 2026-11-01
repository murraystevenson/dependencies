{

	"downloads" : [

		"https://files.pythonhosted.org/packages/38/9b/e422a865e1d5d57d0e509b4e0bf1c1a70a7f6382c29a5aa428df994c8bc8/markupsafe-3.0.4.tar.gz"

	],

	"url" : "https://palletsprojects.com/p/markupsafe/",

	"license" : "LICENSE.txt",

	"dependencies" : [ "Python", "Setuptools" ],

	"environment" : {

		"PATH" : "{buildDir}/bin{pathListSeparator}$PATH",
		"DYLD_FRAMEWORK_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"PYTHONPATH" : "{buildDir}/python"

	},

	"commands" : [

		"python setup.py install --root / --prefix {buildDir} --install-lib {pythonSitePackagesDir}",

	],

}
