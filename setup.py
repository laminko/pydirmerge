#!/usr/bin/env python

def main():
    from distutils.core import setup
    
    setup(name='pydirmerge',
          version='1.0.0',
          description='Python directories merger',
          author='lmk',
          author_email='lminko.lmk@gmail.com',
          url='http://code.google.com/p/pydirmerge',
          scripts=['pydirmerge.py'],
         )
    
if __name__ == '__main__':
    main()