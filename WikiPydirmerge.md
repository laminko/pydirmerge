**Content**
  * [Introduction](WikiPydirmerge#Introduction.md)
  * [Download](WikiPydirmerge#Download.md)
  * [Install](WikiPydirmerge#Install.md)
  * [How to use](WikiPydirmerge#How_to_use.md)

# Introduction #

This is a python utility program to merge folders in different locations with same name and same or different contents.

The purpose is to merge folders after unfinished or uncompleted folders moving.


# Download #

To download latest, click [here](http://code.google.com/p/pydirmerge/downloads/detail?name=pydirmerge%201.0.2.tar.gz)!

# Install #

To extract tar.gz.
```
~$tar -xf pydirmerge\ latest.tar.gz
```

Enter into extracted directory.
```
~$cd pydirmerge\ latest
```

To install, enter following code.
```
~$sudo python setup.py install
```

Enter your root password and press Enter. It will continue installation.

# How to use #

Quick Guide:
<pre>
usage: pydirmerge.py [-h] [-v] [-m] [-V] -i DIR [DIR ...] -o DIR<br>
<br>
To merge separated folders into one.<br>
<br>
optional arguments:<br>
-h, --help        show this help message and exit<br>
-v                Verbose mode.<br>
-m                Use Move and Merge mode. Default is Copy and Merge mode.<br>
-V                show program's version number and exit<br>
-i DIR [DIR ...]  Source folders. AT LEAST TWO FOLDERS REQUIRED.<br>
-o DIR            Destination folder.<br>
</pre>

### Merging directories ###
There are two modes to merge directories:
  1. Copy and Merge and
  1. Move and Merge.

**Note!** Copy and Merge is default mode.

### Copy and Merge mode ###

To merge directories, please enter:
```
pydirmerge.py -i /home/user1/folder1 /home/user1/other/folder1 -o /home/user/recover/folder1
```
Program will copy files and folders from two folders(_/home/user1/folder1_ and _/home/user1/other/folder1_) to destination folder(_/home/user/recover/folder1_).

### Move and Merge mode ###

To merge directories, please enter and add **-m**:
```
pydirmerge.py -m -i /home/user1/folder1 /home/user1/other/folder1 -o /home/user/recover/folder1
```
Program will copy files and folders from two folders(_/home/user1/folder1_ and _/home/user1/other/folder1_) to destination folder(_/home/user/recover/folder1_).

### Verbose mode ###
Just put **-v** above command. Output will be displayed.
```
pydirmerge.py -v -i /home/user1/folder1 /home/user1/other/folder1 -o /home/user/recover/folder1
```