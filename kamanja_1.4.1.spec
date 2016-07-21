Name:           Kamanja
Version: 	1.4.1_2.11       
Release:        1%{?dist}
Summary:        Kamanja is a real time decisioning system

License:        GPL
URL:            http://kamanja.org
Source0:        Kamanja-1.4.1_2.11.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot       

Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives	

Prefix: %{_prefix}
%description
A RPM package for Kamanja binaries

%prep
%setup -q

%install
mkdir -p "$RPM_BUILD_ROOT%{_prefix}/Kamanja_1.4.1_2.11"
cp -R * "$RPM_BUILD_ROOT%{_prefix}/Kamanja_1.4.1_2.11"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/Kamanja_1.4.1_2.11
%doc %{_prefix}/Kamanja_1.4.1_2.11/documentation
%config %{_prefix}/Kamanja_1.4.1_2.11/config

%post
%{_sbindir}/update-alternatives --install /usr/bin/Kamanja Kamanja $RPM_INSTALL_PREFIX/Kamanja_1.4.1_2.11/bin/kamanja 300

%postun
%{_sbindir}/update-alternatives --remove  Kamanja $RPM_INSTALL_PREFIX/Kamanja_1.4.1_2.11/bin/kamanja
