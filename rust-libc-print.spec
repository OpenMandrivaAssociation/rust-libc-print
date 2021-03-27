%bcond_without check
%global debug_package %{nil}

%global crate libc-print

Name:           rust-%{crate}
Version:        0.1.16
Release:        1
Summary:        Println! and eprintln! macros on libc without stdlib

# Upstream license specification: Apache-2.0 OR MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/libc-print
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(libc) >= 0.2.84 with crate(libc) < 0.3.0)
%endif

%global _description %{expand:
Println! and eprintln! macros on libc without stdlib.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(libc-print) = 0.1.16
Requires:       cargo
Requires:       (crate(libc) >= 0.2.84 with crate(libc) < 0.3.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(libc-print/default) = 0.1.16
Requires:       cargo
Requires:       crate(libc-print) = 0.1.16

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
