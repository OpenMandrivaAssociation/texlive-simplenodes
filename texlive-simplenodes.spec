%global tl_name simplenodes
%global tl_revision 62888

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Simple nodes in four colors written in TikZ for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/simplenodes
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplenodes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplenodes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX macro package for generating simple node-based flow
graphs or diagrams built upon the TikZ package. The package provides two
basic commands, one to generate a node and one to create links between
nodes. The positioning of the nodes is not handled by the package itself
but is preferably done in a tabular environment. In total, four simple
node types are defined, loosely based on the nomenclature and color
patterns of the popular Java script Bootstrap.

