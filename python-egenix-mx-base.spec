%define name egenix-mx-base
%define version 2.0.1
%define release 1

Summary: eGenix mx-Extensions for Python - BASE package
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Copyright: Copyright (c) 1997-2001, Marc-Andre Lemburg, All Rights Reserved; Copyright (c) 2000-2001, eGenix.com Software GmbH, All Rights Reserved
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Vendor: eGenix.com Software GmbH, Langenfeld, Germany <info@egenix.com>
Packager: Marc-Andre Lemburg <mal@egenix.com>
Url: http://www.lemburg.com/python/mxExtensions.html

%description
The eGenix mx Extension Series are a collection of
Python extensions written in ANSI C and Python
which provide a large spectrum of useful additions
to everyday Python programming.

The BASE package includes the Open Source subpackages
of the series and is needed by all other add-on
packages of the series.

This software is brought to you by eGenix.com and
distributed under the eGenix.com Public License.


%prep
%setup

%build
env CFLAGS="$RPM_OPT_FLAGS" /usr/local/bin/python1.5 setup.py build

%install
/usr/local/bin/python1.5 setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README mx/Doc mx/DateTime/Doc mx/Proxy/Doc mx/BeeBase/Doc mx/Queue/Doc mx/Stack/Doc mx/TextTools/Doc mx/Tools/Doc mx/DateTime/LICENSE mx/DateTime/COPYRIGHT
