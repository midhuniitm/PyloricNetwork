import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using ..\\..\\..\\nC.bat -python XXX.py' or '../../../nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc # Many useful functions such as SimManager.runMultipleSims found here

projFile = File(os.getcwd(), "../PyloricPacemakerNetwork.ncx")

simConfigs = []
simConfigs.append("Default Simulation Configuration")


if len(sys.argv)==2 and sys.argv[1] == "-v1":
    
    print("Generating NeuroML v1.8.1 files...")
    nc.generateNeuroML1(projFile, simConfigs)
    
else:
    
    nc.generateNeuroML2(projFile, simConfigs)

    extra_files = ['.test.*']
    if len(sys.argv)==2 and sys.argv[1] == "-f":
        extra_files.append('LEMS_PyloricPacemakerNetwork.xml')
        extra_files.append('PyloricPacemakerNetwork.net.nml')

    from subprocess import call
    for f in extra_files:
        call(["git", "checkout", "../generatedNeuroML2/%s"%f])

quit()
