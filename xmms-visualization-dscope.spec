Summary:	Dual Scope.
Summary(pl):	Podwójny Zakres.
Name:		xmms-visualization-dscope
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://hem.passagen.se/joakime/dscope-%{version}.tar.gz
URL:		http://hem.passagen.se/joakime/linuxapp.html
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dual Scope plugin for XMMS.

%description -l pl
Plugin Podwójnego Zakresu.

%prep
%setup -q -n dscope-%{version}

%build
%{__make} \
	OPT="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT`xmms-config --visualization-plugin-dir` \
	$RPM_BUILD_ROOT`xmms-config --data-dir`

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT`xmms-config --visualization-plugin-dir` \
	XMMS_DATADIR=$RPM_BUILD_ROOT`xmms-config --data-dir`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%attr(755,root,root) %{_libdir}/xmms/*/*.so
%{_datadir}/xmms/*
