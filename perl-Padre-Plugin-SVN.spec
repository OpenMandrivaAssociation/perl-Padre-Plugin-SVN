%define upstream_name    Padre-Plugin-SVN
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Dialog for SVN tasks
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Padre)
BuildRequires:	perl(SVN::Class)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Padre plugin with dialog for SVN tasks.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# sometimes fails without X display available
%if %{?_with_test:1}%{?!_with_test:0}
%make test
%endif

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 657815
- rebuild for updated spec-helper

  + Buchan Milne <bgmilne@mandriva.org>
    - Disable tests by default (requires X display), use --with-test to run tests

* Tue Oct 26 2010 Buchan Milne <bgmilne@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 589504
- import perl-Padre-Plugin-SVN

