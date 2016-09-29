Name:           Kamanja
Version:        1.5.3_2.11
Release:        1%{?dist}
Summary:        Kamanja is a real time decisioning system

License:        GPL
URL:            http://kamanja.org
Source0:        Kamanja-%{version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot

Prefix: %{_prefix}
%description
A RPM package for Kamanja binaries

%prep
%setup -q

%install
mkdir -p "$RPM_BUILD_ROOT%{_prefix}/Kamanja_%{version}"
cp -R * "$RPM_BUILD_ROOT%{_prefix}/Kamanja_%{version}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(777,kamanja,kamanja,-)
%{_prefix}/Kamanja_%{version}
%doc %{_prefix}/Kamanja_%{version}/documentation
%config %{_prefix}/Kamanja_%{version}/config

%post
if [ "$1" = "1" ]; then
    [ -L $RPM_INSTALL_PREFIX/kamanja ]  && rm -f $RPM_INSTALL_PREFIX/kamanja || echo "File Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
    ln -s $RPM_INSTALL_PREFIX/Kamanja_%{version}/ $RPM_INSTALL_PREFIX/kamanja
    echo "$RPM_INSTALL_PREFIX/Kamanja_%{version}" >> /tmp/kamanja_vers.temp
    echo "First install complete"
else
    [ -L $RPM_INSTALL_PREFIX/kamanja ]  && rm -f $RPM_INSTALL_PREFIX/kamanja || echo "File Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
    ln -s $RPM_INSTALL_PREFIX/Kamanja_%{version}/ $RPM_INSTALL_PREFIX/kamanja
    sed '1d' /tmp/kamanja_vers.temp  > /tmp/kamanja_vers.temp_1; mv /tmp/kamanja_vers.temp_1 /tmp/kamanja_vers.temp # POSIX
    echo "$RPM_INSTALL_PREFIX/Kamanja_%{version}" >> /tmp/kamanja_vers.temp
    echo "Upgrade complete"
fi

%postun
if [ "$1" = "1"  ]; then
        echo "First uninstall complete"
else
        [ -L $RPM_INSTALL_PREFIX/kamanja ]  && rm -f $RPM_INSTALL_PREFIX/kamanja || echo "File Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
        [ -d $RPM_INSTALL_PREFIX/Kamanja_%{version} ]  && rm -r $RPM_INSTALL_PREFIX/Kamanja_%{version} || echo "Dir Not Found" >> $RPM_INSTALL_PREFIX/rpm.log
        sed -e '/%{version}/d' /tmp/kamanja_vers.temp > /tmp/kamanja_vers.temp_1 && mv /tmp/kamanja_vers.temp_1 /tmp/kamanja_vers.temp
        PREV_VER=`tail -1 /tmp/kamanja_vers.temp`
        if [ -s /tmp/kamanja_vers.temp  ]; then
                ln -s $PREV_VER $RPM_INSTALL_PREFIX/kamanja
        else
                rm /tmp/kamanja_vers.temp
        fi
        echo "Upgrade uninstall  complete"
fi
