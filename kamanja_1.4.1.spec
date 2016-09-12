Name:           kamanja
Version:        1.4.1_2.11
Release:        1%{?dist}
Summary:        Kamanja is a real time decisioning system

License:        GPL
URL:            http://kamanja.org
Source0:        kamanja-%{version}.tar.gz


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
mkdir -p "$RPM_BUILD_ROOT%{_prefix}/kamanja_%{version}"
cp -R * "$RPM_BUILD_ROOT%{_prefix}/kamanja_%{version}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(777,kamanja,kamanja,-)
%{_prefix}/kamanja_%{version}
%doc %{_prefix}/kamanja_%{version}/documentation
%config %{_prefix}/kamanja_%{version}/config

%post
[ -L $RPM_INSTALL_PREFIX/kamanja ]  && rm -f $RPM_INSTALL_PREFIX/kamanja || echo "File Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
 ln -s $RPM_INSTALL_PREFIX/kamanja_%{version}/ $RPM_INSTALL_PREFIX/kamanja
echo "$RPM_INSTALL_PREFIX/kamanja_%{version}" >> /tmp/kamanja_vers.temp

%postun
[ -L $RPM_INSTALL_PREFIX/kamanja ]  && rm -f $RPM_INSTALL_PREFIX/kamanja || echo "File Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
[ -d $RPM_INSTALL_PREFIX/kamanja_%{version} ]  && rm -r $RPM_INSTALL_PREFIX/kamanja_%{version} || echo "Dir Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
sed -e '/%{version}/d' /tmp/kamanja_vers.temp > /tmp/kamanja_vers.temp_1 && mv /tmp/kamanja_vers.temp_1 /tmp/kamanja_vers.temp
PREV_VER=`tail -1 /tmp/kamanja_vers.temp`
if [ -s /tmp/kamanja_vers.temp  ]; then
        ln -s $PREV_VER $RPM_INSTALL_PREFIX/kamanja
else
        rm /tmp/kamanja_vers.temp
fi
