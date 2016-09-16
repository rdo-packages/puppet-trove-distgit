%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-trove
Version:        XXX
Release:        XXX
Summary:        Puppet module for OpenStack Trove
License:        Apache-2.0

URL:            https://launchpad.net/puppet-trove

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-stdlib
Requires:       puppet-openstacklib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Trove

%prep
%setup -q -n openstack-trove-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/trove/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/trove/



%files
%{_datadir}/openstack-puppet/modules/trove/


%changelog

