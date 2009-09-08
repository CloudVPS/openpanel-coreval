%define version 0.9.1

%define libpath /usr/lib
%ifarch x86_64
  %define libpath /usr/lib64
%endif

Summary: cli
Name: openpanel-coreval
Version: %version
Release: 1
License: GPLv2
Group: Development
Source: http://packages.openpanel.com/archive/openpanel-coreval-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
Requires: openpanel-core >= 0.8.0
Requires: libgrace

%description
cli
the commandline interface
%prep
%setup -q -n openpanel-coreval-%version

%build
BUILD_ROOT=$RPM_BUILD_ROOT
./configure
make

%install
BUILD_ROOT=$RPM_BUILD_ROOT
rm -rf ${BUILD_ROOT}
mkdir -p ${BUILD_ROOT}/usr/bin
install -m 755 coreval ${BUILD_ROOT}/usr/bin

%post

%files
%defattr(-,root,root)
/
