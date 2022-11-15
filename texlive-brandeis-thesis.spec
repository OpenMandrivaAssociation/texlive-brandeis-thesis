Name:		texlive-brandeis-thesis
Version:	59832
Release:	1
Summary:	A class for Brandeis University M.A. theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/brandeis-thesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-thesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-thesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
brandeis-thesis.cls provides the structures and formatting
information for an M.A. thesis for the Brandeis University
Graduate School of Arts and Sciences.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/brandeis-thesis
%{_texmfdistdir}/tex/latex/brandeis-thesis
%doc %{_texmfdistdir}/doc/latex/brandeis-thesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
