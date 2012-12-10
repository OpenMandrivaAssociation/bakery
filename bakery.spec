%define name 	bakery
%define version 2.6.3
%define release 4

%define api 2.6
%define api2 6
%define major 	1
%define libname %mklibname %name %{api}_%{api2}_%major
%define develname %mklibname -d %name %{api}

Summary: 	C++ Framework for Document-based GNOME applications
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://bakery.sourceforge.net/
License: 	LGPLv2+
Group: 		System/Libraries
Source: 	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRequires:	gtkmm2.4-devel gconfmm2.6-devel libglademm-devel >= 2.4 
BuildRequires:	libxml++-devel >= 2.23.1
BuildRequires:  gnome-vfsmm2.6-devel
BuildRequires:	libexpat-devel
BuildRequires:	libsm-devel
BuildRequires:	intltool

%description
A C++ Framework for Document-based GNOME applications, using gtkmm. It allows
use of the Document/View architecture.

%package i18n
Summary: C++ Framework for document-based GNOME applications
Group: System/Internationalization

%description i18n
This package contains the translations for %name.

%package -n	%libname
Group:		System/Libraries
Summary:	C++ Framework for document-based GNOME applications
Requires: %{name}-i18n >= %{version}

%description -n %libname
A C++ Framework for Document-based GNOME applications, using gtkmm. It allows
use of the Document/View architecture.

%package -n %develname
Group:          Development/C++
Summary:        Static libraries and header files from %name
Provides:       %name-devel = %version-%release
Provides:	lib%name-devel = %version-%release
Provides:	libbakery%{api}-devel = %version-%release
Requires:       %libname = %version
Obsoletes: %mklibname -d bakery 2.4_1

%description -n %develname
Static libraries and headers from %name.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
%find_lang %name

%files i18n -f %{name}.lang

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%_libdir/libbakery-%{api}-.%{api2}.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc docs/*.html
%_libdir/*.so
%_libdir/*.a
%_libdir/pkgconfig/*.pc
%_libdir/bakery-%{api}
%_includedir/%name-%api/



%changelog
* Mon Sep 12 2011 Götz Waschk <waschk@mandriva.org> 2.6.3-3mdv2012.0
+ Revision: 699459
- rebuild

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.6.3-2mdv2011.0
+ Revision: 436766
- rebuild

* Tue Feb 10 2009 Götz Waschk <waschk@mandriva.org> 2.6.3-1mdv2009.1
+ Revision: 339222
- update to new version 2.6.3

* Fri Dec 12 2008 Funda Wang <fwang@mandriva.org> 2.6.2-1mdv2009.1
+ Revision: 313551
- new version 2.6.2

* Mon Dec 08 2008 Götz Waschk <waschk@mandriva.org> 2.6.1-1mdv2009.1
+ Revision: 311948
- new version
- update to new version 2.6.1

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-3mdv2009.1
+ Revision: 301022
- rebuilt against new libxcb

* Tue Oct 14 2008 Götz Waschk <waschk@mandriva.org> 2.6.0-2mdv2009.1
+ Revision: 293578
- split out translations

* Sun Oct 12 2008 Götz Waschk <waschk@mandriva.org> 2.6.0-1mdv2009.1
+ Revision: 292956
- fix license
- fix build deps
- new version
- new major

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.5.1-2mdv2009.0
+ Revision: 266235
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Götz Waschk <waschk@mandriva.org>
    - fix directory ownership

* Tue Apr 15 2008 Götz Waschk <waschk@mandriva.org> 2.5.1-1mdv2009.0
+ Revision: 193790
- new version
- bump deps
- new api version

* Sun Jan 13 2008 Götz Waschk <waschk@mandriva.org> 2.4.4-1mdv2008.1
+ Revision: 151042
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Götz Waschk <waschk@mandriva.org> 2.4.3-1mdv2008.1
+ Revision: 113667
- new version

* Wed Oct 10 2007 Götz Waschk <waschk@mandriva.org> 2.4.2-2mdv2008.1
+ Revision: 96827
- fix obsoleting the old devel package

* Fri Oct 05 2007 Götz Waschk <waschk@mandriva.org> 2.4.2-1mdv2008.1
+ Revision: 95565
- new version
- new devel name
- update file list

