Summary:	WindowMaker dockapps plugin for the Xfce desktop environment
Name:		xfce4-wmdock-plugin
Version:	0.3.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-wmdock-plugin
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	libwnck-devel
Obsoletes:	xfce-wmdock-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
