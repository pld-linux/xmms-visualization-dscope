Summary:	Dual Scope
Summary(pl.UTF-8):   Podwójny Zakres
Name:		xmms-visualization-dscope
Version:	1.3.1
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dscope-v%{version}.tar.gz
# Source0-md5:	a883144570402cd67eb1090a4b9b529a
URL:		http://www.shell.linux.se/bm/index.php
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dual Scope plugin for XMMS.

%description -l pl.UTF-8
Wtyczka Podwójnego Zakresu dla XMMS-a.

%prep
%setup -q -n dscope-v%{version}

%build
%{__make} \
	OPT="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_visualization_plugindir} \
	$RPM_BUILD_ROOT%{xmms_datadir}

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT%{xmms_visualization_plugindir} \
	XMMS_DATADIR=$RPM_BUILD_ROOT%{xmms_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
%{xmms_datadir}/*
