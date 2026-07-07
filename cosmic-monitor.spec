%undefine _debugsource_packages
Name:           cosmic-monitor
Version:        1.2.0
#define beta beta.7
Release:        %{?beta:0.%{beta}.}1
Summary:        COSMIC System Monitor
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-monitor
Source0:        https://github.com/pop-os/cosmic-monitor/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  make
BuildRequires:  rust-packaging
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(glib-2.0)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
