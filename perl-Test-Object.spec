#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Object
Version  : 0.08
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Object-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Object-0.08.tar.gz
Summary  : 'Thoroughly testing objects via registered handlers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Object-license = %{version}-%{release}
Requires: perl-Test-Object-perl = %{version}-%{release}
Requires: perl(Test::More)
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Test-Object,
version 0.08:
Thoroughly testing objects via registered handlers

%package dev
Summary: dev components for the perl-Test-Object package.
Group: Development
Provides: perl-Test-Object-devel = %{version}-%{release}
Requires: perl-Test-Object = %{version}-%{release}

%description dev
dev components for the perl-Test-Object package.


%package license
Summary: license components for the perl-Test-Object package.
Group: Default

%description license
license components for the perl-Test-Object package.


%package perl
Summary: perl components for the perl-Test-Object package.
Group: Default
Requires: perl-Test-Object = %{version}-%{release}

%description perl
perl components for the perl-Test-Object package.


%prep
%setup -q -n Test-Object-0.08
cd %{_builddir}/Test-Object-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Object
cp %{_builddir}/Test-Object-0.08/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Object/f02c5c32ea4eb38241a1a5f3f6c03301a1051dc9
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Object.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Object/f02c5c32ea4eb38241a1a5f3f6c03301a1051dc9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
