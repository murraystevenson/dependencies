{

	"downloads" : [ "https://www.python.org/ftp/python/3.13.16/Python-3.13.16.tgz" ],

	"publicVariables" : {

		"pythonVersion" : "3.13",
		"pythonMajorVersion" : "3",
		"pythonMinorVersion" : "13",
		"pythonIncludeDir" : "{buildDir}/include/python{pythonVersion}",
		"pythonLibDir" : "{buildDir}/lib",

	},

	"url" : "https://www.python.org",

	"license" : "LICENSE",

	"dependencies" : [ "LibFFI", "TBB" ],

	"environment" : {

		"LDFLAGS" : "-L{buildDir}/lib",
		"CPPFLAGS" : "-I{buildDir}/include",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"./configure --prefix={buildDir} {libraryType} --with-ensurepip=install",
		"make -j {jobs}",
		"make install",
		"{buildDir}/bin/python3 -m pip install setuptools==81.0.0",

	],

	"manifest" : [

		"bin/python{executableExtension}",
		"bin/python*[0-9]{executableExtension}",

		"include/python*",

		"lib/{libraryPrefix}python*{sharedLibraryExtension}*",
		"lib/Python.framework*",
		"lib/python{pythonVersion}",

	],

	"variables" : {

		"libraryType" : "--enable-shared",

	},

	"platform:linux" : {

		"symbolicLinks" : [

			( "{buildDir}/bin/python", "python3" ),

		],

	},

	"platform:macos" : {


		"variables" : {

			"libraryType" : "--enable-framework={buildDir}/lib",

		},

		"environment" : {

			"MACOSX_DEPLOYMENT_TARGET" : "12.0",

		},

		"publicVariables" : {


			"pythonIncludeDir" : "{buildDir}/lib/Python.framework/Headers",
			"pythonLibDir" : "{buildDir}/lib/Python.framework/Versions/{pythonVersion}/lib",

		},

		"symbolicLinks" : [

			( "{buildDir}/bin/python", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonMajorVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonVersion}" ),
			( "{buildDir}/lib/Python.framework/Versions/Current/lib/libpython{pythonMajorVersion}.dylib", "libpython{pythonMajorVersion}.{pythonMinorVersion}.dylib" ),
		],

	},

	"platform:windows" : {

		"publicVariables" : {

			"pythonIncludeDir" : "{buildDir}/include",
			"pythonLibDir" : "{buildDir}/libs",

		},

		"manifest" : [

			"bin/python{executableExtension}",
			"bin/{libraryPrefix}python*{sharedLibraryExtension}*",
			"bin/concrt140{sharedLibraryExtension}",
			"bin/msvcp140*{sharedLibraryExtension}",
			"bin/vcruntime140*{sharedLibraryExtension}",

			"libs",

			"DLLs",

			# Gross. But here's the reasoning for now: we can't put the modules into a directory
			# like `lib/` as on Linux because it causes havoc with cmake finding the site-packages
			# directory for downstream projects that need to install their Python modules.
			# If we just do `Lib/*` then the packager will sweep up everything in the `lib`
			# folder at the end of the entire dependencies build, not at the time Python is built.
			# We can glob for the top-level modules. But package directories must be listed explicitly. 
			# So for now to come up with this list, do a build of just Python, and then a simple
			# Python script or similar to get a list of everything in the `lib` folder.
			"Lib/*.py",
			"Lib/__phello__",
			"Lib/__pycache__",
			"Lib/_pyrepl",
			"Lib/asyncio",
			"Lib/collections",
			"Lib/concurrent",
			"Lib/ctypes",
			"Lib/curses",
			"Lib/dbm",
			"Lib/email",
			"Lib/encodings",
			"Lib/html",
			"Lib/http",
			"Lib/importlib",
			"Lib/json",
			"Lib/logging",
			"Lib/multiprocessing",
			"Lib/pathlib",
			"Lib/pydoc_data",
			"Lib/re",
			"Lib/site-packages",
			"Lib/sqlite3",
			"Lib/sysconfig",
			"Lib/tomllib",
			"Lib/unittest",
			"Lib/urllib",
			"Lib/wsgiref",
			"Lib/xml",
			"Lib/xmlrpc",
			"Lib/zipfile",
			"Lib/zoneinfo",

			# Double gross. Python on Windows seems pretty insistent on having the
			# includes in the `include` directory, not a subdirectory. Many of the
			# GafferDependencies projects can handle it in a subdirectory, but
			# PySide and perhaps others can't. There's also a good change putting
			# includes in a subdirectory would break installing things with pip
			# or setuptools (the distutils.sysconfig.get_config_var("INCLUDEPY") will
			# return the wrong value if the includes are located anywhere except `include`)
			"include/abstract.h",
			"include/bltinmodule.h",
			"include/boolobject.h",
			"include/bytearrayobject.h",
			"include/bytesobject.h",
			"include/ceval.h",
			"include/codecs.h",
			"include/compile.h",
			"include/complexobject.h",
			"include/cpython",
			"include/critical_section.h",
			"include/datetime.h",
			"include/descrobject.h",
			"include/dictobject.h",
			"include/dynamic_annotations.h",
			"include/enumobject.h",
			"include/errcode.h",
			"include/exports.h",
			"include/fileobject.h",
			"include/fileutils.h",
			"include/floatobject.h",
			"include/frameobject.h",
			"include/genericaliasobject.h",
			"include/import.h",
			"include/internal",
			"include/intrcheck.h",
			"include/iterobject.h",
			"include/listobject.h",
			"include/lock.h",
			"include/longobject.h",
			"include/marshal.h",
			"include/memoryobject.h",
			"include/methodobject.h",
			"include/modsupport.h",
			"include/moduleobject.h",
			"include/monitoring.h",
			"include/object.h",
			"include/objimpl.h",
			"include/opcode.h",
			"include/opcode_ids.h",
			"include/osdefs.h",
			"include/osmodule.h",
			"include/patchlevel.h",
			"include/pyatomic.h",
			"include/pybuffer.h",
			"include/pycapsule.h",
			"include/pyconfig.h",
			"include/pydtrace.h",
			"include/pyerrors.h",
			"include/pyexpat.h",
			"include/pyframe.h",
			"include/pyhash.h",
			"include/pylifecycle.h",
			"include/pymacconfig.h",
			"include/pymacro.h",
			"include/pymath.h",
			"include/pymem.h",
			"include/pyport.h",
			"include/pystate.h",
			"include/pystats.h",
			"include/pystrcmp.h",
			"include/pystrtod.h",
			"include/Python.h",
			"include/pythonrun.h",
			"include/pythread.h",
			"include/pytypedefs.h",
			"include/py_curses.h",
			"include/rangeobject.h",
			"include/setobject.h",
			"include/sliceobject.h",
			"include/structmember.h",
			"include/structseq.h",
			"include/sysmodule.h",
			"include/traceback.h",
			"include/tupleobject.h",
			"include/typeslots.h",
			"include/unicodeobject.h",
			"include/warnings.h",
			"include/weakrefobject.h",

			# `lib` prefix is correct for Windows
			"DLLs/libssl*{sharedLibraryExtension}*",
			"DLLs/libcrypto*{sharedLibraryExtension}*",
		],

		"environment" : {

			"PATH" : "{buildDir}\\bin;%PATH%",
			"DefaultWindowsSDKVersion" : "10.0.22621.0",

		},

		"commands" : [

			"call PCbuild/build.bat -p x64 --no-tkinter \"/p:PlatformToolset=v143\"",

			# Copy the directory layout to our build directory
			"PCbuild\\amd64\\python.exe PC\\layout -s . -b PCbuild\\amd64 -v --precompile --include-pip --include-dev --include-stable --copy {buildDir}",
			"{buildDir}\\python.exe -m pip install setuptools==81.0.0",

		],

		"postMovePaths" : {

			"{buildDir}/python.exe" : "{buildDir}/bin",
			"{buildDir}/python{pythonMajorVersion}{pythonMinorVersion}.dll" : "{buildDir}/bin",
			"{buildDir}/python{pythonMajorVersion}.dll" : "{buildDir}/bin",
			"{buildDir}/vcruntime*.dll" : "{buildDir}/bin",
			"externals/openssl-bin-1.1.1u/amd64/libcrypto.lib" : "{buildDir}/lib",
			"externals/openssl-bin-1.1.1u/amd64/libssl.lib" : "{buildDir}/lib",
			"externals/openssl-bin-1.1.u/amd64/include/opensll" : "{buildDir}/include",

		}

	}

}
