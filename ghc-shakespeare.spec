# cabal2spec-0.25.2
# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name shakespeare

%global common_summary Haskell compile-time templating library

%global common_description Shakespeare is a template family for type-safe, efficient templates\
with simple variable interpolation. Shakespeare templates can be used\
inline with a quasi-quoter or in an external file. Shakespeare\
interpolates variables according to the type being inserted.

Name:           ghc-%{pkg_name}
Version:        1.0.0.2
Release:        2%{?dist}
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        BSD
# BEGIN cabal2spec
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
ExclusiveArch:  %{ghc_arches_with_ghci}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros %{!?without_hscolour:hscolour}
# END cabal2spec
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel

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
