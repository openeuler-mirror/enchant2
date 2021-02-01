Name:           enchant2
Version:        2.2.15
Release:        1
Summary:        Generic spell checking library
License:        LGPLv2+
URL:            https://github.com/AbiWord/enchant
Source0:        https://github.com/AbiWord/enchant/releases/download/v%{version}/enchant-%{version}.tar.gz

BuildRequires:  automake autoconf libtool gcc-c++ glib2-devel aspell-devel hunspell-devel libvoikko-devel

Provides:       bundled(gnulib) %{name}-aspell = %{version}-%{release} %{name}-voikko = %{version}-%{release}
Obsoletes:      %{name}-aspell < %{version}-%{release} %{name}-voikko < %{version}-%{release}

%description
Enchant aims to provide a simple but comprehensive abstraction for dealing
with different spell checking libraries in a consistent way. A client, such
as a text editor or word processor, need not know anything about a specific
spell-checker, and since all back-ends are plugins, new spell-checkers can
be added without needing any change to the program using Enchant.

%package devel
Summary:        Development package for %{name}
Requires:       %{name} = %{version}-%{release} glib2-devel

%description devel
This package contains some libraries and header files for
development of %{name}.

%package help
Summary:        Help package for %{name}
Requires:       %{name} = %{version}-%{release}

%description help
This package contains some man help files for %{name}.

%prep
%autosetup -p1 -n enchant-%{version}

autoreconf -ifv

%build
%configure --with-aspell --with-hunspell-dir=%{_datadir}/myspell  --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build pkgdatadir=%{_datadir}/enchant-2

%install
%make_install pkgdatadir=%{_datadir}/enchant-2
%{delete_la}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_bindir}/{enchant-2,enchant-lsmod-2}
%{_libdir}/libenchant-2.so.*
%{_libdir}/enchant-2/*
%{_datadir}/enchant-2

%files devel
%{_libdir}/libenchant-2.so
%{_libdir}/pkgconfig/enchant-2.pc
%{_includedir}/enchant-2

%files help
%{_mandir}/man1/*

%changelog
* Mon Feb 1 2021 chengguipeng1 <chengguipeng1@huawei.com> - 2.2.15-1
- DESC: update to 2.2.15

* Sun Jan 19 2020 wutao <wutao61@huawei.com> - 2.2.3-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Mon Nov 04 2019 huzhiyu <huzhiyu1@huawei.com> - 2.2.3-6
- Package init
