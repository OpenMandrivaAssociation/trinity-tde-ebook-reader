%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg tde-ebook-reader
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		0.99.6
Release:		%{?tde_version:%{tde_version}_}3
Summary:		e-book reader for TDE
Group:			Applications/Publishing
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/office/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:  	cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:   trinity-tde-cmake
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# UNIBREAK support
BuildRequires:  pkgconfig(libunibreak)

BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(sqlite3)

%description
tde-ebook-reader is an e-book reader for TDE.

Main features:
 * supports several open e-book formats: fb2, html, chm, plucker,
   palmdoc, ztxt, tcr (psion text), rtf, oeb, openreader, nonBuildOption:    -DRM'ed
   mobipocket, plain text, epub, eReader
 * reads directly from tar, zip, gzip, bzip2 archives (you can have
   several books in one archive)
 * supports a structured view of your e-book collection
 * automatically determines encodings
 * automatically generates a table of contents
 * keeps the last open book and the last read positions for all open books
   between runs
 * automatic hyphenation (patterns for several languages are included)
 * searching and downloading books from www.feedbooks.com and www.litres.ru
 * partial CSS support for epub files

%files
%defattr(-,root,root,-)
%{tde_prefix}/bin/tde-ebook-reader
%{tde_prefix}/share/applications/tde/tde-ebook-reader.desktop
%{tde_prefix}/share/apps/tde-ebook-reader/
%{tde_prefix}/share/man/man1/tde-ebook-reader.1*

##########

%package -n libzlcore-tqt
Requires:	libzlcore-data-tqt
Summary:	Summary:  TQt3-based development library (shared library)

%description -n libzlcore-tqt
This is the core of Summary: , the library that tde-ebook-reader is based on.

%files -n libzlcore-tqt
%{tde_prefix}/%{_lib}/libzlcore-tqt.so.*

##########

%package -n libzlcore-tqt-devel
Requires:	libzlcore-tqt
Summary:	TQt3-based development library (development files)

%description -n libzlcore-tqt-devel
This package contains development files for the Summary:  core.

%files -n libzlcore-tqt-devel
%{tde_prefix}/include/zlibrary-tqt/core
%{tde_prefix}/%{_lib}/libzlcore-tqt.la
%{tde_prefix}/%{_lib}/libzlcore-tqt.so

##########

%package -n libzlcore-data-tqt
Summary:	TQt3-based development library (support files)

%description -n libzlcore-data-tqt
This package contains the support files for the core of Summary: , the library
that the fbreader e-book reader is based on.

%files -n libzlcore-data-tqt
%{tde_prefix}/share/zlibrary-tqt/keynames.desktop-tqt.xml
%{tde_prefix}/share/zlibrary-tqt/languagePatterns.zip
%{tde_prefix}/share/zlibrary-tqt/unicode.xml.gz
%{tde_prefix}/share/zlibrary-tqt/default/
%{tde_prefix}/share/zlibrary-tqt/encodings/
%{tde_prefix}/share/zlibrary-tqt/resources/

##########

%package -n libzltext-tqt
Requires:	libzlcore-tqt
Requires:	libzltext-data-tqt
Summary:	TQt3-based text model/viewer part (shared library)

%description -n libzltext-tqt
This package provides text model/viewer part of Summary: .

%files -n libzltext-tqt
%{tde_prefix}/%{_lib}/libzltext-tqt.so.*

##########

%package -n libzltext-tqt-devel
Requires:	libzltext-tqt
Summary:	TQt3-based text model/viewer part (development files)

%description -n libzltext-tqt-devel
This package contains development files for the Summary:  text model/viewer
library.

%files -n libzltext-tqt-devel
%{tde_prefix}/include/zlibrary-tqt/text
%{tde_prefix}/%{_lib}/libzltext-tqt.la
%{tde_prefix}/%{_lib}/libzltext-tqt.so

##########

%package -n libzltext-data-tqt
Summary:	TQt3-based text model/viewer part (support files)

%description -n libzltext-data-tqt
This package contains the support files for the text model/viewer part
of Summary: .

%files -n libzltext-data-tqt
%{tde_prefix}/share/zlibrary-tqt/hyphenationPatterns.zip


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"

