#
# TODO:
#	- fix gettextize
#
Summary:	Network dump data displayer and editor
Summary(pl.UTF-8):	Wyświetlacz i edytor zrzutów sieciowych
Name:		netdude
Version:	0.5.0
Release:	0.1
License:	Distributable
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/netdude/%{name}-%{version}.tar.gz
# Source0-md5:	af7c302c2aaeee28f4a38d800f2991a0
Patch0:		%{name}-am.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-lt_ptr.patch
Patch3:		%{name}-duplicate_files.patch
URL:		http://netdude.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libltdl-devel
BuildRequires:	libnetdude-devel
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netdude is the NETwork DUmp data Displayer and Editor for tcpdump
tracefiles. It is a GUI-based tool that allows you to make detailed
changes to packets in tcpdump tracefiles.

%description -l pl.UTF-8
Netdude (NETwork DUmp data Displayer and Editor) to program do
wyświetlania i edycji plików zrzutów sieciowych (tracefiles) z
tcpdumpa. Jest to narzędzie z graficznym interfejsem, pozwalające
wykonać szczegółowe zmiany w pakietach zrzutów z tcpdumpa.

%package devel
Summary:	Header files for developing netdude plugins
Summary(pl.UTF-8):	Pliki nagłówkowe do budowy wtyczek netdude
Group:		Development
Requires:	%{name} = %{version}-%{release}
Obsoletes:	netdude-static

%description devel
Header files for developing netdude plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do budowy wtyczek netdude.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
rm -rf libltdl
#%%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-tcpdump=%{_sbindir}/tcpdump \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*/*.a

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING README ROADMAP TODO AUTHORS
%attr(755,root,root) %{_bindir}/netdude*
%{_datadir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/protocols
%attr(755,root,root) %{_libdir}/%{name}/*/nd*.so
%{_libdir}/%{name}/*/nd*.la
%{_mandir}/man1/netdude.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
