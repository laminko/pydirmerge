#!/usr/bin/env python
import argparse
import sys
import os
import shutil
import traceback

class appy(object):
    
    def __init__(self):
        self._app_name = 'pydirmerge.py'
        self._version = '1.0.1'
        

class dirMerger(object):
    
    def __index__(self):
        self._input_dirs = []
        self._output_dir = ''
        self._verbose = False
        
    def recursiveFDs(self, path):
        filepaths = []
        folders = []
        for root, dirs, files in os.walk(path):
            filepaths += [ os.path.join(root, f) for f in files if f != '.directory']
            folders += [ os.path.join(root, d) for d in dirs ]
        return (sorted(filepaths), sorted(folders))
        
    def createDirs(self, dirs, old_path, new_path):
        for d in dirs:
            destination = d.replace(old_path, new_path)
            if not os.path.exists(destination):
                if self._verbose:
                    print 'Creating: %s' % destination
                os.makedirs(destination)
        
    def moveFiles(self, files, old_path, new_path):
        for f in files:
            destination = f.replace(old_path, new_path)
            if not os.path.exists(destination):
                if self._verbose:
                    print 'Copying: from %s to %s' % (f, destination)
                shutil.copyfile(f, destination)
            else:
                if self._verbose:
                    print 'Skipped: %s' % f
        
    def mergeDirs(self):
        print 'Started ...'
        for idir in self._input_dirs:
                fs, ds = self.recursiveFDs(idir) #FILEs, DIRs
                self.createDirs(ds, idir, self._output_dir)
                self.moveFiles(fs, idir, self._output_dir)
        print 'Finished ...'
    
if __name__ == '__main__':
    
    obj_ap = appy()
    obj_dm = dirMerger()
    
    parser = argparse.ArgumentParser(description='To merge separated folders into one.')
    parser.add_argument('-v', action = 'store_true', help = 'Verbose mode.')
    parser.add_argument('-V', action = 'version', version = 'version %s' % obj_ap._version)
    parser.add_argument('-i', type = str, required = True, metavar = 'DIR', nargs = '+', help = 'Source folders. AT LEAST TWO FOLDERS REQUIRED.')
    parser.add_argument('-o', type = str, required = True, metavar = 'DIR', nargs = 1, help = 'Destination folder.')
    args = parser.parse_args()
    
    paras = vars(args)
    obj_dm._input_dirs = paras.get('i')
    obj_dm._output_dir = ''.join(paras.get('o'))
    obj_dm._verbose = paras.get('v')
    obj_dm.mergeDirs()
    