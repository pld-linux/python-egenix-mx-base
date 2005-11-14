# TODO make examples package

%define		module	egenix-mx-base
%define		mxdir	%{py_sitedir}/mx

Summary:	eGenix mx-Extensions for Python
Summary(pl):	eGenix mx-Extensions dla j�zyka Python
Name:		python-%{module}
Version:	2.0.5
Release:	9
License:	distributable
Group:		Libraries/Python
#Source0Download: http://www.egenix.com/files/python/eGenix-mx-Extensions.html
Source0:	http://www.egenix.com/files/python/%{module}-%{version}.tar.gz
# Source0-md5:	a793a8fd2d5f646a2fb683d2d967a16b
URL:		http://www.egenix.com/files/python/eGenix-mx-Extensions.html
BuildRequires:	python
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	python-modules >= 2.2.2
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The eGenix mx Extension Series are a collection of Python extensions
written in ANSI C and Python which provide a large spectrum of useful
additions to everyday Python programming.

This package includes the Open Source subpackages of the series and is
needed by all other add-on packages of the series.

%description -l pl
eGenix mx Extensions Series jest zestawem modu��w, u�atwiaj�cych �ycie
ka�demu programi�cie pisz�cemu w j�zyku Python, napisanych w ANSI C i
Pythonie.

Ten pakiet zawiera podstawowe modu�y wymagane przez inne pakiety.

%package devel
Summary:	Basic header files for eGenix extensions
Summary(pl):	Podstawowe pliki nag��wkowe dla rozszerze� eGenix
Group:		Development/Languages/Python

%description devel
Basic header files for eGenix extensions.

%description devel -l pl
Podstawowe pliki nag��wkowe dla rozszerze� eGenix.

%package -n python-mx-DateTime
Summary:	Date and time Python extension
Summary(pl):	Obiekty daty i czasu dla j�zyka Python
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	python-%{module} = %{version}-%{release}

%description -n python-mx-DateTime
mxDateTime is an extension package that provides three new object
types - DateTime, DateTimeDelta and RelativeDateTime, which let you
store and handle date/time values in a much more natural way than by
using ticks (seconds since 01.01.1970 0:00 UTC; the encoding used by
the time module).

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

%description -n python-mx-DateTime -l pl
mxDateTime jest pakietem modu��w, kt�re definiuj� trzy nowe klasy -
DateTime, DateTimeDelta oraz RelativeDateTime. Umo�liwiaj� one
przechowywanie oraz operowanie na dacie i czasie w bardziej naturalny
spos�b ni� za pomoc� sekund od pocz�tku 1 stycznia 1970 (tak jak w
module time).

Programista mo�e dodawa�, odejmowa�, mno�y� (w sensie arytmetycznym),
serializowa�, a tak�e mno�y� (w sesnie rozmna�ania :-) obiekty.
Instancje w/w klas mog� by� konwertowane do napis�w i sekund.
Dodatkowo modu� zawiera kilka u�ytecznych funkcji do tworzenia nowych
obiekt�w i ich formatowania.

Opr�cz, �atwych w u�yciu, klas j�zyka Python, pakiet dostarcza tak�e
bardzo wygodny interfejs w C, kt�ry mo�e by� wykorzystany do tworzenia
innych rozszerze� (np.: pakiet mxODBC). W szczeg�lno�ci, cecha ta jest
interesuj�ca w przypadku aplikacji bazodanowych, kt�re operuj� na
dacie i czasie.

%package -n python-mx-DateTime-devel
Summary:	Headers for date and time Python extension
Summary(pl):	Nag��wki modu��w daty i czasu
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{version}-%{release}

%description -n python-mx-DateTime-devel
Headers for date and time Python extension.

%description -n python-mx-DateTime-devel -l pl
Nag��wki dla modu��w daty i czasu.

%package -n python-mx-TextTools
Summary:	Efficient text manipulation extensions for Python
Summary(pl):	Wydajne manipulowanie tekstem w j�zyku Python
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	python-%{module} = %{version}-%{release}

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

%description -n python-mx-TextTools -l pl
Pakiet mxTextTools dostarcza szereg u�ytecznych typ�w i funkcji, kt�re
implementuj� wysokiej jako�ci algorytmy do wyszukiwania i manipulacji
tekstu. Programista dostaje wydajne (na poziomie kodu napisanego w
j�zyku C) narz�dzie bez potrzeby kompilacji i konsolidacji, kiedy
zajdzie potrzeba zmiany sposobu interpretacji tekstu.

Pakiet mo�e mie� zastosowanie w aplikacjach, kt�re musz� interpretowa�
tekst zadany w konkretnym formacie, a tak�e wyszukiwa�, pobiera� i
manipulowa� tekstem.

%package -n python-mx-Stack
Summary:	Stack implementation for Python
Summary(pl):	Implementacja stosu dla j�zyka Python
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	python-%{module} = %{version}-%{release}

%description -n python-mx-Stack
mxStack is an extension package that provides a new object type called
Stack. It works much like what you would expect from such a type,
having .push() and .pop() methods and focusses on obtaining maximum
speed at low memory costs.

%description -n python-mx-Stack -l pl
Pakiet mxStack zawiera implementacj� stosu, kt�ra zawiera typowe
metody takie jak pop() czy push(). Mechanizm zosta� napisany tak by,
przy minimalnym zu�yciu pami�ci, by� bardzo wydajny.

%package -n python-mx-Queue
Summary:	Queue implementation for Python
Summary(pl):	Implementacja kolejki dla j�zyka Python
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	python-%{module} = %{version}-%{release}

%description -n python-mx-Queue
mxQueue is an extension package that provides a new object type called
Queue. It works much like what you would expect from such a type,
having .push() and .pop() methods and focusses on obtaining maximum
speed at low memory costs.

%description -n python-mx-Queue -l pl
Pakiet mxQueue zawiera implementacj� kolejki, kt�ra zawiera typowe
metody takie jak pop() czy push(). Mechanizm zosta� napisany tak by,
przy minimalnym zu�yciu pami�ci, by� bardzo wydajny.

%package -n python-mx-Tools
Summary:	Some handy functions and objects which provides new builtins for Python
Summary(pl):	Kilka u�ytecznych klas i funkcji w postaci wew. mechanizm�w Pythona
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	python-%{module} = %{version}-%{release}

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

%description -n python-mx-Tools -l pl
Pakiet mxTools zawiera kilka u�ytecznych klas i funkcji, kt�re daj�
wi�cej mo�liwo�ci programi�cie, w postaci wewn�trznych mechanizm�w
j�zyka Python.

Pakiet ten instaluje, jako mechanizmy wewn�trzne Pythona, wszystkie
funkcje i klasy po ich pierwszym do��czeniu do kodu. Oznacza to, �e s�
one dost�pne dla innych modu��w bez jakichkolwiek dodatkowych
zabieg�w. Wystarczy doda� lini� "import mx.Tools.NewBuiltins" do
odpowiedniego skryptu (site.py) i zdefiniowane funkcje oraz klasy b�d�
widoczne dla wszystkich u�ytkownik�w tak, jak by by�y wbudowane w
j�zyk Python.

%package -n python-mx-Proxy
Summary:	Support for Bastion like implementations for Python
Summary(pl):	Wsparcie dla implementacji typu Bastion dla j�zyka Python
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	python-%{module} = %{version}-%{release}

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

%description -n python-mx-Proxy -l pl
Pakiet mxProxy dostarcza nowe klasy, kt�re implementuj� funkcjonalno��
typu Bastion bez potrzeby ograniczania �rodowiska, w kt�rym jest
wykonywana aplikacja.

Podstawowymi zaletami s�: bezpieczne obudowywanie danych (ukryte
obiekty nie s� dost�pne z poziomu Pythona, poniewa� s� one
przechowywane w wewn�trznych strukturach j�zyka C), konfigurowalne
metody do pobierania warto�ci atrybut�w oraz protok�, kt�ry pomaga w
rozbijaniu zap�tlonych referencji podczas usuwania obiekt�w.

Ostatnia wersja pakietu implementuje tzw. s�abe referencje, kt�re nie
powoduj� wyciek�w pami�ci w przypadku referencji zap�tlonych.

%package -n python-mx-BeeBase
Summary:	High performance construction kit for disk based indexed databases (B+Tree)
Summary(pl):	Wysokiej jako�ci pakiet do tworzenia indeksowanych baz danych (B+Tree)
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	python-%{module} = %{version}-%{release}

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

%description -n python-mx-BeeBase -l pl
mxBeeBase jest wysokiej jako�ci pakietem do tworzenia indeksowanych
baz danych. Zawiera komponenty, kt�re mo�na razem ��czy� w celu
zbudowania w�asnej bazy. Obecny limit ilo�ci danych wynosi 2GB (max.
warto�� liczby ca�kowitej typu long na platformach 32 bitowych).

Dwoma podstawowymi komponentami w tym pakiecie s� indeksy oraz
rekordy. Rekord mo�e by� zmiennej d�ugo�ci i zawiera mechanizmy
ochrony, automatycznego odzyskiwania, blokowania, a tak�e
wieloprocesowego dost�pu do danych. Do indeksowania s� u�ywane bardzo
wydajne B-drzewa zaimplementowane na podstawie Cookbook B+Tree Thomasa
Newmanna.

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_incdir}/mx
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitedir}

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.h \
	-exec mv {} $RPM_BUILD_ROOT%{py_incdir}/mx \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README mx/LICENSE mx/COPYRIGHT mx/Doc/mxLicense.html
%dir %{mxdir}
%dir %{py_incdir}/mx
%{mxdir}/*.py[co]

%dir %{mxdir}/Misc
%{mxdir}/Misc/*.py[co]

%files devel
%defattr(644,root,root,755)
%{py_incdir}/mx/mxh.h

%files -n python-mx-DateTime
%defattr(644,root,root,755)
%doc mx/DateTime/Doc/*.html
%dir %{mxdir}/DateTime
%{mxdir}/DateTime/*.py[co]

%dir %{mxdir}/DateTime/mxDateTime
%{mxdir}/DateTime/mxDateTime/*.py[co]
%attr(755,root,root) %{mxdir}/DateTime/mxDateTime/*.so

%files -n python-mx-DateTime-devel
%defattr(644,root,root,755)
%{py_incdir}/mx/mxDateTime.h

%files -n python-mx-TextTools
%defattr(644,root,root,755)
%doc mx/TextTools/Doc/*.html
%dir %{mxdir}/TextTools
%{mxdir}/TextTools/*.py[co]

%dir %{mxdir}/TextTools/mxTextTools
%{mxdir}/TextTools/mxTextTools/*.py[co]
%attr(755,root,root) %{mxdir}/TextTools/mxTextTools/*.so

%dir %{mxdir}/TextTools/Constants
%{mxdir}/TextTools/Constants/*.py[co]

%files -n python-mx-Stack
%defattr(644,root,root,755)
%doc mx/Stack/Doc/*.html
%dir %{mxdir}/Stack
%{mxdir}/Stack/*.py[co]

%dir %{mxdir}/Stack/mxStack
%{mxdir}/Stack/mxStack/*.py[co]
%attr(755,root,root) %{mxdir}/Stack/mxStack/*.so

%files -n python-mx-Queue
%defattr(644,root,root,755)
%doc mx/Queue/Doc/*.html
%dir %{mxdir}/Queue
%{mxdir}/Queue/*.py[co]

%dir %{mxdir}/Queue/mxQueue
%{mxdir}/Queue/mxQueue/*.py[co]
%attr(755,root,root) %{mxdir}/Queue/mxQueue/*.so

%files -n python-mx-Tools
%defattr(644,root,root,755)
%doc mx/Tools/Doc/*.html
%dir %{mxdir}/Tools
%{mxdir}/Tools/*.py[co]

%dir %{mxdir}/Tools/mxTools
%{mxdir}/Tools/mxTools/*.py[co]
%attr(755,root,root) %{mxdir}/Tools/mxTools/*.so

%files -n python-mx-Proxy
%defattr(644,root,root,755)
%doc mx/Proxy/Doc/*.html
%dir %{mxdir}/Proxy
%{mxdir}/Proxy/*.py[co]

%dir %{mxdir}/Proxy/mxProxy
%{mxdir}/Proxy/mxProxy/*.py[co]
%attr(755,root,root) %{mxdir}/Proxy/mxProxy/*.so

%files -n python-mx-BeeBase
%defattr(644,root,root,755)
%doc mx/BeeBase/Doc/*.html
%dir %{mxdir}/BeeBase
%{mxdir}/BeeBase/*.py[co]

%dir %{mxdir}/BeeBase/mxBeeBase
%{mxdir}/BeeBase/mxBeeBase/*.py[co]
%attr(755,root,root) %{mxdir}/BeeBase/mxBeeBase/*.so
