Name:           Kamanja
Version: 	1.5.0_2.11       
Release:        1%{?dist}
Summary:        Kamanja is a real time decisioning system

License:        GPL
URL:            http://kamanja.org
Source0:        Kamanja-1.5.0_2.11.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot       

%description
A RPM package for Kamanja binaries

%prep
%setup -q

%install
mkdir -p "$RPM_BUILD_ROOT/applications"
cp -R * "$RPM_BUILD_ROOT/applications"

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/applications

%post
bash /applications/bin/SetPaths.sh $KAFKA_HOME
