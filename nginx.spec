#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v2
# autospec commit: e661f3a625d7
#
# Source0 file verified with key 0xA0EA981B66B0D967 (k.pavlov@f5.com)
#
Name     : nginx
Version  : 1.24.0
Release  : 86
URL      : https://nginx.org/download/nginx-1.24.0.tar.gz
Source0  : https://nginx.org/download/nginx-1.24.0.tar.gz
Source1  : nginx-setup.service
Source2  : nginx.service
Source3  : nginx.tmpfiles
Source4  : https://nginx.org/download/nginx-1.24.0.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nginx-bin = %{version}-%{release}
Requires: nginx-config = %{version}-%{release}
Requires: nginx-data = %{version}-%{release}
Requires: nginx-lib = %{version}-%{release}
Requires: nginx-license = %{version}-%{release}
Requires: nginx-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: build.patch
Patch2: 0001-Rework-nginx-configuration-directories.patch

%description
Documentation is available at http://nginx.org

%package bin
Summary: bin components for the nginx package.
Group: Binaries
Requires: nginx-data = %{version}-%{release}
Requires: nginx-config = %{version}-%{release}
Requires: nginx-license = %{version}-%{release}
Requires: nginx-services = %{version}-%{release}

%description bin
bin components for the nginx package.


%package config
Summary: config components for the nginx package.
Group: Default

%description config
config components for the nginx package.


%package data
Summary: data components for the nginx package.
Group: Data

%description data
data components for the nginx package.


%package lib
Summary: lib components for the nginx package.
Group: Libraries
Requires: nginx-data = %{version}-%{release}
Requires: nginx-license = %{version}-%{release}

%description lib
lib components for the nginx package.


%package license
Summary: license components for the nginx package.
Group: Default

%description license
license components for the nginx package.


%package services
Summary: services components for the nginx package.
Group: Systemd services
Requires: systemd

%description services
services components for the nginx package.


%prep
%setup -q -n nginx-1.24.0
cd %{_builddir}/nginx-1.24.0
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1700525276
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --prefix=/var/www \
--conf-path=/usr/share/nginx/conf/nginx.conf \
--sbin-path=/usr/bin/nginx \
--pid-path=/run/nginx.pid \
--lock-path=/run/lock/nginx.lock \
--modules-path=/usr/lib64/nginx \
--http-log-path=syslog:server=unix:/dev/log \
--http-client-body-temp-path=/var/lib/nginx/client-body \
--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
--http-proxy-temp-path=/var/lib/nginx/proxy \
--http-scgi-temp-path=/var/lib/nginx/scgi \
--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
--user=httpd \
--group=httpd \
--with-threads \
--with-ipv6 \
--with-debug \
--error-log-path=stderr \
--with-file-aio \
--with-http_ssl_module \
--with-http_v2_module \
--with-poll_module \
--with-select_module \
--with-stream=dynamic \
--with-stream_ssl_module
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1700525276
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nginx
cp %{_builddir}/nginx-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/nginx/de0ea043351e203ff16503c81a431405422ff3a1 || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/nginx-setup.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/nginx.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/tmpfiles.d/nginx.conf
## Remove excluded files
rm -f %{buildroot}*/var/www/html/50x.html
rm -f %{buildroot}*/var/www/html/index.html
## install_append content
# these are just copies
rm -f %{buildroot}/usr/share/nginx/conf/*.default
# template configuration
install -m0644 conf/server.conf.example %{buildroot}/usr/share/nginx/conf/
install -m0644 conf/nginx.conf.example %{buildroot}/usr/share/nginx/conf/
# move these to a "template" location
mkdir -p %{buildroot}/usr/share/nginx/html
install -m0644 html/50x.html %{buildroot}/usr/share/nginx/html/
install -m0644 html/index.html %{buildroot}/usr/share/nginx/html/

mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/nginx.service %{buildroot}/usr/share/clr-service-restart/nginx.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nginx

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/nginx.conf

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/nginx.service
/usr/share/nginx/conf/fastcgi.conf
/usr/share/nginx/conf/fastcgi_params
/usr/share/nginx/conf/koi-utf
/usr/share/nginx/conf/koi-win
/usr/share/nginx/conf/mime.types
/usr/share/nginx/conf/nginx.conf
/usr/share/nginx/conf/nginx.conf.example
/usr/share/nginx/conf/scgi_params
/usr/share/nginx/conf/server.conf.example
/usr/share/nginx/conf/uwsgi_params
/usr/share/nginx/conf/win-utf
/usr/share/nginx/html/50x.html
/usr/share/nginx/html/index.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx/ngx_stream_module.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nginx/de0ea043351e203ff16503c81a431405422ff3a1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nginx-setup.service
/usr/lib/systemd/system/nginx.service
