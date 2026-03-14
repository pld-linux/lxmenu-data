Summary:	Files required to build menu for LXDE
Summary(pl.UTF-8):	Pliki menu dla LXDE
Name:		lxmenu-data
Version:	0.1.7
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://github.com/lxde/lxmenu-data/archive/refs/tags/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	0de7cd2810e0ea23ebea2b91cfee246c
URL:		http://www.lxde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.40.0
Requires:	filesystem >= 4.1-15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides files required to build freedesktop.org menu
spec-compliant desktop menus for LXDE.

%description -l pl.UTF-8
Pakiet zawiera pliki potrzebne do zbudowania menu LXDE zgodnego z
freedesktop.org.

%prep
%setup -q

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{_sysconfdir}/xdg/menus/lxde-applications.menu
%{_datadir}/desktop-directories/lxde-*.directory
