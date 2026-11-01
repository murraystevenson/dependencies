{

	"downloads" : [

		"https://files.pythonhosted.org/packages/2d/01/beb7331fc6c8d1c49dd051e3611379bfe379e915c808e1301506027fce9d/psutil-5.9.6.tar.gz"

	],

	"url" : "https://github.com/giampaolo/psutil",

	"license" : "LICENSE",

	"dependencies" : [ "Python", "Setuptools" ],

	"environment" : {

		"PATH" : "{buildDir}/bin{pathListSeparator}$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"DYLD_FRAMEWORK_PATH" : "{buildDir}/lib",
		"PYTHONPATH" : "{buildDir}/python",

	},

	"commands" : [

		"python setup.py install --root / --prefix {buildDir} --install-lib {pythonSitePackagesDir}",

	],

}
