%global tl_name brandeis-thesis
%global tl_revision 68092

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.3
Release:	%{tl_revision}.1
Summary:	A class for Brandeis University M.A. theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/brandeis-thesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-thesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-thesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
brandeis-thesis.cls provides the structures and formatting information
for an M.A. thesis for the Brandeis University Graduate School of Arts
and Sciences.

