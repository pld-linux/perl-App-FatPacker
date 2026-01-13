#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	App
%define		pnam	FatPacker
Summary:	App::FatPacker - pack your dependencies onto your script file
Name:		perl-App-FatPacker
Version:	0.010003
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/App/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86391ef2c798edd830f4f3e69ff2885f
URL:		http://search.cpan.org/dist/App-FatPacker/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
App::FatPacker - pack your dependencies onto your script file

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/fatpack
%{_mandir}/man1/fatpack.1p*
%{_mandir}/man3/App::FatPacker.3pm*
%{_mandir}/man3/App::FatPacker::Trace.3pm*
%{perl_vendorlib}/App/FatPacker.pm
%{perl_vendorlib}/App/FatPacker
