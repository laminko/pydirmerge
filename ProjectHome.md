# About #
| To merge folders in different or separated locations. |
|:------------------------------------------------------|

# Support #
### [Wiki](http://code.google.com/p/pydirmerge/wiki/WikiPydirmerge) ###
Read documentation, What's New?, etc.

### [Forum/Group](https://groups.google.com/forum/?fromgroups#!forum/pydirmerge) ###
Ask general questions, provide feedback to the team, etc.

# How it works #
```
=================================
Before merging
=================================
  test1
  └── aa
      ├── aa 01.txt
      ├── aa 02.txt
      ├── aa 03.txt
      ├── aa 04.txt
      ├── aa 05.txt
      └── aa 06.txt
  test2
  ├── aa
  │   ├── aa 07.txt
  │   ├── aa 08.txt
  │   ├── aa 09.txt
  │   └── aa 10.txt
  └── bb
      ├── bb 01.txt
      ├── bb 02.txt
      ├── bb 03.txt
      ├── bb 04.txt
      ├── bb 05.txt
      └── bb 06.txt
  test3
  ├── aa
  │   ├── aa 11.txt
  │   └── aa 12.txt
  └── bb
      ├── bb 07.txt
      ├── bb 08.txt
      ├── bb 09.txt
      ├── bb 10.txt
      └── cc
	  ├── cc 1.aa
	  ├── cc 2.aa
	  ├── cc 3.aa
	  └── cc 4.aa
=================================
After merging
=================================
  output123/
  ├── aa
  │   ├── aa 01.txt
  │   ├── aa 02.txt
  │   ├── aa 03.txt
  │   ├── aa 04.txt
  │   ├── aa 05.txt
  │   ├── aa 06.txt
  │   ├── aa 07.txt
  │   ├── aa 08.txt
  │   ├── aa 09.txt
  │   ├── aa 10.txt
  │   ├── aa 11.txt
  │   └── aa 12.txt
  └── bb
      ├── bb 01.txt
      ├── bb 02.txt
      ├── bb 03.txt
      ├── bb 04.txt
      ├── bb 05.txt
      ├── bb 06.txt
      ├── bb 07.txt
      ├── bb 08.txt
      ├── bb 09.txt
      ├── bb 10.txt
      └── cc
	  ├── cc 1.aa
	  ├── cc 2.aa
	  ├── cc 3.aa
	  └── cc 4.aa
```