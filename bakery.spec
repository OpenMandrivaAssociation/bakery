%define name 	bakery
%define version 2.4.2
%define release %mkrel 2

%define api 2.4
%define major 	1
%define libname %mklibname %name %{api}_%major
%define develname %mklibname -d %name %{api}

Summary: 	C++ Framework for Document-based GNOME applications
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://bakery.sourceforge.net/
License: 	GPL
Group: 		System/Libraries
Source: 	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRequires:	gtkmm2.4-devel gconfmm2.6-devel libglademm-devel >= 2.4 
BuildRequires:	libxml++-devel >= 2.6 gnome-vfsmm2.6-devel
BuildRequires:	libexpat-devel
BuildRequires:	libsm-devel
Buildroot: 	%_tmppath/%name-%version-buildroot

%description
A C++ Framework for Document-based GNOME applications, using gtkmm. It allows
use of the Document/View architecture.

%package -n	%libname
Group:		System/Libraries
Summary:	C++ Framework for document-based GNOME applications

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
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%_libdir/libbakery-%{api}-%{api}.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc docs/*.html
%_libdir/*.so
%attr(644,root,root) %_libdir/*.la
%_libdir/*.a
%_libdir/pkgconfig/*.pc
%_libdir/bakery-%{api}
%_includedir/%name-2.4/%name/*

