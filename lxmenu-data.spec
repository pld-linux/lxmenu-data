Summary:	Files required to build menu for LXDE
Summary(pl.UTF-8):	Pliki menu dla LXDE
Name:		lxmenu-data
Version:	0.1.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	cc1989444284a65dbc7047348a68d6d4
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.40.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
