Summary:	Network dump data displayer and editor
Summary(pl):	Wy¶wietlacz i edytor zrzutów sieciowych
Name:		netdude
Version:	0.3.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/netdude/%{name}-%{version}.tar.gz
# Source0-md5:	d561feec5388469f3449bb4ba4d89bdf
Patch0:		%{name}-am.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-bpf.patch
URL:		http://netdude.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netdude is the NETwork DUmp data Displayer and Editor for tcpdump
tracefiles. It is a GUI-based tool that allows you to make detailed
changes to packets in tcpdump tracefiles.

%description -l pl
Netdude (NETwork DUmp data Displayer and Editor) to program do
wy¶wietlania i edycji plików zrzutów sieciowych (tracefiles) z
tcpdumpa. Jest to narzêdzie z graficznym interfejsem, pozwalaj±ce
wykonaæ szczegó³owe zmiany w pakietach zrzutów z tcpdumpa.

%package devel
Summary:	Header files for developing netdude plugins
Summary(pl):	Pliki nag³ówkowe do budowy wtyczek netdude
Group:		Development
Requires:	%{name} = %{version}-%{version}
Obsoletes:	netdude-static

%description devel
Header files for developing netdude plugins.

%description devel -l pl
Pliki nag³ówkowe do budowy wtyczek netdude.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing configure.in
rm -rf libltdl
%{__gettextize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README ROADMAP TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/protocols
%attr(755,root,root) %{_libdir}/%{name}/*/*.so
%{_libdir}/%{name}/*/*.la
%{_mandir}/man*/*
%{_gtkdocdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
