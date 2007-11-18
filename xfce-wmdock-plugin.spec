%define oname xfce4-wmdock-plugin

Summary:	WindowMaker dockapps plugin for the Xfce desktop environment
Name:		xfce-wmdock-plugin
Version:	0.1.6
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-wmdock-plugin
Source0:	tp://goodies.xfce.org/_media/projects/panel-plugins/%{oname}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	perl(XML::Parser)
BuildRequires:	libwnck-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The WMdock plugin is a compatibility layer for running 
WindowMaker dockapps on the XFCE desktop. It integrates 
the dockapps into a panel, closely resembling the look 
and feel of the WindowMaker dock or clip, respectively.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
