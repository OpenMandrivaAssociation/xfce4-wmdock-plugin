%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	WindowMaker dockapps plugin for the Xfce desktop environment
Name:		xfce4-wmdock-plugin
Version:	0.3.4
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-wmdock-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-wmdock-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	libwnck-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfcegui4-devel
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


%changelog
* Sun May 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.4-1mdv2011.0
+ Revision: 672536
- update to new version 0.3.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-4mdv2010.1
+ Revision: 543444
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.3.2-3mdv2010.0
+ Revision: 446156
- rebuild

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-2mdv2009.1
+ Revision: 349525
- rebuild for xfce-4.6.0

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-1mdv2009.1
+ Revision: 334565
- update to new version 0.3.2

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 333624
- New version 0.3.1

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-2mdv2009.1
+ Revision: 295034
- rebuild for new Xfce4.6 beta1

* Mon Aug 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 275721
- package translations
- update to new version 0.3.0
- update source url
- run scriplets only for mdv older than 200900

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-4mdv2009.0
+ Revision: 262416
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-3mdv2009.0
+ Revision: 257017
- rebuild

* Mon Feb 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1mdv2008.1
+ Revision: 165230
- new version

* Wed Feb 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.9-1mdv2008.1
+ Revision: 163347
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.8-1mdv2008.1
+ Revision: 135362
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-3mdv2008.1
+ Revision: 110144
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING and NEWS files
- add ChangeLog file to the docs
- use upstream name

* Sat Oct 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-1mdv2008.1
+ Revision: 102632
- import xfce-wmdock-plugin

