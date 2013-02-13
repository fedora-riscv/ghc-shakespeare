# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name shakespeare

%global common_summary Compile-time interpolated templates

%global common_description Shakespeare is a family of type-safe, efficient template languages.\
Shakespeare templates are expanded at compile-time,\
ensuring that all interpolated variables are in scope.\
Variables are interpolated according to their type through a typeclass.\
Shakespeare templates can be used inline with a quasi-quoter\
or in an external file.

Name:           ghc-%{pkg_name}
Version:        1.0.1.4
Release:        2%{?dist}
Summary:        %{common_summary}

License:        MIT
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
# End cabal-rpm deps

%description
%{common_description}


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%ghc_devel_package

%ghc_devel_description


%ghc_devel_post_postun


%ghc_files LICENSE


%changelog
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
