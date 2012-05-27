#!/usr/bin/env python
import argparse
import sys
import os
import shutil
import traceback
import difflib

from datetime import datetime

class appy(object):
    
    def __init__(self):
        self._app_name = 'pydirmerge.py'
        self._version = '1.0.1'
        

class dirMerger(object):
    
    def __index__(self):
        self._input_dirs = []
        self._output_dir = ''
        self._verbose = False
        self._duplicatefiles = ['Source, Destination, Similarity']
        self._logfile = 'log_%s.log' % datetime.now().isoformat()
        
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
        #f = each source file
        sm = difflib.SequenceMatcher()
        for f in files:
            destination = f.replace(old_path, new_path)
            if not os.path.exists(destination):
                if self._verbose:
                    print 'Copying: from %s to %s' % (f, destination)
                shutil.copyfile(f, destination)
            else:
                sm.set_seqs(open(f).read(), open(destination).read())
                similarity = round(sm.quick_ratio(), 2) * 100
                self._duplicatefiles.append('%s, %s, %s' % (f, destination, similarity))
                if self._verbose:
                    print 'Duplicate file found!'
        
    def mergeDirs(self):
        print 'Started ...'
        for idir in self._input_dirs:
            fs, ds = self.recursiveFDs(idir) #FILEs, DIRs
            self.createDirs(ds, idir, self._output_dir)
            self.moveFiles(fs, idir, self._output_dir)
        print 'Finished ...'
        
    def printProlog(self):
        print 'Sources: \n%s\n\nDestination: \n%s' \
        % ('\n'.join(self._input_dirs), self._output_dir)
        
    def printEpilog(self):
        print '''Total duplicate found: %d
        Log file path: %s
        \n[See log file to view duplicate files.]''' \
        % (len(self._duplicatefiles) - 1, os.path.join(self._output_dir, self._logfile))
        
    def writeLog(self):
        print 'Writing log ...'
        tmp_file = open(os.path.join(self._output_dir, self._logfile), 'w')
        tmp_file.writelines(self._duplicatefiles)
        tmp_file.close()
    
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
    obj_dm.printProlog()
    obj_dm.mergeDirs()
    obj_dm.writeLog()
    obj_dm.printEpilog()
    