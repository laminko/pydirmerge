#!/usr/bin/python2.7
import sys
import os
import shutil
import traceback

app_name = 'pydirmerge.py'
version = '1.0.0'
input_dirs = []
output_dir = ''
help_msg = 'python pydirmerge.py [-v] -i <dirs> -o <dir>\n\n' \
          '-v           Verbose mode.\n' \
          '-i <dirs>    Directories to merge. Source directories.\n' \
          '-o <dir>     Destination directory.\n' \
          '-V           Display current version.\n' \
          '-h, --help   Display help message.\n\n' \
          'e.g. python pydirmerge.py -i /test1A /test1B -o /resultAB\n'

def createDirs(dirs, old_path, new_path, v_mode):
    for d in dirs:
        destination = d.replace(old_path, new_path)
        if not os.path.exists(destination):
            if v_mode:
                print 'Creating: %s' % destination
            os.makedirs(destination)

def moveFiles(files, old_path, new_path, v_mode):
    for f in files:
        destination = f.replace(old_path, new_path)
        if not os.path.exists(destination):
            if v_mode:
                print 'Copying: from %s to %s' % (f, destination)
            #shutil.move(f, destination)
            shutil.copyfile(f, destination)
        else:
            if v_mode:
                print 'Skipped: %s' % f

def recursiveFDs(path):
    filepaths = []
    folders = []
    for root, dirs, files in os.walk(path):
        filepaths += [ os.path.join(root, f) for f in files if f != '.directory']
        folders += [ os.path.join(root, d) for d in dirs ]
    return (sorted(filepaths), sorted(folders))
    
if __name__ == '__main__':
    
    val = ''
    i = 0
    v_mode = False
    hasErr = False
    
    while True:
        i += 1
        try:
            val = sys.argv[i]
        except:
            hasErr = True
            print help_msg
            break
        
        if val == '-i':
            while True:
                i += 1
                if sys.argv[i] == '-o':
                    i -= 1
                    break
                input_dirs.append(os.path.abspath(sys.argv[i]))
            
            if len(input_dirs) < 2:
                print 'There shoud be at least two source directories to merge.'
                hasErr = True
                break
            
            print 'Source(s):'
            for idir in input_dirs:
                print idir
            hasErr = False
        
        if val == '-o':
            i += 1
            output_dir = os.path.abspath(sys.argv[i])
            print 'Destination:\n',output_dir
            break
            hasErr = False
            
        if val == '-v':
            v_mode = True
            
        if val == '-V':
            print '%s\n%s\n' % (app_name, version)
            hasErr = True
            break
        
        if val in ['-h', '--help']:
            hasErr = True
            print help_msg
    
    try:
        if not hasErr:
            print 'Started'
            
            for idir in input_dirs:
                fs, ds = recursiveFDs(idir) #FILEs, DIRs
                createDirs(ds, idir, output_dir, v_mode)
                moveFiles(fs, idir, output_dir, v_mode)
            
            print 'Finished'
    except:
        print traceback.format_exc()