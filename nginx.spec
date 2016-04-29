#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nginx
Version  : 1.10.0
Release  : 24
URL      : http://nginx.org/download/nginx-1.10.0.tar.gz
Source0  : http://nginx.org/download/nginx-1.10.0.tar.gz
Source1  : nginx.service
Source2  : nginx.tmpfiles
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nginx-bin
Requires: nginx-config
Requires: nginx-data
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : zlib-dev
Patch1: build.patch
Patch2: stateless.patch

%description
Documentation is available at http://nginx.org

%package bin
Summary: bin components for the nginx package.
Group: Binaries
Requires: nginx-data
Requires: nginx-config

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


%prep
%setup -q -n nginx-1.10.0
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static --prefix=/usr/share/nginx \
--user=httpd \
--group=httpd \
--with-select_module \
--with-poll_module \
--with-threads \
--with-file-aio \
--with-ipv6 \
--with-http_ssl_module \
--with-http_v2_module \
--sbin-path=/usr/bin/nginx \
--pid-path=/run/nginx.pid \
--lock-path=/run/lock/nginx.lock \
--http-log-path=syslog:server=unix:/dev/log \
--conf-path=/usr/share/nginx/conf/nginx.conf \
--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
--error-log-path=stderr \
--http-client-body-temp-path=/var/lib/nginx/client-body \
--http-proxy-temp-path=/var/lib/nginx/proxy \
--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
--http-scgi-temp-path=/var/lib/nginx/scgi \
--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
--with-debug
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/nginx.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/nginx.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nginx

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/nginx.service
/usr/lib/tmpfiles.d/nginx.conf

%files data
%defattr(-,root,root,-)
/usr/share/nginx/conf/fastcgi.conf
/usr/share/nginx/conf/fastcgi.conf.default
/usr/share/nginx/conf/fastcgi_params
/usr/share/nginx/conf/fastcgi_params.default
/usr/share/nginx/conf/koi-utf
/usr/share/nginx/conf/koi-win
/usr/share/nginx/conf/mime.types
/usr/share/nginx/conf/mime.types.default
/usr/share/nginx/conf/nginx.conf
/usr/share/nginx/conf/nginx.conf.default
/usr/share/nginx/conf/scgi_params
/usr/share/nginx/conf/scgi_params.default
/usr/share/nginx/conf/uwsgi_params
/usr/share/nginx/conf/uwsgi_params.default
/usr/share/nginx/conf/win-utf
/usr/share/nginx/html/50x.html
/usr/share/nginx/html/index.html
