#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9D5EAAF69013B842 (nmav@gnutls.org)
#
Name     : gnutls
Version  : 3.6.0
Release  : 42
URL      : ftp://ftp.gnupg.org/gcrypt/gnutls/v3.6/gnutls-3.6.0.tar.xz
Source0  : ftp://ftp.gnupg.org/gcrypt/gnutls/v3.6/gnutls-3.6.0.tar.xz
Source99 : ftp://ftp.gnupg.org/gcrypt/gnutls/v3.6/gnutls-3.6.0.tar.xz.sig
Summary  : Transport Security Layer implementation for the GNU system
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear GPL-3.0 GPL-3.0+ LGPL-2.0+ LGPL-2.1 LGPL-3.0 MIT
Requires: gnutls-bin
Requires: gnutls-lib
Requires: gnutls-doc
Requires: gnutls-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gmp-dev
BuildRequires : gmp-dev32
BuildRequires : gmp-lib32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libidn-dev
BuildRequires : libidn-dev32
BuildRequires : libtasn1-dev
BuildRequires : libtasn1-dev32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libunistring-dev
BuildRequires : libunistring-dev32
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : net-tools
BuildRequires : nettle
BuildRequires : nettle-dev
BuildRequires : nettle-dev32
BuildRequires : nettle-lib
BuildRequires : nettle-lib32
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32p11-kit-1)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : sed
BuildRequires : valgrind
Patch1: 0001-tests-Skip-trust-store-test-as-SSL-trust-uninitialis.patch

%description
ext/         -> Implementation of TLS extensions
auth/        -> Implementation of TLS authentication methods (DHE, SRP etc.)
accelerated/ -> Implementation of cipher acceleration

%package bin
Summary: bin components for the gnutls package.
Group: Binaries

%description bin
bin components for the gnutls package.


%package dev
Summary: dev components for the gnutls package.
Group: Development
Requires: gnutls-lib
Requires: gnutls-bin
Provides: gnutls-devel

%description dev
dev components for the gnutls package.


%package dev32
Summary: dev32 components for the gnutls package.
Group: Default
Requires: gnutls-lib32
Requires: gnutls-bin
Requires: gnutls-dev

%description dev32
dev32 components for the gnutls package.


%package doc
Summary: doc components for the gnutls package.
Group: Documentation

%description doc
doc components for the gnutls package.


%package lib
Summary: lib components for the gnutls package.
Group: Libraries

%description lib
lib components for the gnutls package.


%package lib32
Summary: lib32 components for the gnutls package.
Group: Default

%description lib32
lib32 components for the gnutls package.


%package locales
Summary: locales components for the gnutls package.
Group: Default

%description locales
locales components for the gnutls package.


%prep
%setup -q -n gnutls-3.6.0
%patch1 -p1
pushd ..
cp -a gnutls-3.6.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503427855
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%reconfigure --disable-static --with-default-trust-store-file=%{_sysconfdir}/ssl/cert.pem \
--with-default-trust-store-dir=%{_datadir}/ca-certs
make V=1  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --with-default-trust-store-file=%{_sysconfdir}/ssl/cert.pem \
--with-default-trust-store-dir=%{_datadir}/ca-certs  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1503427855
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang gnutls

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/certtool
/usr/bin/gnutls-cli
/usr/bin/gnutls-cli-debug
/usr/bin/gnutls-serv
/usr/bin/ocsptool
/usr/bin/p11tool
/usr/bin/psktool
/usr/bin/srptool

%files dev
%defattr(-,root,root,-)
/usr/include/gnutls/abstract.h
/usr/include/gnutls/compat.h
/usr/include/gnutls/crypto.h
/usr/include/gnutls/dtls.h
/usr/include/gnutls/gnutls.h
/usr/include/gnutls/gnutlsxx.h
/usr/include/gnutls/ocsp.h
/usr/include/gnutls/openpgp.h
/usr/include/gnutls/pkcs11.h
/usr/include/gnutls/pkcs12.h
/usr/include/gnutls/pkcs7.h
/usr/include/gnutls/self-test.h
/usr/include/gnutls/socket.h
/usr/include/gnutls/system-keys.h
/usr/include/gnutls/tpm.h
/usr/include/gnutls/urls.h
/usr/include/gnutls/x509-ext.h
/usr/include/gnutls/x509.h
/usr/lib64/libgnutls.so
/usr/lib64/libgnutlsxx.so
/usr/lib64/pkgconfig/gnutls.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgnutls.so
/usr/lib32/libgnutlsxx.so
/usr/lib32/pkgconfig/32gnutls.pc
/usr/lib32/pkgconfig/gnutls.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/gnutls/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnutls.so.30
/usr/lib64/libgnutls.so.30.20.0
/usr/lib64/libgnutlsxx.so.28
/usr/lib64/libgnutlsxx.so.28.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgnutls.so.30
/usr/lib32/libgnutls.so.30.20.0
/usr/lib32/libgnutlsxx.so.28
/usr/lib32/libgnutlsxx.so.28.1.0

%files locales -f gnutls.lang
%defattr(-,root,root,-)

