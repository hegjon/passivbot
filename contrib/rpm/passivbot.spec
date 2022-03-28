%global debug_package %{nil}
%global __provides_exclude_from .*
%global __requires_exclude_from .*
AutoReqProv: no

Name:    {{{ git_repo_name name="passivbot" }}}
Version: 5.5.2
Release: {{{ git_repo_version }}}%{?dist}
Summary: Trading bot running on Bybit and Binance Futures

License:    Public Domain
URL:        https://github.com/enarjord/passivbot
VCS:        {{{ git_repo_vcs }}}

Source:     {{{ git_repo_pack }}}

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3-websockets
Requires: python3-aiohttp
Requires: python3-numpy
Requires: python3-dateutil

%description
%{summary}.

%prep
{{{ git_repo_setup_macro }}}

%build
#Just copy the files for now

%install
install -m 0755 -vd %{buildroot}%{_datarootdir}/%{name}
cp -a . %{buildroot}%{_datarootdir}/%{name}

install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 contrib/rpm/passivbot-wrapped.sh %{buildroot}%{_bindir}/%{name}

install -m 0755 -vd %{buildroot}%{_sysconfig}/%{name}
install -m 0755 -vd %{buildroot}%{_sysconfdir}/%{name}/live
install -m 0755 api-keys.example.json %{buildroot}%{_sysconfdir}/%{name}/api-keys.json

install -dD -m 0750 %{buildroot}%{_sharedstatedir}/%{name}

%pre
getent group passivbot >/dev/null || groupadd -r passivbot
getent passwd passivbot >/dev/null || \
  useradd -r -g passivbot -s /sbin/nologin \
    -d %{_sharedstatedir}/%{name} \
    -c 'Passivbot' passivbot
exit 0

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/%{name}/
%{_datarootdir}/%{name}/
%{_sharedstatedir}/%{name}/
%attr(755, root, root) %{_bindir}/%{name}

%changelog
{{{ git_repo_changelog }}}
