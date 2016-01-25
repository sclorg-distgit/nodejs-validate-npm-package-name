%{?scl:%scl_package nodejs-validate-npm-package-name}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-validate-npm-package-name

%global npm_name validate-npm-package-name
%global commit 3af92c881549f1b96f05ab6bfb5768bba94ad72d
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-validate-npm-package-name
Version:	2.2.2
Release:	3%{?dist}
Summary:	Give me a string and I'll tell you if it's a valid npm package name
Url:		https://github.com/npm/validate-npm-package-name
Source0:	https://github.com/npm/%{npm_name}/archive/%{commit}/%{npm_name}-%{commit}.tar.gz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch


%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

BuildRequires:	%{?scl_prefix}npm(builtins)

%description
Give me a string and I'll tell you if it's a valid npm package name

%prep
%setup -q -n %{npm_name}-%{commit}

%nodejs_fixdep builtins

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/validate-npm-package-name

%doc README.md
%doc LICENSE

%changelog
* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 2.2.2-3
- Enable SCL macros

* Tue Jul 28 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.2-2
- Add nodejs_fixdep macro

* Tue Jun 30 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.2-1
- Initial build
