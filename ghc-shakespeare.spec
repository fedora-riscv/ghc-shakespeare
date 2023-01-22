# generated by cabal-rpm-2.1.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name shakespeare
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        2.0.30
Release:        1%{?dist}
Summary:        A toolkit for making compile-time interpolated templates

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-lift-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
Shakespeare is a family of type-safe, efficient template languages.
Shakespeare templates are expanded at compile-time, ensuring that all
interpolated variables are in scope. Variables are interpolated according to
their type through a typeclass.

Shakespeare templates can be used inline with a quasi-quoter
or in an external file.

See the documentation at <http://www.yesodweb.com/book/shakespearean-templates>
for more details.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%if %{with tests}
%cabal_test
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sun Jan 22 2023 Jens Petersen <petersen@redhat.com> - 2.0.30-1
- https://hackage.haskell.org/package/shakespeare-2.0.30/changelog
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Jens Petersen <petersen@redhat.com> - 2.0.26-1
- https://hackage.haskell.org/package/shakespeare-2.0.26/changelog

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 2.0.25-1
- update to 2.0.25

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.24.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.24.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jens Petersen <petersen@redhat.com> - 2.0.24.1-1
- update to 2.0.24.1

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 2.0.24-1
- update to 2.0.24

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 2.0.20-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 2.0.20-1
- update to 2.0.20

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 2.0.15-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 2.0.15-1
- update to 2.0.15

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 2.0.14.1-1
- update to 2.0.14.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Jens Petersen <petersen@redhat.com> - 2.0.12.1-1
- update to 2.0.12.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 2.0.9-1
- update to 2.0.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  8 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.1.1-4
- Rebuild (aarch64 hashes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar  5 2015 Jens Petersen <petersen@redhat.com> - 2.0.1.1-2
- obsolete hamlet, shakespeare-css, shakespeare-i18n, shakespeare-js,
  shakespeare-text

* Wed Sep 17 2014 Jens Petersen <petersen@redhat.com> - 2.0.1.1-1
- update to 2.0.1.1

* Thu Aug 28 2014 Jens Petersen <petersen@redhat.com> - 1.2.1.1-1
- update to 1.2.1.1
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Jens Petersen <petersen@redhat.com> - 1.0.5.1-1
- update to 1.0.5.1

* Wed Aug 28 2013 Jens Petersen <petersen@redhat.com> - 1.0.5-1
- update to 1.0.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Jens Petersen <petersen@redhat.com> - 1.0.4-1
- update to 1.0.4
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 1.0.3.1-1
- update to 1.0.3.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov  7 2012 Jens Petersen <petersen@redhat.com> - 1.0.1.4-1
- update to 1.0.1.4
- license is now MIT

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 1.0.0.2-2
- change prof BRs to devel

* Wed Jun 13 2012 Jens Petersen <petersen@redhat.com> - 1.0.0.2-1
- update to 1.0.0.2

* Thu Apr 26 2012 Jens Petersen <petersen@redhat.com> - 1.0.0.1-1
- update to 1.0.0.1

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 0.11-1
- update to 0.11
- depends on text not blaze-html and failure

* Wed Mar  7 2012 Jens Petersen <petersen@redhat.com> - 0.10.3.1-1
- update to 0.10.3.1
- only build on ghc_arches_with_ghci

* Thu Jan  5 2012 Jens Petersen <petersen@redhat.com> - 0.10.2-2
- update to cabal2spec-0.25.2

* Tue Nov  1 2011 Jens Petersen <petersen@redhat.com> - 0.10.2-1
- update to 0.10.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.10.1.1-1.1
- rebuild with new gmp without compat lib

* Sat Oct  8 2011 Jens Petersen <petersen@redhat.com> - 0.10.1.1-1
- update to 0.10.1.1

* Thu Sep  8 2011 Jens Petersen <petersen@redhat.com> - 0.10.0-2
- BR ghc-*-prof

* Wed Sep  7 2011 Jens Petersen <petersen@redhat.com> - 0.10.0-1
- BSD license; deps

* Wed Sep  7 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.10.0-0
- initial packaging for Fedora automatically generated by cabal2spec-0.23.2
