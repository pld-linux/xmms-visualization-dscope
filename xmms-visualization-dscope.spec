Summary:	Dual Scope
Summary(pl):	Podwójny Zakres
Name:		xmms-visualization-dscope
Version:	1.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dscope-v%{version}.tar.gz
# Source0-md5:	a883144570402cd67eb1090a4b9b529a
URL:		http://www.shell.linux.se/bm/index.php
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _xmms_plugin_dir        %(xmms-config --visualization-plugin-dir)
%define		_xmms_data_dir		%(xmms-config --data-dir)

%description
Dual Scope plugin for XMMS.

%description -l pl
Plugin Podwójnego Zakresu.

%prep
%setup -q -n dscope-v%{version}

%build
%{__make} \
	OPT="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_xmms_plugin_dir} \
	$RPM_BUILD_ROOT%{_xmms_data_dir}

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT%{_xmms_plugin_dir} \
	XMMS_DATADIR=$RPM_BUILD_ROOT%{_xmms_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%attr(755,root,root) %{_xmms_plugin_dir}/*.so
%{_xmms_data_dir}/*
