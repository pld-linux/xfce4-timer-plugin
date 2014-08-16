Summary:	Xfce panel timer plugin
Summary(pl.UTF-8):	Wtyczka panelu Xfce odliczająca czas
Name:		xfce4-timer-plugin
Version:	1.6.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-timer-plugin/1.6/%{name}-%{version}.tar.bz2
# Source0-md5:	3be2a4ccfb2af20441b1d25c2cea5f28
Patch0:		format-security.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple plugin that lets the user run an alarm at a specified
time or at the end of a specified countdown period.

%description -l pl.UTF-8
Wtyczka ta pozwala na powiadamianie o zdefiniowanym wcześniej
zdarzeniu, bądź po upływie określonego odcinka czasu.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-timer
%{_datadir}/xfce4/panel-plugins/xfce4-timer.desktop
%{_iconsdir}/hicolor/*x*/apps/xfce4-timer.png
