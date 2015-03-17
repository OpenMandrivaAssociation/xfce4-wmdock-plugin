%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	WindowMaker dockapps plugin for the Xfce desktop environment
Name:		xfce4-wmdock-plugin
Version:	0.6.0
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-wmdock-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-wmdock-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0)
Obsoletes:	xfce-wmdock-plugin

%description
The WMdock plugin is a compatibility layer for running 
WindowMaker dockapps on the XFCE desktop. It integrates 
the dockapps into a panel, closely resembling the look 
and feel of the WindowMaker dock or clip, respectively.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
