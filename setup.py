#!/usr/bin/env python

def main():
    from distutils.core import setup
    from pydirmerge import appy
    
    obj_ap = appy()
    
    setup(name = obj_ap._app_name,
          version = obj_ap._version,
          description = obj_ap._description,
          author = obj_ap._authors,
          author_email = obj_ap._authors_emails,
          url = obj_ap._url,
          scripts = obj_ap._scripts)
    
if __name__ == '__main__':
    main()