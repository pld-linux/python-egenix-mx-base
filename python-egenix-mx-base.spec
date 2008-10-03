# TODO make examples package

%define		module	egenix-mx-base
%define		mxdir	%{py_sitedir}/mx

Summary:	eGenix mx-Extensions for Python
Summary(pl.UTF-8):	eGenix mx-Extensions dla języka Python
Name:		python-%{module}
Version:	3.1.1
Release:	2
License:	distributable
Group:		Libraries/Python
#Source0Download: http://www.egenix.com/files/python/eGenix-mx-Extensions.html
Source0:	http://www.egenix.com/files/python/%{module}-%{version}.tar.gz
# Source0-md5:	d0f3b1adca33a68867bf50f000060cd6
URL:		http://www.egenix.com/files/python/eGenix-mx-Extensions.html
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The eGenix mx Extension Series are a collection of Python extensions
written in ANSI C and Python which provide a large spectrum of useful
additions to everyday Python programming.

This package includes the Open Source subpackages of the series and is
needed by all other add-on packages of the series.

%description -l pl.UTF-8
eGenix mx Extensions Series jest zestawem modułów, ułatwiających życie
każdemu programiście piszącemu w języku Python, napisanych w ANSI C i
Pythonie.

Ten pakiet zawiera podstawowe moduły wymagane przez inne pakiety.

%package devel
Summary:	Basic header files for eGenix extensions
Summary(pl.UTF-8):	Podstawowe pliki nagłówkowe dla rozszerzeń eGenix
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description devel
Basic header files for eGenix extensions.

%description devel -l pl.UTF-8
Podstawowe pliki nagłówkowe dla rozszerzeń eGenix.

%package -n python-mx-BeeBase
Summary:	High performance construction kit for disk based indexed databases (B+Tree)
Summary(pl.UTF-8):	Wysokiej jakości pakiet do tworzenia indeksowanych baz danych (B+Tree)
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

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

%description -n python-mx-BeeBase -l pl.UTF-8
mxBeeBase jest wysokiej jakości pakietem do tworzenia indeksowanych
baz danych. Zawiera komponenty, które można razem łączyć w celu
zbudowania własnej bazy. Obecny limit ilości danych wynosi 2GB (max.
wartość liczby całkowitej typu long na platformach 32 bitowych).

Dwoma podstawowymi komponentami w tym pakiecie są indeksy oraz
rekordy. Rekord może być zmiennej długości i zawiera mechanizmy
ochrony, automatycznego odzyskiwania, blokowania, a także
wieloprocesowego dostępu do danych. Do indeksowania są używane bardzo
wydajne B-drzewa zaimplementowane na podstawie Cookbook B+Tree Thomasa
Newmanna.

%package -n python-mx-DateTime
Summary:	Date and time Python extension
Summary(pl.UTF-8):	Obiekty daty i czasu dla języka Python
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

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

%description -n python-mx-DateTime -l pl.UTF-8
mxDateTime jest pakietem modułów, które definiują trzy nowe klasy -
DateTime, DateTimeDelta oraz RelativeDateTime. Umożliwiają one
przechowywanie oraz operowanie na dacie i czasie w bardziej naturalny
sposób niż za pomocą sekund od początku 1 stycznia 1970 (tak jak w
module time).

Programista może dodawać, odejmować, mnożyć (w sensie arytmetycznym),
serializować, a także mnożyć (w sesnie rozmnażania :-) obiekty.
Instancje w/w klas mogą być konwertowane do napisów i sekund.
Dodatkowo moduł zawiera kilka użytecznych funkcji do tworzenia nowych
obiektów i ich formatowania.

Oprócz, łatwych w użyciu, klas języka Python, pakiet dostarcza także
bardzo wygodny interfejs w C, który może być wykorzystany do tworzenia
innych rozszerzeń (np.: pakiet mxODBC). W szczególności, cecha ta jest
interesująca w przypadku aplikacji bazodanowych, które operują na
dacie i czasie.

%package -n python-mx-DateTime-devel
Summary:	Header file for DateTime Python extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia DateTime dla Pythona
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{version}-%{release}

%description -n python-mx-DateTime-devel
Header file for DateTime Python extension.

%description -n python-mx-DateTime-devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia DateTime dla Pythona.

%package -n python-mx-Proxy
Summary:	Support for Bastion like implementations for Python
Summary(pl.UTF-8):	Wsparcie dla implementacji typu Bastion dla języka Python
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

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

%description -n python-mx-Proxy -l pl.UTF-8
Pakiet mxProxy dostarcza nowe klasy, które implementują funkcjonalność
typu Bastion bez potrzeby ograniczania środowiska, w którym jest
wykonywana aplikacja.

Podstawowymi zaletami są: bezpieczne obudowywanie danych (ukryte
obiekty nie są dostępne z poziomu Pythona, ponieważ są one
przechowywane w wewnętrznych strukturach języka C), konfigurowalne
metody do pobierania wartości atrybutów oraz protokół, który pomaga w
rozbijaniu zapętlonych referencji podczas usuwania obiektów.

Ostatnia wersja pakietu implementuje tzw. słabe referencje, które nie
powodują wycieków pamięci w przypadku referencji zapętlonych.

%package -n python-mx-Queue
Summary:	Queue implementation for Python
Summary(pl.UTF-8):	Implementacja kolejki dla języka Python
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-mx-Queue
mxQueue is an extension package that provides a new object type called
Queue. It works much like what you would expect from such a type,
having .push() and .pop() methods and focusses on obtaining maximum
speed at low memory costs.

%description -n python-mx-Queue -l pl.UTF-8
Pakiet mxQueue zawiera implementację kolejki, która zawiera typowe
metody takie jak pop() czy push(). Mechanizm został napisany tak by,
przy minimalnym zużyciu pamięci, był bardzo wydajny.

%package -n python-mx-Stack
Summary:	Stack implementation for Python
Summary(pl.UTF-8):	Implementacja stosu dla języka Python
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-mx-Stack
mxStack is an extension package that provides a new object type called
Stack. It works much like what you would expect from such a type,
having .push() and .pop() methods and focusses on obtaining maximum
speed at low memory costs.

%description -n python-mx-Stack -l pl.UTF-8
Pakiet mxStack zawiera implementację stosu, która zawiera typowe
metody takie jak pop() czy push(). Mechanizm został napisany tak by,
przy minimalnym zużyciu pamięci, był bardzo wydajny.

%package -n python-mx-TextTools
Summary:	Efficient text manipulation extensions for Python
Summary(pl.UTF-8):	Wydajne manipulowanie tekstem w języku Python
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

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

%description -n python-mx-TextTools -l pl.UTF-8
Pakiet mxTextTools dostarcza szereg użytecznych typów i funkcji, które
implementują wysokiej jakości algorytmy do wyszukiwania i manipulacji
tekstu. Programista dostaje wydajne (na poziomie kodu napisanego w
języku C) narzędzie bez potrzeby kompilacji i konsolidacji, kiedy
zajdzie potrzeba zmiany sposobu interpretacji tekstu.

Pakiet może mieć zastosowanie w aplikacjach, które muszą interpretować
tekst zadany w konkretnym formacie, a także wyszukiwać, pobierać i
manipulować tekstem.

%package -n python-mx-Tools
Summary:	Some handy functions and objects which provides new builtins for Python
Summary(pl.UTF-8):	Kilka użytecznych klas i funkcji w postaci wew. mechanizmów Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

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

%description -n python-mx-Tools -l pl.UTF-8
Pakiet mxTools zawiera kilka użytecznych klas i funkcji, które dają
więcej możliwości programiście, w postaci wewnętrznych mechanizmów
języka Python.

Pakiet ten instaluje, jako mechanizmy wewnętrzne Pythona, wszystkie
funkcje i klasy po ich pierwszym dołączeniu do kodu. Oznacza to, że są
one dostępne dla innych modułów bez jakichkolwiek dodatkowych
zabiegów. Wystarczy dodać linię "import mx.Tools.NewBuiltins" do
odpowiedniego skryptu (site.py) i zdefiniowane funkcje oraz klasy będą
widoczne dla wszystkich użytkowników tak, jak by były wbudowane w
język Python.

%package -n python-mx-UID
Summary:	Fast Unique Identifiers for Python
Summary(pl.UTF-8):	Szybkie unikalne identyfikatory (UID) dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-mx-UID
UID is an extension package that provides a fast mechanism for
generating unique identification strings (UIDs).

%description -n python-mx-UID -l pl.UTF-8
Pakiet UID dostarcza szybki mechanizm do generowania unikalnych ciągów
znaków (UID).

%package -n python-mx-URL
Summary:	Flexible URL Data-Type for Python
Summary(pl.UTF-8):	Elastyczny typ danych URL dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-mx-URL
URL package provides a new datatype for storing and manipulating URL
values as well as a few helpers related to URL building, encoding and
decoding.

%description -n python-mx-Stack -l pl.UTF-8
Pakiet URL dostarcza nowy typ danych do przechowywania i manipulowania
wartościami URL jak również kilka pomocniczych elementów służących do
tworzenia, kodowania i dekodowania adresów URL.

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
find $RPM_BUILD_ROOT%{py_sitedir} -name '*.py' -o -regex '.*/\(COPYRIGHT\|LICENSE\|README\|Doc\|Examples\)' | xargs rm -rf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README mx/LICENSE mx/COPYRIGHT mx/Doc/*License.txt
%dir %{mxdir}
%dir %{py_incdir}/mx
%{mxdir}/*.py[co]
%dir %{mxdir}/Misc
%{mxdir}/Misc/*.py[co]
%{py_sitedir}/*.egg-info

%files devel
%defattr(644,root,root,755)
%{py_incdir}/mx/mxh.h

%files -n python-mx-BeeBase
%defattr(644,root,root,755)
%doc mx/BeeBase/Doc/*.pdf
%dir %{mxdir}/BeeBase
%{mxdir}/BeeBase/*.py[co]
%dir %{mxdir}/BeeBase/mxBeeBase
%{mxdir}/BeeBase/mxBeeBase/*.py[co]
%attr(755,root,root) %{mxdir}/BeeBase/mxBeeBase/*.so

# -devel if needed
#%{py_incdir}/mx/btr.h
#%{py_incdir}/mx/mxBeeBase.h

%files -n python-mx-DateTime
%defattr(644,root,root,755)
%doc mx/DateTime/Doc/*.pdf
%dir %{mxdir}/DateTime
%{mxdir}/DateTime/*.py[co]
%dir %{mxdir}/DateTime/mxDateTime
%{mxdir}/DateTime/mxDateTime/*.py[co]
%attr(755,root,root) %{mxdir}/DateTime/mxDateTime/*.so

%files -n python-mx-DateTime-devel
%defattr(644,root,root,755)
%{py_incdir}/mx/mxDateTime.h

%files -n python-mx-Proxy
%defattr(644,root,root,755)
%doc mx/Proxy/Doc/*.pdf
%dir %{mxdir}/Proxy
%{mxdir}/Proxy/*.py[co]
%dir %{mxdir}/Proxy/mxProxy
%{mxdir}/Proxy/mxProxy/*.py[co]
%attr(755,root,root) %{mxdir}/Proxy/mxProxy/*.so

# -devel if needed
#%{py_incdir}/mx/mxProxy.h

%files -n python-mx-Queue
%defattr(644,root,root,755)
%doc mx/Queue/Doc/*.pdf
%dir %{mxdir}/Queue
%{mxdir}/Queue/*.py[co]
%dir %{mxdir}/Queue/mxQueue
%{mxdir}/Queue/mxQueue/*.py[co]
%attr(755,root,root) %{mxdir}/Queue/mxQueue/*.so

# -devel if needed
#%{py_incdir}/mx/mxQueue.h

%files -n python-mx-Stack
%defattr(644,root,root,755)
%doc mx/Stack/Doc/*.pdf
%dir %{mxdir}/Stack
%{mxdir}/Stack/*.py[co]
%dir %{mxdir}/Stack/mxStack
%{mxdir}/Stack/mxStack/*.py[co]
%attr(755,root,root) %{mxdir}/Stack/mxStack/*.so

%files -n python-mx-TextTools
%defattr(644,root,root,755)
%doc mx/TextTools/Doc/*.pdf
%dir %{mxdir}/TextTools
%{mxdir}/TextTools/*.py[co]
%dir %{mxdir}/TextTools/mxTextTools
%{mxdir}/TextTools/mxTextTools/*.py[co]
%attr(755,root,root) %{mxdir}/TextTools/mxTextTools/*.so
%dir %{mxdir}/TextTools/Constants
%{mxdir}/TextTools/Constants/*.py[co]

# -devel if needed
#%{py_incdir}/mx/mxTextTools.h
#%{py_incdir}/mx/mxbmse.h
#%{py_incdir}/mx/mxte.h

%files -n python-mx-Tools
%defattr(644,root,root,755)
%doc mx/Tools/Doc/*.pdf
%dir %{mxdir}/Tools
%{mxdir}/Tools/*.py[co]
%dir %{mxdir}/Tools/mxTools
%{mxdir}/Tools/mxTools/*.py[co]
%attr(755,root,root) %{mxdir}/Tools/mxTools/*.so

# -devel if needed
#%{py_incdir}/mx/mxTools.h

%files -n python-mx-UID
%defattr(644,root,root,755)
%doc mx/UID/Doc/*.pdf
%dir %{mxdir}/UID
%{mxdir}/UID/*.py[co]
%dir %{mxdir}/UID/mxUID
%{mxdir}/UID/mxUID/*.py[co]
%attr(755,root,root) %{mxdir}/UID/mxUID/*.so

# -devel if needed
#%{py_incdir}/mx/mxUID.h

%files -n python-mx-URL
%defattr(644,root,root,755)
%doc mx/URL/Doc/*.pdf
%dir %{mxdir}/URL
%{mxdir}/URL/*.py[co]
%dir %{mxdir}/URL/mxURL
%{mxdir}/URL/mxURL/*.py[co]
%attr(755,root,root) %{mxdir}/URL/mxURL/*.so

# -devel if needed
#%{py_incdir}/mx/mxURL.h
