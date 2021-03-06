%define package icoutils
%define version 0.31.1
%define release 1

Summary:	Utility for extracting and converting Microsoft icon and cursor files
Name:		%{package}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Amusements/Graphics
Source:         http://savannah.nongnu.org/download/%{package}/%{package}-%{version}.tar.gz
URL:            http://www.nongnu.org/%{package}
Packager:       Oskar Liljeblad <oskar@osk.mine.nu>
Vendor:         Oskar Liljeblad <oskar@osk.mine.nu>
BuildRoot:      %{_tmppath}/%{package}-%{version}-%{release}-root

%description
The icoutils are a set of program for extracting and converting images in                                                                                       
Microsoft Windows(R) icon and cursor files. These files usually have the                                                                                        
extension .ico or .cur, but they can also be embedded in executables and                                                                                        
libraries (.dll-files).                                                                                                                                         
                                                                                                                                                                
The icotool program converts icon and cursor files into a set of PNG                                                                                            
images. (Each icon/cursor file may contain multiple images, usually of                                                                                          
different sizes and with different number of colors.) Icotool can also                                                                                          
create icon/cursor files from PNG images.                                                                                                                       
                                                                                                                                                                
The wrestool program can extract both icons and cursors from 32-bit ("PE")                                                                                      
and 16-bit ("NE") executables and libraries. It writes .ico and .cur files                                                                                      
that can be used on Windows(R) operating systems as well. Other types of                                                                                        
embedded resourced can be extracted, however only in raw form - icons and                                                                                       
cursors require additional conversion before they can be saved as icon and                                                                                      
cursor files.                                                                                                                                                   
                                                                                                                                                                
The extresso script automates the tasks of extracting and converting icons.                                                                                     
This is done with the help of of special resource scripts. The purpose of                                                                                       
these scripts are to give names to the icons in the executables and                                                                                             
libraries.                                                                                                                                                      

%prep
%setup -q

%build
./configure --prefix=${_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS TODO ChangeLog
%{_bindir}/*
%{_mandir}/*/*
