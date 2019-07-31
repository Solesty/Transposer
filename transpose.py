
import os
class TransposeExtension():

    replaceInternal= True

    # Initializer / Instance Attributes
    def __init__(self, primary, secondary, rootPath):
        primary = str(primary)
        secondary = str(secondary)

        if primary.startswith("."):
            raise ValueError ("Extension should not contain dot")

        if secondary.startswith("."):
            raise ValueError ("Extension should not contain dot")

        self.primaryExtension = "." + primary
        self.secondaryExtension = "." + secondary
        self.rootPath = rootPath
        os.chdir(rootPath)

    def transpose(self, file):
        print("\nTransposing " + os.path.abspath(file))
        newFile = str(file).replace(self.primaryExtension, self.secondaryExtension)
        print("Transposed " + newFile)
        
            # read the content
        fh = open(file, "r")
        lines = fh.readlines()
        newfh = open(newFile, "w")

        newLines = []
        for line in lines:
            line = line = str(line)
            if self.secondaryExtension.endswith("html"):
                line = line.replace( "<?php", "{%" )
                line = line.replace( "?>", "%}" )
                line = line.replace("\");", "\")" )
                line = line.replace("');", "')" )
            elif self.secondaryExtension.endswith("php"):
                line = line.replace( "{%", "<?php" )
                line = line.replace( "%}", "?>" )
                line = line.replace("\")", "\");" )
                line = line.replace("')", "');" )

            if self.replaceInternal:
                line = line.replace( self.primaryExtension, self.secondaryExtension )
            
            newLines.append(line)

        newfh.writelines(newLines)
        newfh.close()
        fh.close()

        os.remove(file)

    def fetchAllFiles(self, extension = None):
        filesBag = []
        for root, dir, files in os.walk(self.rootPath):
                for file in files:
                    dirpath = os.path.join( root, file )
                    if extension != None:
                        if str(file).endswith(extension) and os.path.isfile(dirpath) :
                            filesBag.append( dirpath )
                        # else:
                            # print(dirpath)
                    else:
                        filesBag.append(dirpath)
        return filesBag

    def start(self):
        print("\nInitiated\nUsing " + self.rootPath + "\n")
        files = self.fetchAllFiles(self.primaryExtension)
        for file in files:
            self.transpose(file)
        print("\nDone")
        # if path is None:
        #     path = self.rootPath

        # filesDirectories = os.listdir()
        # for file in filesDirectories:
            # if os.path.isfile(file):
            #     if str(file).endswith( self.primaryExtension ):
            #         self.transpose(os.path.abspath(file) )
            #     else:
            #         print( file + " does not have " + self.primaryExtension )
            # else:
            #     try:
            #         # file = os.path.join( self.rootPath, os.path.abspath(file) )
            #         print(file)
            #         # os.chdir(file)
            #         print("\nDirectory: " + file)
            #         self.start(file)
            #     except OSError as identifier:

            #         pass
                
        # print(filesDirectories)

testRoot = "/home/solesty7/Desktop/ILiveHere/DigitalChurch/testFolder"
testRoot = "/home/solesty7/Desktop/ILiveHere/DigitalChurch/testFolder"

import sys
try:
    rootDir = str(sys.argv[1])
    fromExtension = str(sys.argv[2])
    toExtension = str(sys.argv[3])

    transposeExtension = TransposeExtension(fromExtension, toExtension, rootDir)
    transposeExtension.start()

except IndexError:
    print("""Use this way\ntranspose root-path fromExtension toExtension\nExtension without the dot""")


    
