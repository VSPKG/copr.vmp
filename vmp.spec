Name:         	VMP
Version:      	0.1.1
Release:      	1
Summary:      	Version manager for python
License:      	MIT
URL: 			https://github.com/vineelsai26/VMP
Source: 		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cargo
BuildRequires:	git
BuildRequires:	openssl-devel

%description
Version manager for Python

%define debug_package %{nil}

%prep
%autosetup

%build
rm -rf ./* ./.*
git clone %{url} .
git checkout v%{version}
cargo build --release

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 target/release/vmp %{buildroot}/usr/bin/vmp

%files
/usr/bin/vmp

%changelog
* Wed Aug 17 2024 Vineel Sai <mail@vineelsai.com> - 0.1.1-1
- Initial srpm build
