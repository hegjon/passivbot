%global debug_package %{nil}
%global __provides_exclude_from .*
%global __requires_exclude_from .*
AutoReqProv: no

Name:    {{{ git_name name="passivbot" }}}
Version: 4.0.0
Release: {{{ git_version }}}%{?dist}
Summary: Trading bot running on Bybit and Binance Futures

License:    Public Domain
URL:        https://github.com/enarjord/passivbot
VCS:        {{{ git_vcs }}}

Source:     {{{ git_pack }}}

BuildRequires:  python3.8

%description
%{summary}.

%prep
{{{ git_setup_macro }}}

%build
python3.8 -m venv bundled-env
source bundled-env/bin/activate
pip3.8 install -r requirements.txt

%install
install -m 0755 -vd %{buildroot}%{_datarootdir}/%{name}
cp -a . %{buildroot}%{_datarootdir}/%{name}

install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 contrib/rpm/passivbot-wrapped.sh %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_datarootdir}/%{name}/
%{_bindir}/%{name}

%changelog
{{{ git_changelog }}}
