%global tl_name piechartmp
%global tl_revision 19440

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.0
Release:	%{tl_revision}.1
Summary:	Draw pie-charts using MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/piechartmp
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piechartmp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piechartmp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The piechartmp package is an easy way to draw pie-charts with MetaPost.
The package implements an interface that enables users with little
MetaPost experience to draw charts. A highlight of the package is the
possibility of suppressing some segments of the chart, thus creating the
possibility of several charts from the same data.

