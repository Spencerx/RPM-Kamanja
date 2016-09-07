Name:           kamanja
Version: 	1.5.0_2.11       
Release:        1%{?dist}
Summary:        Kamanja is a real time decisioning system

License:        GPL
URL:            http://kamanja.org
Source0:        kamanja-1.5.0_2.11.tar.gz

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
mkdir -p $RPM_BUILD_ROOT%{_prefix}/kamanja_1.5.0_2.11
cp -R * $RPM_BUILD_ROOT%{_prefix}/kamanja_1.5.0_2.11

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(777,kamanja,kamanja)
%{_prefix}/kamanja_1.5.0_2.11
%doc %{_prefix}/kamanja_1.5.0_2.11/documentation
%config %{_prefix}/kamanja_1.5.0_2.11/config

%post
[ -L /usr/bin/kamanja ]  && rm -f /usr/bin/kamanja || echo "File Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
sudo ln -s $RPM_INSTALL_PREFIX/kamanja_1.5.0_2.11/ /usr/bin/kamanja
echo "$RPM_INSTALL_PREFIX/kamanja_1.5.0_2.11" >> /tmp/kamanja_vers.temp

%postun
[ -L /usr/bin/kamanja ]  && rm -f /usr/bin/kamanja || echo "File Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
[ -d $RPM_INSTALL_PREFIX/kamanja_1.5.0_2.11 ]  && rm -r $RPM_INSTALL_PREFIX/kamanja_1.5.0_2.11 || echo "Dir Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
sed -e '$ d' /tmp/kamanja_vers.temp > /tmp/kamanja_vers.temp_1 && mv /tmp/kamanja_vers.temp_1 /tmp/kamanja_vers.temp
PREV_VER=`tail -1 /tmp/kamanja_vers.temp`
if [ -s /tmp/kamanja_vers.temp  ]; then
        ln -s $PREV_VER /usr/bin/kamanja
else
        rm /tmp/kamanja_vers.temp
fi
