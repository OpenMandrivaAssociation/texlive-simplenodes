Name:		texlive-simplenodes
Version:	62888
Release:	2
Summary:	Simple nodes in four colors written in TikZ for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simplenodes
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplenodes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplenodes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX macro package for generating simple node-based
flow graphs or diagrams built upon the TikZ package. The
package provides two basic commands, one to generate a node and
one to create links between nodes. The positioning of the nodes
is not handled by the package itself but is preferably done in
a tabular environment. In total, four simple node types are
defined, loosely based on the nomenclature and color patterns
of the popular Java script Bootstrap.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/simplenodes
%doc %{_texmfdistdir}/doc/latex/simplenodes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
