#!/usr/bin/python2.7
import argparse
import sys
import os
import shutil
import traceback
import difflib

from datetime import datetime

AUTHORS = ['lmk']
EMAILS = ['lminko.lmk@gmail.com']

class appy(object):
    
    def __init__(self):
        self._app_name = 'pydirmerge.py'
        self._version = '1.0.4'
        self._description = 'Python directories merger'
        self._authors = ', '.join(AUTHORS)
        self._authors_emails = ', '.join(EMAILS)
        self._url = 'http://code.google.com/p/pydirmerge'
        self._scripts = ['pydirmerge.py']
        

class dirMerger(object):
    
    def __init__(self):
        self.input_dirs = []
        self.dup_files = ['Source, Destination, Similarity']
        self.output_dir = ''
        self.verbose = False
        self.isMergeMove = False
        self.logfile = 'log_%s.log' % datetime.now().isoformat()
        self.str_verbose_msg = {True : "Moving", False : "Copying"}
        
    def getNowIsoFormat(self):
        return datetime.now().isoformat()
    
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
                if self.verbose:
                    print 'Creating: %s' % destination
                os.makedirs(destination)
        
    def copyFiles(self, files, old_path, new_path):
        sm = difflib.SequenceMatcher()
        
        #f = each source file
        for f in files:
            
            destination = f.replace(old_path, new_path)
            if not os.path.exists(destination):
                if self.verbose:
                    print '%s: from %s to %s' % (self.str_verbose_msg[self.isMergeMove], f, destination)
                if self.isMergeMove:
                    shutil.move(f, destination)
                else:
                    shutil.copyfile(f, destination)
                
            else:
                sm.set_seqs(open(f).read(), open(destination).read())
                similarity = round(sm.quick_ratio(), 2) * 100
                tmp_fds = '%s, %s, %s' % (f, destination, similarity)
                self.dup_files.append(tmp_fds)
                print 'Duplicate file found! Skipped.'
        
    def mergeDirs(self):
        print '>>>Started ... ON: %s' % self.getNowIsoFormat()
        
        for idir in self.input_dirs:
            fs, ds = self.recursiveFDs(idir) #FILEs, DIRs
            self.createDirs(ds, idir, self.output_dir)
            self.copyFiles(fs, idir, self.output_dir)
            
        print '>>>Finished ... ON: %s' % self.getNowIsoFormat()
        
    def printProlog(self):
        print 'Sources: \n%s\n\nDestination: \n%s' \
            % ('\n'.join(self.input_dirs), self.output_dir)
        
    def printEpilog(self):
        print 'Total duplicate found: %d' \
            '\nLog file path: %s' \
            '\n\n[See log file to view duplicate files.]' \
            % (len(self.dup_files) - 1, os.path.join(self.output_dir, self.logfile))
        
    def writeLog(self):
        print '>>>Writing log ...'
        tmp_file = open(os.path.join(self.output_dir, self.logfile), 'w')
        tmp_file.write('\n'.join(self.dup_files).__add__('\n'))
        tmp_file.close()
    
if __name__ == '__main__':
    
    obj_ap = appy()
    obj_dm = dirMerger()
    
    parser = argparse.ArgumentParser(description='To merge separated folders into one.')
    parser.add_argument('-v', action = 'store_true', help = 'Verbose mode.')
    parser.add_argument('-m', action = 'store_true', help = 'Use Move and Merge mode. Default is Copy and Merge mode.')
    parser.add_argument('-V', action = 'version', version = 'version %s' % obj_ap._version)
    parser.add_argument('-i', type = str, required = True, metavar = 'DIR', nargs = '+',\
        help = 'Source folders. AT LEAST TWO FOLDERS REQUIRED.')
    parser.add_argument('-o', type = str, required = True, metavar = 'DIR', nargs = 1,\
        help = 'Destination folder.')
    args = parser.parse_args()
    
    paras = vars(args)
    
    obj_dm.input_dirs = paras.get('i')
    obj_dm.output_dir = ''.join(paras.get('o'))
    obj_dm.verbose = paras.get('v')
    obj_dm.isMergeMove = paras.get('m')
    obj_dm.printProlog()
    obj_dm.mergeDirs()
    obj_dm.writeLog()
    obj_dm.printEpilog()
