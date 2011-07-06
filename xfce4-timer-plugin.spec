Summary:	Xfce panel timer plugin
Summary(pl.UTF-8):	Wtyczka panelu Xfce odliczająca czas
Name:		xfce4-timer-plugin
Version:	0.6.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-timer-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	2d5330146da1d92ca86034976799a1ad
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= 4.2.0
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

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-timer
%{_datadir}/xfce4/panel-plugins/xfce4-timer.desktop