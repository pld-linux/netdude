Summary:	network dump data displayer and editor
Summary(pl):	Wy¶wietlacz i edytor zrzutów sieciowych
Name:		netdude
Version:	0.3.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-am.patch
Patch1:		%{name}-paths.patch
URL:		http://netdude.sf.net/
BuildRequires:	gtk+-devel
BuildRequires:	libpcap-devel
BuildRequires:	gettext-devel
BuildRequires:	libltdl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dcsvsd

%description -l pl
aaa

%package devel
Summary:	header files for developing netdude plugins
Summary(pl):	pliki nag³ówkowe do budowy pluginów netdude
Group:		Development
Requires:	%{name} = %{version}

%description devel

%description devel -l pl

%package static
Summary:	static plugins for netdude
Summary(pl):	pluginy statyczne do netdude
Group:		Development
Requires:	%{name}-devel = %{version}

%description static

%description static -l pl

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/%{name}/*/*.la
%{_mandir}/man*/*
%{_gtkdocdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}/*/*.a
