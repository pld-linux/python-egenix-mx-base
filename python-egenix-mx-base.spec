
%define module egenix-mx-base
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)
%define mxdir %{python_sitepkgsdir}/mx

Summary:	eGenix mx-Extensions for Python - BASE package
Name:		python-%{module}
Version:	2.0.1
Release:	1
URL:		http://www.lemburg.com/python/mxExtensions.html
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
License:	Distributable
Source0:	http://www.lemburg.com/python/%{module}-%{version}.tar.gz
Requires:	python
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The eGenix mx Extension Series are a collection of Python extensions
written in ANSI C and Python which provide a large spectrum of useful
additions to everyday Python programming.

The BASE package includes the Open Source subpackages of the series
and is needed by all other add-on packages of the series.

This software is brought to you by eGenix.com and distributed under
the eGenix.com Public License.

%package -n python-mx-DateTime
Summary:	Date and time Python extension
Summary(pl):	Obiekty daty i czasu dla jêzyka Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-%{module} = %{version}

%description -n python-mx-DateTime
mxDateTime is an extension package that provides three new object
types, DateTime, DateTimeDelta and RelativeDateTime, which let you
store and handle date/time values in a much more natural way than by
using ticks (seconds since 1.1.70 0:00 UTC; the encoding used by the
time module).

You can add, subtract and even multiply instances, pickle and copy
them and convert the results to strings, COM dates, ticks and some
other more esoteric values. In addition, there are several convenient
constructors and formatters at hand to greatly simplify dealing with
dates and times in real-world applications.

In addition to providing an easy-to-use Python interface the package
also exports a comfortable C API interface for other extensions to
build upon. This is especially interesting for database applications
which often have to deal with date/time values (the mxODBC package is
one example of an extension using this interface).

%description -l pl -n python-mx-DateTime
N/A

%package -n python-mx-TextTools
Summary:	Efficient text manipulation extensions for Python
Summary(pl):	Wydajne manipulowanie tekstem w jêzyku Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-%{module} = %{version}

%description -n python-mx-TextTools
mxTextTools is an extension package for Python that provides several
useful functions and types that implement high-performance text
manipulation and searching algorithms in addition to a very flexible
and extendable state machine, the Tagging Engine, that allows scanning
and processing text based on low-level byte-code "programs" written
using Python tuples. It gives you access to the speed of C without the
need to do any compile and link steps every time you change the
parsing description.

Applications include parsing structured text, finding and extracting
text (either exact or using translation tables) and recombining
strings to form new text.

%description -l pl -n python-mx-TextTools
N/A

%package -n python-mx-Stack
Summary:	Stack implementation for Python
Summary(pl):	Implementacja stosu dla jêzyka Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-%{module} = %{version}

%description -n python-mx-Stack
mxStack is an extension package that provides a new object type called
Stack. It works much like what you would expect from such a type,
having .push() and .pop() methods and focusses on obtaining maximum
speed at low memory costs.

%description -l pl -n python-mx-Stack
N/A

%package -n python-mx-Queue
Summary:	Queue implementation for Python
Summary(pl):	Implementacja stosu dla jêzyka Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-%{module} = %{version}

%description -n python-mx-Queue
N/A

%description -l pl -n python-mx-Queue
N/A

%package -n python-mx-Tools
Summary:	Some handy functions and objects which provides new builtins for Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-%{module} = %{version}

%description -n python-mx-Tools
mxTools is an extension package that includes a collection of handy
functions and objects giving additional functionality in form of new
builtins to the Python programmer.

The package auto-installs the new functions and objects as builtins
upon first import. This means that they become instantely available to
all other modules without any further action on your part. Add the
line import mx.Tools.NewBuiltins to your site.py script and they will
be available to all users at your site as if they were installed in
the Python interpreter itself.

%description -l pl -n python-mx-Tools
N/A

%package -n python-mx-Proxy
Summary:	Support for Bastion like implementations for Python
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-%{module} = %{version}

%description -n python-mx-Proxy
mxProxy is an extension package that provides a new type that is
suitable to implement Bastion like features without the need to use
restricted execution environments.

The type's main features are secure data encapsulation (the hidden
objects are not accessible from Python since they are stored in
internal C structures), customizable attribute lookup methods and a
cleanup protocol that helps in breaking circular references prior to
object deletion.

The latest version adds a very interesting new feature: weak
references which help you work with circular references in a way that
doesn't cause memory leakage in a Python system.

%description -l pl -n python-mx-Proxy
N/A

%package -n python-mx-BeeBase
Summary:	High performance construction kit for disk based indexed databases (B+Tree)
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-%{module} = %{version}

%description -n python-mx-BeeBase
mxBeeBase is a high performance construction kit for disk based
indexed databases. It offers components which you can plug together to
easily build your own custom mid-sized databases (the current size
limit is sizeof(long) which gives you an address range of around 2GB
on 32-bit platforms).

The two basic building blocks in mxBeeBase are storage and index.
Storage is implemented as variable record length data storage with
integrated data protection features, automatic data recovery and
locking for multi process access. Indexes use a high performance
optimized B+Tree implementation built on top of Thomas Niemann's
Cookbook B+Tree implementation.

%description -l pl -n python-mx-BeeBase
N/A

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

gzip -9nf README mx/LICENSE mx/COPYRIGHT mx/Doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz mx/*.gz mx/Doc/*.gz mx/Doc/mx{Extensions,License}.html
%{mxdir}/*.py?

%dir %{mxdir}/Misc
%{mxdir}/Misc/*.py?

%files -n python-mx-DateTime
%defattr(644,root,root,755)
%doc mx/DateTime/Doc/*.html
%dir %{mxdir}/DateTime
%{mxdir}/DateTime/*.py?

%dir %{mxdir}/DateTime/mxDateTime
%{mxdir}/DateTime/mxDateTime/*.py?
%attr(755,root,root) %{mxdir}/DateTime/mxDateTime/*.so

%files -n python-mx-TextTools
%defattr(644,root,root,755)
%doc mx/TextTools/Doc/*.html
%dir %{mxdir}/TextTools
%{mxdir}/TextTools/*.py?

%dir %{mxdir}/TextTools/mxTextTools
%{mxdir}/TextTools/mxTextTools/*.py?
%attr(755,root,root) %{mxdir}/TextTools/mxTextTools/*.so

%dir %{mxdir}/TextTools/Constants
%{mxdir}/TextTools/Constants/*.py?

%files -n python-mx-Stack
%defattr(644,root,root,755)
%doc mx/Stack/Doc/*.html
%dir %{mxdir}/Stack
%{mxdir}/Stack/*.py?

%dir %{mxdir}/Stack/mxStack
%{mxdir}/Stack/mxStack/*.py?
%attr(755,root,root) %{mxdir}/Stack/mxStack/*.so

%files -n python-mx-Queue
%defattr(644,root,root,755)
%doc mx/Queue/Doc/*.html
%dir %{mxdir}/Queue
%{mxdir}/Queue/*.py?

%dir %{mxdir}/Queue/mxQueue
%{mxdir}/Queue/mxQueue/*.py?
%attr(755,root,root) %{mxdir}/Queue/mxQueue/*.so

%files -n python-mx-Tools
%defattr(644,root,root,755)
%doc mx/Tools/Doc/*.html
%dir %{mxdir}/Tools
%{mxdir}/Tools/*.py?

%dir %{mxdir}/Tools/mxTools
%{mxdir}/Tools/mxTools/*.py?
%attr(755,root,root) %{mxdir}/Tools/mxTools/*.so

%files -n python-mx-Proxy
%defattr(644,root,root,755)
%doc mx/Proxy/Doc/*.html
%dir %{mxdir}/Proxy
%{mxdir}/Proxy/*.py?

%dir %{mxdir}/Proxy/mxProxy
%{mxdir}/Proxy/mxProxy/*.py?
%attr(755,root,root) %{mxdir}/Proxy/mxProxy/*.so

%files -n python-mx-BeeBase
%defattr(644,root,root,755)
%doc mx/BeeBase/Doc/*.html
%dir %{mxdir}/BeeBase
%{mxdir}/BeeBase/*.py?

%dir %{mxdir}/BeeBase/mxBeeBase
%{mxdir}/BeeBase/mxBeeBase/*.py?
%attr(755,root,root) %{mxdir}/BeeBase/mxBeeBase/*.so
